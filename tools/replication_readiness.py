"""Check paper-replication inputs and command-line tools without opening APKs."""

from __future__ import annotations

import argparse
import importlib.util
import os
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def check_path(label: str, path: Path, *, is_dir: bool = False) -> bool:
    exists = path.is_dir() if is_dir else path.is_file()
    status = "present" if exists else "MISSING"
    print(f"[{status}] {label}: {path}")
    return exists


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sdk-platforms",
        type=Path,
        default=Path.home() / "AppData/Local/Android/Sdk/platforms",
        help="Android SDK platforms directory used by FlowDroid.",
    )
    parser.add_argument(
        "--flowdroid-jar",
        type=Path,
        default=ROOT / "tools" / "flowdroid" / "soot-infoflow-cmd-jar-with-dependencies.jar",
        help="Path to the FlowDroid command-line JAR.",
    )
    args = parser.parse_args()

    print("Paper replication readiness (static checks only)")
    print(f"Workspace: {ROOT}")
    print("\nRequired source artifacts")
    artifacts = [
        check_path("Original thesis PDF", ROOT / "papers" / "Tekeste Fekadu (1).pdf"),
        check_path("Base labeled patterns CSV", ROOT / "data" / "replication" / "base_patterns_opt.csv"),
        check_path(
            "FlowDroid callgraph patterns CSV",
            ROOT / "data" / "replication" / "callgraph_flowdroid_opt.csv",
        ),
        check_path(
            "FlowDroid source/sink definitions",
            ROOT / "data" / "replication" / "SourcesAndSinks.txt",
        ),
        check_path("Authorized APK sample directory", ROOT / "data" / "raw" / "apks", is_dir=True),
    ]

    print("\nStatic-analysis tools")
    java_path = shutil.which("java")
    if java_path is None and os.environ.get("JAVA_HOME"):
        java_candidate = Path(os.environ["JAVA_HOME"]) / "bin" / "java.exe"
        if java_candidate.is_file():
            java_path = str(java_candidate)
    if java_path is None:
        java_matches = sorted(Path(r"C:\Program Files\Eclipse Adoptium").glob(r"jdk-*\bin\java.exe"))
        java_path = str(java_matches[-1]) if java_matches else None
    print(f"[{'present' if java_path else 'MISSING'}] Java runtime: {java_path or 'java not found on PATH'}")
    tools = [
        java_path is not None,
        check_path("Apktool JAR", ROOT / "tools" / "apktool" / "apktool.jar"),
        check_path("JADX Windows distribution", ROOT / "tools" / "jadx-cli" / "bin" / "jadx.bat"),
        check_path("Android SDK platforms", args.sdk_platforms, is_dir=True),
        check_path("FlowDroid command-line JAR", args.flowdroid_jar),
    ]

    print(f"\nPython environment: {sys.version.split()[0]} ({sys.executable})")
    required_modules = (
        "androguard",
        "numpy",
        "pandas",
        "sklearn",
        "sentence_transformers",
        "torch",
        "transformers",
        "xgboost",
    )
    modules_ready = True
    for module in required_modules:
        present = importlib.util.find_spec(module) is not None
        print(f"[{'present' if present else 'MISSING'}] Python module: {module}")
        modules_ready = modules_ready and present

    print("\nA complete reproduction also needs licensed JEB/Kavanoz where applicable,")
    print("the original preprocessing/training code and exact model/tokenizer IDs.")
    ready = all(artifacts) and all(tools) and modules_ready
    print(f"\nReadiness: {'READY FOR PIPELINE RUN' if ready else 'BLOCKED BY MISSING INPUTS/TOOLS'}")
    return 0 if ready else 1


if __name__ == "__main__":
    raise SystemExit(main())
