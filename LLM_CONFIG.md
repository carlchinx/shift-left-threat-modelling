# LLM Configuration - HuggingFace gpt-oss-20b:groq

## Overview

The threat modeling system uses **HuggingFace Router** with `openai/gpt-oss-20b:groq` for LLM-enhanced threat analysis.

## Configuration

### Model Details
- **Model ID**: `openai/gpt-oss-20b:groq`
- **Provider**: HuggingFace Router
- **Endpoint**: `https://router.huggingface.co/v1`
- **SDK**: OpenAI Python client (OpenAI-compatible API)
- **System Role**: "Senior Enterprise Architect"

### Authentication
- **Environment Variable**: `HF_TOKEN`
- **Format**: `hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
- **Get Token**: https://huggingface.co/settings/tokens

## Implementation

### Code Example
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
            "content": "Analyze this RAG architecture for security threats..."
        }
    ],
)
```

### System Integration

**File**: [llm_analyzer.py](src/threatmodeling/llm_analyzer.py)

```python
class LLMThreatAnalyzer:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("HF_TOKEN")
        
        self.client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=self.api_key
        )
        self.model = "openai/gpt-oss-20b:groq"
```

## Setup Instructions

### 1. Get HuggingFace Token
Visit https://huggingface.co/settings/tokens and create a new token with:
- **Type**: Read or Write (Read sufficient for inference)
- **Name**: `threatmodeling-llm` (or your preference)

### 2. Set Environment Variable

**PowerShell:**
```powershell
$env:HF_TOKEN='hf_your_token_here'
```

**Bash/Linux:**
```bash
export HF_TOKEN='hf_your_token_here'
```

**Persistent (PowerShell Profile):**
```powershell
# Edit profile
notepad $PROFILE

# Add this line:
$env:HF_TOKEN='hf_your_token_here'
```

### 3. Verify Configuration
```powershell
python -c "import os; print('✓ Token configured' if os.getenv('HF_TOKEN') else '✗ Token not found')"
```

### 4. Run LLM Analysis
```powershell
# Command line
python -m threatmodeling.llm_main

# Web interface
streamlit run app.py
# Then check "Enable gpt-oss-20b:groq Analysis"
```

## Usage Modes

### Mode 1: Knowledge Graph Only (No Token)
```powershell
python -m threatmodeling.semantic_main
```
- Fast, deterministic
- 7 STRIDE-based patterns
- No API costs
- Works offline

### Mode 2: Hybrid Analysis (Requires Token)
```powershell
python -m threatmodeling.llm_main
```
- Knowledge graph PLUS LLM reasoning
- Novel threat identification
- Contextual attack chain analysis
- Requires internet + HF_TOKEN

### Mode 3: Interactive Web UI
```powershell
streamlit run app.py
```
- Toggle LLM on/off in sidebar
- Enter token directly in UI (not persisted)
- Real-time TypeSpec editing
- Visual diagram display

## Parameters

### LLM Analysis Parameters
- **Temperature**: 0.3 (focused, deterministic responses)
- **Response Format**: JSON object (structured threat findings)
- **Token Limit**: Model default (~4K context)
- **Timeout**: 30 seconds default

### Customization

To change model or parameters, edit [llm_analyzer.py](src/threatmodeling/llm_analyzer.py):

```python
# Change model
self.model = "different/model:provider"

# Change temperature (higher = more creative)
response = self.client.chat.completions.create(
    model=self.model,
    temperature=0.7,  # 0.0 to 1.0
    # ...
)
```

## Comparison: Knowledge Graph vs LLM

| Feature | Knowledge Graph | LLM-Enhanced |
|---|---|---|
| **Speed** | Instant | 2-10 seconds |
| **Cost** | Free | Token-based |
| **Offline** | Yes | No |
| **Threats** | 7 patterns | 7+ (novel detection) |
| **Repeatability** | 100% | ~95% (slight variations) |
| **Custom Scenarios** | Limited | Excellent |
| **Mitigations** | Template-based | Contextual |

**Recommendation**: Use knowledge graph during development, add LLM for production threat models.

## Troubleshooting

### "HuggingFace token required"
```
ValueError: HuggingFace token required. Set HF_TOKEN environment variable
```
**Solution**: Set `HF_TOKEN` as shown above

### "Model not found" or 401 Unauthorized
**Possible Causes**:
1. Invalid or expired token
2. Token lacks inference permissions
3. Model not accessible

**Solution**: 
- Regenerate token at huggingface.co/settings/tokens
- Ensure token has "Read" access
- Check model availability

### Rate Limiting
```
429 Too Many Requests
```
**Solution**:
- HuggingFace Router has rate limits
- Wait and retry
- Consider upgrading HuggingFace plan

### Connection Errors
**Requirements**:
- Internet connection
- No firewall blocking `router.huggingface.co`
- OpenAI Python package installed (`pip install openai`)

## Cost & Limits

### HuggingFace Router Pricing
- **Free Tier**: Available with limits
- **Paid Plans**: Check https://huggingface.co/pricing
- **Token Usage**: ~2-5K tokens per analysis

### Token Estimation
For typical RAG architecture (6 components, 8 flows):
- Input: ~1.5K tokens (architecture + prompt)
- Output: ~500-2K tokens (threat findings)
- **Total**: ~2-3.5K tokens per run

## Security Considerations

### Token Storage
⚠️ **Never commit HF_TOKEN to git**

Add to `.gitignore`:
```gitignore
.env
*.env
**/*token*
**/*secret*
```

### Streamlit UI
When entering token in Streamlit:
- Token is NOT persisted to disk
- Only stored in session memory
- Cleared when browser closed
- Use `type="password"` to hide input

### Best Practices
1. Use environment variables for automation
2. Use Streamlit input for one-off analyses
3. Rotate tokens periodically
4. Use read-only tokens when possible
5. Monitor usage at huggingface.co/usage

## Alternative Models

To use different HuggingFace models, modify `llm_analyzer.py`:

```python
# Example: Different model
self.model = "meta-llama/Llama-2-70b-chat-hf"

# Example: Different endpoint (HF Inference Endpoints)
self.client = OpenAI(
    base_url="https://your-endpoint.us-east-1.aws.endpoints.huggingface.cloud/v1",
    api_key=self.api_key
)
```

## Support

- **HuggingFace Router Docs**: https://huggingface.co/docs/api-inference
- **Model Info**: https://huggingface.co/openai/gpt-oss-20b
- **OpenAI SDK**: https://platform.openai.com/docs/api-reference

---

**Status**: ✅ Configured for HuggingFace Router with gpt-oss-20b:groq
**Last Updated**: January 31, 2026
