---
title: "Dark Factory"
type: concept
tags: [ai, agents, engineering, workflow, open-claw]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Dark Factory： OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw.md"]
last_updated: 2026-06-30
---

## Definition
The Dark Factory is Vincent Koc's metaphor for AI-assisted software engineering at scale. It describes a mode of development where an engineer runs multiple parallel agent sessions (swim lanes) simultaneously, acting as a factory manager overseeing production lines rather than a craftsman writing code by hand. The term draws a parallel to the Industrial Revolution's shift from handlooms in cottages to centralized mills — software engineering is undergoing the same transformation, with the bottleneck shifting from code production to human taste and judgment.

## Key Information

- **Origin**: Coined by Vincent Koc in his 2026 talk describing OpenClaw's development velocity
- **Core metaphor**: Engineers become factory managers; agents are the factory workers; the bottleneck is taste, not code production speed
- **Historical parallel**: Industrial Revolution — handlooms in cottages (individual craftsmen) → centralized mills (factory workers); the bottleneck was the weaver's hands → now the bottleneck is taste
- **Implementation**: Running 5-20+ parallel agent swim lanes, each with a different purpose (CI, features, bugs, refactoring, monitoring)
- **Scale**: At peak, Vincent ran ~15 foreground sessions with sub-agents totaling up to 60-70 agents simultaneously
- **Key shift**: "Tokens are no longer the problem... raw compute and my brain space" — the limiting factor becomes human attention and judgment
- **Contrast**: 2025 was "token maxing" (brute force Ralph loops); 2026 is about token efficiency and agent-in-the-loop — the dark factory is the engineering approach that makes this scale manageable
- **Soft skills**: Managing a dark factory requires people-management skills — knowing when agents are bullshitting, how to delegate, when to nuke a session

## Related
- [[summary-20260605 - Dark Factory： OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw]] — primary source
- [[VincentKoc]] — originator of the concept
- [[OpenClaw]] — the project that exemplifies the dark factory approach
- [[Swim Lanes]] — the parallel workstream pattern that enables the dark factory
- [[Bot Looping]] — the more opinionated agent loop approach
- [[Token Maxing]] — 2025's brute force approach that preceded the dark factory
- [[Token Efficiency]] — 2026's shift that the dark factory enables
- [[Agent Parallelism]] — running multiple agents simultaneously
- [[AgentHarness]] — infrastructure for running agent sessions
- [[SayingNo]] — key taste skill in the dark factory era
- [[Vibe Maintainer]] — role engineers evolve into
- [[Ralph Loop]] — the "burn tokens and hope" approach the dark factory improves upon
