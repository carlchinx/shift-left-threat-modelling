from __future__ import annotations

import base64
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Optional


@dataclass(frozen=True)
class ReportInputs:
    typespec_source: str
    compliance_ok: bool
    compliance_log: str
    semantic_log: str
    findings: Iterable
    pytm_log: str
    pytm_findings: Iterable
    architecture_png_path: Optional[str]
    dfd_png_path: Optional[str]


def _read_png_as_data_uri(path: Path) -> str | None:
    if not path.exists():
        return None
    data = path.read_bytes()
    b64 = base64.b64encode(data).decode("ascii")
    return f"data:image/png;base64,{b64}"


def _severity_sort_key(severity: str) -> int:
    order = {"Critical": 0, "High": 1, "Medium": 2, "Low": 3}
    return order.get(severity, 99)


def write_report(output_dir: str, inputs: ReportInputs) -> tuple[str, str]:
    """Write a full report as Markdown + standalone HTML.

    Returns:
        (markdown_path, html_path)
    """

    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    created = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")

    findings_sorted = sorted(list(inputs.findings), key=lambda f: _severity_sort_key(getattr(f, "severity", "")))
    pytm_sorted = list(inputs.pytm_findings)

    md_path = out_dir / "report.md"
    html_path = out_dir / "report.html"

    md_lines: list[str] = []
    md_lines.append(f"# Threat Modeling Report\n\nGenerated: {created}\n")

    md_lines.append("## Inputs\n")
    md_lines.append("- Source: Architecture TypeSpec text\n")
    md_lines.append("- LLM: HuggingFace Router (OpenAI-compatible), model `openai/gpt-oss-20b:groq`\n")

    md_lines.append("## Compliance\n")
    md_lines.append(f"- Status: {'✅ Compliant' if inputs.compliance_ok else '❌ Non-compliant'}\n")
    md_lines.append("\n<details><summary>Compliance log</summary>\n\n```text\n")
    md_lines.append(inputs.compliance_log.rstrip() + "\n")
    md_lines.append("```\n\n</details>\n")

    md_lines.append("## Semantic Findings (KG-grounded + LLM)\n")
    md_lines.append(f"Total findings: **{len(findings_sorted)}**\n")

    if findings_sorted:
        md_lines.append("\n| Severity | Component | Threat | Mitigation |\n|---|---|---|---|\n")
        for f in findings_sorted:
            sev = getattr(f, "severity", "")
            comp = getattr(f, "component", "")
            threat = getattr(f, "threat", "")
            mitigation = getattr(f, "mitigation", "").replace("\n", "<br>")
            md_lines.append(f"| {sev} | {comp} | {threat} | {mitigation} |\n")

    md_lines.append("\n<details><summary>Semantic log</summary>\n\n```text\n")
    md_lines.append(inputs.semantic_log.rstrip() + "\n")
    md_lines.append("```\n\n</details>\n")

    md_lines.append("## PyTM Findings\n")
    md_lines.append(f"Total findings: **{len(pytm_sorted)}**\n")

    if pytm_sorted:
        md_lines.append("\n| # | Threat ID | Description | Target | Severity |\n|---:|---|---|---|---|\n")
        for i, finding in enumerate(pytm_sorted, 1):
            md_lines.append(
                "| "
                + " | ".join(
                    [
                        str(i),
                        str(getattr(finding, "threat_id", "")),
                        str(getattr(finding, "description", "")),
                        str(getattr(finding, "target", "")),
                        str(getattr(finding, "severity", "")),
                    ]
                )
                + " |\n"
            )

    md_lines.append("\n<details><summary>PyTM log</summary>\n\n```text\n")
    md_lines.append(inputs.pytm_log.rstrip() + "\n")
    md_lines.append("```\n\n</details>\n")

    md_lines.append("## Diagrams\n")
    if inputs.architecture_png_path:
        md_lines.append(f"- Architecture: `{inputs.architecture_png_path}`\n")
    if inputs.dfd_png_path:
        md_lines.append(f"- PyTM DFD: `{inputs.dfd_png_path}`\n")

    md_path.write_text("".join(md_lines), encoding="utf-8")

    arch_uri = _read_png_as_data_uri(Path(inputs.architecture_png_path)) if inputs.architecture_png_path else None
    dfd_uri = _read_png_as_data_uri(Path(inputs.dfd_png_path)) if inputs.dfd_png_path else None

    def esc(text: str) -> str:
        return (
            text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )

    html = [
        "<!doctype html>",
        "<html>",
        "<head>",
        "<meta charset='utf-8' />",
        "<meta name='viewport' content='width=device-width, initial-scale=1' />",
        "<title>Threat Modeling Report</title>",
        "<style>",
        "body{font-family:Segoe UI,Arial,sans-serif;max-width:1100px;margin:24px auto;padding:0 16px;}",
        ".badge{display:inline-block;padding:2px 8px;border-radius:999px;font-size:12px;border:1px solid #ccc;}",
        ".ok{background:#e8fff0;border-color:#9ee6b2;}",
        ".bad{background:#ffecec;border-color:#ffb3b3;}",
        "table{border-collapse:collapse;width:100%;margin:12px 0;}",
        "th,td{border:1px solid #ddd;padding:8px;vertical-align:top;}",
        "th{background:#f6f6f6;text-align:left;}",
        "details{margin:10px 0;}",
        "pre{background:#0b0b0b;color:#e7e7e7;padding:12px;border-radius:8px;overflow:auto;}",
        "img{max-width:100%;border:1px solid #ddd;border-radius:10px;}",
        "</style>",
        "</head>",
        "<body>",
        f"<h1>Threat Modeling Report</h1>",
        f"<div>Generated: <code>{esc(created)}</code></div>",
        "<h2>Compliance</h2>",
        f"<div class='badge {'ok' if inputs.compliance_ok else 'bad'}'>",
        ("✅ Compliant" if inputs.compliance_ok else "❌ Non-compliant"),
        "</div>",
        "<details><summary>Compliance log</summary><pre>",
        esc(inputs.compliance_log.rstrip()),
        "</pre></details>",
        "<h2>Semantic Findings (KG-grounded + LLM)</h2>",
        f"<div>Total findings: <b>{len(findings_sorted)}</b></div>",
    ]

    if findings_sorted:
        html.append("<table><thead><tr><th>Severity</th><th>Component</th><th>Threat</th><th>Mitigation</th></tr></thead><tbody>")
        for f in findings_sorted:
            html.append(
                "<tr>"
                f"<td>{esc(str(getattr(f, 'severity', '')))}</td>"
                f"<td>{esc(str(getattr(f, 'component', '')))}</td>"
                f"<td>{esc(str(getattr(f, 'threat', '')))}</td>"
                f"<td>{esc(str(getattr(f, 'mitigation', ''))).replace(chr(10), '<br>')}</td>"
                "</tr>"
            )
        html.append("</tbody></table>")

    html.extend(
        [
            "<details><summary>Semantic log</summary><pre>",
            esc(inputs.semantic_log.rstrip()),
            "</pre></details>",
            "<h2>PyTM Findings</h2>",
            f"<div>Total findings: <b>{len(pytm_sorted)}</b></div>",
        ]
    )

    if pytm_sorted:
        html.append("<table><thead><tr><th>#</th><th>Threat ID</th><th>Description</th><th>Target</th><th>Severity</th></tr></thead><tbody>")
        for i, finding in enumerate(pytm_sorted, 1):
            html.append(
                "<tr>"
                f"<td>{i}</td>"
                f"<td>{esc(str(getattr(finding, 'threat_id', '')))}</td>"
                f"<td>{esc(str(getattr(finding, 'description', '')))}</td>"
                f"<td>{esc(str(getattr(finding, 'target', '')))}</td>"
                f"<td>{esc(str(getattr(finding, 'severity', '')))}</td>"
                "</tr>"
            )
        html.append("</tbody></table>")

    html.extend(
        [
            "<details><summary>PyTM log</summary><pre>",
            esc(inputs.pytm_log.rstrip()),
            "</pre></details>",
            "<h2>Diagrams</h2>",
        ]
    )

    if arch_uri:
        html.append("<h3>Architecture</h3>")
        html.append(f"<img src='{arch_uri}' alt='Architecture diagram' />")

    if dfd_uri:
        html.append("<h3>PyTM DFD</h3>")
        html.append(f"<img src='{dfd_uri}' alt='DFD diagram' />")

    html.append("</body></html>")
    html_path.write_text("".join(html), encoding="utf-8")

    return str(md_path), str(html_path)
