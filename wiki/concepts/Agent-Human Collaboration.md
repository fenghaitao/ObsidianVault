---
title: "Agent-Human Collaboration"
type: concept
tags: [agents, human-in-the-loop, trust, control, collaboration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora.md"]
last_updated: 2026-06-26
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
- Better interface: high-bandwidth, persistent, domain-specific artifacts (documents, tabular reviews) where humans can quickly see what the agent did and inject judgment
- The right interface varies by industry and task type

## Related
- [[summary-20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora]] — source
- [[VerifiersRule]] — drives the trust dimension
- [[High-Bandwidth Artifacts]] — the proposed interface paradigm
- [[Decision Log]] — non-blocking elicitation pattern
- [[Skills]] — encoding human judgment into work nodes
- [[Elicitation]] — asking the human at decision points
- [[Guardrails]] — limiting agent scope to increase trust
- [[Task Decomposition]] — breaking tasks into verifiable sub-tasks
- [[HumanInTheLoopWorkflows]] — related pattern
- [[JacobLauritzen]] — presented this framework
