"""
Threat Knowledge Graph

This knowledge graph serves as the grounding layer for semantic threat detection.
It encodes threat patterns, STRIDE categories, and architectural anti-patterns
that the semantic compiler queries when analyzing architectures.
"""
import networkx as nx
from dataclasses import dataclass
from typing import List, Set


@dataclass
class ThreatPattern:
    """A reusable threat pattern in the knowledge graph."""
    id: str
    name: str
    description: str
    stride_category: str  # Spoofing, Tampering, Repudiation, InfoDisclosure, DoS, ElevationOfPrivilege
    severity: str
    triggers: List[str]  # Conditions that activate this pattern
    mitigations: List[str]
    cwe_ids: List[str] = None
    capec_ids: List[str] = None


class ThreatKnowledgeGraph:
    """
    Knowledge graph encoding threat patterns for RAG/LLM architectures.
    
    This graph is queried by the semantic compiler to detect threats
    based on architectural patterns, flow types, and trust boundaries.
    """
    
    def __init__(self):
        self.graph = nx.DiGraph()
        self._build_threat_ontology()
    
    def _build_threat_ontology(self):
        """Build the threat pattern knowledge graph."""
        
        # === STRIDE-based threat patterns ===
        
        patterns = [
            ThreatPattern(
                id="STRIDE-S-001",
                name="Trust Boundary Violation",
                description="Data flow crosses from lower to higher trust zone without validation",
                stride_category="Spoofing",
                severity="Medium",
                triggers=[
                    "flow_crosses_trust_boundary",
                    "source_trust_level < destination_trust_level"
                ],
                mitigations=[
                    "Implement schema validation at boundary",
                    "Require authentication and authorization",
                    "Use mutual TLS for inter-zone communication"
                ],
                cwe_ids=["CWE-20", "CWE-346"],
                capec_ids=["CAPEC-111"]
            ),
            
            ThreatPattern(
                id="STRIDE-T-001",
                name="Malicious Content Ingestion",
                description="Untrusted file upload may contain executable code or exploits",
                stride_category="Tampering",
                severity="High",
                triggers=[
                    "flow_type == 'Ingestion'",
                    "crosses_trust_boundary",
                    "handles_binary_data"
                ],
                mitigations=[
                    "Sandboxed parsing environment",
                    "Magic number and MIME type verification",
                    "Antivirus/malware scanning",
                    "Content Security Policy enforcement",
                    "Input size limits"
                ],
                cwe_ids=["CWE-434", "CWE-94"],
                capec_ids=["CAPEC-1", "CAPEC-242"]
            ),
            
            ThreatPattern(
                id="AI-INJECT-001",
                name="Indirect Prompt Injection via Retrieval",
                description="Malicious instructions embedded in retrieved context can hijack LLM behavior",
                stride_category="ElevationOfPrivilege",
                severity="Critical",
                triggers=[
                    "flow_type == 'ContextInjection'",
                    "source_component_type == 'Datastore'",
                    "destination_component_type == 'LLM'"
                ],
                mitigations=[
                    "Treat all retrieved content as untrusted input",
                    "Use ChatML or structured prompting to separate data from instructions",
                    "Implement output filtering and validation",
                    "Content provenance tracking",
                    "Limit LLM capabilities (function calling restrictions)"
                ],
                cwe_ids=["CWE-74", "CWE-94"],
                capec_ids=["CAPEC-248"]
            ),
            
            ThreatPattern(
                id="AI-POISON-001",
                name="Training Data Poisoning via Embedding Store",
                description="Attacker poisons vector store with malicious embeddings to influence retrieval",
                stride_category="Tampering",
                severity="High",
                triggers=[
                    "component_type == 'VectorDatastore'",
                    "accepts_external_input == True"
                ],
                mitigations=[
                    "Input validation on ingestion pipeline",
                    "Embedding integrity checks",
                    "Anomaly detection on vector distributions",
                    "Access control on embedding storage"
                ],
                cwe_ids=["CWE-20"],
                capec_ids=["CAPEC-149"]
            ),
            
            ThreatPattern(
                id="AI-LEAK-001",
                name="Model Inversion / Prompt Leakage",
                description="Sensitive data from training or system prompts leaked via LLM responses",
                stride_category="InformationDisclosure",
                severity="High",
                triggers=[
                    "component_type == 'LLM'",
                    "handles_sensitive_data == True"
                ],
                mitigations=[
                    "Output filtering and PII detection",
                    "Differential privacy techniques",
                    "Prompt guarding and system message protection",
                    "Rate limiting and monitoring"
                ],
                cwe_ids=["CWE-200"],
                capec_ids=["CAPEC-116"]
            ),
            
            ThreatPattern(
                id="STRIDE-I-001",
                name="Data Exfiltration via Retrieval",
                description="Unauthorized access to sensitive embeddings through retrieval queries",
                stride_category="InformationDisclosure",
                severity="Medium",
                triggers=[
                    "flow_type == 'Retrieval'",
                    "source_component_type == 'Datastore'",
                    "data_classification in ['Confidential', 'Restricted']"
                ],
                mitigations=[
                    "Query authorization and filtering",
                    "Data classification enforcement",
                    "Audit logging of all retrieval operations",
                    "Row-level security on vector store"
                ],
                cwe_ids=["CWE-200", "CWE-359"],
                capec_ids=["CAPEC-116"]
            ),
            
            ThreatPattern(
                id="AI-DOS-001",
                name="Resource Exhaustion via LLM Overload",
                description="Attacker submits computationally expensive prompts to DoS the system",
                stride_category="DenialOfService",
                severity="Medium",
                triggers=[
                    "component_type == 'LLM'",
                    "public_facing == True"
                ],
                mitigations=[
                    "Rate limiting per user/API key",
                    "Token limits on input/output",
                    "Request timeout enforcement",
                    "Cost-based throttling"
                ],
                cwe_ids=["CWE-400"],
                capec_ids=["CAPEC-469"]
            ),
        ]
        
        # Add patterns to graph
        for pattern in patterns:
            self.graph.add_node(
                pattern.id,
                pattern=pattern,
                type="ThreatPattern",
                stride=pattern.stride_category,
                severity=pattern.severity
            )
        
        # Add STRIDE categories
        stride_categories = ["Spoofing", "Tampering", "Repudiation", 
                            "InformationDisclosure", "DenialOfService", 
                            "ElevationOfPrivilege"]
        
        for category in stride_categories:
            self.graph.add_node(category, type="STRIDECategory")
        
        # Link patterns to STRIDE categories
        for pattern in patterns:
            self.graph.add_edge(pattern.id, pattern.stride_category, relationship="belongs_to")
    
    def query_threats_for_flow(self, flow_type: str, src_zone: str, dst_zone: str, 
                                src_component_type: str = None, 
                                dst_component_type: str = None) -> List[ThreatPattern]:
        """
        Query the knowledge graph for applicable threats given a data flow.
        
        This is the grounding mechanism for semantic threat detection.
        """
        applicable_threats = []
        
        trust_levels = {"Internet": 0, "DMZ": 1, "Trusted": 2, "HighSide": 3}
        crosses_boundary = trust_levels.get(src_zone, 0) < trust_levels.get(dst_zone, 0)
        
        for node_id in self.graph.nodes():
            node_data = self.graph.nodes[node_id]
            if node_data.get("type") != "ThreatPattern":
                continue
            
            pattern = node_data["pattern"]
            
            # Evaluate triggers
            matches = False
            
            for trigger in pattern.triggers:
                if "flow_type ==" in trigger:
                    expected_flow = trigger.split("==")[1].strip().strip("'\"")
                    if flow_type == expected_flow:
                        matches = True
                
                if "flow_crosses_trust_boundary" in trigger and crosses_boundary:
                    matches = True
                
                if "source_trust_level < destination_trust_level" in trigger and crosses_boundary:
                    matches = True
                
                if "source_component_type ==" in trigger and src_component_type:
                    expected = trigger.split("==")[1].strip().strip("'\"")
                    if src_component_type == expected:
                        matches = True
                
                if "destination_component_type ==" in trigger and dst_component_type:
                    expected = trigger.split("==")[1].strip().strip("'\"")
                    if dst_component_type == expected:
                        matches = True
            
            if matches:
                applicable_threats.append(pattern)
        
        return applicable_threats
    
    def get_all_patterns(self) -> List[ThreatPattern]:
        """Get all threat patterns in the knowledge graph."""
        patterns = []
        for node_id in self.graph.nodes():
            node_data = self.graph.nodes[node_id]
            if node_data.get("type") == "ThreatPattern":
                patterns.append(node_data["pattern"])
        return patterns


# Singleton instance
_knowledge_graph = None

def get_threat_knowledge_graph() -> ThreatKnowledgeGraph:
    """Get the global threat knowledge graph instance."""
    global _knowledge_graph
    if _knowledge_graph is None:
        _knowledge_graph = ThreatKnowledgeGraph()
    return _knowledge_graph
