---
title: "summary-20250724 - Build ANY AI Agent with this Context Engineering Blueprint"
type: source
tags: [source, transcript, context-engineering, prp, pydantic-ai, ai-agents]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20250724 - Build ANY AI Agent with this Context Engineering Blueprint.md"]
last_updated: 2026-06-19
---

## Core Summary

[[ColeMedin]] releases a **PydanticAI-specific [[PRPFramework]] template** — the third in the use-case-template series after the generic intro and the MCP server template. Walks through using it to build a Research + Email-Draft agent (primary [[PydanticAI]] agent + sub-agent for Gmail OAuth-driven drafting) end-to-end in [[ClaudeCode]]. Cements the pattern: *the PRP framework specialized per domain delivers near-one-shot agent generation.*

## Key Points

- **The PydanticAI-specific template** — contains:
  - A base PRP hyper-tuned with PydanticAI best practices, common gotchas, and references to Cole's existing Pydantic AI examples.
  - Slash commands `/generate-pydantic-ai-prp` and `/execute-pydantic-ai-prp` adapted for the agent-building flow.
  - An `examples/` folder pre-populated with Cole's previously-built Pydantic AI agents.
  - A `CLAUDE.md` with PydanticAI-specific global rules (file structure, env-var handling, provider abstraction).
- **The three-part PydanticAI pattern** baked into the template — the same pattern Cole has reinforced across the Archon series: dependencies → agent definition → tools. The `initial.md` template literally has sections for each of these.
- **`copy-template.py` script** — Cole's pattern for instantiating a working directory from the template, so you can reuse the template across many agents without polluting the canonical version.
- **Demo agent built**: research agent (Brave web search) + email sub-agent (Gmail OAuth + draft creation). Roughly one-shotted; two minor iterations needed to fix conversation history in CLI and a flaky test.
- **Cross-IDE portability**: the slash commands are markdown files. If your IDE doesn't natively support `/foo` syntax, just paste the file contents into your prompt and tell it to use this as the prompt. Cole demonstrates this with [[ClaudeCode]] and Kiro AI.
- **The use-case-template vision** — Cole's larger plan, now a Dynamis community project: a repository of PRP templates per (language × project type), so anyone can drop into a near-zero-friction starting point for their specific build.
- **Validation gates and confidence-score iteration** — same pattern as the MCP video (`summary-context-engineering-101`). Read the generated PRP, ask "how do we get to 10/10 confidence?", refine, then execute.

## Related

- [[ContextEngineering]] — applied
- [[PRPFramework]] — specialized for PydanticAI
- [[PydanticAI]] — target framework for generated agents
- [[ClaudeCode]] — primary AI IDE
- [[ColeMedin]] — author
- [[Rasmus]] — original PRP framework creator
- [[ValidationGates]] — sub-pattern
- [[summary-20250703 - Context Engineering is the New Vibe Coding (Learn this Now)]] — intro to the trilogy
- [[summary-20250717 - Context Engineering 101 - The Simple Strategy to 100x AI Coding]] — MCP-template precedent for this PydanticAI template
