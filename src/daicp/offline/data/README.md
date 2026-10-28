# Dataset Preparation and Auditing

## Responsibilities

- `inventory.py`: discover sources and produce file inventories.
- `profiling.py`: inspect schemas and data quality.
- `dataset_tools.py`: audit CoreOps and locate external PCAP tools.
- `visualization.py`: build audit plots and dashboards.
- `src001.py`: stream network observations without exposing labels.
- `coreops_preparation.py`: select operational evidence by time window and separate references.
- `coreops_metrics.py`: select NF availability and metric observations by time window.
- `preparation.py`: offline contracts, SHA-256 fingerprints, partitions, and transactional output.

The first four modules retain the existing notebook interfaces. Exploratory audits
remain in `notebooks/data_audit/`; reproducible preparation uses classes. Original
values are not corrected or removed without an audit-supported policy.

## SRC-001

```python
from pathlib import Path
from daicp.offline.data.src001 import NetworkIncidentReader
from daicp.offline.data.preparation import DatasetPreparer

reader = NetworkIncidentReader()
records = reader.read(Path("data/raw/SRC-001_netslab_5g_oran_idd/Network_Dataset.csv"))
DatasetPreparer().prepare(records, Path("data/processed/src001-v1"))
```

Set `limit=100` for an explicit development run; the default processes all records.
The adapter requires known columns, preserves observed values as text, and rejects
malformed rows. `attack_category`, `attack_type`, `traffic_type`, and the original
UID are stored exclusively in references. Identical observations share a partition.
This does not guarantee independence between sessions or scenarios: final evaluation
requires independent acquisition groups established after auditing. No CSV/PCAP/TXT/DB
associations are invented. Scenario filenames can reveal answers and are not
included automatically in RCA context.

## CoreOps

```python
from pathlib import Path
from datetime import datetime
from daicp.offline.data.coreops_preparation import CoreOpsIncidentReader, IncidentWindow
from daicp.offline.data.preparation import DatasetPreparer

windows = [IncidentWindow(
    "incident-001", datetime.fromisoformat("2026-05-18T15:22:05+08:00"),
    datetime.fromisoformat("2026-05-18T15:36:26+08:00"), "acquisition-run-01",
)]
records = CoreOpsIncidentReader(log_timezone="Asia/Shanghai").read(
    Path("data/raw/SRC-002_coreops/CoreOps-22NFs"), windows)
DatasetPreparer().prepare(records, Path("data/processed/coreops-v1"))
```

Windows are explicit experimental selections, not incident detection. Use neutral
IDs and group overlapping windows or windows from the same acquisition to prevent
cross-partition leakage. Log year and timezone are explicit assumptions that must
be corroborated by auditing. Windows without evidence or crossing a year boundary
are rejected. Logs from all available NFs are considered; fault targets do not
select them. Per-file line limits and truncation are disclosed.

Injection labels and mitigation hints remain in references; overlapping faults do
not establish causality. Global availability and per-NF `scrape_ok` and
`restart_detected` columns are included; `metrics_columns` selects other observable
columns. Up to `max_metric_rows=5` rows per file are retained, with omitted counts.
No interpolation or causal inference is performed. The explicit timezone also
applies to metric timestamps lacking a timezone. `aligned_fault_window.json` and
injector logs are not runtime evidence. Preparation defaults to 30 lines per log;
reduce the window or limits to fit the model context budget.

## Artifacts and Reproducibility

Each new version directory contains:

- `incidents.jsonl`: partition and incident with traceable observations.
- `references.jsonl`: evaluation labels/references linked by incident ID.
- `manifest.json`: schema version, seed, evaluation fraction, counts, and source hashes.

Never pass `references.jsonl` to indexing or RCA. Separation is a program
responsibility boundary, not operating-system access control. `DatasetPreparer`
does not overwrite versions or allow outputs under `raw/`. Failed preparation leaves
the destination version untouched. IDs and partitions are deterministic for a given
source, configuration, and path. Hash partitioning does not guarantee exact proportions,
especially with few groups.
