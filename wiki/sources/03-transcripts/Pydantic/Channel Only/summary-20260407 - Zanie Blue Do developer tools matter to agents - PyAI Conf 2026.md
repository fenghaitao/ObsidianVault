---
title: "summary-20260407 - Zanie Blue Do developer tools matter to agents - PyAI Conf 2026"
type: source
tags: [source, pydantic, pyai-conf, developer-tools, agents, astral]
sources: ["raw/03-transcripts/Pydantic/Channel Only/20260407 - Zanie Blue Do developer tools matter to agents - PyAI Conf 2026.md"]
last_updated: 2026-06-25
---

## Core Summary

Zanie Blue (Astral, makers of Ruff/UV/TY) examines how agents interact with developer tools and how tool design must evolve for agentic consumers. Key themes: tools provide deterministic feedback that agents need for correctness; output formats must be optimized for agents (machine-readable, context-efficient); scaling to hundreds of agents creates new requirements; and agents may eventually build their own purpose-built tools.

## Key Points

- Agents need deterministic tool feedback for correctness — testing, static analysis, type checking, linting
- Tool output optimization: JSON output can be more verbose than human output; need context-efficient formats
- Pattern: persist verbose output to files, give agents pointers instead of full output in context
- Language servers (LSPs) were designed for humans — agent-specific protocols may be needed
- Plugins become more important: agents can define custom lint rules as a form of memory
- Confidence levels: agents don't get fatigued by false positives, so tools can emit lower-confidence diagnostics
- Trust model: should agents be allowed to use escape hatches like `# noqa` suppressions? Probably not
- Sandboxing UV: reduced permissions for agentic use (no filesystem access outside working directory)
- Existential question: will agents eventually just modify tools like UV themselves?

## Related

- [[UV]] — Astral's Python package manager
- [[Ruff]] — Astral's Python linter/formatter
- [[TY]] — Astral's type checker
- [[DeveloperTools]] — the category being reshaped by agents
- [[AgenticProgramming]] — the paradigm driving tool evolution
