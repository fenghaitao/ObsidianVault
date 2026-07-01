---
title: "summary-20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora"
type: source
tags: [source, transcript, ai, agents, vertical-ai, agent-human-collaboration, legal-tech, ui-ux]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora.md"]
last_updated: 2026-06-26
---

## Core Summary
Jacob Lauritzen, CTO of Legora (a vertical AI company for law firms), argues that complex, long-running agents need more than a chat interface. Chat is one-dimensional and low-bandwidth — it tries to collapse a tree of work into a linear conversation. Instead, agents and humans should collaborate through high-bandwidth, persistent artifacts (documents, tabular reviews) that match the domain. He introduces the Verifier's Rule: if a task is solvable and easy to verify, AI will solve it. For tasks that are hard to verify (like writing contracts), he proposes strategies including proxy verification, task decomposition, guardrails, skills, and elicitation — with the human providing judgment at critical decision points.

## Key Points
- The new economics of production: doing work is now extremely cheap; planning and reviewing work are the new bottlenecks
- Verifier's Rule (coined by Jason Warner): if a task is solvable and easy to verify, AI will solve it — applies to both foundation models (RL) and agents (loop until correct)
- Different industries and tasks fall at different points on the solvability/verifiability spectrum: checking contract definitions (easy to verify), writing contracts (hard to verify — only a judge can truly verify), litigation strategy (impossible to verify — no objective truth)
- Two dimensions of agent-human collaboration: Trust (how much review is needed) and Control (how effectively a human can instill their knowledge into the agent's work)
- Increasing trust: bring tasks down the verifiability spectrum (e.g., TDD for coding), use proxy verification (compare against golden contracts), decompose tasks, add guardrails (limit what the agent can do)
- Increasing control: planning (steer upfront but inefficient — requires doing all the work to know what to do), skills (encode human judgment into work nodes with contingency handling), elicitation (ask the human at decision points, log decisions for later review)
- Skills are superior to planning because they handle contingencies: a skill for reviewing termination clauses can encode special EU law that the agent wouldn't know about during planning
- Elicitation should be non-blocking: agents should make decisions and log them, letting humans review and reverse later
- Chat is one-dimensional — it collapses a work tree/DAG into a linear conversation, making it impossible to review complex agent work effectively
- High-bandwidth artifacts: domain-specific persistent interfaces (documents with highlighting and commenting, tabular reviews) where humans can quickly see what the agent did and inject judgment
- Example from Legora: tabular review — agent spins up a known primitive, flags items needing human input, human reviews quickly, then kicks off the rest of the agent
- Agents are not humans and should not be constrained to human language interfaces — language is the universal interface for humans, but agents can interact through richer artifacts

## Related
- [[JacobLauritzen]] — speaker, CTO of Legora
- [[Legora]] — company, collaborative AI workspace for law firms
- [[JasonWarner]] — coined Verifier's Rule
- [[ClaudeCode]] — referenced for YOLO mode and planning inefficiency
- [[VerifiersRule]] — the core principle
- [[AgentHuman Collaboration]] — trust and control dimensions
- [[HighBandwidth Artifacts]] — the proposed interface paradigm
- [[Vertical AI]] — Legora's domain
- [[Decision Log]] — non-blocking elicitation pattern
- [[Context Rot]] — failure mode of long-running agents
- [[Elicitation]] — asking the human at decision points
- [[Guardrails]] — limiting agent scope to increase trust
- [[Task Decomposition]] — breaking tasks into verifiable sub-tasks
- [[ProgressiveDiscovery]] — skills handle contingencies through progressive discovery
- [[Skills]] — encoding human judgment into work nodes
