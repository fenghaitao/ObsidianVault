---
title: "AgentIsolation"
type: concept
tags: [agents, safety, worktrees, sandboxing, cursor]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor.md"]
last_updated: 2026-06-29
---

## Definition

Agent Isolation is the practice of ensuring an AI agent operates only within its designated scope — a specific directory, work tree, or environment — and does not modify files or execute commands outside that boundary. It can be achieved through mechanical enforcement (physically preventing access) or prompt-based trust (instructing the model to stay within bounds).

## Key Information

- In Cursor's original work tree implementation, isolation was mechanically enforced: the agent could not physically touch files outside its work tree
- In the new skill-based implementation, isolation relies on prompt instructions ("do not ever work outside this and do not ever escape") — described as "vibes-based"
- Weaker models like Haiku frequently deviate from isolation instructions and work in the primary checkout
- Stronger models like Composer and Grok maintain isolation more reliably
- Isolation degrades over long sessions as models forget their constraints
- Cursor uses two evals to measure isolation: "did the model do work in its work tree" and "did the model do work in the primary checkout"
- RL training for Composer aims to improve isolation compliance

## Related

- [[summary-20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor]] — source
- [[GitWorktrees]] — the isolation mechanism
- [[VibesBasedSafety]] — the trust-based approach
- [[Cursor]] — the product
- [[IsolatedEnvironments]] — related concept for cloud agents
