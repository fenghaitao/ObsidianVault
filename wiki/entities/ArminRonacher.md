---
title: "ArminRonacher"
type: entity
tags: [person, python, flask, sentry, open-source]
sources: [raw/03-transcripts/Pydantic/Channel Only/20260325 - Armin Ronacher Leaning In To Find Out - PyAI Conf 2026.md]
last_updated: 2026-06-25
---

## Definition

Armin Ronacher is the creator of Flask (Python web framework) and a developer at Sentry. Known for deep thinking about how AI coding agents work and how to build systems that survive model evolution.

## Key Information

### On Coding Agents and RL

- Key insight: coding agents are overrepresented in RL training data because coding sessions produce measurable reward signals (tests pass, code committed)
- Our collective usage of coding agents shapes future models through RL feedback loops
- What's overrepresented in training: Unix workflows, files/diffs, build tools, REPL patterns
- What's underrepresented: UI clicking, proprietary systems, binary data, video

### Building Robust Agents

- Strategy: build "tiny programmable worlds" — give agents virtual filesystems and code execution
- Use common languages (Python, JavaScript) — models have massive training data for them
- SQL beats custom DSLs for data queries because of training data volume
- External state changes that don't appear in session data confuse models
- Use your own session traces as training data for your agents
- Monty is an example of a well-designed programmable world

## Related

- [[Flask]] — web framework he created
- [[Sentry]] — company he works at
- [[Monty]] — referenced in his talk
- [[CodingAgents]] — the agent category he analyzes
- [[ReinforcementLearning]] — the mechanism driving model improvement
- [[summary-20260325 - Armin Ronacher Leaning In To Find Out - PyAI Conf 2026]] — source
