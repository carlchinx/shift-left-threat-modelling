from __future__ import annotations

import io
import os
import sys
from dataclasses import dataclass
import json
from dotenv import load_dotenv

from threatmodeling.rag_model import build_model as build_pytm_model
from threatmodeling.reporting import ReportInputs, write_report
from threatmodeling.semantic_compiler import TYPESPEC_SOURCE, analyze_typespec
from threatmodeling.validate import validate_compliance
from threatmodeling.visualize import generate_architecture_diagram
from threatmodeling.pytm_visualize import visualize_dfd
from threatmodeling.semantic_compiler import SemanticInterpreter
from threatmodeling.mathematical_verifier import (
    sha256_file,
    sha256_text,
    verify_llm_findings,
    verify_semantic_graph,
)

# Load environment variables from .env file
load_dotenv()


@dataclass(frozen=True)
class PipelineResult:
    output_dir: str
    report_md_path: str
    report_html_path: str
    architecture_png_path: str
    dfd_png_path: str
    findings_count: int
    pytm_findings_count: int


def _capture_output(func):
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    try:
        result = func()
        output = buffer.getvalue()
    finally:
        sys.stdout = old_stdout
    return result, output


def run_end_to_end_pipeline(
    *,
    typespec_source: str = TYPESPEC_SOURCE,
    hf_token: str | None = None,
    output_dir: str = "out",
    strict_compliance: bool = True,
) -> PipelineResult:
    """End-to-end pipeline:

    Accept architecture (TypeSpec text) -> KG-grounded semantic + mandatory LLM ->
    generate architecture diagram -> run PyTM -> generate full report.
    """

    hf_token_to_use = hf_token or os.getenv("HF_TOKEN")
    if not hf_token_to_use:
        raise RuntimeError(
            "HF_TOKEN is required (LLM is mandatory). Create a .env file with: HF_TOKEN=hf_..."
        )

    compliance_ok, compliance_log = _capture_output(
        lambda: validate_compliance(typespec_source=typespec_source)
    )
    if strict_compliance and not compliance_ok:
        raise RuntimeError(
            "Specification mismatch detected (TypeSpec != PyTM). Fix compliance before running pipeline."
        )

    # Build graph for invariant verification (captured separately from analysis logs)
    graph, graph_log = _capture_output(lambda: SemanticInterpreter().build_graph(typespec_source))
    graph_verification = verify_semantic_graph(graph)
    if not graph_verification.ok:
        raise RuntimeError("Graph invariants failed: " + "; ".join(graph_verification.errors))

    findings, semantic_log = _capture_output(
        lambda: analyze_typespec(typespec_code=typespec_source, hf_token=hf_token_to_use)
    )

    _, viz_log = _capture_output(
        lambda: generate_architecture_diagram(
            output_path=os.path.join(output_dir, "architecture.png"),
            typespec_source=typespec_source,
            findings=findings,
        )
    )

    tm = build_pytm_model()
    _, pytm_process_log = _capture_output(lambda: tm.process())

    dfd_png_path = os.path.join(output_dir, "dfd.png")
    _, dfd_log = _capture_output(lambda: visualize_dfd(tm, output_path=dfd_png_path, findings=getattr(tm, 'findings', [])))

    pytm_findings = getattr(tm, "findings", []) or []

    # LLM layer verifiability: check each LLM finding references a real component and allowed fields.
    # Note: analyze_typespec merges KG + LLM into Finding objects; here we only verify the schema-level invariants.
    llm_like = []
    for f in findings:
        threat = getattr(f, "threat", "")
        if isinstance(threat, str) and "(LLM-" in threat:
            llm_like.append(
                type(
                    "_Tmp",
                    (),
                    {
                        "threat_id": threat.split("(")[-1].rstrip(")"),
                        "component": getattr(f, "component", ""),
                        "severity": getattr(f, "severity", ""),
                        "description": getattr(f, "threat", ""),
                        "mitigation": getattr(f, "mitigation", ""),
                    },
                )()
            )
    llm_verification = verify_llm_findings(llm_like, graph)
    if not llm_verification.ok:
        raise RuntimeError("LLM findings invariants failed: " + "; ".join(llm_verification.errors))

    # Write verification artifact
    verification = {
        "typespec_sha256": sha256_text(typespec_source),
        "compliance_ok": bool(compliance_ok),
        "graph": graph_verification.summary,
        "llm_findings": llm_verification.summary,
        "architecture_png_sha256": sha256_file(os.path.join(output_dir, "architecture.png")),
        "dfd_png_sha256": sha256_file(dfd_png_path),
    }
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "verification.json"), "w", encoding="utf-8") as f:
        json.dump(verification, f, indent=2)

    report_inputs = ReportInputs(
        typespec_source=typespec_source,
        compliance_ok=bool(compliance_ok),
        compliance_log=compliance_log,
        semantic_log=(graph_log + "\n" + semantic_log + "\n" + viz_log).strip(),
        findings=findings,
        pytm_log=(pytm_process_log + "\n" + dfd_log).strip(),
        pytm_findings=pytm_findings,
        architecture_png_path=os.path.join(output_dir, "architecture.png"),
        dfd_png_path=dfd_png_path,
    )

    report_md_path, report_html_path = write_report(output_dir, report_inputs)

    return PipelineResult(
        output_dir=output_dir,
        report_md_path=report_md_path,
        report_html_path=report_html_path,
        architecture_png_path=os.path.join(output_dir, "architecture.png"),
        dfd_png_path=dfd_png_path,
        findings_count=len(list(findings)),
        pytm_findings_count=len(list(pytm_findings)),
    )
