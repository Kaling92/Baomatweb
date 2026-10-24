# Research data layout

This directory intentionally contains no malware binaries, private datasets, API credentials, or model checkpoints. Obtain and handle any APK samples only under institutional approval and in an isolated analysis VM.

Place permitted APK inputs under `raw\apks\`. Keep original thesis artifacts, when received from the author or supervisor, under `replication\`: `base_patterns_opt.csv`, `callgraph_flowdroid_opt.csv`, and the exact FlowDroid `SourcesAndSinks.txt`. Store generated decompilation, FlowDroid outputs, cleaned datasets, checkpoints, and fold predictions under `derived\`; do not overwrite original inputs.

The `replication_readiness.py` script checks whether the expected input files, tools, and Python ML modules are available. It never reads or executes APK content. Missing original thesis datasets cannot be reconstructed from the aggregate counts in the PDF.
