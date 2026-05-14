import streamlit as st
import io
import sys
import os
from dotenv import load_dotenv
from threatmodeling.rag_model import build_model as build_pytm_model
from threatmodeling.semantic_compiler import analyze_typespec, TYPESPEC_SOURCE
from threatmodeling.validate import validate_compliance
from threatmodeling.visualize import generate_architecture_diagram
from threatmodeling.pytm_visualize import visualize_dfd
from threatmodeling.pipeline import run_end_to_end_pipeline

# Load environment variables from .env file
load_dotenv()


def capture_output(func):
    """Capture stdout from a function."""
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    try:
        result = func()
        output = buffer.getvalue()
    finally:
        sys.stdout = old_stdout
    return result, output


st.set_page_config(
    page_title="Threat Modeling Dashboard",
    page_icon="🔒",
    layout="wide"
)

st.title("🔒 RAG Architecture Threat Model")
st.markdown("**Gemini-style Managed RAG** threat analysis using PyTM and semantic compilation")

# Compliance check banner
with st.spinner("Validating specification compliance..."):
    is_compliant, compliance_output = capture_output(validate_compliance)

if is_compliant:
    st.success("✅ Specifications are synchronized and compliant")
else:
    st.error("❌ Specification mismatch detected! PyTM and TypeSpec are out of sync.")
    with st.expander("🔍 View Compliance Report", expanded=True):
        st.code(compliance_output, language="text")

# Sidebar for configuration
st.sidebar.header("Analysis Options")
analysis_mode = st.sidebar.radio(
    "Choose Analysis Mode:",
    ["Semantic Compiler", "PyTM", "Both"]
)

st.sidebar.markdown("---")
st.sidebar.subheader("🤖 LLM (Required)")
hf_token = st.sidebar.text_input(
    "HuggingFace Token (HF_TOKEN)",
    type="password",
    value=os.getenv("HF_TOKEN", ""),
    help="Required. Get token from huggingface.co/settings/tokens or set in .env file",
)
if not hf_token:
    st.sidebar.warning("⚠️ HF_TOKEN required (set in .env or above)")

st.sidebar.markdown("---")
st.sidebar.subheader("🚀 End-to-End")
run_full = st.sidebar.button(
    "Run Full Pipeline",
    help="Architecture -> KG+LLM semantic -> diagrams -> PyTM -> full report",
    disabled=not bool(hf_token),
)

# Main content tabs
if run_full:
    st.header("🚀 End-to-End Pipeline")
    with st.expander("📝 Edit TypeSpec Source", expanded=True):
        typespec_input = st.text_area(
            "TypeSpec Architecture Definition:",
            value=TYPESPEC_SOURCE,
            height=300,
            key="typespec_full_pipeline",
        )

    with st.spinner("Running end-to-end pipeline..."):
        try:
            result, pipeline_log = capture_output(
                lambda: run_end_to_end_pipeline(
                    typespec_source=typespec_input,
                    hf_token=hf_token,
                    output_dir="out",
                    strict_compliance=True,
                )
            )
            st.success("Pipeline complete")
            st.markdown(f"- Report (Markdown): `{result.report_md_path}`")
            st.markdown(f"- Report (HTML): `{result.report_html_path}`")
            st.markdown(f"- Architecture PNG: `{result.architecture_png_path}`")
            st.markdown(f"- DFD PNG: `{result.dfd_png_path}`")

            with st.expander("📊 Pipeline Log", expanded=False):
                st.code(pipeline_log, language="text")
        except Exception as e:
            st.error(f"Pipeline failed: {e}")

if analysis_mode in ["Semantic Compiler", "Both"]:
    st.header("🧠 Semantic Compiler Analysis")
    
    with st.expander("📝 Edit TypeSpec Source", expanded=False):
        typespec_input = st.text_area(
            "TypeSpec Architecture Definition:",
            value=TYPESPEC_SOURCE,
            height=300
        )
    
    can_run_semantic = bool(hf_token)
    if st.button("🔍 Analyze TypeSpec", key="semantic_analyze", disabled=not can_run_semantic):
        with st.spinner("Running semantic analysis..."):
            findings, output = capture_output(
                lambda: analyze_typespec(typespec_input, hf_token=hf_token)
            )

            _, viz_output = capture_output(
                lambda: generate_architecture_diagram(
                    output_path="out/architecture.png",
                    typespec_source=typespec_input,
                    findings=findings,
                )
            )
            
            st.success(f"Analysis complete! Found {len(findings)} threat(s)")
            
            # Display output
            with st.expander("📊 Analysis Log", expanded=True):
                st.code(output, language="text")

            with st.expander("📈 Diagram Generation Log", expanded=False):
                st.code(viz_output, language="text")
            
            # Display findings in a structured way
            if findings:
                st.subheader("🚨 Threat Findings")
                
                # Group by severity
                severity_order = ["Critical", "High", "Medium", "Low"]
                severity_colors = {
                    "Critical": "🔴",
                    "High": "🟠", 
                    "Medium": "🟡",
                    "Low": "🟢"
                }
                
                for severity in severity_order:
                    severity_findings = [f for f in findings if f.severity == severity]
                    if severity_findings:
                        st.markdown(f"### {severity_colors.get(severity, '⚪')} {severity} Severity")
                        
                        for i, finding in enumerate(severity_findings, 1):
                            with st.container():
                                col1, col2 = st.columns([1, 3])
                                with col1:
                                    st.metric("Component", finding.component)
                                with col2:
                                    st.warning(f"**Threat:** {finding.threat}")
                                    st.info(f"**Mitigation:** {finding.mitigation}")
                                st.divider()
            
            # Display architecture diagram
            st.subheader("🏗️ Architecture Diagram")
            try:
                import os
                if os.path.exists("out/architecture.png"):
                    from PIL import Image
                    img = Image.open("out/architecture.png")
                    st.image(img, caption="Semantic Architecture Diagram", width="stretch")
                else:
                    st.warning("Architecture diagram not found. Run visualization to generate it.")
            except Exception as e:
                st.error(f"Could not display diagram: {e}")


if analysis_mode in ["PyTM", "Both"]:
    if analysis_mode == "Both":
        st.markdown("---")
    
    st.header("📊 PyTM Analysis")
    
    if st.button("🔍 Run PyTM Model", key="pytm_analyze"):
        with st.spinner("Building PyTM model..."):
            tm = build_pytm_model()
            tm.process()

            # Generate standalone DFD visualization
            _, dfd_output = capture_output(lambda: visualize_dfd(tm, output_path="out/dfd.png"))
            
            # Display findings
            st.subheader("Threat Findings")
            if tm.findings:
                st.success(f"Found {len(tm.findings)} threat(s)")
                
                for i, finding in enumerate(tm.findings, 1):
                    with st.expander(f"{i}. {finding.threat_id}: {finding.description}", expanded=True):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown(f"**Target:** {finding.target}")
                        with col2:
                            st.markdown(f"**Severity:** {finding.severity}")
            else:
                st.info("No threats identified by PyTM (may require custom threat database)")
            
            # DFD - display PNG image
            st.subheader("Data Flow Diagram")
            try:
                import os
                if os.path.exists("out/dfd.png"):
                    from PIL import Image
                    img = Image.open("out/dfd.png")
                    st.image(img, caption="PyTM Data Flow Diagram", width="stretch")
                    with st.expander("📊 DFD Generation Log", expanded=False):
                        st.code(dfd_output, language="text")
                else:
                    st.warning("DFD image not found. Run PyTM analysis to generate it.")
            except Exception as e:
                st.error(f"Could not display DFD: {e}")


# Footer
st.sidebar.markdown("---")
st.sidebar.info(
    """
    **About**
    
    This dashboard demonstrates two complementary 
    threat modeling approaches:
    
    - **Semantic Compiler**: Graph-based analysis 
      of TypeSpec architecture definitions
    - **PyTM**: Traditional threat modeling with 
      STRIDE framework
    """
)
