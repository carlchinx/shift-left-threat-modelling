# threatModelling (PyTM + Semantic Compiler)

A Python project that models a **Gemini-style Managed RAG** architecture using **two complementary approaches**:

1. **PyTM** - Traditional threat modeling with data flow diagrams
2. **Semantic Compiler** - Graph-based threat analysis from TypeSpec-style architecture definitions

## Prereqs
- Python 3.10+

## Setup
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -r requirements.txt
```

## Run

### Validate Compliance (Recommended First Step)
Ensure both specifications are strictly synchronized:

```powershell
python -m threatmodeling.validate
```

This validates:
- **Component alignment** - TypeSpec namespaces match PyTM processes
- **Trust zone consistency** - All components in correct boundaries
- **Data flow semantics** - Flow types match @dataFlow decorators

### Web Interface (Recommended)
Launch the interactive Streamlit dashboard:

```powershell
streamlit run app.py
```

This provides a web UI to:
- Run both analysis approaches
- Edit TypeSpec architecture definitions
- View threat findings grouped by severity
- Export DFD diagrams

### Command Line

#### Option 1: PyTM Model
Generates a threat report and a DFD `.dot` file using PyTM's threat database.

```powershell
python -m threatmodeling
```

#### Option 2: Semantic Compiler
Analyzes TypeSpec-style architecture and generates threats using deterministic graph rules.

```powershell
python -m threatmodeling.semantic_main
```

This approach identifies:
- **Trust boundary violations** (Internet → DMZ → Trusted → HighSide)
- **Ingestion risks** (malicious content, RCE)
- **RAG-specific threats** (indirect prompt injection via vector retrieval)

#### Option 3: LLM-Enhanced Analysis (gpt-oss-20b:groq via HuggingFace)
Combines knowledge graph rules with LLM reasoning for comprehensive analysis.

```powershell
# Set your HuggingFace token
$env:HF_TOKEN='hf_your-token-here'

python -m threatmodeling.llm_main
```

Benefits:
- **Knowledge Graph**: Deterministic STRIDE-based patterns
- **gpt-oss-20b:groq**: Novel threat identification and contextual analysis
- **AI-Specific Threats**: Prompt injection, model poisoning, data leakage

#### Visualization
Generate standalone architecture diagrams (PNG format, no external tools required):

```powershell
python -m threatmodeling.visualize
```

This creates:
- `out/architecture.png` - Semantic compiler architecture diagram
- Trust zones with color coding
- Data flows with risk levels

## Outputs
- **`out/architecture.png`** - Semantic architecture diagram (standalone PNG)
- **`out/dfd.png`** - PyTM data flow diagram (standalone PNG)

All visualizations are generated using matplotlib - **no graphviz binary required**.

## Architecture Compliance

This project maintains **strict specification compliance** between two representations:

1. **TypeSpec Definition** ([semantic_compiler.py](src/threatmodeling/semantic_compiler.py#L143)) - Declarative architecture with semantic decorators
2. **PyTM Model** ([rag_model.py](src/threatmodeling/rag_model.py)) - Programmatic threat model

Both MUST represent the identical architecture:
- **Components**: RAGClient, GatewayService, IngestionWorker, VectorDatastore, **ContextInjectionEngine**, **GeminiLLM** (6 components)
- **Trust Zones**: Internet → DMZ → Trusted → HighSide
- **Data Flows**: Control, Ingestion, Retrieval, ContextInjection, Inference

### Threat Detection Layers

1. **Knowledge Graph** ([threat_knowledge_graph.py](src/threatmodeling/threat_knowledge_graph.py))
   - 7 STRIDE-based threat patterns
   - AI-specific threats (prompt injection, poisoning, leakage)
   - CWE/CAPEC references

2. **LLM Reasoning** ([llm_analyzer.py](src/threatmodeling/llm_analyzer.py)) *(Optional)*
   - gpt-oss-20b:groq contextual analysis (via HuggingFace Router)
   - Novel threat identification
   - Requires `HF_TOKEN`

Run `python -m threatmodeling.validate` to verify synchronization.

📖 **[Full Compliance Reference](docs/COMPLIANCE.md)** - Canonical architecture specification and maintenance rules  
📖 **[Setup Guide](SETUP.md)** - LLM integration and token configuration
