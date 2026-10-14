# SRC-002 — CoreOps

## Overview

This directory contains the selected subset of the CoreOps dataset used for
developing and evaluating the DAICP MVP.

CoreOps provides operational logs, network function metrics, and fault-injection
ground truth from experimental 5G Core environments.

Raw dataset files are intentionally excluded from Git.

## 1. Source Information

- **Dataset:** [CoreOps — Hugging Face](https://huggingface.co/datasets/zixuan0615/CoreOps)
- **Repository:** [CoreOps — GitHub](https://github.com/qinzixuan-bupt/CoreOps)
- **Selected Environment:** CoreOps-22NFs
- **Dataset License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Code License:** Apache 2.0 (GitHub repository)
- **Access Date:** 2026-10-14

## 2. Directory Structure

```text
SRC-002_coreops/
├── README.md
├── CoreOps-22NFs/
│   ├── labels/
│   │   ├── fault_labels.json
│   │   └── injector_run_20260518_145436.log
│   ├── logs/
│   │   └── *.log
│   └── metrics/
│       ├── aligned_fault_window.json
│       ├── global_matrix.csv
│       └── per_nf0525/
│           ├── pcf_20260518_142750.csv
│           ├── amf-a1_20260518_142750.csv
│           └── smf-e1_20260518_142750.csv
└── context/
    └── topo.yaml
```

## 3. Selected Data

### 3.1 Ground Truth

- `labels/fault_labels.json`
- `labels/injector_run_20260518_145436.log`

These files provide fault-injection metadata, affected network functions,
fault categories, timestamps, and execution records.

### 3.2 Operational Logs

- `logs/*.log`

All published operational logs from the CoreOps-22NFs environment are selected.

These logs support the investigation of network function behavior, errors,
service interactions, and potential fault propagation across components.

### 3.3 Metrics

- `metrics/aligned_fault_window.json`
- `metrics/global_matrix.csv`
- `metrics/per_nf0525/pcf_20260518_142750.csv`
- `metrics/per_nf0525/amf-a1_20260518_142750.csv`
- `metrics/per_nf0525/smf-e1_20260518_142750.csv`

The selected metrics provide fault time windows, network function availability,
and individual NF performance observations.

Additional per-NF metrics may be incorporated when required by specific
evaluation scenarios.

### 3.4 Infrastructure Context

- `context/topo.yaml`

This file originates from the CoreOps GitHub repository and describes the
experimental 5G Core network topology.

It provides infrastructure context for interpreting relationships between
network functions.

## 4. Download

The selected dataset files can be downloaded from:

https://huggingface.co/datasets/zixuan0615/CoreOps

The initial subset excludes:

- `CoreOps-97NFs/`
- `RCA_Agent/`
- `results/`
- Unselected per-NF metrics

The original dataset directory structure is preserved.

The topology file is obtained separately from:

https://github.com/qinzixuan-bupt/CoreOps/blob/main/CoreOps-22NFs/topo.yaml

## 5. Data Handling

- Raw data must remain unchanged.
- Raw dataset files must not be committed to Git.
- Dataset provenance and licensing information must be preserved.
- Dataset revisions and file hashes should be recorded for reproducibility.
- Ground-truth labels must remain separate from agent-visible evidence.
- Generated and processed data must be stored outside the raw directory.

## 6. Evaluation Considerations

Before incorporating the selected data into the DAICP evaluation pipeline,
the following conditions must be verified:

1. File integrity and readability.
2. Timestamp consistency across logs, metrics, and fault labels.
3. Ground-truth consistency with fault-injection records.
4. Operational evidence coverage for selected incidents.
5. Potential overlapping fault windows.
6. Potential data leakage.
7. Availability of baseline observations before fault injection.

The initial evaluation will focus on selected operational fault families:

- Network connectivity failures.
- Network function availability failures.
- Resource contention and performance degradation.

The final selection of incidents depends on the availability and reliability
of their supporting operational evidence.

## 7. References

For dataset provenance, project scope, and selection decisions, see:

[Data Sources](../../../docs/data/01_data_sources.md)

Original resources:

- [CoreOps Dataset](https://huggingface.co/datasets/zixuan0615/CoreOps)
- [CoreOps GitHub Repository](https://github.com/qinzixuan-bupt/CoreOps)
- [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)