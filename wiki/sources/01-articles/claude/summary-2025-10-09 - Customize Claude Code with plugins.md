---
title: "summary-2025-10-09 - Customize Claude Code with plugins"
type: source
tags: [source, original-material, claude-code, plugins, marketplace]
sources: ["raw/01-articles/claude/2025-10-09 - Customize Claude Code with plugins.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic introduced Claude Code plugins: lightweight, installable packages bundling any combination of slash commands, agents, MCP servers, and hooks — Claude Code's existing extension points — so teams can share powerful setups with a single install command. Plugins install via the `/plugin` command (public beta) and toggle on/off to manage context and complexity. Plugin marketplaces (a git/GitHub repo or URL hosting a `.claude-plugin/marketplace.json` file) let anyone discover, curate, and distribute plugins to the community or across an organization.

## Key Points

- **Plugins** package any combination of slash commands, agents, MCP servers, and hooks — Claude Code's four customization extension points — for one-command installation.
- Installed via `/plugin` (public beta); designed to toggle on/off to reduce system prompt context and complexity when not needed.
- Plugins are becoming Anthropic's standard way to bundle and share Claude Code customizations going forward.
- Common use cases: DevOps automation, documentation generation, project management, testing suites.
- **Plugin marketplaces**: curated collections hosted via a git repo, GitHub repo, or URL with a `.claude-plugin/marketplace.json` file, letting developers discover and install plugins, distribute approved plugins org-wide, or build on shared solutions.
- To use: `/plugin marketplace add user-or-org/repo-name`, then browse/install via the `/plugin` menu.
- **Community examples**: engineer Dan Ávila's marketplace offers DevOps, documentation, project-management, and testing plugins; engineer Seth Hobson curated 80+ specialized sub-agents distributed via plugins.
- Anthropic published example plugins for PR reviews, security guidance, Claude Agent SDK development, and a meta-plugin for creating new plugins, at `anthropics/claude-code`.
- Works across terminal and VS Code.

## Related

- [[ClaudeCode]] — the tool plugins extend
- [[ClaudeCodePlugins]] — the concept this article introduces
- [[ClaudeCodeSkills]] — a related, composable extension mechanism (skills can be bundled inside plugins)
- [[ModelContextProtocol]] — MCP servers are one of the four things a plugin can bundle
