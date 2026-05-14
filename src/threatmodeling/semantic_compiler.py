import os
import re
import networkx as nx
from dataclasses import dataclass
from typing import List, Dict, Optional
from dotenv import load_dotenv
from .threat_knowledge_graph import get_threat_knowledge_graph
from .llm_analyzer import LLMThreatAnalyzer

# Load environment variables from .env file
load_dotenv()

# ==============================================================================
# LAYER 1: THE SEMANTIC INTERPRETER
# Parsing TypeSpec to build the Navigable Property Graph
# ==============================================================================

@dataclass
class Finding:
    component: str
    severity: str
    threat: str
    mitigation: str

class SemanticInterpreter:
    def __init__(self):
        # Regex patterns to simulate TypeSpec AST parsing
        self.re_namespace = re.compile(r'namespace\s+(\w+)')
        self.re_trust = re.compile(r'@trustZone\("(\w+)"\)')
        self.re_flow = re.compile(r'@dataFlow\("(\w+)"\)')
        self.re_classification = re.compile(r'@classification\("(\w+)"\)')
        self.re_op = re.compile(r'op\s+(\w+)')
        
        self.graph = nx.DiGraph()
        self.current_zone = "Unknown"
        self.current_node = None
        self.current_classification = None

    def build_graph(self, typespec_code: str) -> nx.DiGraph:
        print(f"[*] INTERPRETER: Parsing Specification...")
        
        # 1. First Pass: Identify Nodes (Components) and Properties
        lines = typespec_code.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Capture Context (Decorators apply to the next definition)
            if match := self.re_trust.search(line):
                self.current_zone = match.group(1)
            
            if match := self.re_classification.search(line):
                self.current_classification = match.group(1)
            
            # Create Nodes
            if match := self.re_namespace.search(line):
                node_name = match.group(1)
                self.graph.add_node(
                    node_name, 
                    type="Component", 
                    trust_zone=self.current_zone,
                    classification=self.current_classification
                )
                self.current_node = node_name
                print(f"    -> Node Created: {node_name} (Zone: {self.current_zone})")

            # Create Edges based on architectural flow patterns
            if match := self.re_op.search(line):
                op_name = match.group(1)
                flow_type = "Control"  # default
                
                # Scan previous lines for decorators
                for j in range(max(0, i-3), i):
                    if '@dataFlow' in lines[j]:
                        flow_match = self.re_flow.search(lines[j])
                        if flow_match:
                            flow_type = flow_match.group(1)
                            break

                # Architecture-specific wiring (matches new TypeSpec)
                if self.current_node == "RAGClient":
                    pass  # Actor, no ops
                elif self.current_node == "GatewayService":
                    # Gateway receives from client
                    self.graph.add_edge("RAGClient", "GatewayService", flow_type="Control", operation=op_name)
                elif self.current_node == "IngestionWorker":
                    # Client -> Gateway -> Ingestion -> VectorStore
                    if op_name == "processUpload":
                        self.graph.add_edge("RAGClient", "GatewayService", flow_type="Ingestion", operation="upload")
                        self.graph.add_edge("GatewayService", "IngestionWorker", flow_type="Ingestion", operation=op_name)
                        self.graph.add_edge("IngestionWorker", "VectorDatastore", flow_type="Control", operation="storeEmbeddings")
                elif self.current_node == "InferenceEngine":
                    # Gateway -> Inference, Datastore -> Inference (retrieval), Inference injects context
                    if op_name == "generateResponse":
                        self.graph.add_edge("GatewayService", "InferenceEngine", flow_type="Control", operation="query")
                        self.graph.add_edge("InferenceEngine", "VectorDatastore", flow_type="Retrieval", operation="fetchEmbeddings")
                        self.graph.add_edge("VectorDatastore", "InferenceEngine", flow_type="ContextInjection", operation="returnChunks")
                        self.graph.add_edge("InferenceEngine", "GatewayService", flow_type="Control", operation=op_name)
                elif self.current_node == "VectorDatastore":
                    # Datastore operations handled by other components
                    pass

        return self.graph

# ==============================================================================
# LAYER 2: THE THREAT COMPILER
# Deterministic Rules applied to the Graph
# ==============================================================================

class ThreatCompiler:
    def __init__(self, graph: nx.DiGraph):
        self.graph = graph
        self.findings: List[Finding] = []
        self.knowledge_graph = get_threat_knowledge_graph()  # Grounding layer

    def compile_threats(self):
        print(f"\n[*] COMPILER: Evaluating Graph Logic with Knowledge Graph...")
        print(f"    Knowledge Graph: {len(self.knowledge_graph.get_all_patterns())} threat patterns loaded")
        
        # Trust levels for boundary analysis
        trust_levels = {"Internet": 0, "DMZ": 1, "Trusted": 2, "HighSide": 3}
        
        # Analyze each edge (data flow) against the knowledge graph
        for u, v, data in self.graph.edges(data=True):
            src_zone = self.graph.nodes[u].get('trust_zone', 'Internet')
            dst_zone = self.graph.nodes[v].get('trust_zone', 'Internet')
            flow_type = data.get('flow_type', 'Control')
            
            # Determine component types for more specific matching
            src_type = self._infer_component_type(u)
            dst_type = self._infer_component_type(v)
            
            # Query knowledge graph for applicable threats
            applicable_patterns = self.knowledge_graph.query_threats_for_flow(
                flow_type=flow_type,
                src_zone=src_zone,
                dst_zone=dst_zone,
                src_component_type=src_type,
                dst_component_type=dst_type
            )
            
            # Generate findings from matched patterns
            for pattern in applicable_patterns:
                self.findings.append(Finding(
                    component=v,  # Target is destination
                    severity=pattern.severity,
                    threat=f"{pattern.name} ({pattern.id})",
                    mitigation="\n".join(f"  - {m}" for m in pattern.mitigations)
                ))
    
    def _infer_component_type(self, component_name: str) -> str:
        """Infer component type from name for knowledge graph queries."""
        name_lower = component_name.lower()
        if 'client' in name_lower:
            return 'Actor'
        elif 'gateway' in name_lower or 'api' in name_lower:
            return 'Gateway'
        elif 'datastore' in name_lower or 'vector' in name_lower or 'store' in name_lower:
            return 'Datastore'
        elif 'llm' in name_lower or 'gemini' in name_lower or 'model' in name_lower:
            return 'LLM'
        elif 'ingest' in name_lower or 'upload' in name_lower:
            return 'IngestionService'
        elif 'retriev' in name_lower or 'context' in name_lower:
            return 'Retriever'
        else:
            return 'Process'

    def generate_report(self):
        print("\n" + "="*60)
        print("SEMANTIC THREAT MODEL REPORT")
        print("="*60)
        for f in self.findings:
            print(f"[{f.severity.upper()}] Component: {f.component}")
            print(f"   Threat:     {f.threat}")
            print(f"   Mitigation: {f.mitigation}")
            print("-" * 60)

# ==============================================================================
# EXECUTION PIPELINE
# ==============================================================================

# The TypeSpec - MUST match rag_model.py architecture
TYPESPEC_SOURCE = """
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
"""

def analyze_typespec(typespec_code: str = TYPESPEC_SOURCE, hf_token: str | None = None):
    """
    Run semantic analysis on TypeSpec source.
    
    Args:
        typespec_code: TypeSpec architecture definition
        hf_token: HuggingFace token (or set HF_TOKEN env var). Required (LLM is mandatory).
    """
    # 1. Interpret
    interpreter = SemanticInterpreter()
    property_graph = interpreter.build_graph(typespec_code)
    
    # 2. Compile (Knowledge Graph)
    compiler = ThreatCompiler(property_graph)
    compiler.compile_threats()
    
    # 3. LLM-Enhanced Analysis (Mandatory)
    hf_token_to_use = hf_token or os.getenv("HF_TOKEN")
    if not hf_token_to_use:
        raise RuntimeError(
            "HF_TOKEN is required (LLM is mandatory). Create a .env file with: HF_TOKEN=hf_..."
        )

    print("\n[*] LLM ANALYZER: Querying gpt-oss for AI-assisted threat detection...")
    llm_analyzer = LLMThreatAnalyzer(api_key=hf_token_to_use)
    llm_findings = llm_analyzer.analyze_architecture(property_graph, typespec_code)
    print(f"    -> LLM identified {len(llm_findings)} additional threats")

    # Merge LLM findings with knowledge graph findings
    for llm_finding in llm_findings:
        compiler.findings.append(
            Finding(
                component=llm_finding.component,
                severity=llm_finding.severity,
                threat=f"{llm_finding.description} ({llm_finding.threat_id})",
                mitigation=llm_finding.mitigation,
            )
        )
    
    # 4. Report
    compiler.generate_report()
    
    return compiler.findings


if __name__ == "__main__":
    analyze_typespec()
