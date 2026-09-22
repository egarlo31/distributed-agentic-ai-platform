# Project Methodology

## Document Control

| Field | Value |
|---|---|
| Document Title | Project Methodology |
| Document ID | DAICP-METH-001 |
| Project | Distributed Agentic AI Platform for 5G RCA |
| Document Type | Project Methodology |
| Version | 0.1 |
| Status | Draft |
| Author | Emilio García |
| Owner | Project Engineering |
| Created | 2026-09-21 |
| Last Updated | 2026-09-21 |
| Classification | Internal / Project |

## Revision History

| Version | Date | Author | Description | Status |
|---|---|---|---|---|
| 0.1 | 2026-09-21 | Emilio García | Initial project methodology definition | Draft |
| 0.2 | 2026-09-22 | Emilio García | Complete project methodology definition | In Review |

## Review and Approval

| Role | Name | Status | Date |
|---|---|---|---|
| Author | Emilio García | In Progress | TBD |
| Technical Reviewer | TBD | Pending | TBD |
| Approver | TBD | Pending | TBD |

## 1. Purpose

The purpose of this document is to define the engineering methodology used to
design, implement, integrate, verify, and evaluate the Intelligent Copilot for
5G Troubleshooting and Root Cause Analysis.

The methodology establishes a controlled and iterative development process that
integrates software engineering, data engineering, AI engineering, retrieval,
agentic capabilities, security controls, and system verification.

This document defines how the project will be developed. Project dates,
durations, milestones, and activity scheduling are defined separately in the
Project Plan.

## 2. Methodology Overview

The project shall follow an iterative systems and software engineering lifecycle,
supported by GenAIOps practices, including LLMOps, for the development,
evaluation, deployment, monitoring, and continuous improvement of its generative
AI components.

The engineering approach combines:

- systems and software engineering for requirements, architecture, integration,
  interfaces, security, verification, and validation;

- GenAIOps practices for the lifecycle management of generative AI components,
  including LLMs, prompts, retrieval pipelines, RAG systems, evaluation,
  deployment, monitoring, and continuous improvement;

- controlled agent engineering practices for orchestration, tool use, execution
  boundaries, observability, human approval, and operational safety;

- iterative and evidence-based development, in which technical decisions and
  system changes are validated through measurable evaluation results.

Development shall begin from the approved system requirements baseline and
progress through architecture, data and knowledge preparation, baseline
implementation, retrieval, AI-assisted analysis, agent integration, system
verification, evaluation, and MVP validation.

Each major capability shall be implemented, integrated, and evaluated before
additional system complexity is introduced.

## 3. Development Lifecycle

The project lifecycle shall consist of the following phases:

1. Requirements Baseline
2. Architecture and System Design
3. Data and Knowledge Preparation
4. Baseline System Development
5. Retrieval and RAG Development
6. LLM-Assisted Root Cause Analysis
7. Agent and Tool Integration
8. System Integration
9. Verification, Evaluation, and Hardening
10. MVP Validation
11. Deployment and Operational Readiness

Verification and evaluation activities shall not be restricted to a single
phase. Relevant components shall be tested and evaluated incrementally
throughout the lifecycle.

The lifecycle shall allow iteration between phases when evaluation results,
technical limitations, risks, requirement changes, or operational findings
require refinement.

GenAIOps practices, including versioning, evaluation, observability,
deployment controls, and lifecycle monitoring, shall be applied across the
relevant phases rather than treated as an isolated development stage.

## 4. Requirements Management

System development shall be controlled using the approved System Requirements
Specification as the active requirements baseline.

Requirements shall remain uniquely identifiable through their corresponding
requirement IDs and shall be maintained through the Requirements Traceability
Matrix.

Each requirement shall maintain a defined status throughout the project
lifecycle, such as proposed, approved, implemented, verified, or changed.

Changes affecting approved requirements shall be documented, reviewed,
version-controlled, and evaluated for impact before being incorporated into the
active requirements baseline.

Requirement changes shall consider their possible impact on:

- system architecture;
- interfaces;
- data and knowledge components;
- AI and agent behavior;
- security and operational controls;
- verification and acceptance criteria;
- project schedule.

Implementation and verification activities shall maintain bidirectional
traceability between requirements, system components, and applicable tests or
acceptance criteria.

Obsolete or superseded requirements shall remain historically traceable through
version control and documented change records.

## 5. Architecture and Design Process

System architecture shall be defined before implementation of tightly coupled
or high-impact system components.

Architecture activities shall identify and document:

- major system components and their responsibilities;
- component boundaries and dependencies;
- communication interfaces and protocols;
- data flows and information exchanges;
- AI, LLM, retrieval, and RAG services;
- agent orchestration and tool-execution boundaries;
- persistent storage and knowledge repositories;
- authentication, authorization, and security boundaries;
- observability and audit components;
- deployment environments and infrastructure boundaries;
- relevant quality attributes and architectural constraints.

Architecture descriptions shall use appropriate views and models to represent
the system from different engineering perspectives, including when applicable:

- logical or component view;
- data and information-flow view;
- deployment view;
- security and trust-boundary view;
- AI and agent interaction view;
- operational or runtime view.

Architectural decisions with significant technical, security, operational, or
lifecycle impact shall be documented before implementation using Architecture
Decision Records (ADRs).

Significant architectural decisions shall record, when applicable:

- the problem or decision context;
- considered alternatives;
- selected decision;
- technical rationale;
- consequences and trade-offs;
- affected requirements.

Architecture artifacts shall maintain traceability to the applicable system
requirements and shall be reviewed when significant requirement, infrastructure,
security, AI, or deployment changes occur.

## 6. Data and Knowledge Engineering Process

Data and knowledge engineering shall follow a controlled and traceable process
for acquiring, preparing, validating, transforming, and incorporating technical
information into the system.

The process shall include, when applicable:

1. source identification and authorization;
2. data and document acquisition or ingestion;
3. source inspection and profiling;
4. schema, format, and content analysis;
5. cleaning and normalization when required;
6. validation against the intended system use;
7. metadata, lineage, and provenance registration;
8. transformation and preprocessing;
9. document segmentation or chunking when required;
10. embedding generation and indexing;
11. data and knowledge quality assessment;
12. versioning of relevant datasets, documents, indexes, and processing
    configurations;
13. controlled incorporation into the knowledge base or evaluation environment.

Knowledge incorporated into the operational knowledge base shall remain
traceable to its original source and validation status.

Authoritative source information shall remain distinguishable from
system-generated or AI-generated information.

Data intended for system evaluation shall be controlled separately from
development and knowledge-construction data when required to prevent evaluation
leakage.

Historical incidents used as evaluation ground truth shall contain a known and
validated root cause and documented resolution.

Changes to preprocessing, chunking, embedding, indexing, metadata, or knowledge
ingestion configurations that may materially affect system behavior shall be
version-controlled and reevaluated before being incorporated into the active
system configuration.

## 7. AI and Retrieval Development Process

AI and retrieval capabilities shall be developed incrementally and evaluated
against defined baselines before additional complexity is introduced.

The process shall include, when applicable:

1. baseline definition;
2. evaluation dataset and ground-truth preparation;
3. embedding and retrieval configuration;
4. retrieval evaluation;
5. RAG integration;
6. LLM-assisted incident analysis;
7. prompt and context design;
8. evidence, citation, and groundedness evaluation;
9. quantitative and qualitative system evaluation;
10. latency, computational-resource, and operational-cost measurement;
11. error and failure analysis;
12. refinement based on measured results;
13. controlled promotion of validated configurations.

AI development artifacts that may affect system behavior shall be versioned
when applicable, including:

- model and provider identifiers;
- embedding models;
- prompts and system instructions;
- retrieval configurations;
- chunking and indexing configurations;
- evaluation datasets;
- experiment configurations;
- evaluation results.

Experiments shall preserve sufficient configuration and result information to
support reproducibility and comparison between alternatives.

Changes shall be accepted based on measurable improvement, satisfaction of
applicable requirements, or justified engineering need rather than increased
model complexity alone.

AI components shall be evaluated before deployment and periodically during
operation according to the applicable system risks, metrics, and acceptance
criteria.

## 8. Agent and Tool Development Process

Agent capabilities shall be introduced only after the underlying retrieval,
analysis, and system interfaces are sufficiently testable.

Agent development shall include, when applicable:

- task and agent responsibility definition;
- agent input and output contracts;
- authorized tool interfaces and tool schemas;
- execution boundaries;
- action risk classification;
- least-privilege permissions;
- controlled context and state management;
- credential and secret isolation;
- sandbox execution;
- engineer approval gates;
- execution timeouts and bounded retries;
- prevention of uncontrolled or recursive execution loops;
- explicit failure and exception handling;
- execution logging and distributed tracing;
- emergency interruption;
- recovery or rollback support;
- scenario-based agent evaluation;
- security and misuse testing.

Tools shall expose explicitly defined inputs, outputs, permissions, expected
effects, and failure conditions.

Agent actions capable of modifying operational resources shall be subject to the
risk classification, authorization, and human-approval controls established in
the SRS.

Agent behavior shall be evaluated using representative troubleshooting
scenarios before promotion to environments with greater operational privileges.

Evaluation shall consider, when applicable:

- task completion;
- tool-selection correctness;
- argument and parameter correctness;
- evidence use;
- unnecessary tool calls;
- failed or repeated actions;
- policy violations;
- latency and resource consumption;
- recovery behavior;
- human-intervention requirements.

Agent execution shall remain observable and traceable without requiring
exposure of internal model chain-of-thought.

Agent capabilities shall not bypass the human-supervision, security, safety, or
operational-control requirements defined in the SRS.

## 9. Integration Process

System components shall be integrated incrementally rather than through a single
final integration stage.

Integration shall verify communication and compatibility between:

- incident ingestion;
- knowledge retrieval;
- AI inference;
- agent orchestration;
- tools and external APIs;
- persistent storage;
- user interface;
- authentication and authorization;
- observability and audit services.

Component interfaces shall define, when applicable:

- expected inputs and outputs;
- data schemas and formats;
- communication protocols;
- authentication requirements;
- error and failure responses;
- timeout and retry behavior;
- version compatibility.

Integration shall progress through controlled environments before production-
oriented deployment.

Each integration increment shall include applicable:

- interface and contract testing;
- integration testing;
- error and failure-path testing;
- observability and trace verification;
- security-control verification;
- regression testing.

Integration failures shall be recorded, analyzed, and resolved before dependent
capabilities are promoted to the next integration stage.

Changes to components or interfaces that may affect existing integrations shall
trigger the applicable regression tests.

Each integration increment shall be considered complete only when its defined
interfaces operate correctly and applicable requirements remain satisfied.

## 10. Verification and Validation

Verification shall determine whether system components and integrated
capabilities satisfy their specified requirements, interfaces, and design
constraints.

Validation shall determine whether the integrated system provides technically
appropriate and useful support for the intended 5G troubleshooting and Root
Cause Analysis use case under representative operating conditions.

Verification and validation activities shall maintain traceability to the
applicable requirements and acceptance criteria defined in the SRS.

Activities shall include, when applicable:

- static review and inspection;
- unit or component testing;
- functional testing;
- interface and integration testing;
- regression testing;
- end-to-end system testing;
- retrieval evaluation;
- RAG and groundedness evaluation;
- historical incident RCA evaluation;
- agent and tool evaluation;
- security testing;
- safety and authorization testing;
- failure-injection and recovery testing;
- performance and resource-utilization measurement;
- baseline comparison;
- human engineering review.

AI-related evaluation shall use controlled datasets, documented configurations,
defined metrics, and reproducible test conditions whenever applicable.

Evaluation evidence shall preserve, when applicable:

- evaluated system or component version;
- model and prompt configuration;
- retrieval and knowledge configuration;
- dataset or incident set used;
- test procedure;
- metrics and thresholds;
- observed results;
- pass, fail, or review status;
- identified defects or limitations.

Failed verification or validation activities shall result in defect analysis,
corrective action, and applicable regression testing before the affected
capability is accepted.

Validation activities should use conditions representative of the intended
operational environment whenever technically feasible.

Final acceptance shall be based on the acceptance criteria and MVP Acceptance
Gate defined in the approved System Requirements Specification.

## 11. Security, Risk, and Human Oversight

Security, AI risk, and operational safety controls shall be incorporated
throughout the development lifecycle rather than introduced only before
deployment.

The project shall identify and evaluate technical, security, AI, data, and
operational risks that may affect system behavior or telecommunications
infrastructure.

Risk-management activities shall include, when applicable:

- risk identification;
- threat modeling;
- likelihood and impact assessment;
- risk classification;
- mitigation definition;
- residual-risk evaluation;
- risk acceptance or escalation;
- periodic reassessment after significant system changes.

Security and operational controls shall include:

- authenticated access;
- role-based authorization;
- least-privilege access;
- credential and secret protection;
- sensitive-data protection;
- environment separation;
- controlled tool execution;
- operational action classification;
- engineer approval for controlled actions;
- audit logging and traceability;
- emergency interruption;
- failure containment;
- recovery and rollback when supported.

AI-specific risks shall be evaluated when applicable, including:

- unsupported or hallucinated technical conclusions;
- incorrect or misleading retrieved evidence;
- prompt injection or malicious input;
- unauthorized tool invocation;
- excessive agent permissions;
- unintended information disclosure;
- evaluation or data leakage;
- model, prompt, or retrieval configuration changes that degrade system behavior.

Controls shall be proportional to the potential impact of the affected
capability or operational action.

AI-generated recommendations shall support human engineering decisions rather
than replace operational authority.

An authorized engineer shall retain final authority over operational actions
that require human approval according to the SRS.

## 12. Configuration and Change Management

System artifacts whose modification may affect behavior, evaluation,
traceability, security, or deployment shall be placed under appropriate
configuration and version control.

Controlled artifacts may include:

- source code;
- system configuration;
- prompts and system instructions;
- agent configurations;
- AI model and provider identifiers;
- embedding models;
- retrieval configuration;
- chunking and indexing configuration;
- knowledge-base indexes;
- datasets and evaluation datasets;
- data-processing pipelines;
- tools and scripts;
- infrastructure and deployment configuration;
- test and evaluation configuration;
- documentation.

Each relevant configuration shall remain identifiable by version or revision
when required to reproduce system behavior.

Changes with significant technical, security, AI, operational, or schedule
impact shall be evaluated before incorporation into the active baseline.

Change evaluation shall consider, when applicable:

- reason for the change;
- affected requirements;
- affected architecture or interfaces;
- affected data or knowledge artifacts;
- AI and agent behavior;
- security and operational risk;
- required tests and regression tests;
- deployment impact;
- rollback requirements;
- schedule impact.

Changes shall progress through the applicable development, test, validation,
and deployment environments before promotion to a more privileged operational
environment.

Validated configurations shall be distinguishable from experimental or
unapproved configurations.

Where technically supported, previous validated configurations shall remain
recoverable to support rollback after unsuccessful changes.

Git shall be used for source-code and documentation version control.

Additional versioning or artifact-management mechanisms may be used for models,
datasets, experiments, indexes, and deployment artifacts when Git alone is not
appropriate.

Approved baselines and major project milestones may be identified using
repository tags.

## 13. Iteration and Review Process

Each development iteration shall follow the general cycle:

Requirement or Objective
→ Design
→ Implementation
→ Test
→ Measurement
→ Review
→ Refinement

Each iteration shall begin from an identifiable system or component baseline and
shall preserve sufficient information to compare its results with previous
iterations.

Review activities shall consider, when applicable:

- requirement satisfaction;
- technical correctness;
- evaluation metrics;
- defects and failures;
- security and operational risks;
- resource utilization;
- architectural impact;
- configuration changes;
- lessons learned.

An iteration may return to an earlier development activity when:

- acceptance criteria are not satisfied;
- evaluation results are insufficient;
- a technical limitation is identified;
- a security or operational risk is detected;
- an architectural change becomes necessary;
- a configuration change degrades validated system behavior.

Results and decisions from each relevant iteration shall be used to refine
subsequent development activities.

## 14. Phase Exit Criteria

A project phase may be considered complete when:

- its required technical outputs have been produced;
- applicable requirements remain traceable;
- required tests, evaluations, or reviews have been completed;
- defined acceptance or quality conditions for the phase have been satisfied;
- blocking defects or risks have been identified and resolved, mitigated, or
  formally accepted;
- resulting artifacts are version-controlled;
- relevant configuration and evaluation evidence has been preserved;
- dependencies required by the next phase are available.

Phase-specific exit criteria may be defined when a development stage requires
additional technical, security, data-quality, or evaluation conditions.

A phase shall not be considered complete when unresolved critical issues prevent
the safe or technically valid execution of the subsequent phase.

Phase completion does not imply final system acceptance.

Final MVP acceptance shall be determined using the acceptance gate and criteria
defined in the approved System Requirements Specification.