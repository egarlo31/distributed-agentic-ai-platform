# Data Pipeline

## 1. Purpose

This document defines the data preparation flow used to transform selected raw
telecommunications data into reproducible inputs for development and evaluation
of the DAICP MVP.

## 2. Pipeline Scope

The pipeline initially processes data from:

- `SRC-001 — NetsLab-5G-ORAN-IDD`

The initial scope covers:

- network traffic data;
- lower-layer 5G/O-RAN telemetry;
- scenario and attack labels;
- metadata required for source traceability.

## 3. Processing Flow

The data pipeline follows these stages:

1. Raw data acquisition
2. Source inventory
3. Data quality audit
4. Schema and label inspection
5. Cleaning and filtering when required
6. Feature or field selection
7. Metadata and provenance preservation
8. Development and evaluation partitioning
9. Processed dataset generation
10. Versioned output for downstream retrieval and evaluation

## 4. Raw Data

Raw source files are stored under:

`data/raw/<source_id>/`

Raw files shall not be modified.

For SRC-001, the available source formats include:

- `.csv`
- `.pcap`
- `.txt`

## 5. Data Audit

Before transformation, each source shall be inspected for:

- file structure;
- schema;
- row and file counts;
- data types;
- missing values;
- duplicated records;
- label distribution;
- invalid or inconsistent values;
- temporal structure when available;
- source relationships and alignment;
- possible evaluation leakage.

Audit results are produced in:

`notebooks/data_audit/`

## 6. Data Preparation

Transformations shall only be introduced when justified by the source audit.

Possible preparation operations include:

- removal or correction of invalid records;
- duplicate handling;
- normalization of field names or formats;
- label normalization;
- filtering of selected scenarios;
- preservation of relevant identifiers and timestamps;
- extraction of metadata required for traceability.

The original source values shall remain recoverable from the raw data.

## 7. Processed Data

Processed artifacts shall be stored under:

`data/processed/`

Processed datasets shall preserve:

- source identifier;
- scenario or label;
- relevant technical fields;
- provenance information;
- processing version or configuration when applicable.

## 8. Evaluation Separation

Data used for evaluation shall be separated from development data when required
to reduce evaluation leakage.

The exact partitioning strategy will be defined after the structure and quality
of the available data have been validated.

## 9. Reproducibility

Data preparation steps that affect downstream system behavior shall be
implemented as reproducible code rather than manual modifications.

Raw data, processing code, and resulting processed artifacts shall remain
traceable to the corresponding source and pipeline version.