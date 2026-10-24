# Android Security Research & Thesis Replication Workspace

This repository contains the replication protocol, literature review, static analysis pipeline, and controlled proof-of-concept (PoC) laboratory for Android security research based on the 2025 thesis on Android accessibility services and static malware classification.

> [!NOTE]
> This repository intentionally does **not** contain raw malware samples, private datasets, model checkpoints, or credentials.

---

## 📁 Repository Structure

- [**`poc/`**](file:///D:/DoAnBaomatweb/poc/README.md): Controlled, observation-only Android Accessibility Service PoC (`A11y Observer Lab`) for studying accessibility event mechanics safely.
- [**`tools/`**](file:///D:/DoAnBaomatweb/tools/README.md): Static analysis binaries and tools (Apktool, JADX, FlowDroid) and Python pipeline scripts (`static_analyzer.py`, `extract_features.py`, `classifier_pipeline.py`, etc.).
- [**`data/`**](file:///D:/DoAnBaomatweb/data/README.md): Guidelines and directory layout for raw, derived, and replication dataset artifacts.
- [**`report/`**](file:///D:/DoAnBaomatweb/report/replication_protocol.md): Detailed replication protocol ([`replication_protocol.md`](file:///D:/DoAnBaomatweb/report/replication_protocol.md)) and prompt engineering logs ([`AI_Prompt_Log.md`](file:///D:/DoAnBaomatweb/report/AI_Prompt_Log.md)).
- [**`literature_review/`**](file:///D:/DoAnBaomatweb/literature_review/summary.md): Summary of source literature, attribution, and methodological limitations ([`summary.md`](file:///D:/DoAnBaomatweb/literature_review/summary.md)).
- [**`papers/`**](file:///D:/DoAnBaomatweb/papers): Research papers and literature references.

---

## 🚀 Quick Start & Environment Setup

### 1. Python Environment Setup
Use Python 3.11 for the analysis scripts:

```powershell
python -m venv .venv-replication
.\.venv-replication\Scripts\Activate.ps1
pip install --upgrade pip
pip install --index-url https://download.pytorch.org/whl/cpu "torch==2.7.1"
pip install -r requirements-replication.txt
```

### 2. Verify Replication Readiness
Run the environment readiness checker from the root directory:

```powershell
.\.venv-replication\Scripts\python.exe .\tools\replication_readiness.py
```

### 3. Android PoC Lab
To build and run the controlled observation sample app:

```powershell
cd poc
gradle :app:assembleDebug
```
Refer to [**`poc/README.md`**](file:///D:/DoAnBaomatweb/poc/README.md) for full instructions on running and observing the lab app.

---

## 📄 Documentation Links
- [Replication Protocol](file:///D:/DoAnBaomatweb/report/replication_protocol.md)
- [Literature Review & Attribution Summary](file:///D:/DoAnBaomatweb/literature_review/summary.md)
- [Tools Setup & Instructions](file:///D:/DoAnBaomatweb/tools/README.md)
- [PoC Lab Guide](file:///D:/DoAnBaomatweb/poc/README.md)
