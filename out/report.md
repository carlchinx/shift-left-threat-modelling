# Threat Modeling Report

Generated: 2026-02-01 13:07:16Z
## Inputs
- Source: Architecture TypeSpec text
- LLM: HuggingFace Router (OpenAI-compatible), model `openai/gpt-oss-20b:groq`
## Compliance
- Status: ✅ Compliant

<details><summary>Compliance log</summary>

```text
======================================================================
SPECIFICATION COMPLIANCE VALIDATION
======================================================================

[1/4] Building PyTM model...
[2/4] Parsing TypeSpec...
[*] INTERPRETER: Parsing Specification...
    -> Node Created: RAGClient (Zone: Internet)
    -> Node Created: GatewayService (Zone: DMZ)
    -> Node Created: IngestionWorker (Zone: Trusted)
    -> Node Created: InferenceEngine (Zone: Trusted)
    -> Node Created: VectorDatastore (Zone: HighSide)

[3/4] Validating Components...
    TypeSpec Components: ['GatewayService', 'InferenceEngine', 'IngestionWorker', 'RAGClient', 'VectorDatastore']
    ✓ All expected components present

[4/4] Validating Trust Zones...
    ✓ RAGClient: Internet
    ✓ GatewayService: DMZ
    ✓ IngestionWorker: Trusted
    ✓ VectorDatastore: HighSide
    ✓ InferenceEngine: Trusted

[5/5] Validating Data Flows...
    ✓ RAGClient -> GatewayService: Ingestion
    ✓ GatewayService -> IngestionWorker: Ingestion
    ✓ IngestionWorker -> VectorDatastore: Control
    ✓ GatewayService -> InferenceEngine: Control
    ✓ InferenceEngine -> VectorDatastore: Retrieval
    ✓ VectorDatastore -> InferenceEngine: ContextInjection
    ✓ InferenceEngine -> GatewayService: Control

[6/6] Validating Knowledge Graph Integration...
    ✓ Knowledge graph loaded: 7 threat patterns

======================================================================
VALIDATION RESULTS
======================================================================

✅ FULL COMPLIANCE - Both specifications are strictly synchronized!
```

</details>
## Semantic Findings (KG-grounded + LLM)
Total findings: **10**

| Severity | Component | Threat | Mitigation |
|---|---|---|---|
| Critical | InferenceEngine | Indirect Prompt Injection via Retrieval (AI-INJECT-001) |   - Treat all retrieved content as untrusted input<br>  - Use ChatML or structured prompting to separate data from instructions<br>  - Implement output filtering and validation<br>  - Content provenance tracking<br>  - Limit LLM capabilities (function calling restrictions) |
| High | GatewayService | Malicious Content Ingestion (STRIDE-T-001) |   - Sandboxed parsing environment<br>  - Magic number and MIME type verification<br>  - Antivirus/malware scanning<br>  - Content Security Policy enforcement<br>  - Input size limits |
| High | IngestionWorker | Malicious Content Ingestion (STRIDE-T-001) |   - Sandboxed parsing environment<br>  - Magic number and MIME type verification<br>  - Antivirus/malware scanning<br>  - Content Security Policy enforcement<br>  - Input size limits |
| Medium | GatewayService | Trust Boundary Violation (STRIDE-S-001) |   - Implement schema validation at boundary<br>  - Require authentication and authorization<br>  - Use mutual TLS for inter-zone communication |
| Medium | IngestionWorker | Trust Boundary Violation (STRIDE-S-001) |   - Implement schema validation at boundary<br>  - Require authentication and authorization<br>  - Use mutual TLS for inter-zone communication |
| Medium | InferenceEngine | Trust Boundary Violation (STRIDE-S-001) |   - Implement schema validation at boundary<br>  - Require authentication and authorization<br>  - Use mutual TLS for inter-zone communication |
| Medium | VectorDatastore | Trust Boundary Violation (STRIDE-S-001) |   - Implement schema validation at boundary<br>  - Require authentication and authorization<br>  - Use mutual TLS for inter-zone communication |
| Medium | InferenceEngine | Data Exfiltration via Retrieval (STRIDE-I-001) |   - Query authorization and filtering<br>  - Data classification enforcement<br>  - Audit logging of all retrieval operations<br>  - Row-level security on vector store |
| Medium | VectorDatastore | Trust Boundary Violation (STRIDE-S-001) |   - Implement schema validation at boundary<br>  - Require authentication and authorization<br>  - Use mutual TLS for inter-zone communication |
| Medium | VectorDatastore | Data Exfiltration via Retrieval (STRIDE-I-001) |   - Query authorization and filtering<br>  - Data classification enforcement<br>  - Audit logging of all retrieval operations<br>  - Row-level security on vector store |

<details><summary>Semantic log</summary>

```text
[*] INTERPRETER: Parsing Specification...
    -> Node Created: RAGClient (Zone: Internet)
    -> Node Created: GatewayService (Zone: DMZ)
    -> Node Created: IngestionWorker (Zone: Trusted)
    -> Node Created: InferenceEngine (Zone: Trusted)
    -> Node Created: VectorDatastore (Zone: HighSide)

[*] INTERPRETER: Parsing Specification...
    -> Node Created: RAGClient (Zone: Internet)
    -> Node Created: GatewayService (Zone: DMZ)
    -> Node Created: IngestionWorker (Zone: Trusted)
    -> Node Created: InferenceEngine (Zone: Trusted)
    -> Node Created: VectorDatastore (Zone: HighSide)

[*] COMPILER: Evaluating Graph Logic with Knowledge Graph...
    Knowledge Graph: 7 threat patterns loaded

[*] LLM ANALYZER: Querying gpt-oss for AI-assisted threat detection...
LLM analysis failed: Error code: 400 - {'error': {'message': "Failed to validate JSON. Please adjust your prompt. See 'failed_generation' for more details.", 'type': 'invalid_request_error', 'code': 'json_validate_failed', 'failed_generation': ''}}
    -> LLM identified 0 additional threats

============================================================
SEMANTIC THREAT MODEL REPORT
============================================================
[MEDIUM] Component: GatewayService
   Threat:     Trust Boundary Violation (STRIDE-S-001)
   Mitigation:   - Implement schema validation at boundary
  - Require authentication and authorization
  - Use mutual TLS for inter-zone communication
------------------------------------------------------------
[HIGH] Component: GatewayService
   Threat:     Malicious Content Ingestion (STRIDE-T-001)
   Mitigation:   - Sandboxed parsing environment
  - Magic number and MIME type verification
  - Antivirus/malware scanning
  - Content Security Policy enforcement
  - Input size limits
------------------------------------------------------------
[MEDIUM] Component: IngestionWorker
   Threat:     Trust Boundary Violation (STRIDE-S-001)
   Mitigation:   - Implement schema validation at boundary
  - Require authentication and authorization
  - Use mutual TLS for inter-zone communication
------------------------------------------------------------
[HIGH] Component: IngestionWorker
   Threat:     Malicious Content Ingestion (STRIDE-T-001)
   Mitigation:   - Sandboxed parsing environment
  - Magic number and MIME type verification
  - Antivirus/malware scanning
  - Content Security Policy enforcement
  - Input size limits
------------------------------------------------------------
[MEDIUM] Component: InferenceEngine
   Threat:     Trust Boundary Violation (STRIDE-S-001)
   Mitigation:   - Implement schema validation at boundary
  - Require authentication and authorization
  - Use mutual TLS for inter-zone communication
------------------------------------------------------------
[MEDIUM] Component: VectorDatastore
   Threat:     Trust Boundary Violation (STRIDE-S-001)
   Mitigation:   - Implement schema validation at boundary
  - Require authentication and authorization
  - Use mutual TLS for inter-zone communication
------------------------------------------------------------
[CRITICAL] Component: InferenceEngine
   Threat:     Indirect Prompt Injection via Retrieval (AI-INJECT-001)
   Mitigation:   - Treat all retrieved content as untrusted input
  - Use ChatML or structured prompting to separate data from instructions
  - Implement output filtering and validation
  - Content provenance tracking
  - Limit LLM capabilities (function calling restrictions)
------------------------------------------------------------
[MEDIUM] Component: InferenceEngine
   Threat:     Data Exfiltration via Retrieval (STRIDE-I-001)
   Mitigation:   - Query authorization and filtering
  - Data classification enforcement
  - Audit logging of all retrieval operations
  - Row-level security on vector store
------------------------------------------------------------
[MEDIUM] Component: VectorDatastore
   Threat:     Trust Boundary Violation (STRIDE-S-001)
   Mitigation:   - Implement schema validation at boundary
  - Require authentication and authorization
  - Use mutual TLS for inter-zone communication
------------------------------------------------------------
[MEDIUM] Component: VectorDatastore
   Threat:     Data Exfiltration via Retrieval (STRIDE-I-001)
   Mitigation:   - Query authorization and filtering
  - Data classification enforcement
  - Audit logging of all retrieval operations
  - Row-level security on vector store
------------------------------------------------------------

[*] INTERPRETER: Parsing Specification...
    -> Node Created: RAGClient (Zone: Internet)
    -> Node Created: GatewayService (Zone: DMZ)
    -> Node Created: IngestionWorker (Zone: Trusted)
    -> Node Created: InferenceEngine (Zone: Trusted)
    -> Node Created: VectorDatastore (Zone: HighSide)
✓ Architecture diagram saved to: out\architecture.png

Diagram includes:
  - 5 components across 4 trust zones
  - 7 data flows
  - 7 threat patterns in knowledge graph

Standalone PNG image generated (no external tools required)
```

</details>
## PyTM Findings
Total findings: **0**

<details><summary>PyTM log</summary>

```text

```

</details>
## Diagrams
- Architecture: `out\architecture.png`
- PyTM DFD: `out\dfd.png`
