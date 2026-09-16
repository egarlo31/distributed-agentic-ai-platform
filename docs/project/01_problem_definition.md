# Problem Definition

## Document Control

| Field | Value                                      |
|---|--------------------------------------------|
| Document Title | System Requirements Specification          |
| Document ID | DAICP-SRS-001                              |
| Project | Distributed Agentic AI Platform for 5G RCA |
| Document Type | System Requirements Specification          |
| Version | 0.1                                        |
| Status | Draft                                      |
| Author | Emilio García                              |
| Owner | Project Engineering                        |
| Created | 2026-08-28                                 |
| Last Updated | 2026-09-07                                 |
| Classification | Internal / Project                         |
| Applicable Standard | ISO/IEC/IEEE 29148:2018                    |

## Revision History

| Version | Date | Author | Description | Status |
|---|---|---|---|---|
| 0.1 | 2026-09-03 | Emilio García | Initial SRS structure | Draft |

## Review and Approval

| Role | Name | Status | Date       |
|---|---|---|------------|
| Author | Emilio García | Completed | 2026-09-28 |
| Technical Reviewer | TBD | Pending | TBD        |
| Approver | TBD | Pending | TBD        |

## Context

In telecommunications operations, especially during troubleshooting and Root 
Cause Analysis activities,
engineers need to consult large amounts of technical information distributed
across documentation,
specifications, procedures, logs, alarms, and other sources. Locating the 
information that is relevant to a specific incident can require considerable
time and often depends heavily on the engineer's
experience and knowledge of where to search.  

Therefore, there is a need to make relevant technical knowledge easier to 
access based on the context of
a network incident, so that engineers can quickly identify what information
they should consult and 
receive assistance throughout the analysis process.  

The project proposes exploring an intelligent system capable of 
interpreting the context of a network problem, 
retrieving related technical knowledge, and acting as a copilot 
to support the engineering team during incident diagnosis and analysis.

## Current situation

In telecommunications engineering environments, troubleshooting and
Root Cause Analysis often require engineers to manually search, read,
compare and validate information from multiple technical sources.  

This information may be distributed across technical documentation, network
procedures, alarms, logs, vendor documentation, internal knowledge bases, and
telecommunications standards. Because these sources are not always centralized or organized according
to the specific needs of each engineering team, engineers may spend significant time
identifying which information is relevant to a particular incident.  

As a result, troubleshooting can involve considerable manual effort in information retrieval, analysis, 
and validation before a root cause hypothesis can be established.

## Problem Statement

Telecommunications engineers spend significant manual effort retrieving 
technical knowledge, analyzing incident evidence, preparing documentation, 
and supporting operational decisions during troubleshooting. Current 
workflows require engineers to manually locate, correlate, interpret, 
and validate information distributed across multiple technical sources, 
making the process time-consuming and highly dependent on individual expertise.

## Impact

This problem is important because telecommunications companies and 
engineering teams require fast and reliable incident resolution. 
Delays in identifying the root cause of network issues can increase 
service restoration time, prolong outages or service degradation, 
affect operational performance and SLA compliance, and, in severe cases, 
contribute to customer dissatisfaction or service cancellations.

## Need

There is a need for a centralized and accessible mechanism that allows
telecommunications engineers to retrieve the technical information required
for troubleshooting without having to search across multiple independent
sources or depend excessively on other teams to obtain relevant information.

The required capability should allow engineers to consult technical knowledge
in a clear and context-aware manner, reducing unnecessary information
fragmentation and simplifying access to the evidence needed during incident
analysis.

## Proposed Solution

The proposed solution is to centralize and structure relevant 
telecommunications data into a technical knowledge base, then
use an existing Large Language Model (LLM) to reason over retrieved 
information, generate technical responses, and support troubleshooting 
activities.

A Retrieval-Augmented Generation (RAG) layer will be used to retrieve 
incident-relevant information from the knowledge base, while an agent 
layer will allow the system to recommend actions, query available resources,
and execute approved tools when required.

The engineer will remain in the loop to review, validate, and supervise 
the system’s outputs. The system is intended to function as an engineering 
copilot that reduces the time and effort required to investigate and 
resolve network incidents, rather than replacing human engineering judgment.  
Before implementing the complete system, a Minimum Viable Product (MVP) 
will be developed to validate whether the proposed approach can provide 
measurable value to engineering teams in realistic troubleshooting scenarios.

## Known Limitations and Operating Constraints

### Knowledge update
- The system cannot guarantee real-time knowledge updates unless it is connected 
to continuously updated data sources or operational systems.

### Human oversight and limited autonomy
- The system is not fully autonomous and requires strict human supervision. 
A field engineer must review, validate, and approve relevant analyses, 
recommendations, and operational actions.

### Limited diagnostic responsibility
- The system will not independently resolve all network incidents. Its role 
is to assist engineers by retrieving information, analyzing evidence,
generating documentation, and recommending possible actions.

### Computational infrastructure
- Agent behavior, tool execution, model selection, and resource consumption 
must be adapted to the computational infrastructure available to the 
engineering team.

### Data quality
- System performance will depend on the quality, completeness, and
freshness of the available knowledge base and operational data.

## Scope of the project

### In scope
The project will focus on reducing the time and manual effort required by 
telecommunications engineers to retrieve technical information, analyze 
incidents, and support operational decision-making during troubleshooting 
activities.

The system will assist telecommunications engineers responsible for 
troubleshooting and Root Cause Analysis by retrieving relevant technical 
knowledge, analyzing historical incident data, generating evidence-supported
diagnostic hypotheses and recommended investigation steps while minimizing 
the risk of disrupting the operational environment.

Historical telecommunications data, technical documentation, logs, 
procedures, and previously resolved cases will be used to build and
prepare the system's knowledge base and retrieval mechanisms.

### Out of scope

The initial system will not operate as a fully autonomous troubleshooting 
platform. It will not independently execute critical decisions or resolve 
production incidents without human supervision. 

A qualified engineer will 
remain responsible for reviewing, validating, and approving operational 
recommendations or actions produced by the system.

## Scalability and Future Capabilities

The system architecture will be designed to support future expansion
toward more autonomous agent capabilities. Such capabilities may
eventually allow agents to execute selected diagnostic or remediation 
actions, but human approval will remain a required control for critical 
operational decisions.
The project will also support the incorporation of newly validated 
incidents, technical documents, and resolved cases into the knowledge base.

Rather than requiring complete model retraining whenever new information 
becomes available, the system should allow its external knowledge sources 
and retrieval indexes to be updated incrementally.
The architecture will be optimized to operate within constrained local 
computing environments while maintaining acceptable inference latency and 
resource consumption. Model selection, quantization, retrieval strategies, 
and agent execution should therefore consider computational efficiency.
The system will be designed using portable deployment components so that
workloads can later be migrated from local engineering workstations to 
cloud infrastructure without redesigning the complete application 
architecture.

The architecture should also support deployment on more capable computing 
infrastructure when additional CPU, GPU, memory, storage, or concurrency 
becomes available.
Finally, the system will maintain structured records of application 
errors, agent execution failures, tool execution results, and relevant 
operational events to support debugging, monitoring, auditing, and future 
system improvement.

## Technical Constraints

The system must be designed to operate within the computational resources available to the engineering team.

Primary workstation:
- NVIDIA RTX 5070 GPU
- Intel Core i7 13th Gen processor
- 32 GB RAM
- 2 TB SSD, with approximately 1 TB available for the project

Remote workstation:
- MacBook Air with Apple M5
- 16 GB unified memory

The selection of LLMs, embedding models, vector databases, 
agent runtimes, sandbox environments, and inference configurations 
must therefore consider memory consumption, storage requirements, 
inference latency, and hardware compatibility.