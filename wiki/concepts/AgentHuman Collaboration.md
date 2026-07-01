---
title: "Agent-Human Collaboration"
type: concept
tags: [agents, human-in-the-loop, trust, control, collaboration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - AgentCraft： Putting the Orc in Orchestration — Ido Salomon.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - Beyond Components： Designing Generative UI for MCP Apps — Ruben Casas, Postman.md"]
last_updated: 2026-06-29
---

## Definition
Agent-human collaboration is the paradigm of humans and AI agents working together on complex tasks, characterized by two key dimensions: Trust (how much review the human needs to do) and Control (how effectively the human can instill their knowledge and steer the agent's work).

## Key Information
- Two dimensions of collaboration:
  - **Trust**: ranges from low trust (review every agent trace) to high trust (no review at all). Determined by where the task falls on the verifiability spectrum.
  - **Control**: ranges from low control (only impose judgment at the root level of the work tree) to high control (steer at every node). Determined by the collaboration interface.
- Increasing trust strategies: bring tasks down the verifiability spectrum (TDD, proxy verification), decompose tasks, add guardrails (limit what the agent can do)
- Increasing control strategies: planning (steer upfront — inefficient), skills (encode human judgment into work nodes — handles contingencies), elicitation (ask the human at decision points — with non-blocking decision log)
- Skills are superior to planning because they handle contingencies: a skill for reviewing termination clauses can encode special EU law that wouldn't be known during planning
- Elicitation should be non-blocking: agents make decisions when unsure, log them to a decision log, and humans review/reverse later
- Chat is a poor collaboration interface for complex work: it's one-dimensional, low-bandwidth, and collapses a work tree/DAG into a linear conversation
- **Excalidraw MCP App**: Ruben Casas presents this as the "beyond components" future — a shared canvas where humans and agents collaborate bidirectionally. Users click around and modify UI traditionally while the agent also contributes, creating a true collaborative workspace rather than just output/visualization
- This shared artifact model represents the next evolution beyond static, declarative, or generative UI components
- Better interface: high-bandwidth, persistent, domain-specific artifacts (documents, tabular reviews) where humans can quickly see what the agent did and inject judgment
- The right interface varies by industry and task type
- AgentCraft's workspaces extend collaboration to multi-human scenarios: multiple humans (e.g., product designer and engineer) share a workspace where they can see each other's agents, hand off work, and collaborate in real-time with both humans and agents
- AgentCraft's soft collaboration mechanism: agents announce what they're working on in a shared chat, know what files each participant is changing, and coordinate implicitly
- **Demand-Driven Context**: A specific collaboration pattern where the human acts as domain expert, filling knowledge gaps surfaced by agent failures. The agent produces a checklist of missing information, the human provides answers, and the agent curates the knowledge. This is a structured elicitation pattern optimized for knowledge transfer rather than task steering.

## Related
- [[summary-20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora]] — source
- [[summary-20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure]] — source
- [[VerifiersRule]] — drives the trust dimension
- [[HighBandwidth Artifacts]] — the proposed interface paradigm
- [[Decision Log]] — non-blocking elicitation pattern
- [[Skills]] — encoding human judgment into work nodes
- [[Elicitation]] — asking the human at decision points
- [[Guardrails]] — limiting agent scope to increase trust
- [[Task Decomposition]] — breaking tasks into verifiable sub-tasks
- [[HumanInTheLoopWorkflows]] — related pattern
- [[JacobLauritzen]] — presented this framework
- [[Agent Workspaces]] — AgentCraft's multi-human collaboration feature
- [[AgentCraft]] — orchestrator with workspace-based collaboration
- [[summary-20260425 - AgentCraft： Putting the Orc in Orchestration — Ido Salomon]] — source
- [[DemandDriven Context]] — specific collaboration pattern for knowledge transfer
- [[Agent Failure as Discovery]] — the failure step in the collaboration
- [[Knowledge Curation]] — the curation step in the collaboration
