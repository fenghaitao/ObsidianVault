---
title: "summary-2026-03-05 - Skills explained How Skills compares to prompts, Projects, MCP, and subagents"
type: source
tags: [source, skills, projects, mcp, subagents, prompts]
sources: ["raw/01-articles/claude/2026-03-05 - Skills explained How Skills compares to prompts, Projects, MCP, and subagents.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic positions Skills within Claude's full agentic toolkit — prompts, [[Projects]], subagents, and MCP — clarifying what each provides, when to reach for it, and how they compose. Core distinction: Projects say "here's what you need to know" (static background knowledge); Skills say "here's how to do things" (dynamic, on-demand procedural expertise).

## Key Points

- **Skills**: folders of instructions/scripts/resources loaded dynamically via progressive disclosure — metadata first (~100 tokens), full instructions when relevant (<5k tokens), bundled files/scripts only as needed. Best for domain expertise and personal preferences applied consistently and repeatedly.
- **Prompts**: ephemeral, conversational, natural-language instructions — best for one-off requests, conversational refinement, and ad-hoc formatting. If the same prompt keeps getting typed across conversations, that's the signal to capture it as a Skill instead.
- **Projects**: self-contained workspaces (200K context window) with persistent knowledge bases and custom instructions applying to every chat within them; auto-enables RAG mode (up to 10x capacity) as knowledge approaches context limits. Best for persistent background knowledge on a specific initiative; if the same instructions get copied across multiple Projects, that's a signal to create a Skill instead.
- **Subagents**: specialized assistants (Claude Code, Claude Agent SDK) with their own context window, system prompt, and tool permissions, handling discrete tasks independently. Best for task specialization, context isolation, parallel processing, and restricting tool access (e.g., read-only). Subagents can use Skills — a code-review subagent can apply a language-specific Skill for consistent standards.
- **MCP**: universal connectivity layer to external data/tools (Google Drive, Slack, GitHub, databases, CRMs). MCP connects Claude to data; Skills teach Claude what to do with that data — use both together (MCP for connectivity, Skills for procedural knowledge).
- **Comparison table dimensions**: persistence (Skills: across conversations; Prompts: single conversation; Projects: within project; Subagents: across sessions; MCP: continuous connection), and whether each can include executable code (Skills and MCP: yes; Prompts and Projects: no; Subagents: full agent logic).
- **Worked example**: a competitive-analysis research agent combining a "Competitive Intelligence" Project (uploaded market research + instructions), MCP connections (Google Drive, GitHub), a competitive-analysis Skill (analytical framework), and two Claude Code subagents (market-researcher, technical-analyst) working in parallel — refined turn-by-turn with conversational prompts.

## Related

- [[ClaudeCodeSkills]] — the concept this article positions relative to the rest of the stack
- [[Projects]] — Claude's persistent-context workspace feature, contrasted with Skills
- [[ClaudeCodeSubagents]] — contrasted with Skills for task delegation vs. portable expertise
- [[ModelContextProtocol]] — contrasted with Skills for connectivity vs. procedural knowledge
