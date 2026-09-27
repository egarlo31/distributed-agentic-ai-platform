# Project Plan

## Document Control

| Field | Value |
|---|---|
| Document Title | Project Scope |
| Document ID | DAICP-PS-001 |
| Project | Distributed Agentic AI Platform for 5G RCA |
| Document Type | Project Scope |
| Version | 0.1 |
| Status | Draft |
| Author | Emilio García |
| Owner | Project Engineering |
| Created | 2026-09-26 |
| Last Updated | 2026-09-26 |
| Classification | Internal / Project |

## Revision History

| Version | Date | Author | Description | Status |
|---|---|---|---|---|
| 0.1 | 2026-09-TBD | Emilio García | Initial SRS structure | Draft |

## Review and Approval

| Role | Name | Status | Date       |
|---|---|---|------------|
| Author | Emilio García | Completed | 2026-09-28 |
| Technical Reviewer | TBD | Pending | TBD        |
| Approver | TBD | Pending | TBD        |

## 1. Purpose

The purpose of this document is to define the development and planning approach
for the Minimum Viable Product (MVP) of the Distributed Agentic AI Platform for
5G Root Cause Analysis.

The project plan establishes the methodology, deliverables, activities,
dependencies, time estimates, milestones, and scheduling required to implement
and evaluate the MVP within the available development time and computational
resources.

The plan is intended to keep development focused on producing a functional and
experimentally evaluable system while controlling unnecessary implementation
complexity.

## 2. Project Methodology

The project will follow an iterative and incremental development approach.

Because the system combines data preparation, information retrieval, Large
Language Models, agent tool use, software integration, and experimental
evaluation, the complete solution will not be implemented as a single
development stage.

Instead, the project will be divided into small functional increments. Each
increment will produce a component or result that can be implemented, tested,
and validated before being integrated into the complete system.

The development sequence will be:

1. prepare and inspect the telecommunications data and knowledge sources;
2. define and implement the baseline system;
3. implement and validate the knowledge retrieval component;
4. integrate Retrieval-Augmented Generation with the selected Large Language
   Model;
5. implement controlled agent tool use;
6. integrate the components into the MVP troubleshooting workflow;
7. execute the defined experimental evaluation;
8. analyze the results and complete the project documentation.

Each stage should produce a testable result before development proceeds to the
next level of system complexity.

Technical decisions such as model selection, retrieval configuration, data
processing strategies, and agent behavior may be adjusted during development
when experimental results or computational constraints indicate that a change
is necessary.

The methodology prioritizes a working and evaluable MVP over the implementation
of production-oriented capabilities that are outside the defined project scope.

## 3. Planning Assumptions

The project plan is based on the following assumptions:

- development will be performed primarily in a local environment;
- existing LLMs and available telecommunications datasets will be used;
- development time will be limited and focused on the defined MVP;
- selected incident scenarios will contain sufficient information for evaluation;
- each major component will be validated before full system integration;
- production deployment and enterprise capabilities are not required.

## 4. Deliverables

The project will produce the following main deliverables:

- prepared telecommunications knowledge and evaluation data;
- baseline implementation;
- RAG-based troubleshooting system;
- controlled agent tool capability;
- integrated MVP;
- experimental evaluation results;
- final technical documentation.

## 5. Work Breakdown Structure

The project is divided into the following work packages:

1. **Data Preparation**
   - select and inspect data sources;
   - prepare knowledge and evaluation data.

2. **Baseline Development**
   - implement the baseline approach;
   - verify baseline execution.

3. **RAG Development**
   - implement knowledge retrieval;
   - integrate retrieval with the selected LLM.

4. **Agent Development**
   - define approved tool capabilities;
   - implement controlled tool execution.

5. **System Integration**
   - integrate incident input, retrieval, LLM, agent, and structured output;
   - validate the complete MVP workflow.

6. **Evaluation**
   - execute baseline and proposed-system experiments;
   - collect and analyze results.

7. **Finalization**
   - document results, limitations, and final system configuration.

## 6. Activities and Dependencies

The project activities and their immediate dependencies are defined as follows:

| ID | Activity | Predecessor |
|---|---|---|
| A | Select and inspect data sources | - |
| B | Prepare knowledge and evaluation data | A |
| C | Implement baseline system | B |
| D | Implement knowledge retrieval | B |
| E | Integrate RAG with the selected LLM | C, D |
| F | Define controlled agent tool capability | B |
| G | Implement controlled agent tool execution | F |
| H | Integrate the complete MVP workflow | E, G |
| I | Validate the integrated MVP | H |
| J | Execute experimental evaluation | I |
| K | Analyze experimental results | J |
| L | Complete final documentation | K |

## 7. Time Estimation

Activity durations are estimated in hours using optimistic, most likely, and
pessimistic scenarios.

The project has approximately 10 hours available during weekends and an
expected 2 to 3 working hours from Monday to Friday each week.

The target date for MVP completion is November 22, 2026.

| ID | Activity | Optimistic | Most Likely | Pessimistic |
|---|---|---:|---:|---:|
| A | Select and inspect data sources | 2 h | 3 h | 4 h |
| B | Prepare knowledge and evaluation data | 7 h | 10 h | 14 h |
| C | Implement baseline system | 4 h | 5 h | 7 h |
| D | Implement knowledge retrieval | 6 h | 8 h | 12 h |
| E | Integrate RAG with the selected LLM | 5 h | 7 h | 10 h |
| F | Define controlled agent tool capability | 2 h | 3 h | 4 h |
| G | Implement controlled agent tool execution | 4 h | 6 h | 9 h |
| H | Integrate the complete MVP workflow | 6 h | 9 h | 13 h |
| I | Validate the integrated MVP | 4 h | 6 h | 9 h |
| J | Execute experimental evaluation | 6 h | 9 h | 12 h |
| K | Analyze experimental results | 3 h | 5 h | 7 h |
| L | Complete final documentation | 4 h | 6 h | 8 h |

### 7.1 Optimistic Time

The optimistic estimate represents execution under favorable conditions, with
the required data, models, tools, and development environment available and
without significant implementation problems.

### 7.2 Most Likely Time

The most likely estimate represents the expected development effort under
normal conditions, including regular debugging, configuration, testing, and
minor adjustments.

### 7.3 Pessimistic Time

The pessimistic estimate considers additional debugging, integration problems,
data preparation issues, model configuration changes, or other foreseeable
technical difficulties.

### 7.4 Contingency

A 15% contingency will be added to the estimated project duration to account
for unexpected technical problems and days during the week in which development
may not be possible.

The expected workload is approximately 78 hours before contingency and
approximately 90 hours including contingency.

This remains below the estimated 106–114 hours available before the target
completion date, leaving additional schedule margin before December.

## 8. PERT Schedule

The PERT schedule will use the optimistic, most likely, and pessimistic estimates
defined in the previous section together with the activity dependencies.

A 15% contingency will be considered when calculating the planned activity
durations.

### 8.1 PERT Schedule Table

| ID | Expected Time | Planned Time with Contingency | Start | Finish |
|---|---:|---:|---:|---:|
| A | 3.00 h | 3.45 h | 0.00 | 3.45 |
| B | 10.17 h | 11.69 h | 3.45 | 15.14 |
| C | 5.17 h | 5.94 h | 15.14 | 21.08 |
| D | 8.33 h | 9.58 h | 15.14 | 24.72 |
| E | 7.17 h | 8.24 h | 24.72 | 32.97 |
| F | 3.00 h | 3.45 h | 15.14 | 18.59 |
| G | 6.17 h | 7.09 h | 18.59 | 25.68 |
| H | 9.17 h | 10.54 h | 32.97 | 43.51 |
| I | 6.17 h | 7.09 h | 43.51 | 50.60 |
| J | 9.00 h | 10.35 h | 50.60 | 60.95 |
| K | 5.00 h | 5.75 h | 60.95 | 66.70 |
| L | 6.00 h | 6.90 h | 66.70 | 73.60 |

### 8.2 PERT Network Diagram

The activity network is based on the following dependency structure:

```text
A → B ─→ C ─┐
      ├→ D ─┴→ E ─┐
      └→ F → G ───┴→ H → I → J → K → L
```

**PERT Graph:**

> Insert the final PERT network diagram here.

The diagram should show each activity, its planned duration, and the dependency
relationships defined in Section 6.

## 9. Critical Path

Based on the current activity dependencies and planned durations, the critical
path is:

```text
A → B → D → E → H → I → J → K → L
```

The estimated duration of the critical path, including the 15% contingency, is
approximately:

**73.6 working hours**

Activities outside the critical path may have scheduling flexibility as long as
they are completed before their dependent activities begin.

## 10. Milestones

The following milestones will be used to track project progress:

| Milestone | Related Activity |
|---|---|
| Data and knowledge sources prepared | B |
| Baseline implemented | C |
| RAG pipeline integrated | E |
| Controlled agent capability implemented | G |
| Integrated MVP completed | H |
| MVP validated | I |
| Experimental evaluation completed | J |
| Results analyzed | K |
| Project completed | L |

Calendar dates for these milestones will be assigned when the final project
schedule and Gantt chart are created.

## 11. Project Schedule

The project schedule is based on approximately 12 effective development hours
per week and a target MVP completion date of November 22, 2026.

| Week | Dates | Planned Work |
|---|---|---|
| 1 | Sep 28 – Oct 4 | Data source selection and initial data preparation |
| 2 | Oct 5 – Oct 11 | Complete data preparation, baseline, begin retrieval |
| 3 | Oct 12 – Oct 18 | Complete retrieval and implement initial agent tool capability |
| 4 | Oct 19 – Oct 25 | Complete agent capability and integrate RAG with the LLM |
| 5 | Oct 26 – Nov 1 | Complete RAG and integrate the MVP workflow |
| 6 | Nov 2 – Nov 8 | Validate MVP and begin experimental evaluation |
| 7 | Nov 9 – Nov 15 | Complete evaluation, analyze results, begin final documentation |
| 8 | Nov 16 – Nov 22 | Complete documentation and final project review |

The remaining capacity during the final week will be reserved as schedule margin
for unresolved implementation or evaluation issues.

## 12. Gantt Chart

The Gantt chart will represent the planned execution of activities between
September 28 and November 22, 2026.

```text
Activity                         W1 W2 W3 W4 W5 W6 W7 W8
A  Select data sources           ██
B  Prepare data                  ██ ██
C  Baseline implementation         ██
D  Knowledge retrieval             ██ ██
E  RAG integration                        ██ ██
F  Define agent tool                   ██
G  Implement agent tool                ██ ██
H  MVP integration                            ██
I  MVP validation                                ██
J  Experimental evaluation                       ██ ██
K  Results analysis                                  ██
L  Final documentation                               ██ ██
```

> Insert the final Gantt chart here if a graphical version is generated.

## 13. Risks and Dependencies

### Risks

| Risk | Response |
|---|---|
| Insufficient or unsuitable telecommunications data | Reduce evaluation scope to supported incident scenarios |
| Local computational limitations | Use smaller or quantized models and adjust retrieval configuration |
| LLM or retrieval performance is insufficient | Evaluate alternative configurations within the defined MVP |
| Integration requires more time than expected | Prioritize the core MVP workflow and remove non-essential functionality |
| Lost development days during the week | Use the existing contingency and final schedule margin |

### Dependencies

The project depends on:

- availability and suitability of the selected telecommunications datasets;
- availability of technical documentation for the selected incident scenarios;
- access to compatible LLM and embedding models;
- availability of the local development hardware;
- completion of data preparation before experimental evaluation.