---
title: "ClaudeCode"
type: entity
tags: [tool, coding-agent, anthropic]
sources: [raw/03-transcripts/Claude/Claude Code 101/01 - What is Claude Code.md, raw/03-transcripts/Claude/Claude Code 101/02 - Installing Claude Code.md, raw/03-transcripts/Claude/Claude Code 101/03 - How Claude Code Works.md, raw/03-transcripts/Claude/Claude Code 101/04 - Your first Claude Code prompt.md, raw/03-transcripts/Claude/Claude Code 101/05 - The CLAUDE.md file.md, raw/03-transcripts/Claude/Claude Code 101/06 - The Explore → Plan → Code → Commit workflow in Claude Code.md, raw/03-transcripts/Claude/Claude Code 101/07 - Context Management in Claude Code.md, raw/03-transcripts/Claude/Claude Code 101/08 - MCP in Claude Code.md, raw/03-transcripts/Claude/Claude Code 101/09 - Hooks in Claude Code.md, raw/03-transcripts/Claude/Claude Code Skills/01 - What are skills.md, raw/03-transcripts/Claude/Claude Code subagents/03 - What are subagents.md]
last_updated: 2026-06-23
---

## Definition

Claude Code is Anthropic's agentic coding tool that has direct access to a developer's files, terminal, and codebase. It can read code, edit files, run commands, and integrate with existing developer tools to accelerate software development.

## Key Information

- Available in the terminal, Visual Studio Code, JetBrains IDEs, the Claude desktop app, and the web (claude.ai/code).
- Differs from Claude AI in that it has direct filesystem access rather than requiring copy-paste workflows.
- Operates as an AI agent: an LLM in a real-time loop with access to tools, external services, and other agents.
- By default asks for permission before running commands or modifying files.
- Can search the web for documentation and API references.
- Not infallible: may misunderstand intent, introduce bugs, or over-engineer solutions.

### Installation

- **Terminal (macOS/Linux/WSL):** one-line curl command; Homebrew also available (no auto-update).
- **Windows:** PowerShell (Invoke-RestMethod), CMD (curl), or winget (no auto-update).
- **VS Code:** install the "Claude Code" extension by Anthropic (blue check verified) from the extensions panel.
- **JetBrains:** install the Claude Code plugin from the JetBrains Marketplace.
- **Claude Desktop:** toggle "Code" at the top after sign-in.
- **Web:** claude.ai/code, restricted to GitHub repositories only.
- First run: choose color theme, sign in (Pro/Max/Enterprise or API key), and set directory scope.
- The terminal receives features fastest; IDE integrations offer a more intertwined experience; desktop is good for background tasks; web supports remote GitHub work and parallel sessions.

## Related

- [[summary-01 - What is Claude Code]] — source summary
- [[summary-02 - Installing Claude Code]] — installation guide source
- [[summary-03 - How Claude Code Works]] — internals of the agentic loop
- [[summary-04 - Your first Claude Code prompt]] — prompting and plan mode
- [[summary-05 - The CLAUDE.md file]] — persistent project memory via CLAUDE.md
- [[summary-06 - The Explore → Plan → Code → Commit workflow in Claude Code]] — the recommended workflow
- [[summary-07 - Context Management in Claude Code]] — context management strategies
- [[summary-08 - MCP in Claude Code]] — MCP integration
- [[summary-09 - Hooks in Claude Code]] — deterministic lifecycle hooks
- [[summary-01 - What are skills]] — skills system introduction
- [[summary-03 - What are subagents]] — sub-agents introduction
- [[CLAUDE-md]] — the memory file concept
- [[ExplorePlanCodeCommit]] — the EPCC workflow
- [[ModelContextProtocol]] — the MCP standard
- [[ClaudeCodeHooks]] — the hooks system
- [[ClaudeCodeSkills]] — the skills system
- [[ClaudeCodeSubagents]] — the sub-agents system
- [[AIAgent]] — the agent paradigm Claude Code embodies
- [[AgenticLoop]] — the core operational pattern
- [[ContextWindow]] — the memory constraint Claude Code operates within
