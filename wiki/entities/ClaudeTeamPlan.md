---
title: "Claude Team Plan"
type: entity
tags: [claude, product, subscription, team-collaboration, anthropic]
sources: ["raw/01-articles/claude/2024-05-01 - Introducing the Claude Team plan and iOS app.md", "raw/01-articles/claude/2025-08-20 - Claude Code and new admin controls for business plans.md", "raw/01-articles/claude/2026-01-28 - Updates to Claude Team.md"]
last_updated: 2026-07-04
---

# Claude Team Plan

Claude Team Plan is a subscription offering from [[Anthropic]] enabling businesses to provide Claude access to multiple team members with shared workspace, increased usage limits, and team management tools.

## Key Information

- **Launch date:** May 2024
- **Pricing (at May 2024 launch):** $30 per user per month; superseded by the January 2026 pricing update below
- **Minimum:** 5 seats required
- **Creator:** [[Anthropic]]
- **Target market:** Teams and businesses needing collaborative AI capabilities

## Features

### Core Capabilities
- **Workspace management:** Teams can create shared workspaces with higher usage limits than individual plans
- **User management:** Tools for adding, removing, and managing team members
- **Billing management:** Centralized billing and seat management
- **Security & privacy:** Built with enterprise security and data privacy standards; protects sensitive business information

### Available Features (April 2025+)
- **Research:** In-depth agentic research across web and organizational sources via [[Research|Research capability]]
- **Google Workspace Integration:** Access to Gmail, Calendar, and Google Docs via [[GoogleWorkspaceIntegration|Google Workspace integration]]

### Available Features (August 2025+)
- **Premium seats:** Team plan admins can now upgrade users to premium seats that include [[ClaudeCode]], bundling conversational Claude and the coding agent in one subscription.
- **Extra usage:** Admins can enable extra usage at standard API rates with per-user spend caps for predictable billing.
- **Claude Code analytics:** Team plan includes Claude Code usage analytics alongside granular spend caps and self-serve seat management.

### Available Features (September 2025+)
- **Memory:** Persistent cross-conversation memory of professional context, project details, and preferences via [[ClaudeMemory|Claude Memory]]. Each project has its own isolated memory. Users can view and edit the memory summary in Settings. An [[IncognitoChat|Incognito chat]] mode is available for sessions that should not be saved to memory.

### Available Features (October 2025+)
- **Slack Connector:** Connect a [[Slack]] workspace so Claude can search channels, DMs, and shared files for context during conversations. Also enables the Claude app in Slack for in-channel AI assistance with web search, document analysis, and other capabilities. Admins enable the connector via the Claude directory; users configure it in the "Connectors" tab.

### Pricing Update (January 2026)

Prices lowered and annual discounts introduced: standard seats now $20/month (annual) or $25/month (monthly); premium seats now $100/month (annual) or $125/month (monthly), including 5x the usage of standard seats. Every seat still includes more usage than the Pro plan, and [[ClaudeCode]] is included with every seat regardless of tier. Admins can purchase additional capacity for power users beyond seat allowances.

### Available Features (March 2026+)
- **1M context for Claude Code:** Claude Code sessions on [[Claude4.6Opus|Opus 4.6]] now default automatically to the full 1M-token context window (previously extra usage), reducing compactions and keeping more conversation intact.
- **Auto mode:** Research preview of a new [[ClaudeCode]] permissions mode where a classifier screens tool calls, letting Claude act with fewer interruptions than the default while blocking destructive actions. See [[PermissionModes]].

### Planned Features (Coming Weeks)
- **Source citations:** Citations from reliable sources to verify AI-generated claims
- **Data repository integrations:** Direct integrations with codebases and CRM systems
- **Collaborative iteration:** Tools for teams to iterate together on AI-generated documents and projects
- **Enterprise security:** Highest standards of security and safety maintained throughout

## Strategic Value

The Team Plan represents [[Anthropic]]'s strategy to expand from individual users to enterprise teams by:
1. Enabling workflow customization based on team-specific needs
2. Providing centralized management and billing for organizations
3. Laying groundwork for integrations with enterprise tools and data sources
4. Addressing the need for secure, collaborative AI experiences

## Related

- [[Anthropic]] — creator and provider
- [[Research]] — Research capability available on Team plans
- [[GoogleWorkspaceIntegration]] — Google Workspace integration available on Team plans
- [[ClaudeMax]] — Premium individual plan
- [[ClaudeEnterprise]] — Enterprise plan for organizations
- [[ClaudeCode]] — Now bundled in premium seats for Team plan users (August 2025)
- [[summary-2024-05-01 - Introducing the Claude Team plan and iOS app]] — source article
- [[summary-2025-08-20 - Claude Code and new admin controls for business plans]] — premium seats announcement for Team plan
- [[ClaudeIOSApp]] — complementary mobile product announced simultaneously
- [[summary-2025-09-11 - Bringing memory to Claude]] — memory and incognito chat launch announcement
- [[ClaudeMemory]] — persistent cross-conversation memory feature
- [[IncognitoChat]] — private chat mode introduced with memory
- [[Slack]] — Slack connector available for Team plans (October 2025)
- [[summary-2026-01-28 - Updates to Claude Team]] — January 2026 pricing update
- [[summary-2025-10-01 - Claude and Slack]] — source article on the Slack integration
- [[PermissionModes]] — the permission-mode system auto mode belongs to
- [[summary-2026-03-13 - 1M context is now generally available for Opus 4.6 and Sonnet 4.6]] — 1M context GA announcement
- [[summary-2026-03-24 - Auto mode for Claude Code]] — auto mode research-preview announcement, first available on Team plan
