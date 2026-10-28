<div align="center">

# Instituto Politécnico Nacional

## Escuela Superior de Cómputo

<br><br><br><br>

# Intelligent Copilot for Troubleshooting and Root Cause Analysis in 5G Networks

<br><br><br><br><br>

### Student

Emilio García Lopez

### Group

7BV1

<br><br><br><br><br>

**Course:** Selected Topics in Artificial Intelligence

**Submission date:** September 7, 2026

</div>

## Objective

Design and implement an intelligent copilot to assist telecommunications engineers
during troubleshooting and root cause analysis in 5G networks through technical
knowledge retrieval, language-model-assisted analysis, and controlled tool execution.

The system aims to reduce the effort required to locate, interpret, and connect
technical information during incident diagnosis while keeping engineers responsible
for operational decisions.

## Current State

During telecommunications troubleshooting and root cause analysis, engineers must
manually consult multiple information sources, including technical documentation,
procedures, logs, alarms, specifications, and historical reports.

Information needed to analyze an incident may be distributed across different sources
and formats. Consequently, part of the diagnosis time is spent searching, reading,
connecting, and validating information before a root cause hypothesis can be established.

## Target State

Engineers should have a system that provides centralized access to incident-related
technical knowledge and automatically retrieves relevant information for its context.

The system should assist analysis, provide verifiable evidence, generate hypotheses
and technical documentation, and support controlled diagnostic tasks. Critical
decisions remain under engineering supervision through a Human-in-the-Loop approach.

## Proposed Solution

Develop an intelligent telecommunications engineering copilot with an architecture
comprising:

- a centralized knowledge base;
- ingestion and processing of documentation, logs, and historical cases;
- Retrieval-Augmented Generation (RAG);
- a Large Language Model (LLM) for reasoning and generation;
- an agent responsible for selecting and using tools;
- controlled execution of diagnostic scripts and tools;
- technical report generation;
- traceability of sources, actions, and errors;
- human supervision of critical actions.

### Knowledge Base

Centralize technical documentation, standards, procedures, logs, and historical incidents.

### RAG

Retrieve evidence relevant to the incident context before providing information to
the model.

### LLM

Interpret the incident and retrieved evidence to generate explanations, hypotheses,
and technical documentation.

### Agent

Select the tools required for diagnosis, search, or processing tasks.

### Human-in-the-Loop

The engineer reviews and approves decisions or actions that could affect operational
infrastructure.

## MVP

The first version will validate the main workflow:

Incident
    ↓
Knowledge Retrieval
    ↓
RAG
    ↓
LLM Analysis
    ↓
Root Cause Hypothesis
    ↓
Evidence
    ↓
Engineer Validation

The MVP will be evaluated using historical incidents with known root causes.
The initial objective is to verify that the system can:

- retrieve relevant documentation and evidence for an incident;
- generate a root cause hypothesis grounded in retrieved sources;
- preserve information traceability;
- assist the engineer without autonomously executing critical actions.

Results will be compared with the incident's historical information and resolution.

## Expected Results

Obtain a functional prototype supporting controlled 5G troubleshooting scenarios
through contextual retrieval of technical information and evidence-grounded analysis.
The project will evaluate:

- relevance of retrieved information;
- quality and traceability of generated responses;
- accuracy of root cause hypotheses;
- time required to retrieve information and produce an analysis;
- computational resource consumption;
- agent behavior during tool use.

MVP results will determine whether extending the system to more complex scenarios,
additional integrations, and controlled automation capabilities is feasible.
