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

| Activity ID | Activity | Deliverable / Exit Criterion | Origin | Status |
|---|---|---|---|---|
| A-101 | Define project problem | Approved Problem Definition | Project Definition | Done |
| A-102 | Define system requirements | Approved SRS v1.0 | System Requirements | Done |
| A-103 | Define project methodology | Approved Methodology v1.0 | Project Methodology | Done |
| A-104 | Define MVP scope | Approved MVP Definition | Project Scope | Pending |
| A-105 | Define evaluation strategy | Initial Evaluation Plan | Evaluation | Pending |
| A-106 | Define high-level system architecture | Architecture baseline | System Architecture | Pending |
| A-107 | Build initial project plan | Approved Project Plan baseline | Project Planning | In Progress |

### WP-02 — Data and Knowledge Preparation

| Activity ID | Activity | Deliverable / Exit Criterion | Origin | Status |
|---|---|---|---|---|
| A-201 | Identify and confirm project data sources | Approved list of project data sources | Data Requirements / Problem Definition | Done |
| A-202 | Acquire selected datasets and technical documents | Raw data and document collection available locally | Data Requirements | Pending |
| A-203 | Inspect source structure and content | Initial data/source audit | Data Feasibility | Pending |
| A-204 | Define data inclusion and exclusion criteria | Documented selection criteria | MVP Definition / Evaluation Plan | Pending |
| A-205 | Define data schema and metadata requirements | Initial data and metadata schema | Data Requirements | Pending |
| A-206 | Clean and normalize selected data | Cleaned and normalized dataset/corpus | Data Requirements | Pending |
| A-207 | Extract and preserve source metadata | Metadata associated with every usable source | Traceability Requirements | Pending |
| A-209 | Build the initial telecommunications knowledge corpus | Versioned initial corpus | FR — Technical Knowledge Retrieval | Pending |
| A-210 | Validate corpus integrity and traceability | Corpus validation report | Verification / Data Requirements | Pending |
| A-211 | Create development and evaluation source partitions | Controlled source partitions that reduce evaluation leakage | Evaluation Plan / Leakage Control | Pending |
| A-212 | Version and document the prepared corpus | Reproducible corpus version and manifest | Reproducibility Requirements | Pending |

### WP-03 — Retrieval Baselines

| Activity ID | Activity | Deliverable / Exit Criterion | Origin | Status |
|---|---|---|---|---|
| A-301 | Define retrieval baseline scope and interface | Documented retrieval input/output contract and baseline scope | System Architecture / Retrieval Requirements | Pending |
| A-302 | Implement lexical retrieval baseline | Functional BM25 retriever | FR — Technical Knowledge Retrieval / Baseline Definition | Pending |
| A-303 | Implement dense single-vector retrieval baseline | Functional dense retriever | FR — Technical Knowledge Retrieval / Research Question | Pending |
| A-304 | Define reproducible baseline configurations | Versioned BM25 and dense retrieval configurations | Reproducibility / Baseline Definition | Pending |
| A-305 | Execute functional baseline retrieval tests | Both retrievers operate correctly on the prepared corpus | Verification / Integration Preparation | Pending |
| A-306 | Establish retrieval implementation baseline | Versioned retrieval baselines ready for formal evaluation | Baseline Definition | Pending |

### WP-04 — RAG System

| Activity ID | Activity | Deliverable / Exit Criterion | Origin | Status |
|---|---|---|---|---|
| A-401 | Define the initial RAG pipeline | Documented retrieval-to-generation processing flow | System Architecture / FR — Technical Knowledge Retrieval | Pending |
| A-402 | Define RAG retrieval configuration | Approved retriever selection and retrieval parameters for the initial RAG baseline | Retrieval Baseline / RAG Architecture | Pending |
| A-403 | Integrate retrieval subsystem with the RAG pipeline | Functional query-to-evidence retrieval integration | FR — Technical Knowledge Retrieval | Pending |
| A-404 | Define retrieved-context construction strategy | Documented context assembly policy | RAG Architecture | Pending |
| A-405 | Implement context construction component | Functional evidence-to-context transformation | RAG Architecture / Interface Requirements | Pending |
| A-406 | Preserve evidence provenance through RAG context construction | Source metadata retained through the RAG pipeline | Traceability Requirements | Pending |
| A-407 | Implement retrieval failure and insufficient-evidence handling | Defined behavior for missing, irrelevant, or insufficient evidence | Reliability / Safety Requirements | Pending |
| A-408 | Implement basic RAG logging and observability | Logs for queries, retrieval results, selected context, and processing metadata | Evaluation / Reproducibility | Pending |
| A-409 | Integrate RAG context output with the RCA generation interface | RAG pipeline provides structured evidence context to the generation component | WP-05 / Interface Requirements | Pending |
| A-410 | Execute functional end-to-end RAG pipeline tests | Successful query-to-context-to-generation-interface tests | Verification Plan | Pending |
| A-411 | Establish RAG implementation baseline | Reproducible RAG pipeline v1.0 ready for formal evaluation | Baseline Definition | Pending |

### WP-05 — LLM and RCA Generation

| Activity ID | Activity | Deliverable / Exit Criterion | Origin | Status |
|---|---|---|---|---|
| A-501 | Define RCA generation task | Documented RCA generation objective and input/output contract | FR — RCA Assistance / System Requirements | Pending |
| A-502 | Define structured RCA output format | Approved RCA response schema | FR — RCA Assistance / Traceability | Pending |
| A-503 | Define LLM selection criteria | Documented model selection criteria | Technical Constraints / Resource Feasibility | Pending |
| A-504 | Select initial LLM candidate | Approved initial model configuration | Resource Feasibility / Architecture | Pending |
| A-505 | Define initial prompting and instruction strategy | Versioned RCA instruction template | LLM Generation Design | Pending |
| A-506 | Implement RCA generation component | Functional structured RCA generation module | FR — RCA Assistance | Pending |
| A-507 | Implement LLM-only RCA baseline | Functional RCA pipeline without retrieval | Baseline Definition / Research Evaluation | Pending |
| A-508 | Integrate RAG context with RCA generation | Functional evidence-grounded RCA generation pipeline | WP-04 / FR — RCA Assistance | Pending |
| A-509 | Implement evidence attribution in RCA output | Generated RCA claims linked to supporting evidence | Traceability Requirements | Pending |
| A-510 | Implement uncertainty and abstention behavior | Defined response behavior for insufficient or conflicting evidence | Safety / Reliability Requirements | Pending |
| A-511 | Execute functional RCA generation tests | Successful generation, schema, attribution, and abstention tests | Verification / Integration Preparation | Pending |
| A-512 | Establish RCA generation implementation baseline | Reproducible RCA generation baseline v1.0 ready for formal evaluation | Baseline Definition / Reproducibility | Pending |

### WP-06 — Agentic Capabilities

| Activity ID | Activity | Deliverable / Exit Criterion | Origin | Status |
|---|---|---|---|---|
| A-601 | Define agent responsibilities and autonomy boundaries | Documented agent role, responsibilities, and permitted autonomy | System Requirements / AI Governance | Pending |
| A-602 | Define agent state and execution lifecycle | Documented agent state model and execution lifecycle | System Architecture | Pending |
| A-603 | Define agent planning and action-selection strategy | Documented initial planning and action policy | Agent Architecture / Research | Pending |
| A-604 | Define available agent tools and semantic contracts | Approved tool registry with tool purposes, inputs, and outputs | Functional Requirements / Security Requirements | Pending |
| A-605 | Implement standardized tool invocation interface | Functional interface for requesting and receiving tool executions | Interface Requirements | Pending |
| A-606 | Implement agent execution loop | Functional action-observation execution loop | FR — Agentic Assistance | Pending |
| A-607 | Integrate technical knowledge retrieval as an agent tool | Agent can invoke retrieval when additional evidence is required | FR — Technical Knowledge Retrieval | Pending |
| A-608 | Integrate RCA generation with the agent workflow | Agent can request and produce evidence-supported RCA output | FR — RCA Assistance | Pending |
| A-609 | Implement agent state and context management | Task state, observations, evidence, and tool results maintained during execution | Architecture / Reliability | Pending |
| A-610 | Implement execution limits and stopping conditions | Controlled limits for steps, tool calls, failures, and termination | Safety / Operational Requirements | Pending |
| A-611 | Implement human approval checkpoints | Actions requiring supervision are blocked until explicitly approved | Governance / Safety Requirements | Pending |
| A-612 | Implement tool-result validation and error handling | Invalid, failed, or incomplete tool results handled without uncontrolled execution | Reliability Requirements | Pending |
| A-613 | Implement agent action logging and traceability | Reconstructable agent action and observation history | Traceability / Evaluation | Pending |
| A-614 | Execute functional agent workflow tests | Agent successfully completes controlled action-observation workflows | Verification / Integration Preparation | Pending |
| A-615 | Establish agent implementation baseline | Reproducible agent baseline v1.0 ready for formal evaluation | Baseline Definition / Reproducibility | Pending |

### WP-07 — Tool Execution and Sandboxing

| Activity ID | Activity | Deliverable / Exit Criterion | Origin | Status |
|---|---|---|---|---|
| A-701 | Define tool execution threat model | Documented execution threats, assets, and trust boundaries | AI Governance / Security Requirements | Pending |
| A-702 | Define sandbox security and isolation requirements | Approved execution, isolation, and resource-control requirements | Security / Operational Requirements | Pending |
| A-703 | Select sandboxing mechanism and document architecture decision | Approved sandbox technology decision and ADR | Architecture / ADR | Pending |
| A-704 | Define sandbox permission and execution policy | Approved tool allowlist, filesystem, network, and privilege policies | Security Requirements | Pending |
| A-705 | Define sandbox execution input/output contract | Standardized execution request and result schema | Interface Requirements | Pending |
| A-706 | Build isolated execution environment | Functional isolated execution environment | Security Requirements | Pending |
| A-707 | Implement sandbox execution controller | Controlled component for starting, monitoring, and terminating executions | FR — Tool Execution | Pending |
| A-708 | Implement resource and runtime controls | CPU, memory, process, and execution-time limits enforced | Reliability / Security Requirements | Pending |
| A-709 | Implement isolation and privilege controls | Filesystem, network, privilege, and syscall restrictions enforced | Security Requirements | Pending |
| A-710 | Implement structured execution results, logging, and audit trail | stdout, stderr, exit status, metadata, and execution records available | Traceability / Governance | Pending |
| A-711 | Execute functional sandbox and isolation tests | Sandbox passes controlled isolation, resource-limit, and termination tests | Verification / Integration Preparation | Pending |
| A-712 | Establish sandbox implementation baseline | Reproducible sandbox baseline v1.0 ready for integration and formal verification | Architecture / Reproducibility | Pending |

### WP-08 — System Integration

| Activity ID | Activity | Deliverable / Exit Criterion | Origin | Status |
|---|---|---|---|---|
| A-801 | Define system integration strategy and sequence | Documented integration sequence and dependencies | System Architecture / Integration Planning | Pending |
| A-802 | Review and finalize component interface contracts | Compatible and approved interfaces between system components | Interface Requirements / Interface Management | Pending |
| A-803 | Integrate knowledge corpus with retrieval subsystem | Retrieval subsystem operates correctly on the prepared project corpus | WP-02 / WP-03 | Pending |
| A-804 | Integrate retrieval subsystem with RAG pipeline | Functional query-to-evidence-to-context flow | WP-03 / WP-04 | Pending |
| A-805 | Integrate RAG context with RCA generation | Functional evidence-grounded RCA generation flow | WP-04 / WP-05 | Pending |
| A-806 | Integrate RCA generation with agent workflow | Agent can invoke and consume RCA generation capability | WP-05 / WP-06 | Pending |
| A-807 | Integrate agent tool interface with sandbox execution controller | Agent tool calls execute through the controlled sandbox layer | WP-06 / WP-07 | Pending |
| A-808 | Integrate human approval and control mechanisms | Actions requiring approval respect defined human-in-the-loop controls | Governance / Safety Requirements | Pending |
| A-809 | Integrate system-wide logging and trace correlation | Retrieval, generation, agent, and sandbox events can be correlated end-to-end | Traceability Requirements | Pending |
| A-810 | Implement cross-component error propagation and recovery | Component failures are propagated and handled in a controlled manner | Reliability Requirements | Pending |
| A-811 | Execute incremental integration tests | All planned subsystem integration pairs pass functional integration tests | Integration Plan | Pending |
| A-812 | Execute complete end-to-end system test | Incident-to-RCA workflow operates across the complete integrated system | System Requirements | Pending |
| A-813 | Resolve critical integration defects and establish integrated system baseline | Critical integration defects resolved and reproducible integrated MVP baseline established | Configuration Management / Integration | Pending |

### WP-09 — Evaluation and Experiments

| Activity ID | Activity | Deliverable / Exit Criterion | Origin | Status |
|---|---|---|---|---|
| A-901 | Define research questions and experimental hypotheses | Approved research questions, evaluation objectives, and testable hypotheses | Project Methodology / Research Methodology | Pending |
| A-902 | Define experimental systems and baselines | Approved comparison matrix identifying baseline and proposed system configurations | Baseline Definition / Evaluation Plan | Pending |
| A-903 | Define evaluation datasets, queries, and scenarios | Versioned evaluation set with relevance evidence, RCA references, and agent scenarios | Evaluation Plan / Data Requirements | Pending |
| A-904 | Define evaluation framework and metrics | Approved retrieval, RCA, agent, and system-level metrics and scoring procedures | Evaluation Plan | Pending |
| A-905 | Define experimental protocol, controls, and fixed variables | Reproducible experiment protocol and controlled configuration | Experiment Protocol / Reproducibility | Pending |
| A-906 | Implement experiment execution and result-capture harness | Reproducible experiment runner with configuration, output, and metadata capture | Reproducibility Requirements | Pending |
| A-907 | Execute retrieval baseline experiments | BM25 and dense single-vector retrieval benchmark results | Research Question / WP-03 | Pending |
| A-908 | Execute LLM-only and RAG-assisted RCA experiments | Comparable RCA results for non-retrieval and RAG configurations | WP-04 / WP-05 | Pending |
| A-909 | Execute agentic system experiments | Agentic workflow experiment results | WP-06 / Research Questions | Pending |
| A-910 | Execute robustness and controlled failure-case experiments | Results for missing, conflicting, irrelevant, or failed evidence/tool conditions | Risk / Evaluation | Pending |
| A-911 | Measure end-to-end latency and computational resource usage | System performance and resource benchmark results | Performance / Resource Feasibility | Pending |
| A-912 | Perform comparative and statistical analysis | Comparative analysis with appropriate uncertainty/statistical treatment | Research Methodology | Pending |
| A-913 | Conduct qualitative and component-level failure analysis | Categorized retrieval, generation, agent, and execution failure cases | Research / Evaluation | Pending |
| A-914 | Evaluate research hypotheses and answer research questions | Evidence-based findings for each defined hypothesis and research question | Research Methodology | Pending |
| A-915 | Document experimental limitations and threats to validity | Explicit internal, external, construct, and experimental limitations | Research Methodology | Pending |
| A-916 | Establish final experimental results baseline | Versioned and reproducible experiment results package | Project Evaluation / Reproducibility | Pending |

### WP-10 — Verification and Validation

| Activity ID | Activity | Deliverable / Exit Criterion | Origin | Status |
|---|---|---|---|---|
| A-1001 | Review and baseline the requirements set for verification | Approved and versioned requirements baseline | System Requirements / Traceability | Pending |
| A-1002 | Define verification matrix, methods, and procedures | Requirements Verification Matrix with verification method, procedure, and acceptance criteria for each applicable requirement | Verification Plan | Pending |
| A-1003 | Define validation objectives and representative operational scenarios | Approved validation objectives and 5G troubleshooting scenarios derived from stakeholder needs | Problem Definition / Need / MVP Definition | Pending |
| A-1004 | Prepare the verification and validation environment | Reproducible V&V configuration, datasets, tools, and system baseline ready for execution | Deployment / Verification Plan | Pending |
| A-1005 | Execute functional, data, and interface verification | Verified FR, data, knowledge, and interface requirements with recorded evidence | System Requirements | Pending |
| A-1006 | Execute security and sandbox verification | Verified security, isolation, permission, and execution-control requirements | Security Requirements / WP-07 | Pending |
| A-1007 | Execute performance, operational, and reliability verification | Verified performance, operational, and reliability requirements | Performance / Operational Requirements | Pending |
| A-1008 | Execute end-to-end system verification | Integrated system demonstrates compliance with applicable system-level requirements | System Requirements | Pending |
| A-1009 | Record requirement compliance and verification evidence | Updated Requirements Traceability Matrix with PASS / FAIL / BLOCKED status and evidence | Traceability | Pending |
| A-1010 | Resolve verification discrepancies and execute regression verification | Critical nonconformities corrected and affected verification procedures successfully repeated | Verification Process / Corrective Action | Pending |
| A-1011 | Execute system validation scenarios | Representative 5G troubleshooting scenarios completed under defined conditions | Validation Plan | Pending |
| A-1012 | Evaluate fulfillment of the intended troubleshooting need | Evidence-based assessment of whether the MVP satisfies defined stakeholder needs within project scope | Problem Definition / Need | Pending |
| A-1013 | Analyze validation anomalies, limitations, and unresolved gaps | Documented validation findings and limitations | Validation Process | Pending |
| A-1014 | Produce Verification and Validation Report | Complete V&V report with requirements compliance and validation findings | Project Acceptance | Pending |
| A-1015 | Establish V&V status baseline | Verification and validation evidence frozen for the evaluated MVP configuration | Configuration Management / Acceptance | Pending |

### WP-11 — Deployment and Reproducibility

| Activity ID | Activity | Deliverable / Exit Criterion | Origin | Status |
|---|---|---|---|---|
| A-1101 | Define MVP deployment topology | Approved deployment topology identifying runtime components and execution boundaries | System Architecture / Operational Constraints | Pending |
| A-1102 | Define runtime environment and dependency policy | Documented OS, runtime, model, software, and dependency requirements | Reproducibility Requirements | Pending |
| A-1103 | Define configuration and secrets management approach | Approved configuration strategy with sensitive values excluded from source control | Security / Deployment Requirements | Pending |
| A-1104 | Define configuration-item and artifact version identifiers | Versioning convention for code, models, corpus, prompts, and system configuration | Configuration Management / Traceability | Pending |
| A-1105 | Containerize required MVP components | Functional and version-controlled Docker images | Deployment Requirements | Pending |
| A-1106 | Implement local orchestration, persistence, and runtime storage | Working local orchestration with required volumes and persistent artifacts | Deployment / Data Requirements | Pending |
| A-1107 | Implement health, readiness, and basic operational checks | Runtime components expose observable operational status | Reliability Requirements | Pending |
| A-1108 | Create reproducible build and environment initialization procedure | System can be rebuilt from repository source and controlled dependencies | Reproducibility Requirements | Pending |
| A-1109 | Create reproducible startup and execution procedure | Integrated MVP can be started and operated using a documented procedure | Deployment Requirements | Pending |
| A-1110 | Execute clean-environment deployment and reproducibility tests | System successfully rebuilt and executed from a clean controlled environment | Verification / Reproducibility Requirements | Pending |
| A-1111 | Document deployment and execution runbook | Complete deployment, configuration, startup, shutdown, and troubleshooting instructions | Technical Data Management | Pending |
| A-1112 | Establish deployable and reproducible MVP baseline | Versioned deployment configuration ready for final project baseline | Configuration Management | Pending |

### WP-12 — Final Documentation and Presentation

| Activity ID | Activity | Deliverable / Exit Criterion | Origin | Status |
|---|---|---|---|---|
| A-1201 | Review and consolidate as-built project documentation | Complete and internally consistent documentation reflecting the implemented MVP | Technical Data Management / Project Plan | Pending |
| A-1202 | Finalize system architecture, interfaces, and technical diagrams | Final as-built architecture and supporting diagrams | System Architecture / As-Built System | Pending |
| A-1203 | Consolidate traceability, experimental results, and V&V evidence | Final traceability matrix, experiment evidence, and V&V results package | WP-09 / WP-10 / Requirements Traceability | Pending |
| A-1204 | Document final limitations, conclusions, and future work | Explicit findings, limitations, conclusions, and prioritized post-MVP work | Evaluation / Validation / Research Findings | Pending |
| A-1205 | Prepare final technical report | Complete final project report supported by project evidence and references | Project Deliverables | Pending |
| A-1206 | Complete repository README and user/deployment guidance | Repository can be understood, built, executed, and evaluated from its documentation | WP-11 / Reproducibility | Pending |
| A-1207 | Prepare final demonstration scenario | Stable and repeatable end-to-end demonstration scenario | MVP Definition / Validation | Pending |
| A-1208 | Prepare final presentation | Completed presentation based on final architecture, results, and conclusions | Project Deliverables | Pending |
| A-1209 | Conduct final technical review and demonstration rehearsal | Technical claims verified against evidence and demonstration completed without critical failures | Research / Presentation Readiness | Pending |
| A-1210 | Freeze final project baseline | Final code, documentation, configurations, models, corpus versions, and results identified | Configuration Management | Pending |
| A-1211 | Create final repository release and Git tag | Versioned and identifiable final project release | Configuration Management | Pending |
| A-1212 | Deliver project and archive final artifacts | Final presentation/demo completed and project artifacts preserved | Project Completion / Technical Data Management | Pending |

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