---
title: "summary-20260521 - Anthropic Just Dropped a Masterclass on Building Agent Harnesses (for Large Codebases)"
type: source
tags: [source, original-material, large-codebases, ai-layer, lsp, hooks, anthropic]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260521 - Anthropic Just Dropped a Masterclass on Building Agent Harnesses (for Large Codebases).md"]
last_updated: 2026-06-20
---

## Core Summary

[[ColeMedin]] walks through [[Anthropic]]'s blog post on **using Claude Code in large codebases** (multi-million-line monorepos, decades-old legacy, dozens of repos), backed by his own demo repo + a "AI layer" plugin. The unifying thesis: **"the harness matters as much as the model"** — the [[AILayer]] (a codebase's *third* component alongside code and tests) is what lets [[ClaudeCode]]'s [[AgenticSearch]] navigate scale. See [[LargeCodebaseStrategies]] for the consolidated playbook.

## Key Points

- **Agentic search, not indexing**: Claude Code navigates like an engineer (grep, folder structure, CLI tools) — no vector index to keep in sync — but works best with **enough starting context to know where to look**. Hence the strategies are about curating that context.
- **The AI layer = 7 components** (each maps to a strategy): global rules, skills, MCP servers, sub-agents, **hooks**, **LSP**, and code search. Visualized by how often each is used in a session — **global rules are the always-on foundation**; the rest fire sporadically.
- **Lean + layered global rules**: keep root `CLAUDE.md` short (giant rule files *hurt* performance — there's research); place **subdirectory `CLAUDE.md` files** that auto-load when you edit there (rules version of [[ProgressiveDisclosure]]). You can also `cd` into a subdir and start Claude there — it walks *up* the tree loading every `CLAUDE.md`, honing focus. Add a **codebase map** (directory structure + brief descriptions) for discovery when structure isn't enough; scope tests/lint per subdir; ignore build artifacts.
- **Hooks for self-improvement** (the standout): a **stop hook** runs a *headless* Claude session at end-of-turn to reflect on changes and **propose `CLAUDE.md` updates** (output to a markdown review you action later) — automated [[SystemEvolution]] that keeps rules from going stale. A **start hook** loads role/team-specific context dynamically (e.g. pull Confluence, git status/history). (Most people only use hooks defensively to *block* actions; the higher-value use is continuous improvement.)
- **Path-scoped skills**: a `SKILL.md` can be scoped to specific paths so it activates only in the relevant part of the codebase. Cole's distinction: **global rules = conventions; skills = workflows** (with overlap).
- **LSP via MCP**: expose Language Server Protocol (go-to-definition, find-references, symbol search) through an MCP server so Claude navigates by **symbol, not string** — essential past ~6-digit LOC where grep is slow and token-inefficient. Cole built a local codebase-search MCP (`where-is`, `find-references`) that complements grep.
- **Sub-agents split exploration from editing**: dispatch token-heavy research/exploration to a [[SubAgent]] (its own context), return only a summary — so the editing context isn't pre-bloated.
- **Cole's "AI layer" plugin**: installs the self-improving stop hook, an explorer sub-agent, the codebase-search MCP/LSP, and a scoped-skill example into any repo (`/plugin marketplace add <path>` → `/plugin install`).
- **Org adoption advice** (from Anthropic): **assign ownership** — a small team champions the initial AI-layer build-out in a "quiet investment period," then rolls out a *standard*, avoiding everyone evolving separate AI layers or being disappointed by an unconfigured tool.

## Related

- [[LargeCodebaseStrategies]] — the consolidated playbook
- [[AILayer]] — the 7-component layer (+ LSP, layered rules, self-improving hooks)
- [[ModularRulesArchitecture]] — layered/subdirectory CLAUDE.md
- [[AgenticSearch]] — what LSP complements for large codebases
- [[SystemEvolution]] — the self-improving stop hook
- [[ClaudeSkills]] — path-scoped skills
- [[Anthropic]] — author of the blog post
