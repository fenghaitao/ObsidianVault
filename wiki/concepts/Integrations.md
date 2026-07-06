---
title: "Integrations"
type: concept
tags: [integrations, mcp, feature, claude-ai, productivity]
sources: [raw/01-articles/claude/2025-05-01 - Claude can now connect to your world.md, raw/01-articles/claude/2025-10-16 - Claude and your productivity platforms.md, raw/01-articles/claude/2026-01-26 - Your favorite work tools are now interactive connectors inside Claude.md, raw/01-articles/claude/2026-04-23 - New connectors in Claude for everyday life.md]
last_updated: 2026-07-04
---

# Integrations

**Integrations** are a feature enabling [[Claude.ai]] users to connect their apps and tools directly to Claude, allowing the AI assistant to gain deep context about user work and take actions across multiple platforms. Integrations use [[ModelContextProtocol|remote MCP servers]] to securely connect Claude to third-party services.

## Definition

Integrations provide users with a curated set of pre-built, pre-configured remote [[ModelContextProtocol|MCP]] servers. When enabled, they allow Claude to:
- Access data and context from connected applications
- Search across user data using [[Research|advanced Research mode]]
- Take actions and create content within connected platforms
- Understand project histories, task statuses, and organizational knowledge

## Key Characteristics

- **User-driven**: Users can discover and connect any number of integrations to Claude
- **Remote-first**: Integrations use remote MCP servers rather than requiring local installation
- **Integrated experience**: Works seamlessly across web and desktop apps
- **Pre-built**: Developers create and host integration servers; users choose which to enable
- **Easy development**: Developers can create custom integrations in as little as 30 minutes using Anthropic's documentation

## Available Integrations (as of May 2025)

Initial set includes major platforms:
- **Atlassian**: Jira (task management), Confluence (documentation)
- **Zapier**: Connects thousands of apps through pre-built workflows
- **Cloudflare**: CDN and infrastructure management
- **Intercom**: Customer communication and feedback
- **Asana**: Project and task management
- **Square**: Point-of-sale and payments
- **Sentry**: Error tracking and monitoring
- **PayPal**: Payments and financial services
- **Linear**: Issue and project tracking
- **Plaid**: Financial data and account linking

Additional integrations in development from Stripe, GitLab, Box, and others.

## Slack Integration (October 2025)

The **[[Slack]] connector** (October 2025) allows Claude to search a user's Slack workspace — channels, DMs, and shared files — during conversations and research sessions. This is a bidirectional integration:

- **Claude in Slack**: Claude is added as an app to a Slack workspace (via Slack Marketplace), enabling in-channel and in-thread assistance with full Claude capabilities.
- **Slack connector in Claude**: Slack is connected as a data source in Claude.ai, so Claude can pull workspace context into any conversation.

Availability: Claude Team and Enterprise at launch; expanded to Claude Pro and Max on January 26, 2026.

## Microsoft 365 Connector (October 2025)

A connector (via the [[ModelContextProtocol|MCP connector]]) gives Claude access to [[Microsoft]] 365 as a data source — the reverse direction from [[Microsoft365Copilot]], where Claude is instead a model option inside Microsoft's own Copilot product:

- **SharePoint and OneDrive**: search and analyze documents across sites and libraries without manual upload.
- **Outlook**: access email threads and analyze communication patterns for project status, client feedback, or team alignment.
- **Teams**: search chat conversations, channel discussions, and meeting summaries to surface decisions and track updates.

Available for all Claude Team and Enterprise plan customers; admins must enable the connector before individual users authenticate.

## Enterprise Search (October 2025)

[[EnterpriseSearch]] is a dedicated, company-branded shared project that searches across *all* of an organization's connected data sources in one place (rather than one tool at a time), personalized with the company's name and custom prompts. Available to all Team and Enterprise organizations once an admin sets it up and curates data sources.

## MCP Apps: Interactive Connectors (January 2026)

**MCP Apps**, an official MCP extension, lets integrations render a live, interactive UI directly inside a Claude conversation instead of only exchanging data/actions in the background — building Asana project timelines, drafting/sending formatted Slack messages, or visualizing Figma diagrams without tab-switching. Available for Asana, Slack, and Figma at launch (Salesforce/Agentforce 360 planned), across Claude mobile, web, desktop (Free through Enterprise) and [[ClaudeCowork|Claude Cowork]]. Since MCP Apps is a protocol extension rather than a Claude-only feature, any MCP-supporting AI product can adopt it. See [[ModelContextProtocol]].

## Everyday-Life Connectors (April 2026)

Starting April 23, 2026, Claude expanded connectors beyond work tools to apps used throughout the week: AllTrails, Audible, Booking.com, Instacart, Intuit Credit Karma, Intuit TurboTax, Resy, Spotify, StubHub, Taskrabbit, Thumbtack, Tripadvisor, Uber, Uber Eats, and Viator, with more planned. The Claude connector directory (launched July 2025) has grown to 200+ connectors spanning design, finance, productivity, and health apps used daily by millions.

Key changes accompanying this expansion:
- **Dynamic, contextual surfacing**: Claude now suggests the right connector mid-conversation based on what the user is doing (e.g., a weekend-hike request surfaces AllTrails results, refinable conversationally — "shorter," "more scenic," "dog-friendly" — without leaving the thread). When multiple connected apps could help, Claude shows them all, ranked by usefulness — never by paid placement; Claude remains ad-free with no sponsored answers.
- **User control over data**: connecting a service grants Claude access on the user's behalf; that app's data isn't used to train Anthropic's models, the app can't see the user's other Claude conversations, and users can disconnect at any time.
- **Confirmation before action**: Claude is designed to check with the user before booking or purchasing anything on their behalf.
- **Availability**: all Claude plans, with mobile in beta. Full list at claude.ai/directory/connectors; third parties can submit their product for inclusion.

## Use Cases

### Example: Zapier Integration
Claude can access thousands of apps through Zapier's pre-built workflows, automating processes across software stacks. For instance, Claude can automatically pull sales data from [[HubSpot]] and prepare meeting briefs based on calendar information.

### Example: Atlassian Integration
With Jira and Confluence connections, Claude can:
- Collaborate on building new products
- Manage tasks more effectively
- Scale work by summarizing and creating multiple pages and work items simultaneously

### Example: Intercom Integration
Connect Intercom to enable faster response to user feedback. [[Intercom]]'s AI agent Fin can take actions like filing bugs in [[Linear]] when users report issues, managing the entire workflow from feedback to bug resolution in a single conversation.

## Integration with Research

[[Research|Advanced Research mode]] can search across any connected integration in addition to the web and [[GoogleWorkspaceIntegration|Google Workspace]]. This allows Claude to conduct comprehensive investigations using internal organizational data alongside external sources.

## Availability

As of May 2025:
- Integrations in beta on Max, Team, and Enterprise plans
- Coming soon to Pro plan
- Web platform: Claude.ai

## Related

- [[ModelContextProtocol]] — Underlying protocol enabling integrations
- [[Research]] — Capability that searches across integrated data sources
- [[Claude.ai]] — Platform providing integrations to users
- [[ToolUse]] — Underlying mechanism for integration tool invocation
- [[GoogleWorkspaceIntegration]] — Example integration with organizational data
- [[Slack]] — Communication platform added as a connector in October 2025
- [[summary-2025-10-01 - Claude and Slack]] — Source article on the Slack integration
- [[Microsoft]] — Productivity suite added as a connector in October 2025
- [[Microsoft365Copilot]] — the inverse integration (Claude embedded inside Microsoft's own product)
- [[EnterpriseSearch]] — cross-tool search capability introduced alongside the Microsoft 365 connector
- [[summary-2025-10-16 - Claude and your productivity platforms]] — Source article on the Microsoft 365 connector and enterprise search
- [[ClaudeCowork]] — product now supporting MCP Apps
- [[summary-2026-01-26 - Your favorite work tools are now interactive connectors inside Claude]] — MCP Apps announcement
- [[Intuit]] — Credit Karma and TurboTax connectors added in the April 2026 everyday-life expansion
- [[summary-2026-04-23 - New connectors in Claude for everyday life]] — announcement of the everyday-life connector expansion
