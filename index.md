---
layout: default
title: Shift-Left Threat Modelling
description: PyTM + Semantic Compiler for a Gemini-style Managed RAG architecture.
---

# Shift-Left Threat Modelling

A Python project that models a **Gemini-style Managed RAG** architecture using **two complementary approaches**:

1. **PyTM** — Traditional threat modeling with data flow diagrams.
2. **Semantic Compiler** — Graph-based threat analysis from TypeSpec-style architecture definitions.

## Documentation

- [Project README](README.md)
- [Compliance & Validation](docs/COMPLIANCE.md)
- [Project Summary](PROJECT_SUMMARY.md)
- [Setup Guide](SETUP.md)
- [LLM Configuration](LLM_CONFIG.md)
- [Standalone Visualization](STANDALONE_VISUALIZATION.md)

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
