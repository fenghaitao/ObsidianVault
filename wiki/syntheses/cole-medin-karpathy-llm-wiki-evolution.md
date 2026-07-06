---
title: "cole-medin-karpathy-llm-wiki-evolution"
type: synthesis
tags: [synthesis, karpathy-llm-wiki, second-brain, okf, cole-medin]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260126 - I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260406 - I Built Self-Evolving Claude Code Memory w⧸ Karpathy's LLM Knowledge Bases.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260702 - Finally, an Open Standard for the Karpathy LLM Wiki is HERE.md"
last_updated: 2026-07-06
---

# How Cole Medin's Coverage of the Karpathy LLM Wiki Pattern Evolved

[[ColeMedin]] has returned to [[AndrejKarpathy]]'s LLM-Wiki idea three times across six months, and each pass adds a different layer: first he *builds* the pattern without naming it, then he *names and extends* it, then he covers someone else *standardizing* it.

## Stage 1 (Jan 2026) — Building it before naming it: the Second Brain

In `summary-20260126 - I Built My Second Brain with Claude Code + Obsidian + Skills`, Cole introduces his [[SecondBrain]]: [[ClaudeCode]] as the agent, [[Obsidian]] as the markdown canvas, [[ClaudeSkills]] as the capability layer. Per [[SecondBrain]]'s own page, this is "the direct philosophical ancestor" of the Karpathy pattern — Cole is already running a compile-into-markdown, cross-linked personal knowledge system, but at this point he frames it around the Claude-Code-+-Obsidian-+-Skills stack rather than around Karpathy's article specifically. The underlying mechanics (accumulate → structure → cross-link → query) are the same ones [[KarpathyLLMWiki]] would later name explicitly.

## Stage 2 (Apr 2026) — Naming it and extending it: self-evolving memory

`summary-20260406 - I Built Self-Evolving Claude Code Memory w⧸ Karpathy's LLM Knowledge Bases` is, per [[KarpathyLLMWiki]]'s own frontmatter, **"THE source for this vault's architecture."** Here Cole:

- Explicitly credits [[AndrejKarpathy]] and lays out the **compiler analogy** — raw material is source code, an LLM ingest pass is the compiler, the resulting wiki is the executable, `/lint` is the test suite, `/query` is runtime. (This is the exact analogy [[CLAUDE.md]] and this vault's `/ingest`, `/lint`, `/query` skills are built from.)
- Cites Karpathy's own insight that auto-maintained `index.md` files beat reaching for vector-based RAG at moderate scale — no embeddings, no vector DB, just an agent navigating markdown.
- Adds his own contribution: apply the *identical architecture* to **internal** data (his own conversations with his coding agent) rather than **external** data (articles, papers). Session logs become the `raw/` equivalent; session-start/pre-compact/session-end hooks capture and summarize them; a daily flush process compiles them into the wiki. This is the same wiki-compiling loop Karpathy described for external material, redirected inward at the agent's own working memory.

So Stage 2 is where the pattern gets both its name in Cole's content *and* its first genuine extension (external-knowledge tool → internal-memory tool).

## Stage 3 (Jul 2026) — Someone else standardizes it: Google's OKF

By `summary-20260702 - Finally, an Open Standard for the Karpathy LLM Wiki is HERE`, the pattern has spread widely enough that Cole identifies a new problem: **everyone's wiki is structured differently.** Karpathy's gist describes the *idea*, not a schema, so no two LLM wikis share metadata fields or folder conventions — which means they can't be shared between people, teams, or each other's agents.

[[Google]]'s **[[OpenKnowledgeFormat]] (OKF)** answers this directly: a thin standard (nested indexes + "bundles" for organization; `type` as the only required metadata field) layered *on top of* Karpathy's pattern, not a replacement for it. Cole draws the explicit analogy: **"what MCP did for agent-to-tool communication, OKF is doing for agent-to-knowledge-base communication"** (see [[ModelContextProtocol]]). He demonstrates the payoff directly — publishing an OKF "bundle" of his own AI-coding videos that anyone can hand to their own coding agent and query immediately, without re-ingesting his transcripts themselves.

## The throughline

| Stage | Date | What changed | Source |
|---|---|---|---|
| 1. Build | Jan 2026 | Practice the pattern (Second Brain) before naming it | [[summary-20260126 - I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How)]] |
| 2. Name + extend | Apr 2026 | Credit Karpathy explicitly; extend external-knowledge compiling to internal agent memory | [[summary-20260406 - I Built Self-Evolving Claude Code Memory w⧸ Karpathy's LLM Knowledge Bases]] |
| 3. Standardize | Jul 2026 | Google's OKF solves the interoperability gap the pattern never addressed | [[summary-20260702 - Finally, an Open Standard for the Karpathy LLM Wiki is HERE]] |

Each stage keeps the compiler-not-retriever core idea intact ([[KarpathyLLMWiki]] vs. [[RetrievalAugmentedGeneration]]) while solving a problem the prior stage exposed: Stage 1 exposes the need for a named architecture; Stage 2's internal-memory variant and this vault's own build expose the need for shared conventions; Stage 3 (OKF) is Google's answer to exactly that gap.

This vault is itself a live data point in the lineage — see [[vault-architecture-mapped-to-cole-teachings]] for how its own `CLAUDE.md`/`raw`/`wiki` schema instantiates Stage 2's architecture directly, ahead of any OKF adoption.

## Related

- [[KarpathyLLMWiki]] — the pattern this synthesis traces across Cole's coverage
- [[SecondBrain]] — Stage 1, the pre-naming implementation
- [[OpenKnowledgeFormat]] — Stage 3, Google's standardization
- [[AndrejKarpathy]] — original pattern author
- [[ColeMedin]] — the consistent narrator across all three stages
- [[ModelContextProtocol]] — the analogy Cole draws for OKF
- [[vault-architecture-mapped-to-cole-teachings]] — this vault as a Stage-2 instance of the pattern
