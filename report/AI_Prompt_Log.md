# AI Prompt Log (AI_Prompt_Log.md)

## Session Log: Student & AI Collaborative Research & Coding

### Log 1
> **Student:** Scan full repo for knowledge and help me replicate and implement the tools required from the thesis paper.

> **Assistant:** Scanned workspace root, discovered thesis PDF (Fekadu 2025), reviewed literature review and replication protocol, and verified Python replication virtual environment (`.venv-replication`).

---

### Log 2
> **Student:** How do we build a static analysis tool using Androguard to extract API call sequences inside `onAccessibilityEvent` from APKs?

> **Assistant:** Provided `static_analyzer.py` and subsequently expanded it into `extract_features.py` to parse APK bytecode and build a synthetic dataset engine with overlapping family vocabularies.

---

### Log 3
> **Student:** Can you write an XGBoost script comparing `StratifiedKFold` vs `GroupKFold` to demonstrate fold leakage in malware classification?

> **Assistant:** Implemented `train_xgboost_leakage_demo.py` to run side-by-side cross-validation, revealing the inflated paper accuracy vs realistic family-aware accuracy.

---

### Log 4
> **Student:** I got a `ValueError` with `GroupKFold` because some folds lack class labels. How can we fix this?

> **Assistant:** Proposed and implemented the Dummy Augmentation algorithm (appending dummy rows per class into `X_train` per fold) to resolve the XGBoost multi-class folding crash.

---

### Log 5
> **Student:** Explain how the thesis paper's tools approach the problem? Explain like I'm 5.

> **Assistant:** Provided an ELI5 analogy comparing accessibility services to a "Robot Helper" on a school playground, explaining static code analysis and machine learning detection.

---

### Log 6
> **Student:** Now explain in technical detail for engineering people how their code and tools work.

> **Assistant:** Delivered a technical breakdown of static APK parsing, TF-IDF vectorization, and XGBoost cross-validation.

---

### Log 7
> **Student:** I don't quite understand what we did. Can we have a master summary file explaining each tool, method, step-by-step experiment, results, and presentation cheat sheet?

> **Assistant:** Created `report/master_defense_summary.artifact.md` consolidating the research workflow, tool mechanics, execution steps, and defense Q&A.

---

### Log 8
> **Student:** The summary is still too abstract. Rewrite it so a 1st grader can understand it.

> **Assistant:** Wrote an ELI5 story narrative (`eli5_master_story.artifact.md`) using playground analogies.

---

### Log 9
> **Student:** That's too childish! Rewrite the master file with specific technical details so I understand how everything works.

> **Assistant:** Developed a rigorous technical master walkthrough (`master_technical_walkthrough.artifact.md`) detailing code architecture and data flow.

---

### Log 10
> **Student:** Can you generate Figure 5.4 performance comparison bar chart programmatically?

> **Assistant:** Created `tools/generate_figure_5_4.py` using `matplotlib` / `seaborn` and saved the publication-quality image at `report/figure_5_4_performance_comparison.png`.

---

### Log 11
> **Student:** Generate Figure 5.5 confusion matrix heatmap from actual execution data.

> **Assistant:** Created `tools/generate_figure_5_5.py` reading `error_analysis_report.json` and rendered `report/figure_5_5_confusion_matrix.png`.

---

### Log 12
> **Student:** Generate Figure 6.1 (StratifiedKFold vs GroupKFold data splitting comparison) and Figure 6.2 (Performance drop bar chart).

> **Assistant:** Created `tools/generate_figure_6_1.py` (illustrating Fold Leakage and Global TF-IDF Leakage) and `tools/generate_figure_6_2.py` (visualizing the 28.45% performance drop).

---

### Log 13
> **Student:** Generate Figure 4.1 (ML pipeline architecture) and Figure 4.2 (Reproducibility workflow).

> **Assistant:** Created `tools/generate_figure_4_1.py` and `tools/generate_figure_4_2.py` flowchart generator scripts.

---

### Log 14
> **Student:** Generate Figure 4.3 (Simulated terminal console output screenshot).

> **Assistant:** Created `tools/generate_figure_4_3.py` rendering a realistic dark-mode CLI output image at `report/figure_4_3_terminal_output.png`.

---

### Log 15
> **Student:** Why did the paper use Clustering and Sentence-Transformers if fold leakage still happened?

> **Assistant:** Explained that clustering groups similar items but row-level random splitting (`StratifiedKFold`) scatters those similar rows across train and test, causing leakage.

---

### Log 16
> **Student:** Wait, did the authors use TinyBERT or XGBoost + TF-IDF in the paper?

> **Assistant:** Clarified that the paper evaluated **both** TinyBERT (deep learning) and XGBoost (baseline).
