# Data Flow

## 1. Purpose

This document describes how incident data, technical evidence, retrieved
knowledge, tool results, and generated Root Cause Analysis outputs move through
the DAICP MVP.

## 2. Input Sources

The MVP receives information from:

- incident input;
- prepared telecommunications datasets;
- technical knowledge sources;
- approved diagnostic or information-retrieval tools.

For the initial MVP, SRC-001 provides operational evidence for:

- F1 — Security / anomalous network activity.

## 3. Processing Flow

The main data flow is:

1. an incident and its available technical context are provided to the system;
2. the incident context is normalized into the format required by the analysis
   components;
3. the retrieval component searches the prepared technical knowledge base;
4. retrieved evidence and source metadata are passed to the RCA generation
   component;
5. the Large Language Model generates one or more Root Cause Analysis
   hypotheses;
6. when additional information is required, the agent may invoke an approved
   diagnostic or information-retrieval tool;
7. tool results are returned to the active analysis context;
8. the system produces a structured troubleshooting result containing the
   hypothesis, supporting evidence, source references, tool results when
   applicable, and identified uncertainty or limitations.

## 4. Evidence and Provenance Flow

Source information shall remain associated with technical evidence throughout
the workflow.

The system shall preserve, when applicable:

- source identifier;
- source type;
- original record or file reference;
- scenario or label;
- relevant timestamp;
- processing or retrieval metadata.

Generated hypotheses shall remain distinguishable from source-derived evidence.

## 5. Data Boundaries

The data flow distinguishes between:

- raw source data;
- processed development data;
- retrieval-ready knowledge;
- evaluation data;
- runtime analysis context;
- generated troubleshooting outputs.

Raw source data shall not be modified by downstream processing.

Evaluation data shall remain separated from development data when required to
reduce evaluation leakage.

## 6. Tool Result Flow

Approved tools may provide additional evidence during analysis.

Tool results shall:

- be associated with the active incident;
- preserve the tool identifier;
- preserve execution status;
- preserve relevant output;
- be available to the agent and RCA generation component when applicable;
- be included in the final structured output when relevant.

## 7. Output Flow

The final troubleshooting result shall contain, when applicable:

- Root Cause Analysis hypothesis;
- supporting technical evidence;
- source references;
- tool execution results;
- uncertainty or limitations;
- recommended next investigation steps.

The output shall preserve sufficient traceability to reconstruct the evidence
used during the analysis.

## 8. MVP Constraints

The initial data flow is limited to the controlled local development and
evaluation environment.

The MVP does not require:

- production telecommunications data ingestion;
- autonomous remediation;
- unrestricted tool execution;
- real-time production integration;
- distributed or cloud infrastructure.