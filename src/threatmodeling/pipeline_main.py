"""End-to-end pipeline CLI.

Usage:
  python -m threatmodeling.pipeline_main
  python -m threatmodeling.pipeline_main --typespec path/to/arch.tsp

Env:
  HF_TOKEN (required)
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path

from threatmodeling.pipeline import run_end_to_end_pipeline
from threatmodeling.semantic_compiler import TYPESPEC_SOURCE


def main() -> None:
    parser = argparse.ArgumentParser(description="Run end-to-end threat modeling pipeline")
    parser.add_argument("--typespec", type=str, default=None, help="Path to TypeSpec architecture file")
    parser.add_argument("--out", type=str, default="out", help="Output directory")
    parser.add_argument(
        "--hf-token",
        type=str,
        default=None,
        help="HuggingFace token (preferred: set HF_TOKEN env var instead)",
    )
    parser.add_argument(
        "--no-strict",
        action="store_true",
        help="Do not fail fast on TypeSpec/PyTM compliance mismatch",
    )

    args = parser.parse_args()

    if args.typespec:
        typespec_source = Path(args.typespec).read_text(encoding="utf-8")
    else:
        typespec_source = TYPESPEC_SOURCE

    hf_token = args.hf_token or os.getenv("HF_TOKEN")
    if not hf_token:
        raise SystemExit(
            "HF_TOKEN is required (LLM is mandatory). Set it, e.g. PowerShell: $env:HF_TOKEN='hf_...'"
        )

    result = run_end_to_end_pipeline(
        typespec_source=typespec_source,
        hf_token=hf_token,
        output_dir=args.out,
        strict_compliance=not args.no_strict,
    )

    print("=" * 70)
    print("END-TO-END PIPELINE COMPLETE")
    print("=" * 70)
    print(f"Output dir: {result.output_dir}")
    print(f"Architecture PNG: {result.architecture_png_path}")
    print(f"DFD PNG: {result.dfd_png_path}")
    print(f"Report (Markdown): {result.report_md_path}")
    print(f"Report (HTML): {result.report_html_path}")
    print(f"Semantic findings: {result.findings_count}")
    print(f"PyTM findings: {result.pytm_findings_count}")


if __name__ == "__main__":
    main()
