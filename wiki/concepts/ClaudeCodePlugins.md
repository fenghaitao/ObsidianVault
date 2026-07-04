---
title: "ClaudeCodePlugins"
type: concept
tags: [claude-code, plugins, marketplace, extensibility]
sources: ["raw/01-articles/claude/2025-10-09 - Customize Claude Code with plugins.md"]
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

## Related

- [[ClaudeCode]] — the tool plugins extend
- [[ClaudeCodeSkills]] — a composable extension mechanism that can be bundled inside a plugin
- [[ClaudeCodeSubagents]] — sub-agents are one of the four things a plugin can bundle
- [[ClaudeCodeHooks]] — hooks are one of the four things a plugin can bundle
- [[ModelContextProtocol]] — MCP servers are one of the four things a plugin can bundle
- [[ClaudeAgentSDK]] — subject of one of Anthropic's example plugins
- [[summary-2025-10-09 - Customize Claude Code with plugins]] — source announcement
