# Specification Compliance Reference

## Overview
This project maintains **two equivalent representations** of the same RAG architecture. Both MUST stay synchronized.

## Canonical Architecture

### Components & Trust Zones

| Component | Trust Zone | Type | Purpose |
|-----------|------------|------|---------|
| `RAGClient` | Internet | Actor | End user / external client |
| `GatewayService` | DMZ | Process | API gateway, traffic routing |
| `IngestionWorker` | Trusted | Process | Document processing & embedding |
| `VectorDatastore` | HighSide | Datastore | Embeddings storage (high-value asset) |
| `ContextInjectionEngine` | Trusted | Process | Retrieves and injects context |
| `GeminiLLM` | HighSide | Process | Language model for generation (critical asset) |

### Data Flows & Semantics

| Source | Destination | Flow Type | Operation | Risk |
|--------|-------------|-----------|-----------|------|
| RAGClient | GatewayService | `Control` | routeRequest | Untrusted input |
| RAGClient | GatewayService | `Ingestion` | upload | Malicious file upload |
| GatewayService | IngestionWorker | `Ingestion` | processUpload | RCE via parsing |
| IngestionWorker | VectorDatastore | `Control` | generateEmbeddings | Data poisoning |
| GatewayService | ContextInjectionEngine | `Control` | query | Query manipulation |
| ContextInjectionEngine | VectorDatastore | `Retrieval` | fetchEmbeddings | Data exfiltration |
| VectorDatastore | ContextInjectionEngine | `ContextInjection` | returnChunks | Indirect prompt injection |
| ContextInjectionEngine | GeminiLLM | `ContextInjection` | injectContext | Prompt injection |
| GeminiLLM | GatewayService | `Inference` | generateResponse | Model inversion, PII leakage |

### Data Classifications

| Data Object | Classification | PyTM Enum |
|-------------|----------------|-----------|
| User Query | Internal/Sensitive | `Classification.SENSITIVE` |
| Uploaded Document | Confidential | `Classification.SENSITIVE` |
| Embeddings | Restricted | `Classification.RESTRICTED` |
| Model Response | Public | `Classification.PUBLIC` |

## TypeSpec Representation

Location: [`src/threatmodeling/semantic_compiler.py`](../src/threatmodeling/semantic_compiler.py#L143)

```typespec
@trustZone("Internet")
namespace RAGClient {}

@trustZone("DMZ")
namespace GatewayService {
    @route("/api/v1/query")
    op routeRequest(@body payload: string): void;
}

@trustZone("Trusted")
namespace IngestionWorker {
    @route("/upload")
    @dataFlow("Ingestion") 
    op processUpload(@body @classification("Confidential") doc: bytes): void;
}

@trustZone("Trusted")
namespace InferenceEngine {
    @route("/generate")
    @dataFlow("ContextInjection")
    op generateResponse(@body prompt: string): string;
}

@trustZone("HighSide")
namespace VectorDatastore {
    @dataFlow("Retrieval")
    op fetchEmbeddings(query: string): bytes;
}
```

## PyTM Representation

Location: [`src/threatmodeling/rag_model.py`](../src/threatmodeling/rag_model.py)

```python
# Components
client = Actor("RAGClient")
gateway = Process("GatewayService")
ingestion = Process("IngestionWorker")
inference = Process("InferenceEngine")
vector_store = Datastore("VectorDatastore")

# Flows
Dataflow(client, gateway, "routeRequest")  # Control
Dataflow(client, gateway, "upload")  # Ingestion
Dataflow(gateway, ingestion, "processUpload")  # Ingestion
Dataflow(gateway, inference, "generateResponse")  # Control
Dataflow(inference, vector_store, "fetchEmbeddings")  # Retrieval
Dataflow(vector_store, inference, "returnEmbeddings")  # ContextInjection
```

## Compliance Validation

Run the validator to ensure both specifications match:

```bash
python -m threatmodeling.validate
```

### What Gets Validated

1. **Component Names** - All namespace/process names match exactly
2. **Trust Zones** - Each component in correct boundary (Internet/DMZ/Trusted/HighSide)
3. **Data Flows** - All edges present with correct flow types
4. **Flow Semantics** - Ingestion, Retrieval, Control, ContextInjection match

### Expected Threats

Both approaches should identify:

| Severity | Threat | Component | Root Cause |
|----------|--------|-----------|------------|
| CRITICAL | Indirect Prompt Injection | InferenceEngine | ContextInjection from untrusted datastore |
| HIGH | Malicious Content Ingestion | IngestionWorker | Ingestion flow from Internet |
| MEDIUM | Trust Boundary Violations | Multiple | Zone transitions without validation |

## Maintenance Rules

When modifying the architecture:

1. ✅ **Edit TypeSpec first** in `semantic_compiler.py`
2. ✅ **Update PyTM model** in `rag_model.py` to match
3. ✅ **Run validator** to confirm compliance
4. ✅ **Update this document** if canonical architecture changes

Never edit specifications independently!
