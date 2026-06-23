---
title: "vault-architecture-mapped-to-cole-teachings"
type: synthesis
tags: [synthesis, analysis, self-referential, vault-design, karpathy]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260406 - I Built Self-Evolving Claude Code Memory w⧸ Karpathy's LLM Knowledge Bases.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260126 - I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260402 - Full Guide - Build Your Own AI Second Brain with Claude Code.md"
last_updated: 2026-06-20
---

# How This Vault Maps to What Cole Medin Teaches

A self-referential synthesis: this knowledge base is itself an instance of the patterns it documents. Here's the mapping between *this vault's actual implementation* and the [[KarpathyLLMWiki]] / [[SecondBrain]] patterns Cole teaches.

## The core claim

This vault is a [[KarpathyLLMWiki]] — Karpathy's "compile, don't retrieve" pattern — operated by [[ClaudeCode]] (via the Claudian plugin) inside [[Obsidian]], using [[ClaudeSkills]] for its operations. That's exactly the [[SecondBrain]] stack Cole describes, minus the proactive heartbeat.

## The compiler analogy, mapped to our files

Karpathy frames the LLM Wiki as a compiler pipeline ([[KarpathyLLMWiki]]). Here's how each stage maps to *this vault*:

| Compiler stage | Karpathy / Cole's term | This vault's implementation |
|---|---|---|
| Source code | `raw/` (immutable) | `raw/03-transcripts/` — the Cole Medin transcripts |
| Compiler | the ingest LLM | `.claude/skills/ingest/SKILL.md` |
| Executable | `wiki/` (what you query) | `wiki/{concepts,entities,sources,syntheses}/` |
| Index | `index.md` (the most important file) | `wiki/index.md` |
| Test suite | "linting" | `.claude/skills/lint/SKILL.md` |
| Runtime | querying | `.claude/skills/query/SKILL.md` (this very skill) |
| System description | `agents.md` | `CLAUDE.md` (the schema) |

This is a near-perfect match to the architecture in [[summary-20260406 - I Built Self-Evolving Claude Code Memory w⧸ Karpathy's LLM Knowledge Bases]]. The vault was deliberately built on this pattern.

## Where we follow Cole exactly

- **Markdown on the filesystem.** [[Obsidian]] is the canvas; everything is `.md`. Karpathy and Cole both use Obsidian for exactly this reason — markdown is the LLM's native format and Claude Code owns the filesystem directly (no MCP abstraction, unlike Notion). Sources: [[SecondBrain]], [[Obsidian]].
- **Index-first navigation, no vector DB.** Karpathy's insight — "the LLM is pretty good about auto-maintaining index files" — is exactly our `/query` skill's step 1: always read `wiki/index.md` first, then follow links. No [[RetrievalAugmentedGeneration]] infrastructure needed at this scale.
- **Bidirectional linking + no orphans.** Our `CLAUDE.md` schema mandates a `## Related` section on every page. The graph view (an [[Obsidian]] feature Karpathy specifically praises) lets the agent traverse relationships.
- **Append-only log.** `wiki/log.md` mirrors Cole's daily-log concept — a grep-friendly operation history.
- **Skills with [[ProgressiveDisclosure]].** Our ingest/query/lint skills are exactly the [[ClaudeSkills]] pattern: a `SKILL.md` per capability, loaded on demand.

## Where we deliberately diverge

| Cole's approach | This vault | Why |
|---|---|---|
| **Hook-automated** (session-start, pre-compact, session-end hooks auto-capture and promote) | **Human-triggered** (you run `/ingest`) | Control + cost visibility. Decided at vault setup — we explicitly chose manual ingest so token spend is visible and intentional. |
| **Internal data** (Cole's self-evolving variant captures *conversations* with the agent) | **External data** (we ingest *curated transcripts*) | We're doing the *original* Karpathy pattern (external research material), not Cole's internal-memory variant. |
| **Heartbeat / proactivity** (the agent acts on your behalf autonomously) | **None** — read/write wiki only | This vault is a knowledge base, not a personal assistant. No [[LethalTrifecta]] exposure because there's no private-data + exfiltration agency. |
| **Selective vs. exhaustive** | We curated 11 of 49 transcripts | Deliberate signal-over-noise choice; matches Karpathy's "high-quality sources" emphasis. |

## The two variants of the pattern, and which we are

[[summary-20260406 - I Built Self-Evolving Claude Code Memory w⧸ Karpathy's LLM Knowledge Bases]] distinguishes:
- **Karpathy's original** — external data (articles, papers) → compiled wiki. **← This is us.**
- **Cole's variant** — internal data (agent conversations) → self-evolving memory.

Both share the identical raw→compiler→wiki→lint→query architecture. We implement the external-data version, human-triggered.

## What this means practically

Because the vault *is* the pattern, the wiki can reason about its own design. This very synthesis was produced by the `/query` skill reading pages about the pattern the skill implements. The [[KarpathyLLMWiki]] and [[SecondBrain]] pages are simultaneously *documentation of Cole's teaching* and *documentation of this vault's architecture*.

## The compounding loop (our version)

Cole's compounding loop: ask → synthesize across pages → file the answer back → wiki grows → future answers improve. **This synthesis is that loop in action** — it's a query result being filed back into `wiki/syntheses/`, exactly as the pattern prescribes. Source: [[KarpathyLLMWiki]].

## Related

- [[KarpathyLLMWiki]] — the pattern this vault implements
- [[SecondBrain]] — the stack (Claude Code + Obsidian + Skills)
- [[Obsidian]] — the canvas / this app
- [[ClaudeCode]] — the agent (via Claudian)
- [[ClaudeSkills]] — how ingest/query/lint are implemented
- [[ProgressiveDisclosure]] — why the skills scale
- [[AndrejKarpathy]] — pattern originator
- [[ColeMedin]] — the teacher whose content fills this vault
- [[summary-20260406 - I Built Self-Evolving Claude Code Memory w⧸ Karpathy's LLM Knowledge Bases]] — the canonical architecture source
- [[summary-20260402 - Full Guide - Build Your Own AI Second Brain with Claude Code]] — the comprehensive second-brain build
