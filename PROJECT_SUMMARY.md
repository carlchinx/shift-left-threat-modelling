# Project Summary: PyTM + Semantic Threat Modeling

## ✅ What You Have

### 1. **Correct RAG Architecture** (6 Components)
Matches reference architecture with proper separation of concerns:

```
Internet → DMZ → Trusted → HighSide

┌─────────────┐
│  RAGClient  │ (Internet) - End user
└──────┬──────┘
       │ HTTPS
┌──────▼──────────────┐
│  GatewayService     │ (DMZ) - API gateway, routing
└──────┬──────────────┘
       │
       ├─► IngestionWorker (Trusted) → VectorDatastore (HighSide)
       │   File upload & embedding generation
       │
       └─► ContextInjectionEngine (Trusted) ⟷ VectorDatastore
           Retrieves context → GeminiLLM (HighSide)
                              ↓
                         LLM inference & response
```

### 2. **Standalone Visualizations** (No External Tools)
- **matplotlib-based**: PNG images generated directly in Python
- **No graphviz binary**: Works on any system with Python
- **High-quality output**: 300 DPI production-ready diagrams

Generated files:
- `out/architecture.png` - Semantic compiler diagram (trust zones, flow types)
- `out/dfd.png` - PyTM data flow diagram (STRIDE-based)


### 3. **Threat Detection Stack**

#### **Layer 1: Knowledge Graph** (7 Patterns)
File: [threat_knowledge_graph.py](src/threatmodeling/threat_knowledge_graph.py)

| ID | Threat | Severity | Category |
|---|---|---|---|
| STRIDE-S-001 | Trust Boundary Violation | Medium | Spoofing |
| STRIDE-T-001 | Malicious Content Ingestion | High | Tampering |
| **AI-INJECT-001** | **Indirect Prompt Injection** | **Critical** | Elevation of Privilege |
| AI-POISON-001 | Training Data Poisoning | High | Tampering |
| AI-LEAK-001 | Model Inversion / Prompt Leakage | High | Information Disclosure |
| STRIDE-I-001 | Data Exfiltration via Retrieval | Medium | Information Disclosure |
| AI-DOS-001 | Resource Exhaustion | Medium | Denial of Service |

#### **Layer 2: LLM Reasoning** (Optional)
File: [llm_analyzer.py](src/threatmodeling/llm_analyzer.py)
- HuggingFace Router with `openai/gpt-oss-20b:groq`
- Novel threat identification via LLM
- Requires `HF_TOKEN`

### 4. **Dual Specification Compliance**

**TypeSpec** ([semantic_compiler.py](src/threatmodeling/semantic_compiler.py))
```typespec
@trustZone("HighSide")
namespace GeminiLLM {
    @dataFlow("Inference")
    op generateResponse(@body prompt: string, context: string): string;
}
```

**PyTM** ([rag_model.py](src/threatmodeling/rag_model.py))
```python
llm = Process("GeminiLLM")
llm.inBoundary = highside

Dataflow(retriever, llm, "injectContext")  # ContextInjection
Dataflow(llm, gateway, "generateResponse")  # Inference
```

### 5. **Generated Artifacts**

**Standalone PNG Images** (no external tools needed):
```
out/
├── architecture.png     # Semantic compiler diagram (292 KB)
└── dfd.png             # PyTM data flow diagram (297 KB)
```

**Technology**: matplotlib + networkx - works on any Python environment

## 🚀 Usage

### Basic Analysis (No API Key)
```powershell
# Validate compliance
python -m threatmodeling.validate

# PyTM analysis + DFD diagram
python -m threatmodeling

# Semantic analysis (knowledge graph)
python -m threatmodeling.semantic_main

# Generate architecture diagram
python -m threatmodeling.visualize
```

All commands generate **standalone PNG images** - no external tools required.

### LLM-Enhanced Analysis
```powershell
# Set API key
$env:HF_TOKEN='hf_your-token-here'

# Run hybrid analysis
python -m threatmodeling.llm_main
```

### Web Interface
```powershell
streamlit run app.py
```
- Toggle "Enable gpt-oss-20b:groq Analysis" for LLM enhancement
- Edit TypeSpec in real-time
- View threats grouped by severity
- **View PNG diagrams directly in browser**

## 📊 Validation Results

```
✅ 6/6 components synchronized
✅ 4/4 trust zones validated
✅ 8/8 data flows correct
✅ 7 threat patterns loaded
```

## 🎯 Key Threats Detected

### CRITICAL
1. **Indirect Prompt Injection** (AI-INJECT-001)
   - **Targets**: ContextInjectionEngine, GeminiLLM
   - **Vector**: Malicious instructions in retrieved context hijack LLM
   - **Mitigation**: ChatML delimiters, output filtering, capability limits

### HIGH
2. **Malicious Content Ingestion** (STRIDE-T-001)
   - **Target**: IngestionWorker
   - **Vector**: RCE via file parsing
   - **Mitigation**: Sandboxed parsing, antivirus, MIME validation

3. **Training Data Poisoning** (AI-POISON-001)
   - **Target**: VectorDatastore
   - **Vector**: Attacker poisons embeddings
   - **Mitigation**: Input validation, anomaly detection

## 📁 Project Structure

```
threatModelling/
├── src/threatmodeling/
│   ├── rag_model.py              # PyTM model (6 components)
│   ├── semantic_compiler.py      # TypeSpec parser + compiler
│   ├── threat_knowledge_graph.py # 7 STRIDE patterns (grounding)
│   ├── llm_analyzer.py           # HuggingFace gpt-oss integration
│   ├── validate.py               # Compliance checker
│   ├── visualize.py              # Matplotlib PNG generator
│   └── __main__.py               # PyTM runner with PNG export
├── app.py                        # Streamlit UI
├── out/                          # Generated PNG diagrams
├── docs/COMPLIANCE.md            # Architecture reference
├── SETUP.md                      # LLM setup guide
└── README.md
```

## 🔗 Quick Links

- **View Diagrams**: Open `out/architecture.png` or `out/dfd.png` in any image viewer
- **HuggingFace Tokens**: https://huggingface.co/settings/tokens
- **HuggingFace Router**: https://huggingface.co/docs/api-inference/index
- **PyTM Docs**: https://github.com/izar/pytm

## Key Changes from DOT Files

✅ **Standalone PNG generation** using matplotlib  
✅ **No graphviz binary** dependency  
✅ **Direct image display** in Streamlit UI  
✅ **300 DPI quality** for documentation  
✅ **Cross-platform** - works on any OS with Python

---

**Status**: ✅ Production-ready threat modeling system with standalone PNG visualizations

