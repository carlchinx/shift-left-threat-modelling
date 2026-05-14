"""
Visualization generator for threat model architecture.

Generates enhanced DFD showing:
- Component types
- Trust zones
- Data flows with types
- Threat severity overlays

Standalone visualization using matplotlib/networkx (no external dependencies).
"""
import os
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from threatmodeling.semantic_compiler import SemanticInterpreter, TYPESPEC_SOURCE
from threatmodeling.threat_knowledge_graph import get_threat_knowledge_graph


def generate_architecture_diagram(
    output_path: str = "out/architecture.png", *, typespec_source: str | None = None, findings: list = None
):
    """Generate comprehensive architecture diagram as standalone PNG with threat overlays.
    
    Args:
        output_path: Path to save the PNG diagram
        typespec_source: TypeSpec architecture definition source
        findings: List of threat findings to overlay on the diagram
    """
    
    # Parse TypeSpec
    typespec_source_to_use = TYPESPEC_SOURCE if typespec_source is None else typespec_source
    interpreter = SemanticInterpreter()
    graph = interpreter.build_graph(typespec_source_to_use)
    
    # Get knowledge graph for context
    kg = get_threat_knowledge_graph()
    
    # Analyze threat findings by component
    threat_severity_map: dict[str, str] = {}
    threat_count_map: dict[str, int] = {}
    
    if findings:
        severity_order = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}
        component_threats: dict[str, list] = {}
        
        for finding in findings:
            component = finding.component if hasattr(finding, 'component') else str(finding)
            severity = finding.severity if hasattr(finding, 'severity') else 'Medium'
            
            if component not in component_threats:
                component_threats[component] = []
            component_threats[component].append(severity)
        
        # Determine highest severity for each component
        for comp_name, severities in component_threats.items():
            highest = min(severities, key=lambda s: severity_order.get(s, 99))
            threat_severity_map[comp_name] = highest
            threat_count_map[comp_name] = len(severities)
    
    # Define trust zone colors
    zone_colors = {
        "Internet": "#ffcccc",
        "DMZ": "#ffffcc",
        "Trusted": "#ccffcc",
        "HighSide": "#ccccff"
    }
    
    # Flow type colors
    flow_colors = {
        "Control": "#808080",
        "Ingestion": "#ff8c00",
        "Retrieval": "#4169e1",
        "ContextInjection": "#dc143c",
        "Inference": "#9370db"
    }
    
    # Group nodes by trust zone
    zones = {}
    for node in graph.nodes():
        zone = graph.nodes[node].get('trust_zone', 'Unknown')
        if zone not in zones:
            zones[zone] = []
        zones[zone].append(node)
    
    # Create hierarchical layout
    pos = {}
    zone_order = ["Internet", "DMZ", "Trusted", "HighSide"]
    y_spacing = 2.0
    x_spacing = 3.0
    
    for zone_idx, zone_name in enumerate(zone_order):
        if zone_name in zones:
            nodes_in_zone = zones[zone_name]
            for node_idx, node in enumerate(nodes_in_zone):
                x = zone_idx * x_spacing
                # Center nodes vertically if multiple in zone
                y_offset = (len(nodes_in_zone) - 1) * y_spacing / 2
                y = node_idx * y_spacing - y_offset
                pos[node] = (x, y)
    
    # Create figure
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_aspect('equal')
    ax.axis('off')

    def _shift_text_by_pixels(text_obj, dx_pixels: float, dy_pixels: float) -> None:
        x_data, y_data = text_obj.get_position()
        x_disp, y_disp = ax.transData.transform((x_data, y_data))
        new_x_data, new_y_data = ax.transData.inverted().transform((x_disp + dx_pixels, y_disp + dy_pixels))
        text_obj.set_position((new_x_data, new_y_data))

    def _resolve_text_overlaps(texts: list, *, max_iter: int = 200, pad_pixels: float = 3.0) -> None:
        if not texts:
            return

        fig.canvas.draw()
        renderer = fig.canvas.get_renderer()

        def _bbox(t):
            return t.get_window_extent(renderer=renderer).expanded(1.02, 1.10)

        for _ in range(max_iter):
            moved_any = False
            bboxes = [_bbox(t) for t in texts]

            for i in range(len(texts)):
                for j in range(i + 1, len(texts)):
                    if not bboxes[i].overlaps(bboxes[j]):
                        continue

                    overlap_y = min(bboxes[i].y1, bboxes[j].y1) - max(bboxes[i].y0, bboxes[j].y0)
                    dy = max(overlap_y + pad_pixels, pad_pixels)
                    direction = 1.0 if bboxes[j].y0 >= bboxes[i].y0 else -1.0
                    _shift_text_by_pixels(texts[j], 0.0, direction * dy)
                    moved_any = True

                    fig.canvas.draw()
                    renderer = fig.canvas.get_renderer()
                    bboxes = [_bbox(t) for t in texts]

            if not moved_any:
                break
    
    # Draw trust zone backgrounds
    zone_rects = {}
    for zone_idx, zone_name in enumerate(zone_order):
        if zone_name in zones:
            x_center = zone_idx * x_spacing
            # Calculate bounds
            y_positions = [pos[n][1] for n in zones[zone_name]]
            y_min, y_max = min(y_positions) - 0.8, max(y_positions) + 0.8
            
            rect = FancyBboxPatch(
                (x_center - 1.2, y_min),
                2.4, y_max - y_min,
                boxstyle="round,pad=0.1",
                facecolor=zone_colors[zone_name],
                edgecolor='black',
                linewidth=2,
                alpha=0.3,
                zorder=0
            )
            ax.add_patch(rect)
            
            # Zone label
            ax.text(x_center, y_max + 0.3, f"Trust Zone:\n{zone_name}",
                   ha='center', va='bottom', fontsize=10, fontweight='bold',
                   bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    # Draw edges first (so they're behind nodes)
    import math
    edge_list = {}  # Track all edges between same node pairs

    edge_label_texts = []
    
    # First pass: collect all edges between same pairs
    edges_data = list(graph.edges(data=True))
    for u, v, data in edges_data:
        pair_key = tuple(sorted([u, v]))
        if pair_key not in edge_list:
            edge_list[pair_key] = []
        edge_list[pair_key].append((u, v, data))
    
    # Second pass: draw edges with proper offsets
    for u, v, data in edges_data:
        flow_type = data.get('flow_type', 'Control')
        operation = data.get('operation', '')
        
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        
        # Determine this edge's index among edges between this pair
        pair_key = tuple(sorted([u, v]))
        edges_for_pair = edge_list[pair_key]
        edge_idx = next(i for i, (eu, ev, ed) in enumerate(edges_for_pair) if eu == u and ev == v and ed == data)
        total_edges_for_pair = len(edges_for_pair)
        
        # Calculate arc curvature
        if total_edges_for_pair == 1:
            arc_rad = 0.1
        else:
            # Distribute edges with different curvatures
            if edge_idx % 2 == 0:
                arc_rad = 0.25 + (edge_idx // 2) * 0.2
            else:
                arc_rad = -(0.25 + (edge_idx // 2) * 0.2)
        
        arrow = FancyArrowPatch(
            (x1, y1), (x2, y2),
            arrowstyle='-|>',
            connectionstyle=f"arc3,rad={arc_rad}",
            color=flow_colors.get(flow_type, 'black'),
            linewidth=2.5,
            alpha=0.8,
            zorder=2
        )
        ax.add_patch(arrow)
        
        # Calculate label position with aggressive perpendicular offset
        dx, dy = x2 - x1, y2 - y1
        edge_length = math.sqrt(dx**2 + dy**2)
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        
        if edge_length > 0 and total_edges_for_pair > 1:
            # Perpendicular vector (normalized)
            perp_x = -dy / edge_length
            perp_y = dx / edge_length
            
            # Large offset: stack labels with 0.8 unit spacing
            base_offset = 0.6
            offset_spacing = 0.8
            
            # Center the stack around the edge
            center_offset = (total_edges_for_pair - 1) * offset_spacing / 2
            this_offset = base_offset + (edge_idx * offset_spacing) - center_offset
            
            label_x = mid_x + perp_x * this_offset
            label_y = mid_y + perp_y * this_offset
        else:
            label_x, label_y = mid_x, mid_y + 0.25
        
        label = flow_type if not operation else f"{flow_type}\n{operation}"
        t = ax.text(label_x, label_y, label,
               ha='center', va='center', fontsize=6,
               bbox=dict(boxstyle='round,pad=0.25', facecolor='white', alpha=0.95, 
                        edgecolor=flow_colors.get(flow_type, 'black'), linewidth=1),
               zorder=3)
        edge_label_texts.append(t)
    
    # Threat severity colors for borders
    severity_colors = {
        "Critical": "#FF0000",   # Red
        "High": "#FF8C00",       # Orange
        "Medium": "#FFD700",     # Gold
        "Low": "#90EE90",        # Light green
    }

    # Draw nodes with threat overlays
    for node in graph.nodes():
        x, y = pos[node]
        node_lower = node.lower()
        
        # Determine border color based on threat severity
        has_threat = node in threat_severity_map
        edge_color = severity_colors.get(threat_severity_map.get(node), "black")
        edge_width = 4 if has_threat else 2
        
        # Determine node shape/style
        if 'client' in node_lower:
            # Actor/client - circle
            circle = plt.Circle((x, y), 0.4, facecolor='#f0f0f0', edgecolor=edge_color, linewidth=edge_width, zorder=3)
            ax.add_patch(circle)
        elif 'datastore' in node_lower or 'vector' in node_lower:
            # Database - cylinder-like
            rect = FancyBboxPatch((x - 0.5, y - 0.3), 1.0, 0.6,
                                 boxstyle="round,pad=0.05",
                                 facecolor='#fffacd', edgecolor=edge_color, linewidth=edge_width, zorder=3)
            ax.add_patch(rect)
        else:
            # Process - rounded rectangle
            rect = FancyBboxPatch((x - 0.5, y - 0.3), 1.0, 0.6,
                                 boxstyle="round,pad=0.1",
                                 facecolor='#e0e0e0', edgecolor=edge_color, linewidth=edge_width, zorder=3)
            ax.add_patch(rect)
        
        # Node label
        ax.text(x, y, node, ha='center', va='center', fontsize=9, fontweight='bold', zorder=4)
        
        # Add threat count badge if threats exist
        if has_threat and node in threat_count_map:
            from matplotlib.patches import Circle
            badge = Circle(
                (x + 0.6, y + 0.4),
                0.15,
                facecolor=edge_color,
                edgecolor="white",
                linewidth=1.5,
                zorder=5,
            )
            ax.add_patch(badge)
            ax.text(
                x + 0.6,
                y + 0.4,
                str(threat_count_map[node]),
                ha="center",
                va="center",
                fontsize=7,
                fontweight="bold",
                color="white",
                zorder=6,
            )

    # Final pass: nudge overlapping edge labels apart
    _resolve_text_overlaps(edge_label_texts)
    
    # Add legend
    legend_elements = [
        mpatches.Patch(color=flow_colors['Control'], label='Control Flow'),
        mpatches.Patch(color=flow_colors['Ingestion'], label='Ingestion (HIGH risk)'),
        mpatches.Patch(color=flow_colors['Retrieval'], label='Retrieval'),
        mpatches.Patch(color=flow_colors['ContextInjection'], label='Context Injection (CRITICAL)'),
        mpatches.Patch(color=flow_colors['Inference'], label='LLM Inference'),
    ]
    
    # Add threat severity legend if threats exist
    if threat_severity_map:
        legend_elements.append(mpatches.Patch(color="white", label="───────────────"))
        legend_elements.append(mpatches.Patch(color="white", label="Threat Severity:"))
        legend_elements.append(mpatches.Patch(color=severity_colors["Critical"], label="Critical"))
        legend_elements.append(mpatches.Patch(color=severity_colors["High"], label="High"))
        legend_elements.append(mpatches.Patch(color=severity_colors["Medium"], label="Medium"))
        legend_elements.append(mpatches.Patch(color=severity_colors["Low"], label="Low"))
    
    ax.legend(handles=legend_elements, loc='lower left', fontsize=8, framealpha=0.95)
    
    # Set axis limits with padding
    if pos:
        all_x = [pos[n][0] for n in pos]
        all_y = [pos[n][1] for n in pos]
        ax.set_xlim(min(all_x) - 2, max(all_x) + 2)
        ax.set_ylim(min(all_y) - 2, max(all_y) + 2)
    
    # Title
    plt.title("RAG Threat Model Architecture\nSTRIDE Analysis with Trust Zones", 
             fontsize=14, fontweight='bold', pad=20)
    
    # Add generated timestamp on the image (bottom-right corner in figure coords)
    timestamp = datetime.now().strftime("Generated %Y-%m-%d %H:%M:%S") + " | linkedin.com/in/phiricharles"
    fig.text(0.99, 0.01, timestamp, ha='right', va='bottom', fontsize=8, color='#555555')
    
    # Save figure
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    
    print(f"✓ Architecture diagram saved to: {output_path}")
    print(f"\nDiagram includes:")
    print(f"  - {len(graph.nodes())} components across {len(zones)} trust zones")
    print(f"  - {len(graph.edges())} data flows")
    print(f"  - {len(kg.get_all_patterns())} threat patterns in knowledge graph")
    print(f"\nStandalone PNG image generated (no external tools required)")


if __name__ == "__main__":
    generate_architecture_diagram()
