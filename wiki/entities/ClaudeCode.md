---
title: "ClaudeCode"
type: entity
tags: [tool, coding-agent, anthropic, claude]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer.md"]
last_updated: 2026-06-25
---

## Definition
Claude Code is Anthropic's coding agent that uses Claude models to autonomously write, edit, and manage code. It uses a system prompt and a Claude.md file for user-customizable rules.

## Key Information
- In prompt learning experiments, vanilla Claude Code (with no rules added) resolved approximately 40% of SWE-bench GitHub issues.
- After prompt learning with 150 training examples, Claude Code improved to approximately 45% — a 5 percentage point gain purely from system prompt iteration.
- Claude 4.1 achieved performance near Claude 4.5 (considered state-of-the-art for coding) at two-thirds the cost after prompt optimization.
- Uses a Claude.md file where users can append repository-specific rules, analogous to Cline's rules file.
- Its system prompt has been publicly leaked and discussed, revealing its length and complexity compared to other coding agents.
- Mentioned alongside Cursor as a successful example of coding agents with good planning capabilities.
- Foundation of the Claude Agent SDK — users organically started using Claude Code for non-coding tasks, revealing the bash tool and file system as universal agent primitives.
- The bash tool is what makes Claude Code so effective: instead of custom search/lint/execute tools, it uses grep, npm, and the existing software ecosystem.
- Described as "the first true agent" — the first time AI was seen working autonomously for 10, 20, or 30 minutes.
- Includes sub-agents with best-in-class bash support, handling race conditions and process isolation.
- Has a plugin marketplace (accessible via /plugins) for skill discovery.
- Includes a to-do tool, compacting, hooks, and memory features.
- Architecture: a simple master while-loop (internally called "N0") — while tool calls exist, run the tool, feed results to model, repeat
- Core tools: Read (with token limits), Grep/Glob (instead of RAG), Edit (using unified diffs), Bash (the most important tool), Web Search/Fetch, Todos, Tasks (sub-agents)
- System prompt nudges: concise outputs, use tools over text explanations, match existing code, run commands in parallel, use todo lists
- Context management: H2A async buffer decouples I/O from reasoning; compaction drops middle and summarizes head/tail at ~92% capacity
- Uses trigger phrases for reasoning budgets: think, think hard, think harder, ultra think
- Features Skills: extendable system prompts loaded on demand for specialized tasks
- Sandboxing: pipeline gates bash commands by prefix; containerization for web fetch to prevent prompt injection
- Jared Zoneraich rebuilt his engineering org around Claude Code with the rule: if it takes under an hour, use Claude Code
- Zoneraich personally uses Claude Code for human-like actions (git, local environment, back-and-forth tasks)

## Related
- [[Cline]] — another coding agent benchmarked alongside Claude Code
- [[Cursor]] — another successful coding agent
- [[SWE-bench]] — benchmark used to evaluate Claude Code
- [[PromptLearning]] — technique used to improve Claude Code's performance
- [[RuleBasedPrompting]] — the approach that yielded improvements
- [[summary-20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize]] — source
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — source
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[ClaudeAgentSDK]] — agent framework built on Claude Code
- [[BashTool]] — what makes Claude Code effective
- [[SubAgents]] — key feature
- [[Hooks]] — verification mechanism
- [[MasterWhileLoop]] — core architectural pattern
- [[BashAsUniversalAdapter]] — key design principle
- [[UnifiedDiffing]] — editing approach
- [[TodoListPattern]] — steerability mechanism
- [[Skills]] — extendable system prompt mechanism
- [[SandboxingAndPermissions]] — security layer
- [[ReasoningBudgets]] — thinking tiers
- **XAA Demo**: Claude Code was demonstrated with XAA (Cross-App Access) compatibility, automatically connecting to the Figma MCP server via Okta SSO without consent screens
- **WorkOS Integration**: Uses WorkOS for authentication, enabling XAA support for enterprise SSO connections

- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — source
- [[summary-20260428 - One Login to Rule Them All： Cross-App Access for MCP — Garrett Galow, WorkOS]] — source
- [[WorkOS]] — authentication provider
- [[CrossAppAccess]] — XAA implementation
