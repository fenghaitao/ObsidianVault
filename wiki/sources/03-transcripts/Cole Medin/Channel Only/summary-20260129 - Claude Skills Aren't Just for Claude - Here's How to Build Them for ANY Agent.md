---
title: "summary-20260129 - Claude Skills Aren't Just for Claude - Here's How to Build Them for ANY Agent"
type: source
tags: [source, original-material, claude-skills, progressive-disclosure, pydantic-ai, evals, observability]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260129 - Claude Skills Aren't Just for Claude - Here's How to Build Them for ANY Agent.md"]
last_updated: 2026-06-20
---

## Core Summary

[[ColeMedin]] argues that [[ClaudeSkills]] and [[ProgressiveDisclosure]] are a **universal pattern**, not Claude-only — [[Anthropic]] popularized it, but you can reimplement it in any agent framework. He demonstrates a [[PydanticAI]] "skills agent" template that loads skill descriptions into a **dynamic system prompt** (layer 1) and exposes `load_skill` / `read_reference` / `list_references` tools to pull `skill.md` (layer 2) and reference files (layer 3) on demand. As a bonus he covers two production-readiness practices he rarely gets to show: [[AgentEvaluation]] (PydanticAI's built-in eval framework) and [[AgentObservability]] (Logfire).

## Key Points

- **The problem skills solve**: giving an agent many capabilities without overwhelming its context window. MCP servers and long global rules dump *all* context upfront even if unused; skills let the agent **discover capabilities as it needs them**.
- **Three layers of progressive disclosure**: (1) the skill **description** in the system prompt (always loaded), (2) the full **`skill.md`** instructions (loaded when invoked), (3) optional **reference files / scripts** (loaded only when the skill needs to go deeper). Unlimited depth possible but rarely worth past layer 3.
- **Anthropic best-practice sizing**: description **50–100 words** (~5% of the skill's total context); `skill.md` typically **300–500 lines** (~30%); the rest lives in reference files. Simple skills may need only a `skill.md` (e.g. a timezone/"world clock" skill).
- **Universal implementation (PydanticAI demo)**:
  - A **dynamic system prompt** (`@agent.system_prompt` decorator) scans a `skills/` directory at runtime, extracts each `skill.md`'s YAML front-matter description + path, and injects them alongside the static base prompt.
  - A **toolset** with three tools: `load_skill` (returns a skill.md's contents), `read_reference` (returns a specific reference file), and `list_references` (helps the agent find references if skill.md doesn't link them). Whatever a tool returns enters short-term memory.
  - The base prompt must **explicitly teach the agent what skills are and how/when to invoke them** — LLMs don't innately know how to use this pattern; Claude was trained/prompted to, and custom agents need the same instruction.
  - Framework-agnostic (works with LangChain, CrewAI, no-framework, etc.) and model-agnostic (OpenRouter, Ollama/local, OpenAI). Drop new skill folders into `skills/` and they're available next run — same convention as [[ClaudeCode]].
- **Skill creator meta-skill**: in Claude Desktop → Settings → Capabilities → Skills → example skills, toggle on the **skill creator** — a skill that builds skills (pulls in best practices and walks you through producing a `skill.md` + reference files you can drop into any agent's skills directory).
- **Evals ([[AgentEvaluation]])**: PydanticAI ships a robust eval framework. Define YAML test cases (a "golden dataset") with custom evaluators that assert the **expected skill was loaded** for a given question. Run as a single cheap, fast smoke test (Cole uses **Haiku**; 25/25 cases passed). Run **every time** you change the system prompt or the skill set; failures point to loading bugs, weak descriptions, or a weak system prompt.
- **Observability ([[AgentObservability]])**: **Logfire** (by the Pydantic team) instruments PydanticAI with minimal code — captures every tool call, LLM interaction, token usage, and cost as traces, locally and in production. Lets you inspect *where* an agent went wrong (bad parameter, wrong tool) when a real user reports a problem.

## Related

- [[ClaudeSkills]] — the pattern being generalized
- [[ProgressiveDisclosure]] — the core loading strategy, implemented from scratch
- [[PydanticAI]] — the framework used for the universal skills-agent template
- [[AgentEvaluation]] — golden-dataset evals to verify skill usage
- [[AgentObservability]] — Logfire tracing for production
- [[Anthropic]] — popularized skills and the best-practice guide
- [[ModelContextProtocol]] — the always-loaded counterpoint to skills
