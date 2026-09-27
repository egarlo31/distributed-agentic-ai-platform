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

The activities defined in the Work Breakdown Structure represent the
discrete units of work required to produce the planned project deliverables.

Each activity is defined by:

- a unique Activity ID;
- an associated Work Package;
- a clear activity description;
- a defined deliverable or exit criterion;
- a traceable origin in project requirements, architecture, methodology,
  evaluation, verification, or other project documentation;
- a measurable completion condition;
- a current execution status.

Activities shall be sufficiently detailed to support dependency analysis,
time estimation, scheduling, progress tracking, and verification of completion.

Detailed implementation tasks that do not require independent schedule
control shall be managed as subtasks or repository issues and shall not
necessarily appear as individual Project Plan activities.

The complete set of project activities is defined in Section 3,
Work Breakdown Structure. Activity dependencies are defined in Section 5,
and activity duration estimates are defined in Section 6.

### 4.1 Activity Attributes

| Attribute | Description |
|---|---|
| Activity ID | Unique identifier assigned to the activity. |
| Work Package | WBS element to which the activity belongs. |
| Activity | Concise description of the work to be performed. |
| Deliverable / Exit Criterion | Observable result required to consider the activity complete. |
| Origin | Requirement, document, technical decision, or project need that justifies the activity. |
| Status | Current state of execution: Pending, In Progress, Done, Blocked, or Deferred. |

## 5. Activity Dependencies

Activity dependencies define the logical execution order between project
activities and identify which activities may be performed sequentially or
in parallel.

Dependencies shall be based on technical, logical, information, or
deliverable precedence rather than arbitrary Work Package numbering.

The default dependency relationship used in the project schedule is
Finish-to-Start (FS), meaning that a successor activity cannot begin until
its predecessor has been completed.

Alternative relationships such as Start-to-Start (SS) or Finish-to-Finish
(FF) may be used when concurrent execution is technically justified.

The dependency network shall avoid circular, redundant, or unjustified
relationships and shall preserve opportunities for parallel execution where
possible.

### 5.1 Dependency Attributes

| Attribute | Description |
|---|---|
| Activity ID | Activity whose dependencies are being defined. |
| Predecessor(s) | Activity or activities that must satisfy the required logical relationship before the activity can proceed. |
| Relationship | Logical dependency type, primarily Finish-to-Start (FS). |
| Dependency Rationale | Technical or project reason that justifies the dependency. |

### 5.2 WP-01 — Project Definition and Planning Dependencies

| Activity ID | Predecessor(s) | Relationship | Dependency Rationale |
|---|---|---|---|
| A-101 | — | — | Project-start activity. The project problem, stakeholder need, scope context, and constraints provide the foundation for downstream engineering activities. |
| A-102 | A-101 | FS | System requirements are derived from the defined problem, stakeholder needs, assumptions, constraints, and expected system capabilities. |
| A-103 | A-101 | FS | The project methodology can be defined once the problem, project nature, and objectives are understood; it does not require completion of the full requirements specification. |
| A-104 | A-102 | FS | The MVP scope is bounded using the established system requirements to determine which capabilities are included in the initial implementation. |
| A-105 | A-103, A-104 | FS | The evaluation strategy depends on the selected methodology and on the capabilities actually included in the MVP. |
| A-106 | A-102, A-104 | FS | The high-level architecture must satisfy the applicable requirements while remaining within the defined MVP boundary. |
| A-107 | A-105, A-106 | FS | The initial Project Plan baseline can be finalized once the evaluation approach and high-level architecture provide sufficient information to structure, estimate, and schedule the remaining technical work. |

### 5.3 WP-02 — Data and Knowledge Preparation Dependencies

| Activity ID | Predecessor(s) | Relationship | Dependency Rationale |
|---|---|---|---|
| A-201 | A-104 | FS | Project data sources can be formally selected once the MVP scope identifies the capabilities, technical knowledge, and evidence required for the initial system. |
| A-202 | A-201 | FS | Selected datasets and technical documents must be identified and approved before they are acquired for project use. |
| A-203 | A-202 | FS | Source structure, format, content, metadata, quality, and limitations can be systematically inspected once the selected source collection is available. |
| A-204 | A-203, A-105 | FS | Inclusion and exclusion criteria depend on the characteristics of the available sources and on the evaluation strategy that determines what evidence is relevant to the project objectives. |
| A-205 | A-203 | FS | Data schema and metadata requirements are defined after the actual structure and available fields of the selected sources have been inspected. |
| A-206 | A-204, A-205 | FS | Cleaning and normalization require both approved selection criteria and a defined target data/schema structure. |
| A-207 | A-204, A-205 | FS | Source metadata can be systematically extracted and preserved once the usable source set and required metadata structure have been defined. |
| A-208 | A-206, A-207 | FS | Retrieval-ready document units require normalized source content together with preserved identifiers and source metadata so that later retrieval remains traceable to the original evidence. |
| A-209 | A-208 | FS | The initial telecommunications knowledge corpus is assembled from the prepared and traceable document units. |
| A-210 | A-209 | FS | Corpus integrity, completeness, and source traceability can be validated once the initial corpus has been assembled. |
| A-211 | A-210 | FS | Development and evaluation source partitions are created only after the corpus has passed integrity and traceability checks, reducing the risk of partitioning invalid or incomplete data. |
| A-212 | A-211 | FS | The prepared corpus, its partitions, metadata, and manifest can be versioned and documented once corpus preparation and controlled partitioning are complete. |

### 5.4 WP-03 — Retrieval Baselines Dependencies

| Activity ID | Predecessor(s) | Relationship | Dependency Rationale |
|---|---|---|---|
| A-301 | A-105, A-106 | FS | The retrieval baseline scope and common input/output interface depend on the evaluation strategy and on the high-level system architecture that defines how retrieval interacts with downstream components. |
| A-302 | A-301, A-212 | FS | The lexical retrieval baseline requires an approved retrieval interface and a versioned, prepared telecommunications corpus on which BM25 can operate reproducibly. |
| A-303 | A-301, A-212 | FS | The dense single-vector retrieval baseline requires the common retrieval interface and the same versioned corpus so that its implementation is compatible and later comparisons are controlled. |
| A-304 | A-302, A-303 | FS | Reproducible baseline configurations can be finalized after both retrieval implementations exist and their actual parameters, models, indexing settings, and corpus versions are known. |
| A-305 | A-304 | FS | Functional retrieval tests require configured and reproducible implementations to verify query handling, ranking, top-k behavior, identifiers, scores, and metadata preservation. |
| A-306 | A-305 | FS | The retrieval implementation baseline can be established only after both retrievers have successfully completed the required functional tests. |

### 5.5 WP-04 — RAG System Dependencies

| Activity ID | Predecessor(s) | Relationship | Dependency Rationale |
|---|---|---|---|
| A-401 | A-106, A-301 | FS | The initial RAG pipeline can be defined once the high-level architecture and the common retrieval interface establish the expected retrieval-to-generation flow and component boundaries. |
| A-402 | A-401, A-304 | FS | The initial RAG retrieval configuration depends on the defined RAG flow and on known reproducible configurations for the available retrieval implementations. |
| A-403 | A-402, A-306 | FS | Retrieval can be integrated into the RAG pipeline after the selected retrieval configuration is defined and the retrieval subsystem has passed its functional baseline tests. |
| A-404 | A-402 | FS | The retrieved-context construction strategy depends on the selected retrieval configuration, including the expected evidence representation and retrieval parameters, but does not require completion of retrieval integration. |
| A-405 | A-403, A-404 | FS | The context construction component requires both a functioning retrieval integration and an approved strategy for transforming retrieved evidence into model-ready context. |
| A-406 | A-405 | FS | Evidence provenance can be propagated through the RAG pipeline once the context construction component exists and preserves the source information associated with retrieved evidence. |
| A-407 | A-405 | FS | Failure and insufficient-evidence behavior can be implemented once retrieval and context construction behavior are available to identify missing, irrelevant, or unusable evidence conditions. |
| A-408 | A-406, A-407 | FS | RAG logging and observability can be completed once provenance and failure-handling behavior are implemented so that normal and exceptional execution paths can be recorded. |
| A-409 | A-406, A-407, A-501 | FS | The RAG context output can be aligned with the RCA generation interface after evidence provenance and failure behavior are defined and the RCA generation input/output contract is available. |
| A-410 | A-408, A-409 | FS | Functional end-to-end RAG pipeline testing requires the operational RAG path, observability, and the generation-interface handoff to be available. |
| A-411 | A-410 | FS | The RAG implementation baseline can be established only after the complete RAG pipeline has successfully passed the required functional tests. |

### 5.6 WP-05 — LLM and RCA Generation Dependencies

| Activity ID | Predecessor(s) | Relationship | Dependency Rationale |
|---|---|---|---|
| A-501 | A-102, A-104 | FS | The RCA generation task can be defined once the applicable system requirements and MVP scope establish the intended troubleshooting capability and its boundaries. |
| A-502 | A-501 | FS | The structured RCA output format depends on the defined generation task and must represent the information required from an RCA response in a consistent and traceable form. |
| A-503 | A-501, A-104, A-106 | FS | LLM selection criteria depend on the RCA task, MVP constraints, and high-level architecture, including expected interfaces and deployment/resource constraints. |
| A-504 | A-503 | FS | An initial LLM candidate can be selected only after the technical, functional, and resource criteria for model selection have been defined. |
| A-505 | A-502, A-504 | FS | The prompting and instruction strategy depends on the selected model and on the required structured RCA output format. |
| A-506 | A-505 | FS | The RCA generation component can be implemented once the selected model, prompt/instruction strategy, and required output structure are known. |
| A-507 | A-506 | FS | The LLM-only RCA baseline requires a functional RCA generation component operating without retrieval context. |
| A-508 | A-506, A-409 | FS | RAG context can be integrated into RCA generation after the generation component exists and the RAG subsystem exposes the defined context-to-generation interface. |
| A-509 | A-508 | FS | Evidence attribution in generated RCA output requires the evidence-grounded generation path so that generated claims can be linked to the provenance information supplied by the RAG subsystem. |
| A-510 | A-507, A-508 | FS | Uncertainty and abstention behavior can be implemented consistently once both non-retrieval and evidence-grounded generation paths are available and insufficient or conflicting evidence conditions can be represented. |
| A-511 | A-507, A-509, A-510, A-411 | FS | Functional RCA tests require the LLM-only path, evidence attribution, uncertainty handling, and the tested RAG implementation to verify the complete generation behavior. |
| A-512 | A-511 | FS | The RCA generation implementation baseline can be established only after the generation component and its supported execution modes have passed the required functional tests. |

### 5.7 WP-06 — Agentic Capabilities Dependencies

| Activity ID | Predecessor(s) | Relationship | Dependency Rationale |
|---|---|---|---|
| A-601 | A-102, A-104, A-106 | FS | Agent responsibilities and autonomy boundaries depend on the approved system requirements, MVP scope, and high-level architecture that define the capabilities assigned to the agent and the limits of automated behavior. |
| A-602 | A-601 | FS | The agent state model and execution lifecycle can be defined once the permitted agent responsibilities and autonomy boundaries are established. |
| A-603 | A-601, A-602 | FS | The planning and action-selection strategy depends on the agent role and on the execution lifecycle within which decisions and actions occur. |
| A-604 | A-601, A-301, A-501 | FS | The initial tool registry and semantic contracts depend on the agent responsibilities and on the available retrieval and RCA capability interfaces that the agent may invoke. |
| A-605 | A-604 | FS | A standardized tool invocation interface can be implemented once the available tools and their semantic input/output contracts have been defined. |
| A-606 | A-602, A-603, A-605 | FS | The agent execution loop requires a defined lifecycle, action-selection strategy, and standardized mechanism for invoking tools and receiving observations. |
| A-609 | A-602, A-606 | FS | State and context management can be implemented once the state model and basic execution loop exist, allowing observations, actions, evidence, and intermediate task state to be maintained across execution steps. |
| A-607 | A-605, A-609, A-306 | FS | Technical knowledge retrieval can be integrated as an agent tool after the tool interface and state-management mechanisms exist and the retrieval implementation baseline is available. |
| A-608 | A-609, A-512 | FS | RCA generation can be integrated into the agent workflow after agent state management is available and the RCA generation implementation baseline has been established. |
| A-610 | A-606, A-609 | FS | Execution limits and stopping conditions require a functioning execution loop and state representation through which step counts, retries, failures, and completion conditions can be controlled. |
| A-611 | A-604, A-609 | FS | Human approval checkpoints depend on the defined tool/action registry and agent state so that actions requiring approval can be identified and execution can be suspended and resumed in a controlled manner. |
| A-612 | A-605, A-607 | FS | Tool-result validation and error handling require the standardized tool interface and at least one integrated operational tool so that failed, malformed, incomplete, or invalid results can be handled consistently. |
| A-613 | A-607, A-608, A-610, A-611, A-612 | FS | Agent execution logging and traceability can be completed once the major execution paths, integrated capabilities, control mechanisms, and error-handling behavior are available to be recorded. |
| A-614 | A-613 | FS | Functional agent workflow tests require the implemented retrieval and RCA capabilities, state management, execution controls, approval behavior, error handling, and execution trace to be available. |
| A-615 | A-614 | FS | The agent implementation baseline can be established only after the complete agent workflow has passed its required functional tests. |

### 5.8 WP-07 — Tool Execution and Sandboxing Dependencies

| Activity ID | Predecessor(s) | Relationship | Dependency Rationale |
|---|---|---|---|
| A-701 | A-601, A-604 | FS | The tool-execution threat model depends on the defined agent autonomy boundaries and on the types of tools and operations that may be invoked, since these determine the relevant assets, attack surfaces, and trust boundaries. |
| A-702 | A-701, A-102 | FS | Sandbox security and isolation requirements are derived from the identified execution threats together with the applicable system security and operational requirements. |
| A-703 | A-702, A-106 | FS | The sandboxing mechanism can be selected once the required security properties are known and the high-level architecture establishes the deployment and execution constraints within which the mechanism must operate. |
| A-704 | A-702, A-604 | FS | The sandbox permission and execution policy depends on the defined security requirements and on the approved tool registry so that each tool can be assigned appropriate permissions and restrictions. |
| A-705 | A-605, A-704 | FS | The sandbox execution input/output contract must align with the standardized agent tool interface and with the execution policy that determines what information and controls are required for each sandbox request. |
| A-706 | A-703, A-704 | FS | The isolated execution environment can be built after the sandbox technology and the required permission, filesystem, network, and privilege policies have been selected. |
| A-707 | A-705, A-706 | FS | The sandbox execution controller requires both a functional isolated environment and a defined request/result contract through which executions are started, monitored, terminated, and reported. |
| A-708 | A-702, A-707 | FS | Resource and runtime controls can be implemented once the controller exists and the required CPU, memory, process, and execution-time constraints have been defined. |
| A-709 | A-704, A-706 | FS | Filesystem, network, privilege, and syscall isolation controls are implemented according to the approved execution policy within the selected isolated environment. |
| A-710 | A-705, A-707 | FS | Structured execution results, logging, and audit records require the execution contract and controller so that stdout, stderr, exit status, timestamps, and execution metadata can be captured consistently. |
| A-711 | A-708, A-709, A-710 | FS | Functional sandbox and isolation tests require the resource controls, isolation controls, execution-result handling, and audit mechanisms to be implemented. |
| A-712 | A-711 | FS | The sandbox implementation baseline can be established only after the required functional, isolation, termination, and resource-control tests have passed. |

### 5.9 WP-08 — System Integration Dependencies

| Activity ID | Predecessor(s) | Relationship | Dependency Rationale |
|---|---|---|---|
| A-801 | A-106 | FS | The system integration strategy and sequence depend on the high-level architecture, which identifies the major system components, boundaries, and expected interactions. |
| A-802 | A-801, A-301, A-409, A-605, A-705 | FS | Component interface contracts can be reviewed and finalized once the integration strategy and the retrieval, RAG-to-generation, agent-tool, and sandbox execution interfaces have been defined. |
| A-803 | A-802, A-212, A-306 | FS | The knowledge corpus can be integrated with the retrieval subsystem after the component interfaces are finalized and both the versioned corpus and retrieval implementation baseline are available. |
| A-804 | A-803, A-411 | FS | System-level retrieval-to-RAG integration requires the retrieval subsystem operating on the project corpus and the tested RAG implementation baseline. |
| A-805 | A-804, A-512 | FS | RAG context can be integrated with RCA generation after the retrieval-to-context flow is operational and the RCA generation implementation baseline is available. |
| A-806 | A-805, A-615 | FS | RCA generation can be integrated into the complete agent workflow once the evidence-grounded generation path and the agent implementation baseline are available. |
| A-807 | A-802, A-615, A-712 | FS | The agent tool interface can be connected to controlled sandbox execution after the interface contracts, agent baseline, and sandbox implementation baseline are available. |
| A-808 | A-611, A-807 | FS | Human approval and control mechanisms can be integrated at system level once the agent approval logic exists and tool execution flows through the controlled sandbox path. |
| A-809 | A-806, A-807, A-808 | FS | System-wide trace correlation can be implemented once the principal agent, RCA, sandbox, tool, and human-control execution paths are connected. |
| A-810 | A-806, A-807, A-808 | FS | Cross-component error propagation and recovery require the major integrated execution paths so that failures can be transmitted and handled across component boundaries. |
| A-811 | A-809, A-810 | FS | Incremental integration tests require both unified observability and controlled cross-component failure handling to verify subsystem interactions and diagnose integration defects. |
| A-812 | A-811 | FS | The complete end-to-end system test can be executed after all planned incremental subsystem integrations have successfully completed. |
| A-813 | A-812 | FS | Critical integration defects can be resolved and the integrated system baseline established after complete end-to-end testing identifies the final integration issues requiring correction. |

### 5.10 WP-09 — Evaluation and Experiments Dependencies

| Activity ID | Predecessor(s) | Relationship | Dependency Rationale |
|---|---|---|---|
| A-901 | A-105 | FS | Research questions and experimental hypotheses are derived from the approved evaluation strategy, which establishes the objectives, comparison intent, and general evaluation approach of the project. |
| A-902 | A-901, A-106 | FS | Experimental systems and baselines can be defined once the research questions are established and the high-level architecture identifies the system configurations and components that may be compared. |
| A-903 | A-901, A-212 | FS | Evaluation datasets, queries, and scenarios require defined research questions and a versioned, controlled corpus with established development and evaluation source partitions. |
| A-904 | A-902, A-903 | FS | The evaluation framework and metric set depend on the systems being compared and on the structure, annotations, and expected outputs of the evaluation dataset and scenarios. |
| A-905 | A-904, A-1102 | FS | The experimental protocol, controls, and fixed variables can be finalized once the evaluation framework is defined and the controlled runtime environment and dependency policy are known. |
| A-906 | A-905, A-1104 | FS | The experiment execution and result-capture harness requires an approved experimental protocol and defined identifiers for models, corpus versions, prompts, configurations, and other experimental artifacts. |
| A-907 | A-906, A-306 | FS | Retrieval experiments require the experiment harness and the established lexical and dense retrieval implementation baselines. |
| A-908 | A-906, A-512 | FS | LLM-only and RAG-assisted RCA experiments require the experiment harness and the tested RCA generation baseline supporting both non-retrieval and evidence-grounded generation modes. |
| A-909 | A-906, A-813 | FS | Agentic system experiments require the experiment harness and the integrated system baseline so that the complete agentic workflow can be evaluated under controlled conditions. |
| A-910 | A-907, A-908, A-909 | FS | Robustness and controlled failure-case experiments are executed after nominal retrieval, RCA, and agentic behavior has been characterized, providing reference behavior against which degraded or abnormal conditions can be assessed. |
| A-911 | A-906, A-813, A-1109 | FS | End-to-end latency and computational resource measurements require the controlled experiment harness, the integrated system baseline, and a defined reproducible startup and execution procedure. |
| A-912 | A-907, A-908, A-909, A-910, A-911 | FS | Comparative and statistical analysis requires the completed retrieval, RCA, agentic, robustness, and performance experiment results. |
| A-913 | A-907, A-908, A-909, A-910, A-911 | FS | Qualitative and component-level failure analysis requires completed experimental evidence from the major system configurations, controlled failure cases, and system-level performance measurements. |
| A-914 | A-912, A-913 | FS | Research hypotheses can be evaluated and research questions answered only after quantitative comparative analysis and qualitative failure analysis have been completed. |
| A-915 | A-914 | FS | Experimental limitations and threats to validity can be finalized after the research findings are known and can be assessed against the actual protocol, evidence, and observed limitations. |
| A-916 | A-915 | FS | The final experimental results baseline can be established once findings, limitations, threats to validity, configurations, and supporting experiment artifacts have been completed and documented. |

### 5.11 WP-10 — Verification and Validation Dependencies

| Activity ID | Predecessor(s) | Relationship | Dependency Rationale |
|---|---|---|---|
| A-1001 | A-104 | FS | The requirements set applicable to verification can be reviewed and baselined once the MVP scope determines which system requirements are applicable to the implemented product configuration. |
| A-1002 | A-1001 | FS | Verification methods, procedures, and acceptance criteria are defined against the approved requirements baseline so that each applicable requirement has an identified verification approach. |
| A-1003 | A-104 | FS | Validation objectives and representative operational scenarios are derived from the approved MVP scope, stakeholder need, and intended 5G troubleshooting use of the system. |
| A-1004 | A-1002, A-1003, A-813, A-1109 | FS | The V&V environment can be prepared once the verification procedures and validation scenarios are defined, the integrated system baseline exists, and the system can be started and executed reproducibly. |
| A-1005 | A-1004 | FS | Functional, data, knowledge, and interface verification require the prepared V&V environment, applicable procedures, and controlled integrated system configuration. |
| A-1006 | A-1004 | FS | Security and sandbox verification require the prepared V&V environment and integrated system configuration so that isolation, permission, execution-control, and security requirements can be verified under controlled conditions. |
| A-1007 | A-1004, A-911 | FS | Performance, operational, and reliability verification use the controlled V&V environment together with system-level performance and resource measurements produced under the experimental configuration where applicable. |
| A-1008 | A-1005, A-1006, A-1007 | FS | End-to-end system verification is performed after the applicable functional, security, performance, operational, and reliability requirement groups have been verified at their respective levels. |
| A-1009 | A-1008 | FS | Final requirement compliance status and supporting evidence can be recorded after the planned requirement-level and system-level verification activities have been executed. |
| A-1010 | A-1009 | FS | Verification discrepancies are resolved and affected verification procedures are re-executed after the initial compliance results identify failed, blocked, or nonconforming requirements. |
| A-1011 | A-1003, A-1010 | FS | System validation scenarios are executed after verification is complete and any critical verification discrepancies have been resolved, using the previously defined representative operational scenarios. |
| A-1012 | A-1011, A-916 | FS | Fulfillment of the intended 5G troubleshooting need is evaluated using validation scenario results together with the completed experimental evidence and documented research findings. |
| A-1013 | A-1012 | FS | Validation anomalies, limitations, and unresolved gaps can be analyzed after the system has been evaluated against its intended operational need. |
| A-1014 | A-1013 | FS | The final Verification and Validation Report can be produced once verification evidence, validation findings, discrepancies, corrective actions, and limitations are complete. |
| A-1015 | A-1014 | FS | The V&V status baseline is established after the complete verification and validation evidence package has been reviewed and documented. |

### 5.12 WP-11 — Deployment and Reproducibility Dependencies

| Activity ID | Predecessor(s) | Relationship | Dependency Rationale |
|---|---|---|---|
| A-1101 | A-104, A-106 | FS | The MVP deployment topology depends on the approved MVP scope and high-level architecture, which identify the components, execution boundaries, and runtime responsibilities that must be deployed. |
| A-1102 | A-1101, A-504, A-703 | FS | The runtime environment and dependency policy depend on the deployment topology, the selected LLM configuration, and the selected sandboxing mechanism because these determine operating-system, runtime, model, container, and execution dependencies. |
| A-1103 | A-102, A-1101 | FS | Configuration and secrets management can be defined once applicable security requirements and the deployment topology are known. |
| A-1104 | A-105, A-106 | FS | Configuration-item and artifact version identifiers can be defined once the evaluation strategy and system architecture identify the models, corpus, prompts, configurations, and software artifacts that must be tracked reproducibly. |
| A-1105 | A-1102, A-1103, A-1104, A-813 | FS | MVP components can be containerized after the runtime, configuration, and versioning policies are defined and the integrated system baseline identifies the components that must be packaged. |
| A-1106 | A-1103, A-1105 | FS | Local orchestration, persistence, and runtime storage require the containerized components and the defined configuration strategy so that services, volumes, artifacts, and runtime data can be connected consistently. |
| A-1107 | A-1106 | FS | Health, readiness, and operational checks require the orchestrated runtime environment so that component availability and service dependencies can be observed during system startup and execution. |
| A-1108 | A-1102, A-1104, A-1105, A-1106 | FS | A reproducible build and environment initialization procedure requires controlled dependencies, artifact identifiers, container definitions, and the final local orchestration configuration. |
| A-1109 | A-1107, A-1108 | FS | A reproducible startup and execution procedure can be finalized once the system can be built deterministically enough for the project and its operational health and readiness behavior is available. |
| A-1110 | A-1109, A-1015 | FS | Final clean-environment deployment and reproducibility testing is executed after the V&V status baseline is established so that the configuration proven by V&V is the same configuration whose deployment reproducibility is confirmed. |
| A-1111 | A-1110 | FS | The final deployment and execution runbook is completed after the clean-environment test so that verified setup, startup, shutdown, recovery, and troubleshooting steps can be documented from observed behavior. |
| A-1112 | A-1111 | FS | The deployable and reproducible MVP baseline is established after the final deployment test and operational documentation have been completed. |

### 5.13 WP-12 — Final Documentation and Presentation Dependencies

| Activity ID | Predecessor(s) | Relationship | Dependency Rationale |
|---|---|---|---|
| A-1201 | A-916, A-1015, A-1112 | FS | Final project documentation can be consolidated once the experimental results, V&V status, and deployable/reproducible MVP baselines are available, ensuring that the documentation reflects the actual completed system and its evaluated state. |
| A-1202 | A-813, A-1112 | FS | The final as-built architecture, interfaces, deployment boundaries, and technical diagrams can be completed once the integrated system architecture and final deployable configuration are known. |
| A-1203 | A-916, A-1015 | FS | Final traceability, experimental evidence, and V&V results can be consolidated once the experimental results baseline and V&V status baseline have been completed. |
| A-1204 | A-916, A-1015 | FS | Final conclusions, limitations, and future work depend on the completed experimental findings and validation evidence so that claims remain bounded by the actual project results. |
| A-1205 | A-1201, A-1202, A-1203, A-1204 | FS | The final technical report requires the consolidated project documentation, as-built architecture, project evidence, conclusions, limitations, and future-work analysis. |
| A-1206 | A-1111, A-1202 | FS | The final repository README and usage guidance require the verified deployment/runbook information and the final architecture so that users can understand, build, configure, and execute the system correctly. |
| A-1207 | A-1015, A-1112 | FS | The final demonstration scenario requires a validated system state and a deployable/reproducible MVP baseline so that the demonstration can be executed repeatedly on the intended final configuration. |
| A-1208 | A-1202, A-1203, A-1204, A-1205 | FS | The final presentation is prepared from the final system architecture, experimental and V&V evidence, conclusions, and completed technical report. |
| A-1209 | A-1205, A-1206, A-1207, A-1208 | FS | The final technical review and demonstration rehearsal require the completed report, repository documentation, demonstration scenario, and presentation so that technical claims, evidence, instructions, and presentation readiness can be reviewed together. |
| A-1210 | A-1209 | FS | The final project baseline is frozen only after the technical review and demonstration rehearsal confirm that no critical documentation, implementation, evidence, or presentation issues remain. |
| A-1211 | A-1210 | FS | The final repository release and Git tag are created from the frozen project baseline so that the released version uniquely identifies the reviewed final configuration. |
| A-1212 | A-1211 | FS | Final project delivery and archival occur after the official repository release has been created, ensuring that the presented and preserved artifacts correspond to the identified final project version. |

## 6. Time Estimation
## 7. Schedule Calculation
## 8. Critical Path Analysis
## 9. Milestones
## 10. Project Calendar
## 11. Gantt Chart
## 12. Schedule Risks and Contingencies
## 13. Plan Maintenance