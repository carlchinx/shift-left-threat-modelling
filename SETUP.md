# Threat Modeling Setup Guide

## Quick Start (No API Key Required)

Run basic threat analysis using the knowledge graph:

```powershell
# Validate architecture
python -m threatmodeling.validate

# Run PyTM analysis
python -m threatmodeling

# Run semantic compiler (knowledge graph only)
python -m threatmodeling.semantic_main
```

## LLM-Enhanced Analysis (HuggingFace gpt-oss-20b:groq)

### Prerequisites
1. Get a HuggingFace token from [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
2. Install dependencies:
   ```powershell
   pip install openai
   ```
   (Uses OpenAI-compatible SDK with HuggingFace Router endpoint)

### Setup Token

**PowerShell:**
```powershell
$env:HF_TOKEN='hf_your-token-here'
```

**Bash/Linux:**
```bash
export HF_TOKEN='hf_your-token-here'
```

**Persistent (PowerShell Profile):**
```powershell
# Add to $PROFILE
$env:HF_TOKEN='hf_your-token-here'
```

### Run LLM Analysis

```powershell
python -m threatmodeling.llm_main
```
This combines:
- **Knowledge Graph** (7 STRIDE-based patterns)
- **gpt-oss-20b:groq** (contextual threat analysis via HuggingFace Router)

### Web Interface with LLM

```powershell
streamlit run app.py
```

Then:
1. Check **"Enable gpt-oss-20b:groq Analysis"** in sidebar
2. Enter your HuggingFace token
3. Click **"Analyze TypeSpec"**

## LLM Configuration Details

### Model Information
- **Model**: `openai/gpt-oss-20b:groq`
- **Endpoint**: `https://router.huggingface.co/v1`
- **SDK**: OpenAI-compatible Python client
- **Role**: Senior Enterprise Architect (threat modeling specialist)

### Example Usage
```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)

completion = client.chat.completions.create(
    model="openai/gpt-oss-20b:groq",
    messages=[
        {
            "role": "Senior Enterprise Architect",
            "content": "Analyze this architecture for threats..."
        }
    ],
)
```

## Architecture Overview

### Components
- **RAGClient** (Internet) → End user
- **GatewayService** (DMZ) → API gateway
- **IngestionWorker** (Trusted) → Document processing
- **VectorDatastore** (HighSide) → Embeddings storage
- **ContextInjectionEngine** (Trusted) → Context retrieval
- **GeminiLLM** (HighSide) → Language model (placeholder name)

### Key Flows
1. **Ingestion**: Client → Gateway → Ingestion → VectorStore
2. **Query**: Client → Gateway → Retriever → VectorStore
3. **Context Injection**: VectorStore → Retriever → LLM
4. **Response**: LLM → Gateway → Client

## Threat Detection Methods

### 1. Knowledge Graph (No Token Required)
- **STRIDE-based patterns**
- Trust boundary violations
- Ingestion risks (malicious uploads)
- AI-specific threats (prompt injection, poisoning)
- 7 pre-defined threat patterns with mitigations

### 2. LLM-Enhanced (Requires HF_TOKEN)
- **All knowledge graph threats PLUS:**
- Novel threat identification via gpt-oss-20b:groq
- Contextual reasoning about attack chains
- Custom threat scenarios
- Deeper mitigation recommendations

## Expected Threats

You should see these **CRITICAL** threats:
1. **Indirect Prompt Injection** (AI-INJECT-001)
   - Target: ContextInjectionEngine, GeminiLLM
   - Vector: Malicious instructions in retrieved context
   
2. **Malicious Content Ingestion** (STRIDE-T-001)
   - Target: IngestionWorker
   - Vector: RCE via file parsing

## Troubleshooting

### "HuggingFace token not found"
- Set `HF_TOKEN` environment variable
- Or pass token in Streamlit UI
- Or run without LLM (knowledge graph only)

### "ImportError: No module named 'openai'"
```powershell
pip install openai
```

### "Validation failed"
Both PyTM and TypeSpec specs must match. Run:
```powershell
python -m threatmodeling.validate
```

Check for component/flow mismatches.

## Cost Considerations

**Knowledge Graph**: Free, runs locally

**LLM Analysis**: Uses HuggingFace Router
- Model: `openai/gpt-oss-20b:groq`
- Endpoint: HuggingFace Router (may have usage limits)
- Token usage: ~2-5K tokens per run
- Check pricing at: https://huggingface.co/pricing

Tip: Use knowledge graph during development, LLM for final reports.
