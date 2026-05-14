import os
from dotenv import load_dotenv

from .pipeline import run_end_to_end_pipeline
from .semantic_compiler import TYPESPEC_SOURCE


def main() -> None:
    load_dotenv()
    hf_token = os.getenv("HF_TOKEN")
    if not hf_token:
        raise SystemExit("HF_TOKEN is required (LLM is mandatory). Set HF_TOKEN before running.")

    result = run_end_to_end_pipeline(
        typespec_source=TYPESPEC_SOURCE,
        hf_token=hf_token,
        output_dir="out",
        strict_compliance=True,
    )

    print("=" * 70)
    print("PIPELINE COMPLETE (TypeSpec + PyTM aligned)")
    print("=" * 70)
    print(f"Architecture PNG: {result.architecture_png_path}")
    print(f"DFD PNG: {result.dfd_png_path}")
    print(f"Report (Markdown): {result.report_md_path}")
    print(f"Report (HTML): {result.report_html_path}")
    print(f"Semantic findings: {result.findings_count}")
    print(f"PyTM findings: {result.pytm_findings_count}")



if __name__ == "__main__":
    main()
