---
title: "summary-20260325 - Armin Ronacher Leaning In To Find Out - PyAI Conf 2026"
type: source
tags: [source, pydantic, pyai-conf, coding-agents, reinforcement-learning]
sources: ["raw/03-transcripts/Pydantic/Channel Only/20260325 - Armin Ronacher Leaning In To Find Out - PyAI Conf 2026.md"]
last_updated: 2026-06-25
---

## Core Summary

Armin Ronacher (Flask creator, Sentry) explores why coding agents work so well and how to build systems that survive model changes. Key thesis: coding agents are overrepresented in RL training data because coding sessions produce measurable reward signals (tests pass, code committed). This means models are increasingly optimized for Unix workflows, file diffs, and REPL-style code execution. To build robust agents, lean into what models are already good at: files, execution, and common languages.

## Key Points

- RL training on coding sessions makes models progressively better at agentic coding — our usage shapes future models
- Coding sessions provide clear evaluation signals (tests pass, code committed) unlike open-ended text generation
- What's overrepresented in training: Unix workflows, files/diffs, build tools, incremental edits, REPL patterns
- What's underrepresented: UI clicking, proprietary systems, binary data, video, observability data
- External state changes that don't appear in session data confuse models (e.g., file modified outside the agent)
- Strategy: build "tiny programmable worlds" — give agents a virtual filesystem and code execution, use common languages (Python/JS, not Scheme/Lisp)
- SQL beats custom DSLs for observability queries because models have massive SQL training data
- Use your own session traces as training data for your agents — failures are easy to catch and learn from
- Monty (Pydantic's minimal Python interpreter) is an example of building a programmable world

## Related

- [[ArminRonacher]] — Flask creator, Sentry
- [[Monty]] — Pydantic's secure Python interpreter for AI agents
- [[CodingAgents]] — the agent category dominating RL training
- [[ReinforcementLearning]] — how models become agentic
- [[SamuelColvin]] — Monty creator
