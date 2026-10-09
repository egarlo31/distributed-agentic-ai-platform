# Architecture Overview

## 1. Purpose

This document defines the high-level architecture of the DAICP MVP and the
responsibilities of its main system components.

The architecture is intended to support AI-assisted telecommunications
troubleshooting and Root Cause Analysis while preserving evidence traceability
and controlled agent execution.

## 2. Architectural Scope

The MVP architecture supports the following workflow:

1. receive an incident and its available technical context;
2. retrieve relevant technical information;
3. provide retrieved evidence to an existing Large Language Model;
4. generate Root Cause Analysis hypotheses;
5. allow controlled use of approved diagnostic or information-retrieval tools;
6. produce a structured and traceable troubleshooting result.

The MVP does not include production network integration, autonomous remediation,
or unrestricted agent execution.

## 3. Main Components

| Component | Responsibility |
|---|---|
| Incident Input | Receives the incident and available technical context. |
| Data and Knowledge Layer | Provides prepared telecommunications data, technical documentation, and source metadata. |
| Retrieval Component | Identifies technical information relevant to the incident. |
| LLM / RCA Component | Generates evidence-supported Root Cause Analysis hypotheses. |
| Agent Component | Coordinates analysis and invokes approved tools when additional information is required. |
| Tool Layer | Provides controlled diagnostic and information-retrieval capabilities. |
| Output Component | Produces the structured troubleshooting result with evidence, sources, tool results, and uncertainty information. |
| Observability / Traceability | Records the information required to reconstruct the analysis and associate outputs with their supporting evidence. |

## 4. Component Interaction

The system follows a modular architecture in which retrieval, LLM inference,
agent orchestration, and tool execution remain separate responsibilities.

Components communicate through defined interfaces so that individual
implementations can be modified or replaced without redesigning the complete
system.

Retrieved evidence shall preserve its source information when passed to
downstream components.

Agent tool execution shall remain restricted to explicitly approved tools and
the controlled MVP environment.

## 5. Data and Knowledge Boundaries

Raw project data is maintained separately from processed data and system
knowledge artifacts.

The architecture distinguishes between:

- raw source data;
- processed development data;
- technical knowledge used for retrieval;
- evaluation data;
- generated system outputs.

Source identifiers and relevant provenance information shall be preserved
throughout the processing and analysis workflow.

## 6. Execution Constraints

The MVP shall:

- operate within the available local computing resources;
- use an existing Large Language Model;
- support modular replacement of major AI and retrieval components;
- avoid mandatory cloud dependencies;
- restrict agent actions to the controlled development and evaluation
  environment;
- preserve sufficient execution information for reproducibility and
  traceability.

## 7. Architectural Boundaries

The following capabilities are outside the initial architecture scope:

- direct integration with production telecommunications infrastructure;
- autonomous production remediation;
- unrestricted shell or tool execution;
- enterprise-scale multi-user deployment;
- mandatory distributed or cloud infrastructure.

These capabilities may be considered in future versions without changing the
core responsibilities defined for the MVP.