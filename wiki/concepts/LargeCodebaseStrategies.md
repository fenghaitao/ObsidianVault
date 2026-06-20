---
title: "LargeCodebaseStrategies"
type: concept
tags: [concept, large-codebases, ai-layer, claude-code, lsp, hooks, anthropic]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260521 - Anthropic Just Dropped a Masterclass on Building Agent Harnesses (for Large Codebases).md"
last_updated: 2026-06-20
---

## Definition

A playbook (from [[Anthropic]]'s "Claude Code in large codebases" article, demoed by [[ColeMedin]]) for making AI coding work at scale — multi-million-line monorepos, legacy systems, many repos. The core claim: **"the harness matters as much as the model."** Since [[ClaudeCode]] uses [[AgenticSearch]] (no index), the leverage is in curating the [[AILayer]] so the agent knows *where to look*.

## Key Information

### Lean + layered global rules

- Keep root `CLAUDE.md` **short** (oversized rule files *hurt* performance). See [[ModularRulesArchitecture]].
- Add **subdirectory `CLAUDE.md`** files that auto-load when editing in that slice (rules-level [[ProgressiveDisclosure]]). Starting Claude inside a subdir walks *up* the tree, loading every `CLAUDE.md` — focusing the agent without losing root context.
- Provide a **codebase map** (directories + one-line descriptions) for discovery; scope tests/lint per subdir; ignore build artifacts.

### Self-improving hooks

- **Stop hook** → runs a headless Claude session at end-of-turn to reflect on the changes and **propose `CLAUDE.md` updates** (written to a review file). Keeps rules from going stale — automated [[SystemEvolution]].
- **Start hook** → loads role/team-specific context dynamically (git status/history, Confluence docs for the relevant team).
- (Most teams only use hooks defensively to block actions; continuous improvement is the higher-value use.)

### Path-scoped skills

A `SKILL.md` can be scoped to specific paths so it activates only in relevant directories. Heuristic: **global rules = conventions; skills = workflows** (with overlap — both should be scoped to where they matter).

### LSP via MCP (symbol search, not string)

Expose the **Language Server Protocol** (go-to-definition, find-references, symbol search) through an MCP server so the agent navigates by *symbol*, not by grep string — essential past ~6-digit LOC where grep is slow and token-inefficient. Complements, not replaces, [[AgenticSearch]].

### Sub-agents split exploration from editing

Dispatch token-heavy exploration/research to a [[SubAgent]] (own context window), return only a summary — so the editing context starts lean.

### Organizational ownership

Anthropic's adoption advice: assign a small team to **champion the initial AI-layer build-out** in a "quiet investment period," then roll out a **standard** — avoiding fragmented per-dev AI layers and first-use disappointment from an unconfigured tool.

## Related

- [[AILayer]] — the 7-component layer this playbook configures
- [[ModularRulesArchitecture]] — the layered-`CLAUDE.md` foundation
- [[AgenticSearch]] — how Claude Code navigates; LSP complements it
- [[ClaudeSkills]] — path-scoped skills
- [[SubAgent]] — exploration/editing split
- [[SystemEvolution]] — what the self-improving stop hook automates
- [[ContextRot]] — why all of this (lean, scoped context) matters
- [[Anthropic]], [[ColeMedin]] — source + demonstrator
- [[summary-large-codebases-claude-code]] — primary source
