---
title: "Anthropic"
type: entity
tags: [company, ai-lab, claude, mcp]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/02 - 10x Your AI Agents with this ONE Agent Architecture.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/03 - Coding Subagents - The Next Evolution of AI IDEs.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250414 - The ULTIMATE Guide to Building Your Own MCP Servers (Free Template).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250508 - The EASIEST Possible Strategy for Accurate RAG (Step by Step Guide).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260101 - AI Exploded in 2025 - Here’s Everything That Happened.md"
last_updated: 2026-06-20
---

## Definition

Anthropic is the AI safety company behind the Claude model family and the [[ModelContextProtocol]] standard. Their published guidance on agent architectures is widely cited in the agent-builder community.

## Key Information

### Products mentioned in the playlist

- **Claude** — model family (specifically Claude 3.5 Sonnet and Claude 3.7 Sonnet referenced as the LLMs powering Windsurf agentic coding).
- **Claude Desktop** — the official Claude desktop client; one of the first MCP-aware applications.
- **MCP / Model Context Protocol** — see [[ModelContextProtocol]]. Authored by Anthropic, now widely adopted across the ecosystem.

### 2025 industry milestones (year-in-review)

Per Cole's 2025 recap (`summary-ai-exploded-in-2025`), Anthropic was arguably the defining company of the year:
- Shipped the **Claude 4** family (the point Cole calls Claude "the coding king") and later **Claude Opus 4.5** ("the AI coding king," beating Sonnet 4.5).
- Raised **$13B at a $183B valuation**; paid a **$1.5B** settlement to authors over training-data copyright (~$3K each across ~500K books).
- **[[ClaudeCode]] reached $1B in revenue**; acquired the **Bun** JavaScript runtime to scale it; released **Claude Code for the web** (remote agentic coding, competing with OpenAI's Codex).
- Partnered with IBM (enterprise AI) and entered circular Microsoft/Nvidia investment-and-infrastructure deals.
- **Donated [[ModelContextProtocol]]** to the new **Agentic AI Foundation** (a Linux Foundation directed fund co-founded with Block and OpenAI), and drove adoption of [[ClaudeSkills]] as a context-efficient capability layer.

### Reference: "Building Effective Agents" article

Cole repeatedly cites this Anthropic publication as the canonical taxonomy of agent architectures:
- **Prompt chaining** — sequential single-agent calls.
- **Routing** — a router agent dispatches to specialized handlers.
- **Parallelization** — what Cole calls the [[ParallelAgentArchitecture]]. Multiple specialists run simultaneously, then aggregate. The pattern explored in depth in video 2.
- **Orchestrator-workers** — one orchestrator delegates to dynamically-composed workers.
- **Evaluator-optimizer** — a generator-critic loop.

The article explicitly endorses [[LangGraph]] as a useful framework while warning that frameworks are "a level of abstraction that can sometimes be dangerous" — a warning Cole quotes back in the [[LangChain]] context.

### Reference: "Contextual Retrieval" article

A separate Anthropic publication (distinct from "Building Effective Agents") that introduces [[ContextualRetrieval]] — the per-chunk LLM-generated context augmentation pattern that significantly improves RAG accuracy. Cole's video on contextual retrieval (in `summary-easiest-strategy-for-accurate-rag`) is essentially a walkthrough of this article. Contains evaluation data showing failure-rate reductions from ~10% to under 3% when combined with hybrid search and reranking.

### Anthropic SDKs and developer tooling

Cole heavily uses Anthropic's Python tooling:
- **`FastMCP` from the Anthropic Python SDK** — the canonical way to build [[ModelContextProtocol]] servers in Python. Cole's MCP server template (in `summary-build-your-own-mcp-servers-template`) is built on `FastMCP`.
- **[[PromptCaching]]** — reduces cost ~90% on repeated prompt prefixes; critical for making contextual retrieval economically viable on large corpora.

### Influence on this playlist's content

- The MCP-as-sub-agent pattern Cole demonstrates exists *because* Anthropic shipped MCP and made it ubiquitous in AI IDEs.
- The parallel agent architecture of video 2 is essentially Cole's expanded implementation of the "parallelization" pattern from the Anthropic article.

## Related

- [[ModelContextProtocol]] — Anthropic's protocol that powers most patterns in this playlist
- [[Archon]] — designed to plug into Claude (via MCP) inside AI IDEs
- [[ContextualRetrieval]] — Anthropic-authored RAG enhancement pattern
- [[ParallelAgentArchitecture]] — pattern Anthropic taxonomized
- [[summary-building-effective-agents]] — Anthropic's article (planned wiki page; concept-level)
- [[PromptCaching]] — Anthropic feature critical for contextual retrieval cost
- [[Windsurf]], [[Cursor]] — AI IDEs that ship MCP support and use Claude as their default LLM
- [[summary-20250508 - The EASIEST Possible Strategy for Accurate RAG (Step by Step Guide)]] — walkthrough of Anthropic's contextual retrieval article
- [[summary-20250414 - The ULTIMATE Guide to Building Your Own MCP Servers (Free Template)]] — uses Anthropic's `FastMCP`
- [[summary-20260101 - AI Exploded in 2025 - Here’s Everything That Happened]] — 2025 year-in-review; Anthropic's milestones
