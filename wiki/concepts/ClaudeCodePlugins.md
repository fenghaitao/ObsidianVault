---
title: "ClaudeCodePlugins"
type: concept
tags: [claude-code, plugins, marketplace, extensibility]
sources: ["raw/01-articles/claude/2025-10-09 - Customize Claude Code with plugins.md", "raw/01-articles/claude/2026-01-30 - Customize Cowork with plugins.md", "raw/01-articles/claude/2026-02-24 - Cowork and plugins for teams across the enterprise.md"]
last_updated: 2026-07-04
---

## Definition

Claude Code plugins are lightweight, installable packages bundling any combination of Claude Code's extension points — slash commands, agents, MCP servers, and hooks — into a single shareable unit installed with one command.

## Key Information

- Bundle any combination of: slash commands, sub-agents ([[ClaudeCodeSubagents]]), [[ModelContextProtocol|MCP]] servers, and [[ClaudeCodeHooks|hooks]].
- Installed via the `/plugin` command (public beta as of October 2025); toggle on/off to manage system-prompt context and complexity — enable only when needed.
- Intended as Anthropic's standard way to bundle and share Claude Code customizations going forward, evolving as more extension points are added.
- Common use cases: DevOps automation, documentation generation, project management, testing suites.
- **Plugin marketplaces**: curated collections hosted as a git repository, GitHub repository, or URL containing a `.claude-plugin/marketplace.json` file. Used to share plugins with the community, distribute approved plugins across an organization, or build on existing shared solutions.
  - Add a marketplace: `/plugin marketplace add user-or-org/repo-name`, then browse/install via the `/plugin` menu.
  - Community examples: Dan Ávila's marketplace (DevOps automation, documentation generation, project management, testing suites); Seth Hobson's GitHub repository curating 80+ specialized sub-agents distributed via plugins.
- Anthropic's own example plugins (`anthropics/claude-code`) cover PR reviews, security guidance, [[ClaudeAgentSDK|Claude Agent SDK]] development, and a meta-plugin for creating new plugins.
- Works across both the terminal and the VS Code extension.
- **LSP access point** (May 2026): [[LanguageServerProtocol|Language Server Protocol]] integrations — which give Claude symbol-level "go to definition"/"find references" navigation instead of text pattern-matching — are accessed through the plugin layer rather than being a separate extension point; a common mistake is assuming LSP navigation works automatically without installing the relevant code-intelligence plugin and language server binary.
- **Origin story**: the plugins spec (written by Anthropic engineer Noah) was sent to Claude Code, which returned a prototype close to production-ready — that prototype anchored what the team ultimately shipped and let them validate the UX quickly. See [[summary-2026-03-19 - Product management on the AI exponential]].

## Cowork Plugins (January 2026)

The same bundling concept was extended to [[ClaudeCowork|Claude Cowork]] (research preview): plugins bundle skills, connectors, slash commands, and sub-agents to turn Claude into a role/team/company specialist. Launched with 11 open-sourced plugins (Productivity, Enterprise search, Plugin Create/Customize, Sales, Finance, Data, Legal, Marketing, Customer support, Product management, Biology research), installable from Cowork, a web collection, or GitHub. Currently saved locally; org-wide sharing/private marketplaces planned.

### Private Marketplaces and Admin Controls (February 2026)

Admins can now build org-specific private plugin marketplaces, use private GitHub repositories as plugin sources (private beta), set per-user provisioning and auto-install, and manage everything through a unified "Customize" menu consolidating plugins, skills, and connectors in one place. Plugins remain file-based and portable across both Cowork and anything built on the [[ClaudeAgentSDK|Claude Agent SDK]], making cross-team and cross-partner marketplaces straightforward. New partner-built plugins launched from Slack (Salesforce), LSEG, S&P Global, Apollo, Common Room, and Tribe AI.

- **Data plugin example (April 2026)**: Cowork's data plugin for Snowflake, Databricks, BigQuery, Hex and more bundles 10 skills with 8 MCP servers, illustrating the "bundle skills + MCP servers as a plugin" pattern for unifying multiple context providers with minimal friction. See [[ModelContextProtocol]].

## Related

- [[ClaudeCode]] — the tool plugins extend
- [[ClaudeCodeSkills]] — a composable extension mechanism that can be bundled inside a plugin
- [[ClaudeCodeSubagents]] — sub-agents are one of the four things a plugin can bundle
- [[ClaudeCodeHooks]] — hooks are one of the four things a plugin can bundle
- [[ModelContextProtocol]] — MCP servers are one of the four things a plugin can bundle
- [[ClaudeAgentSDK]] — subject of one of Anthropic's example plugins
- [[summary-2025-10-09 - Customize Claude Code with plugins]] — source announcement
- [[ClaudeCowork]] — product now supporting the same plugin mechanism
- [[summary-2026-01-30 - Customize Cowork with plugins]] — Cowork plugins announcement
- [[ClaudeAgentSDK]] — plugins are portable across this SDK too
- [[PwC]] — customer quote
- [[BlankMetal]] — customer quote
- [[summary-2026-02-24 - Cowork and plugins for teams across the enterprise]] — private marketplaces and admin controls announcement
- [[summary-2026-03-19 - Product management on the AI exponential]] — plugins-spec origin story
- [[summary-2026-04-22 - Building agents that reach production systems with MCP]] — data plugin example bundling skills and MCP servers
- [[LanguageServerProtocol]] — code-intelligence capability accessed through the plugin layer
- [[summary-2026-05-14 - How Claude Code works in large codebases Best practices and where to start]] — LSP-via-plugins access pattern
