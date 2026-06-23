---
title: "Claude Product Landscape: Code, Managed Agents, and Cowork"
type: synthesis
tags: [claude-code, managed-agents, cowork, product-comparison, anthropic]
sources: []
last_updated: 2026-06-23
---

## Question

How do Claude Code, Claude Managed Agents, and Claude Cowork compare, and when should you use each?

## Answer

Anthropic offers three distinct Claude-powered products that serve different audiences and use cases, yet share a common architectural DNA: skills, scheduling, and memory.

### The Three Products

| Dimension | **Claude Code** | **Claude Managed Agents** | **Claude Cowork** |
|---|---|---|---|
| **Audience** | Developers | Engineering teams building production agents | Knowledge workers (legal, sales, marketing, ops) |
| **Interface** | Terminal, VS Code, JetBrains, Desktop, Web | API + platform dashboard | Desktop app with file system access |
| **Primary task** | Read, edit, and run code in a codebase | Build, deploy, and operate production agents at scale | Create and manage documents, spreadsheets, presentations; connect to enterprise systems |
| **Execution model** | Interactive, user-in-the-loop | Autonomous, scheduled, fleet-based | Autonomous, scheduled, human-in-the-loop for approvals |
| **Key mechanism** | Agentic loop with tool access | Harness separating "brain" from "hands" + memory + dreaming | Skills-based reusable processes + cron-triggered scheduled tasks |
| **Context** | Context window with compaction strategies | 1M token context window + file-system memory | Context window + skills that load on demand |
| **Infrastructure** | Local machine | Auto-scaling sandboxes, agentic fleets, vaults | Local machine with enterprise system connectors |

### Shared DNA

All three products share fundamental concepts:

- **Skills:** Reusable, task-specific instruction files. In Claude Code, skills activate on demand via description matching ([[ClaudeCodeSkills]]). In Claude Cowork, skills are the primary mechanism for capturing repeatable processes ([[ClaudeCowork]]). In Managed Agents, skills are self-written by agents to fill knowledge gaps ([[ClaudeManagedAgents]]).
- **Scheduling:** Claude Code has [[ClaudeCodeRoutines]] (`/schedule` for cron-triggered autonomous runs). Claude Cowork has scheduled tasks for recurring knowledge work (weekly metrics reviews, daily briefs). Managed Agents has scheduled deployments on any cadence.
- **Memory and learning:** Managed Agents has the most sophisticated memory system with file-system stores, dreaming, and multi-agent shared memory ([[AgenticMemory]]). Claude Cowork saves learnings back into skills for continuous improvement. Claude Code uses [[CLAUDE-md]] for persistent project memory.

### When to Use Which

**Use Claude Code when:**
- You're a developer working on a codebase
- You need interactive, tight-feedback-loop coding assistance
- You want to explore, plan, code, and commit in a single workflow ([[ExplorePlanCodeCommit]])
- You need IDE integration (VS Code, JetBrains) or terminal-native access

**Use Claude Managed Agents when:**
- You're deploying production agents that need to run autonomously at scale
- You need auto-scaling infrastructure, agentic fleets, and secure secret storage
- You want agents that learn across sessions via dreaming and memory
- You're building agent orchestration into your product (like Notion, Asana, or Rakuten do)

**Use Claude Cowork when:**
- You're a knowledge worker (legal, sales, marketing, ops), not a developer
- You work primarily with documents, spreadsheets, presentations, and enterprise systems
- You want scheduled, autonomous workflows with human-in-the-loop approval
- You need to connect to Gmail, Slack, Salesforce, data warehouses, and other enterprise tools

### The Convergence

These products are converging on a shared vision of autonomous, self-improving agents. Claude Code is gaining scheduling (Routines) and memory-like persistence (CLAUDE.md). Managed Agents has the most advanced memory and dreaming. Claude Cowork brings agentic automation to non-developers. The boundary between "coding tool" and "knowledge work tool" and "agent platform" is blurring — all three are manifestations of the same underlying agent paradigm ([[AgenticLoop]], [[AIAgent]]).

## Related

- [[ClaudeCode]] — the developer-focused agentic coding tool
- [[ClaudeManagedAgents]] — the production agent platform
- [[ClaudeCowork]] — the knowledge worker automation product
- [[ClaudeCodeSkills]] — skills as the reusable mechanism across all three
- [[ClaudeCodeRoutines]] — scheduling in Claude Code
- [[AgenticMemory]] — memory and dreaming, most advanced in Managed Agents
- [[AgenticLoop]] — the core operational pattern shared by all three