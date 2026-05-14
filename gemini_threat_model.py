# PyTM Gemini File Search Threat Model
# Uses standalone matplotlib visualization (no Graphviz required)

import os
import sys
import subprocess
from pathlib import Path
from collections import Counter, defaultdict

def ensure_python_package(pkg: str) -> None:
    import importlib.util
    if importlib.util.find_spec(pkg) is None:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

ensure_python_package("pytm")

from pytm import TM, Boundary, Actor, Server, Lambda, Datastore, Dataflow

# Import standalone visualization from the existing project
sys.path.insert(0, str(Path(__file__).parent / "src"))
from threatmodeling.pytm_visualize import visualize_dfd

# Critical: reset global state so the cell can be executed repeatedly
TM.reset()

tm = TM("Gemini File Search - Managed RAG API")
tm.description = "Threat model for Gemini File Search RAG API"

# Boundaries
user_boundary = Boundary("Developer Environment")
google_api_boundary = Boundary("Google Gemini API")
internal_managed_boundary = Boundary("Google Internal Systems")

# Elements
developer = Actor("Developer / API Client"); developer.inBoundary = user_boundary

client_app = Server("Gemini SDK / REST Client"); client_app.inBoundary = user_boundary
client_app.providesConfidentiality = True
client_app.providesIntegrity = True

gemini_api = Server("Gemini API Gateway"); gemini_api.inBoundary = google_api_boundary
gemini_api.providesAuthentication = True
gemini_api.providesConfidentiality = True
gemini_api.providesIntegrity = True

auth_service = Server("Auth & Billing Service"); auth_service.inBoundary = google_api_boundary
auth_service.providesAuthentication = True

file_store = Datastore("User File Store"); file_store.inBoundary = internal_managed_boundary
file_store.isEncrypted = True
file_store.providesConfidentiality = True
file_store.providesIntegrity = True

embedder = Lambda("Embedding Service"); embedder.inBoundary = internal_managed_boundary
embedder.providesConfidentiality = True

vector_store = Datastore("Vector Store"); vector_store.inBoundary = internal_managed_boundary
vector_store.isEncrypted = True
vector_store.providesConfidentiality = True

retriever = Lambda("Context Injection Engine"); retriever.inBoundary = internal_managed_boundary
retriever.providesIntegrity = True

llm = Server("Gemini LLM"); llm.inBoundary = internal_managed_boundary
llm.providesConfidentiality = True

# Dataflows helper
def mkflow(src, dst, name, *, encrypted=True, protocol=None, authenticates_source=None):
    f = Dataflow(src, dst, name)
    f.isEncrypted = bool(encrypted)
    if protocol is not None:
        f.protocol = protocol
    if authenticates_source is not None:
        f.authenticatesSource = bool(authenticates_source)
    return f

mkflow(developer, client_app, "API key/token", protocol="HTTPS")
mkflow(client_app, auth_service, "Token validation", authenticates_source=True)
mkflow(developer, client_app, "File upload")
mkflow(client_app, gemini_api, "File to API", protocol="HTTPS")
mkflow(gemini_api, file_store, "Store file")
mkflow(file_store, embedder, "Trigger embedding")
mkflow(embedder, vector_store, "Store vectors")
mkflow(developer, client_app, "User prompt")
mkflow(client_app, gemini_api, "Prompt to API", protocol="HTTPS")
mkflow(gemini_api, retriever, "Query vectors")
mkflow(vector_store, retriever, "Relevant chunks")
mkflow(retriever, llm, "Context + prompt")
mkflow(llm, gemini_api, "LLM response")
mkflow(gemini_api, client_app, "API response", protocol="HTTPS")
mkflow(client_app, developer, "Display response")

# Key fix: evaluate findings explicitly
tm.check()
tm.resolve()

out_dir = Path("out")
out_dir.mkdir(exist_ok=True)
dfd_png = out_dir / "gemini_dfd.png"
seq_puml = out_dir / "gemini_sequence.puml"
report_md = out_dir / "gemini_threat_report.md"

# DFD - Use standalone matplotlib visualization with threat overlay
visualize_dfd(tm, str(dfd_png), findings=tm.findings)

# Sequence diagram source (PlantUML text)
seq_puml.write_text(tm.seq(), encoding="utf-8")

# Note: PlantUML rendering requires Java and plantuml.jar
# To render diagrams: java -jar plantuml.jar out/gemini_sequence.puml

# Findings report
severity_order = {"Very High": 0, "High": 1, "Medium": 2, "Low": 3, "Very Low": 4}
findings = sorted(
    tm.findings,
    key=lambda f: (severity_order.get(f.severity, 99), f.threat_id, f.target, int(f.id))
)

sev_counts = Counter(f.severity for f in findings)
total = len(findings)

lines = []
lines.append(f"# Threat Model Report: {tm.name}\n")
lines.append("## Description\n")
lines.append(f"{tm.description}\n")
lines.append("## Summary Statistics\n")
lines.append(f"- Total findings: **{total}**")
for sev in sorted(sev_counts.keys(), key=lambda s: severity_order.get(s, 99)):
    lines.append(f"- {sev}: **{sev_counts[sev]}**")
lines.append("\n## Findings\n")

by_sev = defaultdict(list)
for f in findings:
    by_sev[f.severity].append(f)

for sev in sorted(by_sev.keys(), key=lambda s: severity_order.get(s, 99)):
    lines.append(f"### Severity: {sev}\n")
    for f in by_sev[sev]:
        lines.append(f"#### F{int(f.id):03d} ({f.threat_id}) — {f.description}\n")
        lines.append(f"- **Target:** {f.target}")
        lines.append(f"- **Details:** {f.details}")
        if f.mitigations:
            lines.append(f"- **Mitigations:** {f.mitigations.strip()}")
        if f.references:
            lines.append(f"- **References:** {f.references.strip()}")
        lines.append("")

report_md.write_text("\n".join(lines), encoding="utf-8")

print("✓ Generated:")
print(f"  - {dfd_png}")
print(f"  - {seq_puml}  (PlantUML source)")
print(f"  - {report_md}")
print("\nSummary:")
for sev in sorted(sev_counts.keys(), key=lambda s: severity_order.get(s, 99)):
    print(f"  {sev}: {sev_counts[sev]}")
print(f"  Total: {total}")