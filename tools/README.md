# Analysis toolchain

This directory contains verified open-source binaries used for static analysis. They do not include APK samples. Do not execute malware or install samples on the host or Android emulator.

## Installed releases

Apktool 3.0.3 is stored as `apktool\apktool.jar`. Its SHA-256 is `dbf930b076c6b9be08d57c449cacefc3bdd6b71ebd59b3066fc0e1f5b14f9423`. Run it through the installed JDK:

```powershell
java -jar .\tools\apktool\apktool.jar --version
java -jar .\tools\apktool\apktool.jar d -f -o .\data\derived\apktool\sample-id .\data\raw\apks\sample.apk
```

JADX 1.5.6 is downloaded from the official `skylot/jadx` GitHub release. Use `.\tools\jadx-cli\bin\jadx.bat` for static decompilation and `.\tools\jadx-cli\bin\jadx-gui.bat` for review. A Windows GUI-only distribution is also under `tools\jadx\`. The verified release hashes are `545ea2be9c242511bc145755cf4bda2485ade42966e096f8b4d3da2a230e8974` for `jadx-1.5.6.zip` and `6e070b197d4e40275d10f6559a1661bdd2e2bb325e9ef4181c7ac1286b274d99` for `jadx-gui-1.5.6-win.zip`.

```powershell
.\tools\jadx-cli\bin\jadx.bat --version
.\tools\jadx-cli\bin\jadx.bat -d .\data\derived\jadx\sample-id .\data\raw\apks\sample.apk
.\tools\jadx-cli\bin\jadx-gui.bat
```

FlowDroid 2.15.1 is stored as `flowdroid\soot-infoflow-cmd-jar-with-dependencies.jar`. Its SHA-256 was checked against the checksum published by Maven Central and is `51dadead47a173c494c2fa4855b1e8bd3b54e702a2c4b5ed58e60153009ae218`. Run the command-line help with:

```powershell
java -jar .\tools\flowdroid\soot-infoflow-cmd-jar-with-dependencies.jar --help
```

The Android SDK platform directory and an appropriate, reviewed source/sink definition file are mandatory for analysis. See [`../report/replication_protocol.md`](../report/replication_protocol.md) for commands and the paper-specific missing inputs.

## JDK

FlowDroid requires JDK 11 or later. This project targets JDK 17. The official Eclipse Temurin package can be installed on Windows with:

```powershell
winget install --id EclipseAdoptium.Temurin.17.JDK --exact --source winget --accept-source-agreements --accept-package-agreements
```

Open a new PowerShell window after installation and verify `java -version`. If installation is blocked by policy, use the institution-approved JDK distribution instead. Do not download JDK installers from third-party mirrors.

## Python analysis environment

Use Python 3.11 in the dedicated `.venv-replication` environment. Its pinned compatibility baseline is listed in [`../requirements-replication.txt`](../requirements-replication.txt); these are not claimed to be the original authors' versions, which the thesis does not specify. Install PyTorch's CPU wheel first, then the remaining pinned packages:

```powershell
$python = "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe"
& $python -m venv .\.venv-replication
$python = ".\.venv-replication\Scripts\python.exe"
& $python -m pip install --upgrade pip
& $python -m pip install --index-url https://download.pytorch.org/whl/cpu "torch==2.7.1"
& $python -m pip install -r .\requirements-replication.txt
& $python -m pip check
```

The environment has been validated with Python 3.11.9 and CPU-only PyTorch 2.7.1. The original workspace `.venv` is separate and was not modified by this setup.

The input readiness command is run from the workspace root:

```powershell
.\.venv-replication\Scripts\python.exe .\tools\replication_readiness.py
```

It only checks files, SDK paths, and installed modules. A blocked result is expected until the source thesis datasets, sample set, source/sink definitions, and analysis environment have been acquired.

## Not bundled

JEB is commercial and requires a valid institutional license. The thesis does not provide an install source or version for Kavanoz, so obtain provenance from the author/supervisor rather than using an unofficial binary. APK datasets, the 134/1,497 pattern CSVs, model checkpoints, credentials, and malware are intentionally excluded.
