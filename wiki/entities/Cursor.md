---
title: "Cursor"
type: entity
tags: [tool, code-editor, ai, coding-agent]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251224 - Why Agent Hype can fall short of reality – Joel Becker, METR.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260119 - How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Building your own software factory — Eric Zakariasson, Cursor.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260515 - How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom.md"]
last_updated: 2026-06-30
---

## Definition
Cursor is an AI-powered code editor that integrates LLMs for code generation, editing, and agentic coding workflows. It uses a system prompt that is iteratively refined.

## Key Information
- Mentioned alongside Claude Code and Cline as one of the coding agents whose system prompt has been publicly discussed and analyzed.
- Cited as a successful example of an agent with good planning capabilities, alongside Claude Code.
- Like other coding agents, Cursor's system prompt is not static — it is repeatedly iterated on to improve performance.
- The length and complexity of Cursor's system prompt was highlighted in a viral tweet comparing system prompts across major coding agents.
- Used as the primary AI tool in METR's RCT on developer productivity (March 2025), with Cursor Pro provided to all participants, typically running Claude 3.6/3.7 Sonnet.
- In the RCT, developers using Cursor (with AI allowed) were 19% slower than those without AI access, despite predictions of 20-25% speedup.
- May have had suboptimal capability elicitation at the time of the study compared to METR's heavily optimized agent scaffolding.
- Aman Khan used Cursor to build his demo agent: he gave it a Colab notebook for CrewAI tracing and asked it to build a UI-based LangGraph workflow, which it did.
- Khan also used Cursor to auto-instrument the agent for Arize by giving it a link to Arize docs — demonstrating how PMs can use AI tools to build prototypes without deep engineering support.
- Cursor's Composer is a distilled model that is extremely fast — Jared Zoneraich has been "almost switching completely to it"
- Composer demonstrates that fine-tuning/distillation can build defensibility based on proprietary data
- Cursor is UI-first (not CLI), and its speed is a key differentiator
- Zoneraich personally uses Cursor Composer for speed-sensitive tasks
- Cursor's first version was "so bad" but iterative development made it excellent
- Cursor shows three models running simultaneously, letting users choose state-of-the-art for planning and fast models for execution
- In METR's follow-up talk, Becker noted that three-quarters of RCT participants were totally unfamiliar with Cursor at the start of the study, though all had LLM experience in their core workflow
- Becker showed plots suggesting no clear relationship between Cursor familiarity and productivity in the RCT, though sample sizes were too small for strong conclusions
- One participant who had Cursor as their primary IDE in 2024 and 140+ logged hours was conservatively coded as 30-50 hours of experience
- Cursor 3 is a complete rewrite without VS Code, redesigned for agent-first workflow with multi-agent orchestration and nested agents
- Cursor Cloud Agents provide isolated VM-based agent execution with computer-use self-testing capabilities, running "multiple thousands" of agents per day
- Internal tools include Bugbot (automated PR review), agentic code owners (risk-based auto-approval), and continual learning plugins
- Eric Zakariasson, a Cursor engineer, runs 5-10 agents asynchronously in the cloud at all times
- Cursor Rules should emerge dynamically from agent failures rather than being pre-installed
- The internal dev tool abstracts complex service startup (OrbStack, ClickHouse, Postgres, Redis, Electron, Glass) behind simple commands
- **WorkOS Integration**: Uses WorkOS for authentication — if you've logged into Cursor with username/password or an enterprise IDP, you've used WorkOS
- **XAA Support**: Cursor is implementing Cross-App Access (XAA) via WorkOS, enabling automatic MCP server connections without consent screens when using Okta SSO
- **Git Work Trees**: Shipped in Cursor 2.0 (October 2025) as a code-heavy feature (~15,000 lines). Later replaced with a ~200-line markdown skill/command using /worktree and /bestofn. The new implementation uses agent skills and sub-agents as primitives, with server-controlled commands for prompt iteration.
- **Best of N**: Feature where users give the same task to different models simultaneously in isolated work trees, then compare results. Re-implemented as a ~40-line markdown skill.
- **Commands vs Skills**: Cursor uses server-controlled commands (/worktree, /bestofn) rather than local skills so prompts can be iterated on the backend without client updates.
- **Composer**: Cursor's in-house trained and distilled model, trained via RL. Future versions will include RL tasks for work tree environments.

## Related
- [[ClaudeCode]] — another coding agent compared alongside Cursor
- [[Cline]] — another coding agent compared alongside Cursor
- [[PromptLearning]] — technique applicable to improving Cursor's system prompt
- [[AmanKhan]] — used Cursor to build the workshop demo
- [[summary-20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize]] — source
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — source
- [[summary-20251224 - Why Agent Hype can fall short of reality – Joel Becker, METR]] — source
- [[summary-20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize]] — source
- [[RandomizedControlledTrial]] — study where Cursor was the primary AI tool
- [[SuboptimalCapabilityElicitation]] — possible limitation of Cursor at study time
- [[ModelDistillation]] — technique behind Composer's speed
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — source
- [[summary-20260119 - How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR]] — source
- [[JCurveFamiliarityEffect]] — debated in relation to Cursor familiarity
- [[Cursor3]] — the agent-first IDE rewrite
- [[CursorCloudAgents]] — cloud-based agent infrastructure
- [[Bugbot]] — Cursor's automated PR review tool
- [[Glass]] — Cursor's internal IDE interface component
- [[EricZakariasson]] — Cursor engineer who presented on building a software factory
- [[SoftwareFactory]] — the concept Eric presented using Cursor
- [[CursorRules]] — dynamic rules for steering agent behavior
- [[summary-20260428 - Building your own software factory — Eric Zakariasson, Cursor]] — source
- [[WorkOS]] — authentication provider for Cursor
- [[CrossAppAccess]] — XAA implementation for MCP
- [[summary-20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS]] — source
- [[summary-20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor]] — source
- [[DavidGomes]] — engineer who led the work tree skill refactor
- [[Composer]] — Cursor's in-house model
- [[GitWorktrees]] — the feature re-implemented as a skill
- [[BestOfN]] — competing models on the same task
- [[AgentCommandsVsSkills]] — server-controlled command mechanism
- [[MarkdownAsCode]] — paradigm behind the work tree refactor
- **Intercom evaluation**: Used by Intercom engineers before the company consolidated on Claude Code for the 2x project. Intercom chose to go all-in on Claude Code instead, applying platform consolidation strategy.
- [[summary-20260515 - How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom]] — source (evaluated by Intercom)
- [[Intercom]] — evaluated Cursor before consolidating on Claude Code
- [[Platform Consolidation for AI Coding]] — strategy behind not choosing Cursor
