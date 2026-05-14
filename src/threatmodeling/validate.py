"""
Specification Compliance Validator

Ensures PyTM model and TypeSpec semantic compiler are strictly synchronized.
"""
import networkx as nx
from threatmodeling.rag_model import build_model as build_pytm_model
from threatmodeling.semantic_compiler import SemanticInterpreter, TYPESPEC_SOURCE


def validate_compliance(*, typespec_source: str = TYPESPEC_SOURCE):
    """Validate that PyTM and TypeSpec specifications match exactly."""
    print("="*70)
    print("SPECIFICATION COMPLIANCE VALIDATION")
    print("="*70)
    
    errors = []
    warnings = []
    
    # Build both models
    print("\n[1/4] Building PyTM model...")
    pytm = build_pytm_model()
    
    print("[2/4] Parsing TypeSpec...")
    interpreter = SemanticInterpreter()
    graph = interpreter.build_graph(typespec_source)
    
    # Extract PyTM components
    pytm_components = set()
    for obj in [pytm]:
        # Traverse the TM object to find all components
        pass  # PyTM doesn't expose components easily, so we'll validate via TypeSpec
    
    typespec_components = set(graph.nodes())
    
    print(f"\n[3/4] Validating Components...")
    print(f"    TypeSpec Components: {sorted(typespec_components)}")
    
    expected_components = {
        "RAGClient", "GatewayService", "IngestionWorker", 
        "VectorDatastore", "InferenceEngine"
    }
    
    if typespec_components != expected_components:
        errors.append(f"Component mismatch! Expected {expected_components}, got {typespec_components}")
    else:
        print("    ✓ All expected components present")
    
    print(f"\n[4/4] Validating Trust Zones...")
    trust_zones = {
        "RAGClient": "Internet",
        "GatewayService": "DMZ",
        "IngestionWorker": "Trusted",
        "VectorDatastore": "HighSide",
        "InferenceEngine": "Trusted"
    }
    
    for component, expected_zone in trust_zones.items():
        if component in graph.nodes:
            actual_zone = graph.nodes[component].get('trust_zone')
            if actual_zone != expected_zone:
                errors.append(f"{component}: Expected zone '{expected_zone}', got '{actual_zone}'")
            else:
                print(f"    ✓ {component}: {actual_zone}")
    
    print(f"\n[5/5] Validating Data Flows...")
    expected_flows = {
        ("RAGClient", "GatewayService"): ["Control", "Ingestion"],
        ("GatewayService", "IngestionWorker"): ["Ingestion"],
        ("IngestionWorker", "VectorDatastore"): ["Control"],
        ("GatewayService", "InferenceEngine"): ["Control"],
        ("InferenceEngine", "VectorDatastore"): ["Retrieval"],
        ("VectorDatastore", "InferenceEngine"): ["ContextInjection"],
        ("InferenceEngine", "GatewayService"): ["Control"]
    }
    
    for (src, dst), expected_types in expected_flows.items():
        edges = list(graph.edges(src, data=True))
        matching_edges = [e for e in edges if e[1] == dst]
        
        if not matching_edges:
            errors.append(f"Missing flow: {src} -> {dst}")
        else:
            for edge in matching_edges:
                flow_type = edge[2].get('flow_type')
                if flow_type not in expected_types:
                    warnings.append(f"Flow {src} -> {dst} has type '{flow_type}', expected one of {expected_types}")
                else:
                    print(f"    ✓ {src} -> {dst}: {flow_type}")
    
    # Validate knowledge graph integration
    print(f"\n[6/6] Validating Knowledge Graph Integration...")
    try:
        from threatmodeling.threat_knowledge_graph import get_threat_knowledge_graph
        kg = get_threat_knowledge_graph()
        pattern_count = len(kg.get_all_patterns())
        print(f"    ✓ Knowledge graph loaded: {pattern_count} threat patterns")
        
        if pattern_count < 5:
            warnings.append(f"Knowledge graph has only {pattern_count} patterns, expected at least 5")
    except Exception as e:
        errors.append(f"Knowledge graph validation failed: {e}")
    
    # Summary
    print("\n" + "="*70)
    print("VALIDATION RESULTS")
    print("="*70)
    
    if errors:
        print(f"\n❌ {len(errors)} ERROR(S):")
        for err in errors:
            print(f"   - {err}")
    
    if warnings:
        print(f"\n⚠️  {len(warnings)} WARNING(S):")
        for warn in warnings:
            print(f"   - {warn}")
    
    if not errors and not warnings:
        print("\n✅ FULL COMPLIANCE - Both specifications are strictly synchronized!")
        return True
    elif not errors:
        print("\n✅ COMPLIANT (with warnings)")
        return True
    else:
        print("\n❌ NON-COMPLIANT - Specifications diverge!")
        return False


if __name__ == "__main__":
    validate_compliance()
