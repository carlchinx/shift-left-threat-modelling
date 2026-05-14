"""
CLI for LLM-enhanced threat analysis.

Usage:
    python -m threatmodeling.llm_main
    
Environment:
    HF_TOKEN - Required for HuggingFace LLM analysis
"""
import os
import sys
from threatmodeling.semantic_compiler import analyze_typespec, TYPESPEC_SOURCE


def main():
    """Run LLM-enhanced threat analysis."""
    
    # Check for HuggingFace token
    api_key = os.getenv("HF_TOKEN")
    
    if not api_key:
        print("=" * 70)
        print("LLM-ENHANCED THREAT ANALYSIS")
        print("=" * 70)
        print("\n⚠️  HF_TOKEN environment variable not set")
        print("\nTo enable LLM analysis:")
        print("  1. Get a HuggingFace token from https://huggingface.co/settings/tokens")
        print("  2. Set environment variable:")
        print("     PowerShell: $env:HF_TOKEN='hf_your-token-here'")
        print("     Bash: export HF_TOKEN='hf_your-token-here'")
        raise SystemExit("\nHF_TOKEN is required (LLM is mandatory).")
    else:
        print("=" * 70)
        print("LLM-ENHANCED THREAT ANALYSIS (gpt-oss-20b:groq via HuggingFace)")
        print("=" * 70)
        print("\n✓ HF_TOKEN found (not shown)")
    
    # Run analysis
    try:
        findings = analyze_typespec(
            typespec_code=TYPESPEC_SOURCE,
            hf_token=api_key
        )
        
        print("\n" + "=" * 70)
        print("ANALYSIS COMPLETE")
        print("=" * 70)
        print(f"\nTotal findings: {len(findings)}")
        
        # Breakdown by severity
        severities = {}
        for f in findings:
            severities[f.severity] = severities.get(f.severity, 0) + 1
        
        print("\nBy severity:")
        for sev in ["Critical", "High", "Medium", "Low"]:
            if sev in severities:
                print(f"  {sev}: {severities[sev]}")
        
        print("\n✓ LLM-enhanced analysis completed successfully")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
