---
title: "summary-20260702 - Finally, an Open Standard for the Karpathy LLM Wiki is HERE"
type: source
tags: [source, karpathy-llm-wiki, okf, google, standard, second-brain]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260702 - Finally, an Open Standard for the Karpathy LLM Wiki is HERE.md"]
last_updated: 2026-07-06
---

## Core Summary

Cole Medin introduces [[Google]]'s **Open Knowledge Format (OKF)**, a lightweight standard built on top of [[AndrejKarpathy]]'s LLM-Wiki pattern. Where Karpathy's original gist described the *idea* of an LLM-maintained personal wiki, everyone who built one ended up structuring folders and metadata differently — which means knowledge bases can't be shared or consumed by someone else's agent. OKF standardizes two things: how information is organized (indexes at each level, "bundles" of related documents) and which YAML frontmatter fields exist (only `type` is required; `tags`, `related`, etc. are optional but recommended). Cole demonstrates converting/building a wiki to OKF from its `spec.md`, then shows a concrete example: an "AI coding" bundle of four of his own videos plus extracted concept pages that he's published on GitHub, so viewers can hand the repo link to their own coding agent and immediately query his knowledge base without re-ingesting the transcripts themselves.

## Key Points

- **The problem OKF solves**: Karpathy's pattern is simple enough that a coding agent can one-shot a wiki from the gist, but with no shared standard, every person's wiki has different folder layout and metadata fields (e.g. `tags` vs `categories`), so knowledge bases can't be shared between people/teams/agents.
- **OKF standardizes two things**: (1) organization — indexes at each layer (top-level index → section indexes → documents), giving two layers of navigation; (2) metadata fields — `type` is the single required field (enables filtering, e.g. only "concept" or only "video"); everything else (title, tags, related) is optional but recommended.
- Cole compares it to [[ModelContextProtocol|MCP]]: "what MCP did for agent-to-tool communication, OKF is doing for agent-to-knowledge-base communication."
- **Bundles**: an OKF "bundle" is a packaged, shareable knowledge base (e.g. Cole's own bundle of his best/most current AI-coding videos + extracted concept pages) that another person's agent can consume directly by being pointed at the spec + the bundle's repo/README.
- The critique Cole flags and partly agrees with: OKF is "minimally opinionated" — it doesn't add much substance beyond Karpathy's original pattern. He argues that's the point: a thin standard that's easy to adopt and interoperate on is more valuable than a heavyweight one.
- Cole doesn't expect OKF itself to become *the* permanent standard, but expects something like it to win eventually, and recommends adopting the discipline now regardless.
- Sponsor mention: [[PostHog]], a product analytics platform Cole uses for [[Archon]].

## Related

- [[KarpathyLLMWiki]] — the pattern OKF standardizes on top of
- [[OpenKnowledgeFormat]] — the new entity/standard this video introduces
- [[ModelContextProtocol]] — the analogy Cole draws (MCP for tools, OKF for knowledge bases)
- [[SecondBrain]] — the personal-knowledge-base use case OKF targets
- [[ProgressiveDisclosure]] — the index → drill-down navigation OKF formalizes
- [[PostHog]] — sponsor tool
- [[Google]] — publisher of OKF
- [[AndrejKarpathy]] — original pattern author
- [[ColeMedin]] — narrator/analyst; publishes his own OKF bundle
