---
title: "Verifiers"
type: entity
tags: [library, reinforcement-learning, open-source, llm-training, environments]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Let LLMs Wander： Engineering RL Environments — Stefano Fiorucci.md"]
last_updated: 2026-06-30
---

## Definition
Verifiers is an open-source library by Prime Intellect that provides modular components for creating reinforcement learning environments for LLM agents, usable for both evaluation and training.

## Key Information
- Environments are Python packages that can be easily installed and distributed
- Supports single-turn, multi-turn, tool, and MCP environment types, all built on a multi-turn foundation
- Provides base classes for parsing model responses and defining reward functions
- Abstracts model serving via OpenAI-compatible API endpoints
- Handles single interactions and parallel trajectories, letting developers focus on environment logic
- Comes with its own trainer and integrates with Prime RL, Tinker, and Sky RL
- Tightly integrated with the Environments Hub for community sharing
- Aims to fight environment fragmentation — environments locked into specific training stacks

## Related
- [[PrimeIntellect]] — creator company
- [[PrimeRL]] — integrated training framework
- [[EnvironmentsHub]] — community sharing space
- [[MultiTurnEnvironments]] — core environment type
- [[SingleTurnEnvironments]] — simple environment type
- [[ToolEnvironments]] — tool-equipped environment type
- [[summary-20260408 - Let LLMs Wander： Engineering RL Environments — Stefano Fiorucci]] — source
