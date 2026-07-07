---
title: "MCPConnector"
type: concept
tags: [anthropic, api, mcp, model-context-protocol, integration, agents]
sources: [raw/01-articles/claude/2025-05-22 - New capabilities for building agents on the Anthropic API.md, raw/01-articles/claude/2026-06-08 - Observability for developers building connectors.md, raw/01-articles/claude/2026-06-18 - Centrally manage authorization for MCP connectors.md]
last_updated: 2026-07-07
---

# MCP Connector

The MCP connector is an [[Anthropic]] API feature that automatically manages Model Context Protocol (MCP) server connections, enabling Claude to connect to remote MCP servers without requiring custom client code.

## Definition

The MCP connector handles all aspects of connecting Claude to remote MCP servers within the API:
- Automatic connection management to specified MCP servers
- Tool discovery from connected servers
- Agentic reasoning about which tools to call
- Automatic error handling and authentication
- Integrated response with enhanced data

## How It Works

When Claude receives an API request with MCP servers configured, the connector:
1. Connects to specified MCP servers
2. Retrieves available tools from those servers
3. Reasons about what tool to call and arguments to pass
4. Executes tool calls agentively until sufficient results achieved
5. Manages authentication and error handling
6. Returns enhanced response with integrated data

## Key Benefits

- **Simplified Integration:** Eliminates need to build custom MCP client harnesses
- **Automatic Management:** Handles connection, tool discovery, and error handling
- **Agentic Execution:** Claude automatically determines when and how to use tools
- **Ecosystem Access:** Connect to growing ecosystem of remote MCP servers

## Available MCP Servers

The connector works with remote MCP servers including:
- [[Zapier]] — automation and workflow integration
- [[Asana]] — work management and task tracking

Hundreds of additional connectors available at claude.com/connectors.

## Contrast with Claude Code MCP

[[ModelContextProtocol|MCP in Claude Code]] requires local configuration:
- [[MCPConnector|API MCP connector]] handles remote servers automatically in API requests
- Claude Code MCP requires `.mcp.json` configuration and manual server management
- API connector eliminates custom client code requirement

## Connector Observability Dashboard (June 2026)

In June 2026, [[Anthropic]] launched a public beta [[ConnectorObservability|observability dashboard]] for published connectors, enabling developers to monitor their connectors' performance across all Claude product surfaces. The dashboard tracks key metrics including error rates and latency.

The same launch also enabled **in-app connector directory submission**: developers can submit their [[ModelContextProtocol|MCP]] servers to the directory directly within Claude's Organization Settings, without a separate submission flow.

Key details:
- Found in Claude under **Directory** in **Organization Settings**.
- Requires Admin or Owner access on a Team or Enterprise plan.
- Enterprise Owners can delegate via custom roles with Directory management or Libraries permission.
- Over 300 third-party connectors in the directory, used by millions daily.

## Enterprise-Managed Authorization (June 2026)

In June 2026, [[Anthropic]] launched [[EnterpriseManagedAuthorization|Enterprise-Managed Authorization (EMA)]], allowing admins to provision MCP connectors for their entire organization through their identity provider (starting with [[Okta]]). Users inherit connector access through IdP groups and roles, achieving zero-touch connector setup.

Key details:
- Admins authorize a connector once; users get access automatically on first login.
- Access is consistent across Claude chat, [[ClaudeCode|Claude Code]], and [[ClaudeCowork|Cowork]].
- Admins can require connectors to only connect through the IdP, preventing personal account linking.
- Frictionless revocation: short-lived access tokens expire quickly when users are deprovisioned.
- Built on an open [Enterprise-Managed Authorization extension](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization) to MCP.
- MCP providers supporting EMA at launch: [[Asana]], [[Atlassian]], [[Canva]], [[Figma]], [[Granola]], [[Linear]], [[Supabase]] ([[Slack]] coming soon).
- Available in beta for Claude Team and Enterprise plans.

## Use Cases

- **Workflow automation:** Connect to Asana, Zapier, and other workflow tools
- **Data integration:** Access external databases and services through MCP
- **Multi-system coordination:** Connect to multiple services within single agent workflow
- **Tool-enhanced agents:** Build agents with access to comprehensive tool ecosystems
- **Enterprise provisioning:** Deploy connectors organization-wide via IdP-based EMA

## Availability

- [[Anthropic]] API (beta)
- Works with [[Claude4Opus]] and [[Claude4Sonnet]]

## Related

- [[Anthropic]] — API provider
- [[ModelContextProtocol]] — the protocol standard
- [[AIAgent]] — agents using MCP connector for tool access
- [[ToolUse]] — related tool-calling capability
- [[Asana]] — available remote MCP server
- [[Zapier]] — available remote MCP server
- [[Claude4Opus]] — model with MCP connector support
- [[Claude4Sonnet]] — model with MCP connector support
- [[summary-2025-05-22 - New capabilities for building agents on the Anthropic API]] — announcement article
- [[summary-2026-06-08 - Observability for developers building connectors]] — observability dashboard and in-app submission announcement
- [[ConnectorObservability]] — the observability dashboard for published connectors
- [[summary-02 - Enterprise-managed auth for MCP connectors]] — product-launch teaser for enterprise-managed authentication on MCP connectors
- [[summary-2026-06-18 - Centrally manage authorization for MCP connectors]] — full EMA launch announcement
- [[EnterpriseManagedAuthorization]] — the enterprise auth mechanism for MCP connectors
- [[Okta]] — first identity provider for EMA
- [[LegalAI]] — legal-industry use of MCP connectors (20+ new connectors, May 2026)
