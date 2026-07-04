---
title: "ClaudeCode"
type: entity
tags: [tool, coding-agent, anthropic]
sources: [raw/03-transcripts/Claude/Claude Code 101/01 - What is Claude Code.md, raw/03-transcripts/Claude/Claude Code 101/02 - Installing Claude Code.md, raw/03-transcripts/Claude/Claude Code 101/03 - How Claude Code Works.md, raw/03-transcripts/Claude/Claude Code 101/04 - Your first Claude Code prompt.md, raw/03-transcripts/Claude/Claude Code 101/05 - The CLAUDE.md file.md, raw/03-transcripts/Claude/Claude Code 101/06 - The Explore → Plan → Code → Commit workflow in Claude Code.md, raw/03-transcripts/Claude/Claude Code 101/07 - Context Management in Claude Code.md, raw/03-transcripts/Claude/Claude Code 101/08 - MCP in Claude Code.md, raw/03-transcripts/Claude/Claude Code 101/09 - Hooks in Claude Code.md, raw/03-transcripts/Claude/Claude Code Skills/01 - What are skills.md, raw/03-transcripts/Claude/Claude Code subagents/03 - What are subagents.md, raw/01-articles/claude/2025-06-18 - Remote MCP support in Claude Code.md, raw/01-articles/claude/2025-05-07 - Introducing web search on the Anthropic API.md, raw/01-articles/claude/2025-07-24 - How Anthropic teams use Claude Code.md, raw/01-articles/claude/2025-08-20 - Claude Code and new admin controls for business plans.md, raw/01-articles/claude/2025-09-29 - Building agents with the Claude Agent SDK.md, raw/03-transcripts/Claude/Code with Claude 2026 - San Francisco/13 - Running an AI-native engineering org.md, raw/01-articles/claude/2025-08-06 - Automate security reviews with Claude Code.md, raw/01-articles/claude/2025-10-06 - Optimize code performance quickly.md, raw/01-articles/claude/2025-10-08 - Beyond permission prompts making Claude Code more secure and autonomous.md, raw/01-articles/claude/2025-10-09 - Customize Claude Code with plugins.md, raw/01-articles/claude/2025-10-10 - Build responsive web layouts.md, raw/01-articles/claude/2025-10-15 - How to scale agentic coding across your engineering organization.md]
last_updated: 2026-07-04
---

## Definition

Claude Code is Anthropic's agentic coding tool that has direct access to a developer's files, terminal, and codebase. It can read code, edit files, run commands, and integrate with existing developer tools to accelerate software development.

## Key Information

- Available in the terminal, Visual Studio Code, JetBrains IDEs, the Claude desktop app, and the web (claude.ai/code).
- Differs from Claude AI in that it has direct filesystem access rather than requiring copy-paste workflows.
- Operates as an AI agent: an LLM in a real-time loop with access to tools, external services, and other agents.
- By default asks for permission before running commands or modifying files.
- Can search the web for documentation and API references via [[WebSearch]], with access to current API documentation and technical articles.
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

### Business Plan Integration (August 2025)

Enterprise and Team plan customers can now access Claude Code via **premium seats** that bundle Claude and Claude Code under one subscription. Admins assign standard or premium seats per user; extra usage is available at standard API rates with per-user spend caps. Both plans include Claude Code usage analytics and self-serve seat management. See [[ClaudeEnterprise]] and [[ClaudeTeamPlan]] for plan details. Early adopters:

- **[[Behavox]]** (compliance/security): hundreds of developers onboarded; Claude Code became primary pair programmer.
- **[[Altana]]** (supply chain AI): 2–10x development velocity acceleration for AI/ML systems.

### Usage at Anthropic

Across [[Anthropic]], teams use [[ClaudeCode]] to:

- **Onboarding & Codebase Navigation** — Help new hires understand data pipelines and dependencies; serve as a "first stop" for identifying relevant files for bug fixes and features
- **Testing & Code Review** — Automate unit test generation and integrate with GitHub Actions for PR comments; enable test-driven development workflows
- **Production Debugging** — Diagnose incidents 3x faster by analyzing stack traces; gain confidence fixing bugs in unfamiliar codebases
- **Rapid Prototyping** — Build [[React]] applications with [[TypeScript]] for visualizing [[ReinforcementLearning]] models; develop features autonomously through iterative testing
- **Knowledge Consolidation** — Consolidate scattered technical documentation via [[MCP]] and CLAUDE.md files; create markdown runbooks and troubleshooting guides
- **Custom Automation** — Build tools without dedicated development resources; process data, generate variations, and create specialized workflows

See [[summary-2025-07-24 - How Anthropic teams use Claude Code]] for detailed case studies.

### Scaling Adoption and Activity Metrics (October 2025)

Claude Code includes **Activity Metrics**, tracking lines of code accepted, suggestion acceptance rates, daily active users and sessions, organization-wide and per-user spend, and individual developer metrics — used as one of several success measures (alongside sprint throughput, task completion time, and developer satisfaction) when scaling [[AgenticCoding]] adoption across an engineering organization.

### Responsive Web Layouts (October 2025)

For responsive-design issues spanning multiple stylesheets, Claude Code scans a project's CSS to find fixed-width styles and overflow-causing patterns (with line numbers), replaces them with responsive alternatives, adds breakpoint-specific media queries, tests at multiple viewport widths, and generates a Playwright test suite covering real device sizes to prevent regressions. See [[ResponsiveWebDesign]].

### Plugins (October 2025)

Claude Code plugins bundle any combination of slash commands, sub-agents, MCP servers, and hooks into a single installable package (`/plugin` command, public beta). Plugin marketplaces — a git/GitHub repo or URL with a `.claude-plugin/marketplace.json` file — let teams discover, curate, and distribute plugins organization-wide or to the community. See [[ClaudeCodePlugins]].

### Sandboxing and Claude Code on the Web (October 2025)

To reduce "approval fatigue" from constant permission prompts, Claude Code added a sandboxed bash tool (research preview, built on Linux bubblewrap / macOS Seatbelt) that enforces filesystem and network isolation so Claude can act freely within defined boundaries — enable via `claude --sandbox`. **Claude Code on the web** runs each session in an isolated cloud sandbox where sensitive credentials (git credentials, signing keys) never enter the sandbox; git operations are proxied through a scoped-credential service to [[GitHub]] instead. Both are framed as [[PromptInjection]] containment: even a successful injection can't exfiltrate data or reach unauthorized servers. See [[Sandboxing]].

### Code Performance Optimization (October 2025)

For performance issues spanning multiple files, Claude Code scans an entire codebase, correlates recent changes with performance degradation, and orchestrates targeted fixes (generating tests, validating improvements, preventing regressions) — e.g., detecting N+1 query problems and implementing eager loading, batch queries, composite indexes, or Redis caching. Best focused on performance-critical directories (`api/`, `core/`). [[Ramp]] uses Claude Code this way to accelerate delivery across hundreds of services. See [[CodePerformanceOptimization]].

### Automated Security Reviews (August 2025)

Claude Code added two ways to catch vulnerabilities before production, both built on a specialized security-focused prompt covering SQL injection, XSS, auth flaws, insecure data handling, and dependency vulnerabilities:

- **`/security-review` command**: ad-hoc, pre-commit vulnerability analysis from the terminal; Claude can also implement fixes.
- **GitHub Action**: automatically reviews every new pull request, filters false positives via customizable rules, and posts inline PR comments.

Anthropic uses both internally (including on Claude Code itself), catching a DNS-rebinding remote code execution vulnerability and an SSRF vulnerability in a credential-management proxy before they reached production. See [[AutomatedSecurityReview]] and [[VulnerabilityDetection]].

### Claude Agent SDK (September 2025)

The agent harness powering Claude Code was renamed from the **Claude Code SDK** to the **[[ClaudeAgentSDK]]** to reflect its broader applicability. Anthropic teams use Claude Code to power deep research, video creation, and note-taking in addition to coding — demonstrating that the same harness can drive general-purpose agent workflows. The SDK exposes the agent loop (gather context → take action → verify work) as primitives: agentic file-system navigation, custom tools, bash, code generation, MCP integrations, subagents, and the compact context feature.

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
- [[summary-2025-06-18 - Remote MCP support in Claude Code]] — remote MCP servers announcement
- [[summary-2025-07-24 - How Anthropic teams use Claude Code]] — real-world usage patterns across Anthropic teams
- [[summary-2025-05-07 - Introducing web search on the Anthropic API]] — web search integration announcement
- [[summary-01 - What are skills]] — skills system introduction
- [[summary-03 - What are subagents]] — sub-agents introduction
- [[CLAUDE-md]] — the memory file concept
- [[ExplorePlanCodeCommit]] — the EPCC workflow
- [[ModelContextProtocol]] — the MCP standard
- [[ClaudeCodeHooks]] — the hooks system
- [[ClaudeCodeSkills]] — the skills system
- [[ClaudeCodeSubagents]] — the sub-agents system
- [[AIAgent]] — the agent paradigm Claude Code embodies
- [[AgenticCoding]] — development paradigm Claude Code exemplifies
- [[WebSearch]] — web search capability integrated into Claude Code
- [[AgenticLoop]] — the core operational pattern
- [[ContextWindow]] — the memory constraint Claude Code operates within
- [[analysis-claude-product-landscape]] — comparison with Managed Agents and Cowork
- [[analysis-claude-code-extension-mechanisms]] — when to use Skills, Sub-agents, Hooks, or CLAUDE.md
- [[ClaudeEnterprise]] — Enterprise plan offering Claude Code in premium seats
- [[ClaudeTeamPlan]] — Team plan offering Claude Code in premium seats
- [[Behavox]] — Customer using Claude Code as primary pair programmer
- [[Altana]] — Customer achieving 2–10x development velocity with Claude Code
- [[summary-2025-08-20 - Claude Code and new admin controls for business plans]] — Premium seats and business plan integration announcement
- [[summary-2025-09-29 - Building agents with the Claude Agent SDK]] — SDK rename announcement and agent-building best practices
- [[ClaudeAgentSDK]] — the renamed Claude Code SDK for general-purpose agent development
- [[ContextEngineering]] — file/folder structure as agent context design
- [[summary-13 - Running an AI-native engineering org]] — engineering-org lessons on how bottlenecks, planning, and code review changed inside the Claude Code team
- [[summary-17 - Preview your running app in Claude Code on desktop]] — product-launch teaser for live app preview in the desktop app
- [[summary-23 - Introducing Code Review]] — product-launch teaser introducing the Code Review capability
- [[summary-06 - Find and fix security vulnerabilities with Claude]] — product-launch teaser for vulnerability finding/fixing
- [[summary-25 - Find and fix security vulnerabilities with Claude]] — distinct product-launch teaser with the same title
- [[AutomatedSecurityReview]] — the `/security-review` command and GitHub Action
- [[VulnerabilityDetection]] — vulnerability classes detected by security review features
- [[CodeSecurity]] — broader security practices in Claude Code workflows
- [[GitHub]] — platform hosting the security-review GitHub Action integration
- [[summary-2025-08-06 - Automate security reviews with Claude Code]] — security review feature announcement
- [[CodePerformanceOptimization]] — project-wide performance optimization use case
- [[Ramp]] — customer using Claude Code for performance work across hundreds of services
- [[summary-2025-10-06 - Optimize code performance quickly]] — performance optimization use-case article
- [[Sandboxing]] — filesystem and network isolation underlying the sandboxed bash tool and Claude Code on the web
- [[PromptInjection]] — threat model sandboxing mitigates
- [[summary-2025-10-08 - Beyond permission prompts making Claude Code more secure and autonomous]] — sandboxing and Claude Code on the web announcement
- [[ClaudeCodePlugins]] — the plugin and marketplace system
- [[summary-2025-10-09 - Customize Claude Code with plugins]] — plugins announcement
- [[ResponsiveWebDesign]] — codebase-wide responsive-layout refactoring use case
- [[summary-2025-10-10 - Build responsive web layouts]] — responsive layout use-case article
- [[summary-2025-10-15 - How to scale agentic coding across your engineering organization]] — organizational rollout methodology and Activity Metrics
