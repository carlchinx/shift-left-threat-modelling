import os
from datetime import datetime
from typing import Any

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch


def visualize_dfd(tm: Any, output_path: str = "out/dfd.png", findings: list = None) -> str:
    """Generate standalone PyTM DFD visualization as a PNG with threat overlays.

    Args:
        tm: PyTM threat model
        output_path: Output path for PNG file
        findings: List of threat findings to overlay on the diagram

    Returns the output_path for convenience.
    """

    # Extract components and flows from PyTM model
    components: dict[str, dict[str, str]] = {}
    flows: list[dict[str, str]] = []
    
    # Analyze threat findings by component
    threat_severity_map: dict[str, str] = {}
    threat_count_map: dict[str, int] = {}
    
    if findings:
        severity_order = {"Very High": 0, "High": 1, "Medium": 2, "Low": 3, "Very Low": 4}
        component_threats: dict[str, list] = {}
        
        for finding in findings:
            target = finding.target if hasattr(finding, 'target') else str(finding)
            severity = finding.severity if hasattr(finding, 'severity') else 'Medium'
            
            if target not in component_threats:
                component_threats[target] = []
            component_threats[target].append(severity)
        
        # Determine highest severity for each component
        for comp_name, severities in component_threats.items():
            highest = min(severities, key=lambda s: severity_order.get(s, 99))
            threat_severity_map[comp_name] = highest
            threat_count_map[comp_name] = len(severities)

    # Collect all elements
    for element in tm._elements:
        element_type = type(element).__name__

        if element_type in ["Actor", "Process", "Datastore", "Server", "Lambda", "ExternalEntity"]:
            boundary = getattr(element, "inBoundary", None)
            zone_name = boundary.name if boundary else "Unknown"
            components[element.name] = {"type": element_type, "zone": zone_name}
        elif element_type == "Dataflow":
            flows.append(
                {
                    "source": element.source.name,
                    "sink": element.sink.name,
                    "name": element.name,
                    "protocol": getattr(element, "protocol", ""),
                    "flow_type": getattr(element, "flowType", "Control"),
                }
            )

    # Define positions (similar to semantic visualize layout)
    zone_order = ["Developer Environment", "Google Gemini API", "Google Internal Systems", 
                  "Internet", "DMZ", "Trusted", "HighSide", "Unknown"]
    zone_components: dict[str, list[str]] = {}
    
    # Initialize with all unique zones found
    for name, info in components.items():
        zone = info["zone"]
        if zone not in zone_components:
            zone_components[zone] = []
        zone_components[zone].append(name)
    
    # Sort zones by zone_order preference
    sorted_zones = [z for z in zone_order if z in zone_components]
    sorted_zones.extend([z for z in zone_components.keys() if z not in zone_order])

    pos: dict[str, tuple[float, float]] = {}
    x_spacing = 3.0
    y_spacing = 2.0

    for zone_idx, zone_name in enumerate(sorted_zones):
        nodes_in_zone = zone_components[zone_name]
        for node_idx, node in enumerate(nodes_in_zone):
            x = zone_idx * x_spacing
            y_offset = (len(nodes_in_zone) - 1) * y_spacing / 2
            y = node_idx * y_spacing - y_offset
            pos[node] = (x, y)

    # Create figure
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_aspect("equal")
    ax.axis("off")

    def _shift_text_by_pixels(text_obj, dx_pixels: float, dy_pixels: float) -> None:
        x_data, y_data = text_obj.get_position()
        x_disp, y_disp = ax.transData.transform((x_data, y_data))
        new_x_data, new_y_data = ax.transData.inverted().transform((x_disp + dx_pixels, y_disp + dy_pixels))
        text_obj.set_position((new_x_data, new_y_data))

    def _resolve_text_overlaps(texts: list, *, max_iter: int = 200, pad_pixels: float = 3.0) -> None:
        if not texts:
            return

        # Ensure a renderer exists
        fig.canvas.draw()
        renderer = fig.canvas.get_renderer()

        def _bbox(t):
            # Slight expansion makes "almost touching" count as overlap
            return t.get_window_extent(renderer=renderer).expanded(1.02, 1.10)

        for _ in range(max_iter):
            moved_any = False
            bboxes = [_bbox(t) for t in texts]

            for i in range(len(texts)):
                for j in range(i + 1, len(texts)):
                    if not bboxes[i].overlaps(bboxes[j]):
                        continue

                    # Compute vertical overlap in pixels
                    overlap_y = min(bboxes[i].y1, bboxes[j].y1) - max(bboxes[i].y0, bboxes[j].y0)
                    dy = max(overlap_y + pad_pixels, pad_pixels)

                    # Push the later label away (stable-ish ordering)
                    direction = 1.0 if bboxes[j].y0 >= bboxes[i].y0 else -1.0
                    _shift_text_by_pixels(texts[j], 0.0, direction * dy)
                    moved_any = True

                    # Refresh renderer/bboxes after moving
                    fig.canvas.draw()
                    renderer = fig.canvas.get_renderer()
                    bboxes = [_bbox(t) for t in texts]

            if not moved_any:
                break

    zone_colors = {
        "Developer Environment": "#ffcccc",
        "Google Gemini API": "#ffffcc",
        "Google Internal Systems": "#ccffcc",
        "Internet": "#ffcccc",
        "DMZ": "#ffffcc",
        "Trusted": "#ccffcc",
        "HighSide": "#ccccff",
        "Unknown": "#eeeeee",
    }

    flow_colors = {
        "Control": "#808080",
        "Ingestion": "#ff8c00",
        "Retrieval": "#4169e1",
        "ContextInjection": "#dc143c",
        "Inference": "#9370db",
    }

    # Draw trust zone backgrounds
    for zone_idx, zone_name in enumerate(sorted_zones):
        if zone_name in zone_components and zone_components[zone_name]:
            x_center = zone_idx * x_spacing
            y_positions = [pos[n][1] for n in zone_components[zone_name]]
            y_min, y_max = min(y_positions) - 0.8, max(y_positions) + 0.8

            rect = FancyBboxPatch(
                (x_center - 1.2, y_min),
                2.4,
                y_max - y_min,
                boxstyle="round,pad=0.1",
                facecolor=zone_colors.get(zone_name, "#eeeeee"),
                edgecolor="black",
                linewidth=2,
                alpha=0.3,
                zorder=0,
            )
            ax.add_patch(rect)

            ax.text(
                x_center,
                y_max + 0.3,
                f"Trust Zone:\n{zone_name}",
                ha="center",
                va="bottom",
                fontsize=10,
                fontweight="bold",
                bbox=dict(boxstyle="round", facecolor="white", alpha=0.8),
            )

    # Draw flows
    import math
    edge_list = {}  # Track all edges between same node pairs

    edge_label_texts = []
    
    # First pass: collect all edges between same pairs
    for flow in flows:
        if flow["source"] in pos and flow["sink"] in pos:
            pair_key = tuple(sorted([flow["source"], flow["sink"]]))
            if pair_key not in edge_list:
                edge_list[pair_key] = []
            edge_list[pair_key].append(flow)
    
    # Second pass: draw flows with proper offsets
    for flow in flows:
        if flow["source"] in pos and flow["sink"] in pos:
            x1, y1 = pos[flow["source"]]
            x2, y2 = pos[flow["sink"]]

            flow_type = flow.get("flow_type", "Control")
            
            # Determine this edge's index among edges between this pair
            pair_key = tuple(sorted([flow["source"], flow["sink"]]))
            edges_for_pair = edge_list[pair_key]
            edge_idx = edges_for_pair.index(flow)
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
                (x1, y1),
                (x2, y2),
                arrowstyle="-|>",
                connectionstyle=f"arc3,rad={arc_rad}",
                color=flow_colors.get(flow_type, "black"),
                linewidth=2.5,
                alpha=0.8,
                zorder=2,
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
            
            label = f"{flow_type}\n{flow['name']}" if flow.get("name") else flow_type
            t = ax.text(
                label_x,
                label_y,
                label,
                ha="center",
                va="center",
                fontsize=6,
                bbox=dict(
                    boxstyle="round,pad=0.25",
                    facecolor="white",
                    alpha=0.95,
                    edgecolor=flow_colors.get(flow_type, "black"),
                    linewidth=1,
                ),
                zorder=3,
            )
            edge_label_texts.append(t)

    # Threat severity colors for borders
    severity_colors = {
        "Very High": "#FF0000",  # Red
        "High": "#FF8C00",      # Orange
        "Medium": "#FFD700",    # Gold
        "Low": "#90EE90",       # Light green
        "Very Low": "#D3D3D3"  # Light gray
    }

    # Draw nodes with threat overlays
    for name, info in components.items():
        if name not in pos:
            continue

        x, y = pos[name]
        comp_type = info["type"]
        
        # Determine border color based on threat severity
        has_threat = name in threat_severity_map
        edge_color = severity_colors.get(threat_severity_map.get(name), "black")
        edge_width = 4 if has_threat else 2

        if comp_type == "Actor":
            circle = Circle(
                (x, y),
                0.4,
                facecolor="#f0f0f0",
                edgecolor=edge_color,
                linewidth=edge_width,
                zorder=3,
            )
            ax.add_patch(circle)
        elif comp_type == "Datastore":
            rect = FancyBboxPatch(
                (x - 0.5, y - 0.3),
                1.0,
                0.6,
                boxstyle="round,pad=0.05",
                facecolor="#fffacd",
                edgecolor=edge_color,
                linewidth=edge_width,
                zorder=3,
            )
            ax.add_patch(rect)
        elif comp_type in ["Server", "Lambda", "Process"]:
            rect = FancyBboxPatch(
                (x - 0.5, y - 0.3),
                1.0,
                0.6,
                boxstyle="round,pad=0.1",
                facecolor="#e0e0e0",
                edgecolor=edge_color,
                linewidth=edge_width,
                zorder=3,
            )
            ax.add_patch(rect)
        else:
            # Default for any other type
            rect = FancyBboxPatch(
                (x - 0.5, y - 0.3),
                1.0,
                0.6,
                boxstyle="round,pad=0.1",
                facecolor="#cccccc",
                edgecolor=edge_color,
                linewidth=edge_width,
                zorder=3,
            )
            ax.add_patch(rect)

        ax.text(
            x,
            y,
            name,
            ha="center",
            va="center",
            fontsize=9,
            fontweight="bold",
            zorder=4,
        )
        
        # Add threat count badge if threats exist
        if has_threat and name in threat_count_map:
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
                str(threat_count_map[name]),
                ha="center",
                va="center",
                fontsize=7,
                fontweight="bold",
                color="white",
                zorder=6,
            )

    # Final pass: nudge overlapping edge labels apart
    _resolve_text_overlaps(edge_label_texts)

    legend_elements = [
        mpatches.Patch(color=flow_colors["Control"], label="Control Flow"),
        mpatches.Patch(color=flow_colors["Ingestion"], label="Ingestion (HIGH risk)"),
        mpatches.Patch(color=flow_colors["Retrieval"], label="Retrieval"),
        mpatches.Patch(
            color=flow_colors["ContextInjection"], label="Context Injection (CRITICAL)"
        ),
        mpatches.Patch(color=flow_colors["Inference"], label="LLM Inference"),
    ]
    
    # Add threat severity legend if threats exist
    if threat_severity_map:
        legend_elements.append(mpatches.Patch(color="white", label="───────────────"))
        legend_elements.append(mpatches.Patch(color="white", label="Threat Severity:"))
        legend_elements.append(mpatches.Patch(color=severity_colors["Very High"], label="Very High"))
        legend_elements.append(mpatches.Patch(color=severity_colors["High"], label="High"))
        legend_elements.append(mpatches.Patch(color=severity_colors["Medium"], label="Medium"))
        legend_elements.append(mpatches.Patch(color=severity_colors["Low"], label="Low"))
    
    ax.legend(handles=legend_elements, loc="lower left", fontsize=8, framealpha=0.95)

    if pos:
        all_x = [pos[n][0] for n in pos]
        all_y = [pos[n][1] for n in pos]
        ax.set_xlim(min(all_x) - 2, max(all_x) + 2)
        ax.set_ylim(min(all_y) - 2, max(all_y) + 2)

    plt.title(f"{tm.name}\nPyTM Data Flow Diagram", fontsize=14, fontweight="bold", pad=20)

    # Add generated timestamp on the image (bottom-right corner in figure coords)
    timestamp = datetime.now().strftime("Generated %Y-%m-%d %H:%M:%S") + " | linkedin.com/in/phiricharles"
    fig.text(0.99, 0.01, timestamp, ha="right", va="bottom", fontsize=8, color="#555555")

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches="tight", facecolor="white")
    plt.close(fig)

    return output_path
