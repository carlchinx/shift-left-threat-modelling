---
layout: default
title: Home
nav_order: 1
description: PyTM + Semantic Compiler for a Gemini-style Managed RAG architecture — verifiable, auditable, reproducible.
permalink: /
---

# Shift-Left Threat Modelling
{: .fs-9 }

Compile a TypeSpec-style architecture into a **STRIDE threat model** with a **mathematically-verified compliance report** — produced deterministically from source.
{: .fs-5 .fw-300 }

[Get started](#quick-start){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Latest report (HTML)](out/report.html){: .btn .fs-5 .mb-4 .mb-md-0 .mr-2 }
[View on GitHub](https://github.com/carlchinx/shift-left-threat-modelling){: .btn .fs-5 .mb-4 .mb-md-0 }

---

[![Pages build](https://github.com/carlchinx/shift-left-threat-modelling/actions/workflows/jekyll-gh-pages.yml/badge.svg)](https://github.com/carlchinx/shift-left-threat-modelling/actions/workflows/jekyll-gh-pages.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](#quick-start)
[![Last commit](https://img.shields.io/github/last-commit/carlchinx/shift-left-threat-modelling.svg)](https://github.com/carlchinx/shift-left-threat-modelling/commits/main)

> **Author:** Dr. Charles C. Phiri, CITP, Senior IEEE Member, Fellow (ICTAM) · Independent Researcher / ICTAM Fellow
> **License:** [MIT](LICENSE) © 2026 Charles C. Phiri

---

## Architecture at a glance

![Architecture](out/architecture.png)

Two complementary modelling approaches operate over the same architectural source of truth:

1. **PyTM** — Traditional threat modelling with data-flow diagrams.
2. **Semantic Compiler** — Graph-based threat analysis from TypeSpec-style architecture definitions, verified against a formal compliance schema.

![Data Flow Diagram](out/dfd.png)

---

## Latest report
{: .text-delta }

The pipeline writes deterministic artifacts to `out/`. The current run is published with this site:

| Artifact | Format |
|---|---|
| [Threat Modeling Report](out/report.html) | HTML |
| [Threat Modeling Report](out/report.md) | Markdown |
| [Gemini Threat Report](out/gemini_threat_report.md) | Markdown |
| [Verification Results](out/verification.json) | JSON |
| [Architecture Diagram](out/architecture.png) | PNG |
| [PyTM Data Flow Diagram](out/dfd.png) | PNG |
| [Gemini DFD](out/gemini_dfd.png) | PNG |
| [Gemini Sequence (PlantUML source)](out/gemini_sequence.puml) | PUML |

---

## Background & Article

**Explainer (short):**

<iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7426027060369948672?compact=1" height="399" width="504" frameborder="0" allowfullscreen="" title="Embedded post — Explainer"></iframe>

> Anonymous viewers may see a sign-in prompt — LinkedIn requires an account to render embedded posts. Open the [explainer post directly](https://www.linkedin.com/feed/update/urn:li:ugcPost:7426027060369948672/).

**Main article:**

<iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7423736867189198848?collapsed=1" height="636" width="504" frameborder="0" allowfullscreen="" title="Embedded post — Main article"></iframe>

> Open the [main article directly](https://www.linkedin.com/feed/update/urn:li:ugcPost:7423736867189198848/).

---

## Documentation

- [Project README](README.md)
- [Compliance & Validation](docs/COMPLIANCE.md)
- [Project Summary](PROJECT_SUMMARY.md)
- [Setup Guide](SETUP.md)
- [LLM Configuration](LLM_CONFIG.md)
- [Standalone Visualization](STANDALONE_VISUALIZATION.md)

---

## Quick Start

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -r requirements.txt

# 1. Validate compliance between TypeSpec and PyTM specs
python -m threatmodeling.validate

# 2. Launch the interactive dashboard
streamlit run app.py
```

---

## Cite this work

```bibtex
@software{phiri_shift_left_threat_modelling_2026,
  author  = {Phiri, Charles C.},
  title   = {Shift-Left Threat Modelling: PyTM + Semantic Compiler for Managed RAG Architectures},
  year    = {2026},
  url     = {https://github.com/carlchinx/shift-left-threat-modelling},
  license = {MIT}
}
```

---

## License

This project is licensed under the [MIT License](LICENSE).
Copyright © 2026 **Dr. Charles C. Phiri**, CITP, Senior IEEE Member, Fellow (ICTAM).
