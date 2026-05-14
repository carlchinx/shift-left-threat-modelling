import "@typespec/http";
import "@typespec/rest";

using TypeSpec.Http;

// --- SEMANTIC DECORATORS (The Grammar of Security) ---
// These decorators map directly to Node/Edge properties in the graph.

/** Defines the trust level of the component hosting the namespace. */
dec trustZone(target: unknown, zone: "Internet" | "DMZ" | "Trusted" | "HighSide");

/** Defines the semantic nature of a data flow on an operation. */
dec dataFlow(target: unknown, type: "Ingestion" | "Retrieval" | "Control" | "ContextInjection");

/** Defines the criticality of the data being handled. */
dec classification(target: unknown, level: "Public" | "Internal" | "Confidential" | "Restricted");

// --- ARCHITECTURAL DEFINITION: Gemini Managed RAG ---

@service({ title: "Gemini RAG Architecture" })
@trustZone("Internet") // The Client is in the Wild
namespace RAGClient {
    // Implicit actor
}

@trustZone("DMZ")
namespace GatewayService {
    @route("/api/v1/query")
    @doc("Entry point for all user traffic.")
    op routeRequest(@body payload: string): void;
}

@trustZone("Trusted")
namespace IngestionWorker {
    /**
     * SEMANTIC HOOK: File ingestion implies executable-adjacent risk.
     * The compiler will detect flowType="Ingestion" crossing Internet -> Trusted.
     */
    @route("/upload")
    @dataFlow("Ingestion") 
    op processUpload(@body @classification("Confidential") doc: bytes): void;
}

@trustZone("Trusted")
namespace InferenceEngine {
    /**
     * SEMANTIC HOOK: Retrieval flow into an Agent implies Prompt Injection.
     * The compiler detects: Datastore -> Inference (ContextInjection).
     */
    @route("/generate")
    @dataFlow("ContextInjection")
    op generateResponse(@body prompt: string): string;
}

@trustZone("HighSide")
namespace VectorDatastore {
    @doc("Stores embeddings. High value asset.")
    @dataFlow("Retrieval")
    op fetchEmbeddings(query: string): bytes;
}
