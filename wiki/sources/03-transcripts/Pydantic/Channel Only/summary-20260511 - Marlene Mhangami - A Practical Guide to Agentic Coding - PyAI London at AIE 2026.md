---
title: "summary-20260511 - Marlene Mhangami - A Practical Guide to Agentic Coding - PyAI London at AIE 2026"
type: source
tags: [source, pydantic, pyai-london, agentic-coding, copilot, mcp]
sources: ["raw/03-transcripts/Pydantic/Channel Only/20260511 - Marlene Mhangami - A Practical Guide to Agentic Coding - PyAI London at AIE 2026.md"]
last_updated: 2026-06-25
---

## Core Summary

Marlene Mhangami (Microsoft/GitHub, Core AI team) presents a practical guide to agentic coding structured around the agentic loop: gather context, take action, verify results. Covers instruction files (Copilot instructions, CLAUDE.md, agents.md), context compaction to prevent context rot, MCP for tool access, and verification with Playwright. Key finding: human-written instruction files outperform agent-written ones by 16% or more.

## Key Points

- Agentic loop: gather context -> take action -> verify results (from Anthropic's Claude Code architecture)
- Context gathering: attach files/issues/PRs to chat; use instruction files (Copilot instructions.md, Cursor rules, CLAUDE.md, agents.md)
- Context rot: Chroma study shows LLM performance degrades beyond certain context threshold; compact proactively
- Context compaction in PydanticAI: count tokens, retain only last N messages when threshold exceeded
- Taking action: MCP is the primary way to give agents external tools; demo with Excalidraw and GitHub MCP servers
- Verification: Playwright for browser-based testing of agent-generated code
- Research finding: human-written skills/instructions improve agent performance ~16%; agent-written skills can degrade it ~20% and increase cost

## Related

- [[AgenticCoding]] — the paradigm
- [[ModelContextProtocol]] — tool access protocol
- [[ContextEngineering]] — managing context windows
- [[ClaudeCode]] — reference coding agent architecture
- [[GitHubCopilot]] — Microsoft's coding agent
