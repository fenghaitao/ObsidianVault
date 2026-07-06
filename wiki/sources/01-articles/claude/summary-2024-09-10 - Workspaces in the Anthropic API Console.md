---
title: "Workspaces in the Anthropic API Console"
type: source
tags: [anthropic, api, console, workspaces, resource-management]
sources: [raw/01-articles/claude/2024-09-10 - Workspaces in the Anthropic API Console.md]
last_updated: 2026-06-28
---

## Summary

Anthropic introduced Workspaces in the [[AnthropicConsole]] to help developers efficiently manage multiple Claude deployments. Workspaces are unique environments that provide an abstraction layer for organizing resources and access controls.

## Key Features

**Workspace Capabilities:**
- Organize resources across different environments (development, staging, production)
- Streamline access controls for team members
- Set custom spend limits on a granular level
- Configure custom rate limits per workspace
- Manage multiple Claude deployments from a single organization interface

**Workspace-Scoped API Keys:**
- Each workspace can have dedicated API keys
- Keys are scoped to individual workspace environments
- Enables secure separation of credentials across deployments

## Use Cases

Workspaces are designed for developers using Claude across:
- Different deployment environments (dev, staging, production)
- Different use cases with distinct resource requirements
- Multiple teams or projects requiring separate access controls

## Availability

Workspaces became available to all Anthropic API users in the [[AnthropicConsole]]. Users can create a workspace at the Anthropic Console settings page. Additional guidance is available in the Anthropic Help Center.

## Related

- [[AnthropicConsole]] — the platform providing Workspace functionality
- [[Anthropic]] — the company introducing this feature
- [[AccessControl]] — security and permissions infrastructure enabled by workspaces
