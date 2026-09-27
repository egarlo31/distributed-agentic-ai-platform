# Project Plan

## Document Control

| Field | Value |
|---|---|
| Document Title | Project Plan |
| Document ID | DAICP-PLAN-001 |
| Project | Distributed Agentic AI Platform for 5G RCA |
| Document Type | Project Plan |
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
| 0.1 | 2026-09-21 | Emilio García | Initial project planning structure | Draft |

## Review and Approval

| Role | Name | Status | Date |
|---|---|---|---|
| Author | Emilio García | In Progress | TBD |
| Technical Reviewer | TBD | Pending | TBD |
| Approver | TBD | Pending | TBD |

## 1. Purpose

The purpose of this document is to define the project planning structure for the
development, integration, verification, and validation of the Intelligent Copilot
for 5G Troubleshooting and Root Cause Analysis.

This plan translates the approved project methodology into executable activities,
dependencies, estimated durations, milestones, and schedule information.

The document is intended to support project control by defining:

- the work to be performed;
- the sequence and dependency of activities;
- estimated activity durations;
- schedule calculations;
- critical activities and schedule constraints;
- project milestones;
- the planned project calendar;
- schedule risks and contingencies.

The plan shall be updated when significant changes in scope, dependencies,
technical constraints, resource availability, or validated estimates affect the
project schedule.

## 2. Planning Approach

Project planning shall follow a structured and dependency-based approach.

The project shall first be decomposed into manageable work packages and
activities using a Work Breakdown Structure (WBS).

Each activity shall be identified with sufficient information to support
scheduling and control, including when applicable:

- activity identifier;
- activity description;
- expected deliverable;
- predecessor or dependency;
- required resources;
- estimated effort;
- estimated duration;
- planned start and finish;
- milestone relationship;
- current status.

Activity sequencing shall be based on technical and logical dependencies rather
than arbitrary calendar dates.

Where activity duration is uncertain, three-point estimation may be used:

- Optimistic time (O);
- Most Likely time (M);
- Pessimistic time (P).

The expected duration may be estimated using the PERT expression:

TE = (O + 4M + P) / 6

Critical Path Method (CPM) techniques may be used to determine:

- Early Start (ES);
- Early Finish (EF);
- Late Start (LS);
- Late Finish (LF);
- schedule slack;
- critical activities and the project critical path.

Estimated effort and calendar duration shall be treated as separate planning
variables.

Calendar dates shall be assigned only after activity dependencies, estimated
durations, and resource availability have been defined.

Project milestones shall be established to identify significant technical
baselines, completed deliverables, integration points, and validation events.

The resulting schedule shall be represented using a project calendar and Gantt
chart for monitoring and communication.

The project plan shall be reviewed and updated when significant changes in
scope, requirements, dependencies, estimates, technical risk, or resource
availability affect the active schedule.

## 3. Work Breakdown Structure

### WP-01 — Project Definition and Planning

| Activity ID | Activity | Deliverable / Exit Criterion | Origin |
|---|---|---|---|
| A-101 | Define project problem | Approved Problem Definition | Project Definition |
| A-102 | Define system requirements | Approved SRS v1.0 | System Requirements |
| A-103 | Define project methodology | Approved Methodology v1.0 | Project Methodology |
| A-104 | Define MVP scope | Approved MVP Definition | Project Scope |
| A-105 | Define evaluation strategy | Initial Evaluation Plan | Evaluation |
| A-106 | Define high-level system architecture | Architecture baseline | System Architecture |
| A-107 | Build initial project plan | Approved Project Plan baseline | Project Planning |

### WP-02 — Data and Knowledge Preparation

| Activity ID | Activity | Deliverable / Exit Criterion | Origin |
|---|---|---|---|
| A-201 | Identify and confirm project data sources | Approved list of project data sources | Data Requirements / Problem Definition |
| A-202 | Acquire selected datasets and technical documents | Raw data and document collection available locally | Data Requirements |
| A-203 | Inspect source structure and content | Initial data/source audit | Data Feasibility |
| A-204 | Define data inclusion and exclusion criteria | Documented selection criteria | MVP Definition / Evaluation Plan |
| A-205 | Define data schema and metadata requirements | Initial data and metadata schema | Data Requirements |
| A-206 | Clean and normalize selected data | Cleaned and normalized dataset/corpus | Data Requirements |
| A-207 | Extract and preserve source metadata | Metadata associated with every usable source | Traceability Requirements |
| A-208 | Segment and prepare technical documents for retrieval | Retrieval-ready document units | Retrieval Requirements |
| A-209 | Build the initial telecommunications knowledge corpus | Versioned initial corpus | FR — Technical Knowledge Retrieval |
| A-210 | Validate corpus integrity and traceability | Corpus validation report | Verification / Data Requirements |
| A-211 | Create development and evaluation data partitions | Controlled datasets for development and evaluation | Evaluation Plan / Leakage Control |
| A-212 | Version and document the prepared corpus | Reproducible corpus version and manifest | Reproducibility Requirements |

### WP-03 — Retrieval Baselines

| Activity ID | Activity | Deliverable / Exit Criterion | Origin |
|---|---|---|---|
| A-301 | Define the retrieval evaluation task | Documented retrieval task and relevance criteria | Evaluation Plan / Research Question |
| A-302 | Define the retrieval benchmark dataset | Evaluation queries with relevant evidence annotations | Evaluation Plan |
| A-303 | Define retrieval metrics | Approved set of retrieval metrics | Evaluation Plan |
| A-304 | Implement lexical retrieval baseline | Functional BM25 retriever | FR — Technical Knowledge Retrieval / Baseline Definition |
| A-305 | Implement dense single-vector retrieval baseline | Functional dense retriever | FR — Technical Knowledge Retrieval / Research Question |
| A-306 | Configure retrieval experiment conditions | Reproducible retrieval configuration | Experiment Protocol |
| A-307 | Execute lexical retrieval baseline evaluation | BM25 benchmark results | Evaluation Plan |
| A-308 | Execute dense retrieval baseline evaluation | Dense retrieval benchmark results | Evaluation Plan |
| A-309 | Compare retrieval baseline performance | Comparative results table | Research Question |
| A-310 | Analyze baseline retrieval failures | Documented failure cases and limitations | Research / Evaluation |
| A-311 | Establish retrieval baseline reference | Approved baseline results for later comparison | Baseline Definition |

### WP-04 — RAG System

| Activity ID | Activity | Deliverable / Exit Criterion | Origin |
|---|---|---|---|
| A-401 | Define the initial RAG pipeline | Documented RAG processing flow | System Architecture / FR — Technical Knowledge Retrieval |
| A-402 | Define document segmentation strategy | Approved initial chunking strategy | Data Architecture / Retrieval Requirements |
| A-403 | Implement document segmentation pipeline | Retrieval-ready document chunks | Data Requirements |
| A-404 | Generate and store document embeddings | Versioned embedding representation | RAG Architecture |
| A-405 | Build the vector retrieval index | Functional vector index | FR — Technical Knowledge Retrieval |
| A-406 | Implement query processing and retrieval integration | Query-to-context retrieval pipeline | FR — Technical Knowledge Retrieval |
| A-407 | Define retrieved-context construction strategy | Documented context assembly policy | RAG Architecture |
| A-408 | Integrate retrieved evidence with the LLM | Functional retrieval-augmented generation pipeline | FR — RCA Assistance |
| A-409 | Implement source citation and evidence traceability | Generated responses linked to retrieved evidence | Traceability Requirements |
| A-410 | Implement retrieval failure handling | Defined behavior for insufficient or irrelevant evidence | Reliability / Safety Requirements |
| A-411 | Implement basic RAG logging and observability | Logs for queries, retrieval results, context, and outputs | Evaluation / Reproducibility |
| A-412 | Execute initial end-to-end RAG tests | Functional test results | Verification Plan |
| A-413 | Analyze RAG failure cases | Documented retrieval/generation failure categories | Evaluation / Research |
| A-414 | Establish RAG baseline version | Reproducible RAG baseline v1.0 | Baseline Definition |

### WP-05 — LLM and RCA Generation

| Activity ID | Activity | Deliverable / Exit Criterion | Origin |
|---|---|---|---|
| A-501 | Define RCA generation task | Documented RCA generation objective and input/output contract | FR — RCA Assistance / Evaluation Plan |
| A-502 | Define structured RCA output format | Approved RCA response schema | FR — RCA Assistance / Traceability |
| A-503 | Define LLM selection criteria | Documented model selection criteria | Technical Constraints / Resource Feasibility |
| A-504 | Select initial LLM candidate(s) | Approved initial model configuration | Resource Feasibility / Architecture |
| A-505 | Establish non-RAG LLM baseline | Functional baseline using the selected LLM without retrieval | Baseline Definition / Research Evaluation |
| A-506 | Define initial prompting and instruction strategy | Versioned prompt/instruction template | LLM Generation Design |
| A-507 | Implement RCA generation component | Functional RCA generation module | FR — RCA Assistance |
| A-508 | Integrate retrieved evidence into RCA generation | Evidence-grounded generation pipeline | RAG System / FR — RCA Assistance |
| A-509 | Implement evidence attribution in RCA output | RCA conclusions linked to supporting evidence | Traceability Requirements |
| A-510 | Implement uncertainty and abstention behavior | Defined behavior for insufficient or conflicting evidence | Safety / Reliability Requirements |
| A-511 | Define RCA evaluation rubric | Approved scoring rubric for generated diagnoses | Evaluation Plan |
| A-512 | Build RCA evaluation cases | Versioned RCA benchmark cases with reference evidence | Evaluation Plan |
| A-513 | Execute baseline RCA evaluation | Baseline generation results | Baseline Definition |
| A-514 | Execute evidence-grounded RCA evaluation | RAG-assisted RCA results | Evaluation Plan |
| A-515 | Analyze RCA generation failures | Categorized generation and reasoning failures | Research / Evaluation |
| A-516 | Establish RCA generation baseline version | Reproducible RCA generation baseline v1.0 | Experiment Protocol |

### WP-06 — Agentic Capabilities

| Activity ID | Activity | Deliverable / Exit Criterion | Origin |
|---|---|---|---|
| A-601 | Define agent responsibilities and autonomy boundaries | Documented agent role and permitted responsibilities | System Requirements / AI Governance |
| A-602 | Define agent state and execution lifecycle | Documented agent state model | System Architecture |
| A-603 | Define agent planning strategy | Initial planning policy | Agent Architecture / Research |
| A-604 | Define available agent tools | Approved tool registry and tool contracts | Functional Requirements / Security Requirements |
| A-605 | Implement tool invocation interface | Functional standardized tool interface | Interface Requirements |
| A-606 | Implement initial agent execution loop | Functional action-observation loop | FR — Agentic Assistance |
| A-607 | Integrate retrieval as an agent tool | Agent can invoke technical knowledge retrieval | FR — Technical Knowledge Retrieval |
| A-608 | Integrate RCA generation with agent workflow | Agent can generate evidence-supported RCA output | FR — RCA Assistance |
| A-609 | Implement agent state and context management | Persistent task-state representation during execution | Architecture / Reliability |
| A-610 | Implement execution limits and stopping conditions | Controlled termination behavior | Safety / Operational Requirements |
| A-611 | Implement human approval checkpoints | Human-in-the-loop approval mechanism | Governance / Safety Requirements |
| A-612 | Implement tool-result validation and error handling | Controlled handling of failed or invalid tool results | Reliability Requirements |
| A-613 | Implement agent action logging and traceability | Traceable agent execution history | Traceability / Evaluation |
| A-614 | Define agent evaluation scenarios | Versioned agent benchmark scenarios | Evaluation Plan |
| A-615 | Execute agent capability evaluation | Agent evaluation results | Evaluation Plan |
| A-616 | Analyze agent failure modes | Documented agent failure taxonomy | Research / Risk Management |
| A-617 | Establish agent baseline version | Reproducible agent baseline v1.0 | Baseline Definition |

### WP-07 — Tool Execution and Sandboxing

| Activity ID | Activity | Deliverable / Exit Criterion | Origin |
|---|---|---|---|
| A-701 | Define tool execution threat model | Documented execution threats and trust boundaries | AI Governance / Security Requirements |
| A-702 | Define sandbox security requirements | Approved isolation and execution constraints | Security / Operational Requirements |
| A-703 | Select initial sandboxing mechanism | Documented sandbox technology decision | Architecture / ADR |
| A-704 | Define tool permission model | Approved allowlist and permission rules | Security Requirements |
| A-705 | Define sandbox input/output contract | Standardized execution request and result schema | Interface Requirements |
| A-706 | Build isolated execution environment | Functional sandbox environment | Security Requirements |
| A-707 | Implement sandbox execution controller | Controlled tool execution component | FR — Tool Execution |
| A-708 | Implement CPU, memory, process, and execution-time limits | Enforced resource limits | Reliability / Security Requirements |
| A-709 | Implement filesystem isolation and temporary workspace handling | Controlled filesystem access | Security Requirements |
| A-710 | Implement network access restrictions | Controlled or disabled sandbox network access | Security Requirements |
| A-711 | Implement privilege and syscall restrictions | Reduced execution privileges and syscall surface | Security Requirements |
| A-712 | Implement execution timeout and termination mechanisms | Reliable cancellation of long-running tasks | Operational / Reliability Requirements |
| A-713 | Capture stdout, stderr, exit status, and execution metadata | Structured tool execution results | Interface / Traceability Requirements |
| A-714 | Integrate sandbox with agent tool interface | Agent tools execute through sandbox controller | Agent Architecture |
| A-715 | Implement sandbox execution logging and audit trail | Traceable execution records | Traceability / Governance |
| A-716 | Define sandbox verification tests | Approved isolation and resource-limit test cases | Verification Plan |
| A-717 | Execute sandbox security and isolation tests | Documented verification results | Verification Plan |
| A-718 | Measure sandbox execution overhead | Performance benchmark results | Performance / Evaluation |
| A-719 | Analyze sandbox failure modes | Documented failure and security limitations | Risk / Evaluation |
| A-720 | Establish sandbox baseline version | Reproducible sandbox baseline v1.0 | Architecture / Reproducibility |

### WP-08 — System Integration

| Activity ID | Activity | Deliverable / Exit Criterion | Origin |
|---|---|---|---|
| A-801 | Define system integration strategy | Documented integration sequence and component dependencies | System Architecture / Integration Planning |
| A-802 | Define component interface contracts | Approved interfaces between retrieval, generation, agent, tools, and sandbox | Interface Requirements |
| A-803 | Establish integrated development environment | Reproducible environment for running integrated components | Deployment / Reproducibility |
| A-804 | Integrate knowledge corpus with retrieval subsystem | Retrieval subsystem operating on project corpus | WP-02 / WP-03 |
| A-805 | Integrate retrieval subsystem with RAG pipeline | Functional retrieval-to-context pipeline | WP-03 / WP-04 |
| A-806 | Integrate RAG pipeline with RCA generation component | Functional evidence-grounded RCA generation flow | WP-04 / WP-05 |
| A-807 | Integrate RCA generation with agent workflow | Agent can invoke and use RCA generation capability | WP-05 / WP-06 |
| A-808 | Integrate agent with tool execution interface | Agent can invoke approved tools through standardized interface | WP-06 / WP-07 |
| A-809 | Integrate sandbox execution controller | Tool calls execute through isolated sandbox environment | WP-07 / Security Requirements |
| A-810 | Integrate human approval and control mechanisms | Sensitive actions respect approval boundaries | Governance / Safety Requirements |
| A-811 | Integrate system-wide logging and traceability | Unified trace across retrieval, LLM, agent, and tool actions | Traceability Requirements |
| A-812 | Implement configuration and component version tracking | Reproducible integrated configuration | Reproducibility Requirements |
| A-813 | Implement integrated error propagation and recovery | Controlled handling of failures between components | Reliability Requirements |
| A-814 | Execute incremental integration tests | Successful subsystem integration test results | Verification Plan |
| A-815 | Execute complete end-to-end system test | Functional incident-to-RCA workflow | System Requirements |
| A-816 | Measure integrated system latency and resource usage | Initial system-level performance results | Performance Requirements |
| A-817 | Analyze integration failures and emergent behavior | Documented integration issues and corrective actions | Evaluation / Risk Management |
| A-818 | Establish integrated system baseline | Reproducible integrated MVP baseline v1.0 | Configuration Management |

### WP-09 — Evaluation and Experiments

| Activity ID | Activity | Deliverable / Exit Criterion | Origin |
|---|---|---|---|
| A-901 | Define research questions and evaluation objectives | Approved research questions and evaluation objectives | Project Methodology / Evaluation Plan |
| A-902 | Define experimental hypotheses | Documented testable hypotheses | Research Methodology |
| A-903 | Define experimental systems and baselines | Approved comparison matrix | Baseline Definition |
| A-904 | Define evaluation datasets and scenario subsets | Versioned evaluation dataset and scenario partitions | Evaluation Plan / Data Requirements |
| A-905 | Define retrieval evaluation metrics | Approved retrieval metric set | Retrieval Evaluation |
| A-906 | Define RCA generation metrics and rubric | Approved RCA evaluation rubric | RCA Evaluation |
| A-907 | Define agent evaluation metrics | Approved agent capability metrics | Agent Evaluation |
| A-908 | Define system-level performance metrics | Approved latency/resource/cost metrics | Performance Requirements |
| A-909 | Define experimental controls and fixed variables | Reproducible experiment configuration | Experiment Protocol |
| A-910 | Implement experiment execution harness | Reproducible experiment runner | Reproducibility Requirements |
| A-911 | Execute retrieval experiments | Retrieval experiment results | Research Question / WP-03 |
| A-912 | Execute LLM-only RCA baseline experiments | Baseline RCA results | WP-05 |
| A-913 | Execute RAG-assisted RCA experiments | RAG RCA results | WP-04 / WP-05 |
| A-914 | Execute agentic system experiments | Agentic RCA results | WP-06 |
| A-915 | Execute robustness and failure-case experiments | Robustness and stress-test results | Risk / Evaluation |
| A-916 | Measure latency and computational resource usage | Performance benchmark results | Performance / Resource Feasibility |
| A-917 | Perform comparative statistical analysis | Comparative experiment analysis | Research Methodology |
| A-918 | Conduct qualitative failure analysis | Categorized failure cases and observations | Research / Evaluation |
| A-919 | Document experimental limitations and threats to validity | Threats-to-validity analysis | Research Methodology |
| A-920 | Establish final experimental results baseline | Reproducible experiment results package | Project Evaluation |

### WP-10 — Verification and Validation

| Activity ID | Activity | Deliverable / Exit Criterion | Origin |
|---|---|---|---|
| A-1001 | Review the baselined requirements set | Approved requirements set ready for verification | System Requirements / Traceability |
| A-1002 | Define verification methods for each requirement | Requirements Verification Matrix | Verification Plan |
| A-1003 | Define validation objectives and stakeholder expectations | Validation criteria and expected operational outcomes | Problem Definition / Need / Scope |
| A-1004 | Define verification test procedures | Approved verification procedures | Verification Plan |
| A-1005 | Define validation scenarios | Representative 5G troubleshooting scenarios | Validation Plan / MVP Definition |
| A-1006 | Prepare verification and validation environment | Ready and reproducible V&V environment | System Architecture / Deployment |
| A-1007 | Verify functional requirements | Functional verification results | FR Requirements |
| A-1008 | Verify data and knowledge requirements | Data verification results | Data Requirements |
| A-1009 | Verify interface requirements | Interface verification results | Interface Requirements |
| A-1010 | Verify security and sandbox requirements | Security verification results | Security Requirements |
| A-1011 | Verify performance requirements | Performance verification results | Performance Requirements |
| A-1012 | Verify operational and reliability requirements | Operational verification results | Operational / Reliability Requirements |
| A-1013 | Execute end-to-end system verification | System-level verification results | System Requirements |
| A-1014 | Record requirement compliance status | Updated Requirements Traceability Matrix | Traceability |
| A-1015 | Record and analyze verification discrepancies | Verification discrepancy log | Verification Process |
| A-1016 | Correct verified nonconformities | Resolved critical requirement violations | Corrective Action |
| A-1017 | Re-execute affected verification procedures | Successful regression verification | Verification Process |
| A-1018 | Execute system validation scenarios | Validation results under representative conditions | Validation Plan |
| A-1019 | Evaluate system usefulness for 5G troubleshooting | Evidence that intended operational need is or is not satisfied | Problem Definition / Need |
| A-1020 | Analyze validation anomalies and limitations | Validation findings and limitations | Validation Process |
| A-1021 | Produce Verification and Validation Report | Approved V&V report | Project Acceptance |
| A-1022 | Establish verified and validated MVP baseline | MVP accepted against defined criteria | Acceptance / Configuration Management |

### WP-11 — Deployment and Reproducibility

| Activity ID | Activity | Deliverable / Exit Criterion | Origin |
|---|---|---|---|
| A-1101 | Define deployment architecture for the MVP | Approved deployment topology | System Architecture / Operational Constraints |
| A-1102 | Define runtime environments and dependencies | Documented environment specification | Reproducibility Requirements |
| A-1103 | Define configuration and secrets management approach | Approved configuration strategy | Security / Deployment Requirements |
| A-1104 | Containerize application components | Functional Docker images | Deployment Requirements |
| A-1105 | Define container orchestration for local MVP execution | Working Docker Compose configuration | System Integration / Deployment |
| A-1106 | Pin software and model dependencies | Version-controlled dependency definitions | Reproducibility Requirements |
| A-1107 | Define model, corpus, and configuration version identifiers | Versioning convention for experimental artifacts | Experiment Protocol / Traceability |
| A-1108 | Implement environment initialization procedure | Repeatable setup procedure | Reproducibility Requirements |
| A-1109 | Implement persistent storage and volume handling | Controlled persistence for required system data | Data / Operational Requirements |
| A-1110 | Implement health and readiness checks | Observable component health status | Reliability Requirements |
| A-1111 | Define logging and runtime artifact storage | Persistent logs and experiment outputs | Traceability / Evaluation |
| A-1112 | Create reproducible system build procedure | Repeatable build from repository source | Reproducibility Requirements |
| A-1113 | Create reproducible system startup procedure | System can be started from documented instructions | Deployment Requirements |
| A-1114 | Execute clean-environment deployment test | Successful deployment from a clean environment | Verification Plan |
| A-1115 | Execute reproducibility test | Equivalent configuration produces repeatable system setup | Reproducibility Requirements |
| A-1116 | Document deployment and execution procedure | Deployment/runbook documentation | Final Documentation |
| A-1117 | Package MVP release artifacts | Versioned project release package | Configuration Management |
| A-1118 | Establish deployable MVP baseline | Reproducible deployment baseline v1.0 | Project Acceptance |

### WP-12 — Final Documentation and Presentation

| Activity ID | Activity | Deliverable / Exit Criterion | Origin |
|---|---|---|---|
| A-1201 | Review and consolidate project documentation | Complete and internally consistent documentation set | Technical Data Management / Project Plan |
| A-1202 | Update final system architecture documentation | Architecture reflecting the implemented MVP | System Architecture / As-Built System |
| A-1203 | Update requirements traceability matrix | Complete requirement-to-implementation-to-verification traceability | Requirements Traceability |
| A-1204 | Consolidate experimental results | Final tables, metrics, plots, and experiment summaries | WP-09 / Evaluation Plan |
| A-1205 | Consolidate verification and validation results | Final V&V evidence and acceptance status | WP-10 |
| A-1206 | Document final system limitations | Explicit technical, experimental, and operational limitations | Evaluation / Validation |
| A-1207 | Document future work | Prioritized post-MVP improvements and research opportunities | Project Scope / Research Findings |
| A-1208 | Prepare final technical report | Complete final project report | Project Deliverables |
| A-1209 | Complete repository README and usage documentation | Repository can be understood and executed from documentation | Reproducibility / Deployment |
| A-1210 | Prepare final architecture and results diagrams | Approved visual material for report and presentation | Communication / Documentation |
| A-1211 | Prepare demonstration scenario | Stable and repeatable end-to-end demo | MVP Definition / Validation |
| A-1212 | Execute demonstration rehearsal | Successful rehearsal without critical failures | Presentation Readiness |
| A-1213 | Prepare final presentation | Completed presentation deck | Project Deliverables |
| A-1214 | Review technical claims and supporting evidence | All reported claims traceable to results or references | Research / Technical Data Management |
| A-1215 | Freeze final project baseline | Final code, documentation, models/configuration, and results identified | Configuration Management |
| A-1216 | Create final repository release and Git tag | Versioned final project release | Configuration Management |
| A-1217 | Deliver final project presentation and demonstration | Project formally presented | Project Completion |
| A-1218 | Archive final project artifacts | Final documentation, results, configurations, and evidence preserved | Technical Data Management |

## 4. Activity Definition
## 5. Activity Dependencies
## 6. Time Estimation
## 7. Schedule Calculation
## 8. Critical Path Analysis
## 9. Milestones
## 10. Project Calendar
## 11. Gantt Chart
## 12. Schedule Risks and Contingencies
## 13. Plan Maintenance