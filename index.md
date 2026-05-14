---
layout: default
title: Shift-Left Threat Modelling
description: PyTM + Semantic Compiler for a Gemini-style Managed RAG architecture.
---

# Shift-Left Threat Modelling

A Python project that models a **Gemini-style Managed RAG** architecture using **two complementary approaches**:

1. **PyTM** — Traditional threat modeling with data flow diagrams.
2. **Semantic Compiler** — Graph-based threat analysis from TypeSpec-style architecture definitions.

> **Author:** Dr. Charles C. Phiri, CITP, Senior IEEE Member, Fellow (ICTAM)
> **Affiliation:** Independent Researcher / ICTAM Fellow
> **License:** [MIT](LICENSE) © 2026 Charles C. Phiri

## Background & Article

**Explainer (short):**

<iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7426027060369948672?compact=1" height="399" width="504" frameborder="0" allowfullscreen="" title="Embedded post — Explainer"></iframe>

**Main article:**

<iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7423736867189198848?collapsed=1" height="636" width="504" frameborder="0" allowfullscreen="" title="Embedded post — Main article"></iframe>

## Documentation

- [Project README](README.md)
- [Compliance & Validation](docs/COMPLIANCE.md)
- [Project Summary](PROJECT_SUMMARY.md)
- [Setup Guide](SETUP.md)
- [LLM Configuration](LLM_CONFIG.md)
- [Standalone Visualization](STANDALONE_VISUALIZATION.md)

## Generated Artifacts (`out/`)

Latest pipeline outputs published with this site:

### Reports
- [Threat Modeling Report (Markdown)](out/report.md)
- [Threat Modeling Report (HTML)](out/report.html)
- [Gemini Threat Report](out/gemini_threat_report.md)
- [Verification Results (JSON)](out/verification.json)

### Diagrams
- [Architecture diagram](out/architecture.png)
- [Data Flow Diagram (PyTM)](out/dfd.png)
- [Gemini DFD](out/gemini_dfd.png)
- [Gemini Sequence (PlantUML source)](out/gemini_sequence.puml)

![Architecture](out/architecture.png)

![Data Flow Diagram](out/dfd.png)

## Source

The implementation lives in the GitHub repository:
[carlchinx/shift-left-threat-modelling](https://github.com/carlchinx/shift-left-threat-modelling)

## Quick Start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -r requirements.txt
python -m threatmodeling.validate
streamlit run app.py
```

---

## License

This project is licensed under the [MIT License](LICENSE).
Copyright © 2026 **Dr. Charles C. Phiri**, CITP, Senior IEEE Member, Fellow (ICTAM).
