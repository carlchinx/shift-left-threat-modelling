# Notebooks

Jupyter notebooks supplementing the main pipeline.

| Notebook | Purpose | Outputs |
|---|---|---|
| [`gemini_filesearch_pytm_threat_model.ipynb`](gemini_filesearch_pytm_threat_model.ipynb) | PyTM threat model for the Gemini File Search managed-RAG API: builds the model, renders a DFD, generates a PlantUML sequence diagram, and emits a Markdown threat report. | `out/gemini_dfd.png`, `out/gemini_sequence.puml` (+ `.png` if Java available), `out/gemini_threat_report.md` |

## Running locally

```powershell
# From the repository root
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt jupyter
jupyter notebook notebooks\
```

Native binaries (`graphviz` `dot`, optional `java` for PlantUML) are detected,
not installed by the notebook itself. See the notebook's *Prerequisites & setup*
section for OS-specific commands.

## License

MIT — © 2026 Dr. Charles C. Phiri. See the project [`LICENSE`](../LICENSE).
