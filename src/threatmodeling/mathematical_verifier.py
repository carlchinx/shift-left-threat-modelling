from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

_ALLOWED_TRUST_ZONES = {"Internet", "DMZ", "Trusted", "HighSide"}
_ALLOWED_FLOW_TYPES = {"Ingestion", "Retrieval", "Control", "ContextInjection", "Inference"}
_ALLOWED_SEVERITIES = {"Critical", "High", "Medium", "Low"}


@dataclass(frozen=True)
class VerificationResult:
    ok: bool
    errors: list[str]
    summary: dict[str, Any]


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_file(path: str) -> str | None:
    p = Path(path)
    if not p.exists():
        return None
    return hashlib.sha256(p.read_bytes()).hexdigest()


def verify_semantic_graph(graph: Any) -> VerificationResult:
    errors: list[str] = []

    # Node invariants
    for node, data in graph.nodes(data=True):
        zone = data.get("trust_zone", "Unknown")
        if zone not in _ALLOWED_TRUST_ZONES:
            errors.append(f"Node '{node}' has invalid trust_zone '{zone}'")

    # Edge invariants
    for u, v, data in graph.edges(data=True):
        flow_type = data.get("flow_type", "Control")
        if flow_type not in _ALLOWED_FLOW_TYPES:
            errors.append(f"Edge '{u}->{v}' has invalid flow_type '{flow_type}'")

    summary: dict[str, Any] = {
        "nodes": graph.number_of_nodes(),
        "edges": graph.number_of_edges(),
        "allowed_trust_zones": sorted(_ALLOWED_TRUST_ZONES),
        "allowed_flow_types": sorted(_ALLOWED_FLOW_TYPES),
    }

    return VerificationResult(ok=not errors, errors=errors, summary=summary)


def verify_llm_findings(findings: Iterable[Any], graph: Any) -> VerificationResult:
    errors: list[str] = []
    count = 0

    for f in findings:
        count += 1
        component = getattr(f, "component", None)
        severity = getattr(f, "severity", None)
        threat_id = getattr(f, "threat_id", None)
        description = getattr(f, "description", None)
        mitigation = getattr(f, "mitigation", None)

        if not isinstance(component, str) or not component:
            errors.append(f"LLM finding #{count}: missing/invalid component")
        elif component not in graph.nodes:
            errors.append(f"LLM finding #{count}: component '{component}' not in architecture graph")

        if severity not in _ALLOWED_SEVERITIES:
            errors.append(f"LLM finding #{count}: invalid severity '{severity}'")

        if not isinstance(threat_id, str) or not threat_id:
            errors.append(f"LLM finding #{count}: missing/invalid threat_id")

        if not isinstance(description, str) or not description.strip():
            errors.append(f"LLM finding #{count}: missing/invalid description")

        if not isinstance(mitigation, str) or not mitigation.strip():
            errors.append(f"LLM finding #{count}: missing/invalid mitigation")

    summary: dict[str, Any] = {
        "count": count,
        "allowed_severities": sorted(_ALLOWED_SEVERITIES),
        "constraint": "Each finding must reference an existing component; fields must be non-empty; severity must be in allowed set.",
    }

    return VerificationResult(ok=not errors, errors=errors, summary=summary)
