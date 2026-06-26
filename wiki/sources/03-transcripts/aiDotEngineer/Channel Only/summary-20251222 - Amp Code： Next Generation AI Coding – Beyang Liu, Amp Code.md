---
title: "summary-20251222 - Amp Code： Next Generation AI Coding – Beyang Liu, Amp Code"
type: source
tags: [source, transcript, coding-agent, sub-agents, agent-architecture]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - Amp Code： Next Generation AI Coding – Beyang Liu, Amp Code.md"]
last_updated: 2026-06-25
---

## Core Summary
Amp Code is an opinionated frontier coding agent that rejects the conventional model-selector paradigm in favor of an agent-oriented architecture with specialized sub-agents (Finder, Oracle, Librarian, Kraken). Beyang Liu presents Amp's contrarian design decisions: custom tools over MCP integration, sub-agents for context window management, and a dual-agent model (Smart Agent for complex tasks, Rush Agent for tight-loop edits). The talk also covers Amp's custom TUI framework, editor-integrated code review interface, thread sharing for team learning, and an experimental ad-sponsored inference model to make agents economically accessible.

## Key Points
- Amp is a coding agent invoked from the terminal with a custom TUI framework built from scratch, also available as a VS Code extension
- Rejects MCP-heavy integration in favor of a refined custom tool set tuned to help agents close feedback loops, avoiding context confusion from irrelevant tools
- Uses specialized sub-agents to solve context exhaustion: Finder (codebase search), Oracle (deep reasoning), Librarian (external library context), Kraken (large-scale refactors via codemods)
- Two top-level agents instead of a model selector: Smart Agent (complex tasks with sub-agent access) and Rush Agent (fast, tight-loop edits)
- Built a custom diff viewer and review interface for the editor, recognizing that developers now spend most time reviewing agent output rather than writing code
- Thread sharing enables team learning — teammates can see each other's agent threads and prompting techniques
- Experimental ad network in the terminal sponsors inference costs for the Rush Agent, aiming to make coding agents economically accessible to students and hobbyists
- Recently switched the Smart Agent model to Gemini 3, reporting significant capability improvements

## Related
- [[AmpCode]] — the coding agent product
- [[BeyangLiu]] — speaker and Amp Code team member
- [[SubAgents]] — architectural pattern for context window management
- [[AgentOrientedArchitecture]] — Amp's alternative to model selectors
- [[ContextExhaustion]] — problem of agent context window filling up
- [[AdSponsoredInference]] — novel economic model for agent access
