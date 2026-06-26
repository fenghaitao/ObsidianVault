---
title: "Decision Log"
type: concept
tags: [agents, elicitation, human-in-the-loop, collaboration, non-blocking]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora.md"]
last_updated: 2026-06-26
---

## Definition
A decision log is a non-blocking elicitation pattern where an agent, when unsure about something, makes a decision to unblock itself but records that decision in a log. The human can then review the decision log afterward and reverse decisions if needed, avoiding the bottleneck of the agent waiting for human input.

## Key Information
- Part of the elicitation strategy for agent-human collaboration: instead of blocking and waiting for the human, the agent makes a decision and logs it
- Solves the problem of agents being blocked on human input during long-running complex tasks
- The human reviews the decision log after the agent completes its work (or at checkpoints) rather than being interrupted mid-execution
- Decisions can be reversed if the human disagrees — the agent's work is not lost, just corrected
- Contrasts with blocking elicitation where the agent stops and waits for human input before continuing
- Particularly important when the work tree is large (10x, 100x bigger than simple tasks) — you don't want 50 questions in a chat
- Works well with high-bandwidth artifacts: the decision log can be presented in a structured, reviewable format rather than buried in a chat thread

## Related
- [[summary-20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora]] — source
- [[Elicitation]] — the broader pattern of asking the human
- [[Agent-Human Collaboration]] — the framework this pattern supports
- [[High-Bandwidth Artifacts]] — how decision logs should be presented
- [[JacobLauritzen]] — presented this pattern
- [[HumanInTheLoopWorkflows]] — related human-in-the-loop pattern
