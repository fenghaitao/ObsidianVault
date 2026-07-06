---
title: "Research"
type: concept
tags: [capability, feature, search, agentic]
sources: [raw/01-articles/claude/2025-04-15 - Claude takes research to new places.md, raw/01-articles/claude/2026-01-23 - Building multi-agent systems When and how to use them.md]
last_updated: 2026-07-04
---

# Research

Claude's **Research** capability allows the model to conduct in-depth research by searching across the web and integrated organizational sources (via [[GoogleWorkspaceIntegration|Google Workspace]]) to deliver comprehensive answers in minutes.

## Characteristics

Research operates **agentically**, conducting multiple searches that build on each other while determining what to investigate next. The model:

- Explores different angles of a question automatically
- Works through open questions systematically
- Delivers thorough answers with easy-to-check citations
- Balances speed and quality for practical knowledge work
- Can conduct complex research for up to 45 minutes, with most reports completing in 5-15 minutes

## Advanced Research Mode

An advanced Research mode enables deeper investigations across hundreds of internal and external sources. Claude breaks down complex requests into smaller parts, investigating each deeply before compiling comprehensive reports—work that would typically take hours of manual research.

## Data Sources for Research

Claude can search across multiple data sources:

### Google Workspace
When combined with [[GoogleWorkspaceIntegration|Google Workspace integration]], Claude can access:
- Email (Gmail)
- Calendar events
- Organizational documents (Google Docs)

### Web Search
Web search is available globally on all [[Claude.ai]] paid plans, enabling access to current information across the internet.

### Custom Integrations
With [[Integrations]], Claude can search any application the user connects, allowing research to incorporate data from custom and third-party tools and services.

This eliminates the need to manually upload files or repeatedly provide context about work and schedule.

## Enterprise Cataloging

For [[ClaudeEnterprise|Claude Enterprise]] users, **cataloging** enables specialized indexing of organizational documents. This employs [[RetrievalAugmentedGeneration|Retrieval Augmented Generation (RAG)]] techniques to find information even when:
- Information is buried in lengthy documents
- Knowledge is scattered across multiple files
- Exact file paths are unknown

Enterprise-grade security keeps data within the organization's control.

## Multi-Agent Architecture

Research is cited as an example of the parallelizable-tasks pattern in [[MultiAgentSystem|multi-agent systems]]: a lead agent decomposes a query into independent facets and runs subagents concurrently, each researching independently before the lead agent synthesizes results — improving coverage/thoroughness at the cost of higher token usage versus a single agent.

## Availability

As of May 2025:
- **Integrations and advanced Research**: Beta on Max, Team, and Enterprise plans; coming soon to Pro
- **Web search**: Globally available on all [[Claude.ai]] paid plans

Users toggle on the Research setting in chat to enable it.

Historical availability (April 2025):
- Early beta: Max, Team, and Enterprise plans
- Available in: United States, Japan, Brazil

## Related

[[Integrations]] — Custom tool integrations that Research can search across
[[GoogleWorkspaceIntegration]] — Integration with Gmail, Calendar, and Google Docs  
[[RetrievalAugmentedGeneration]] — Pattern underlying enterprise cataloging  
[[ClaudeEnterprise]] — Enterprise product with advanced research and cataloging  
[[ToolUse]] — Underlying capability enabling agentic search operations
[[ModelContextProtocol]] — Protocol enabling integrations that Research can access
[[MultiAgentSystem]] — the parallel-subagent architecture underlying Research
[[summary-2026-01-23 - Building multi-agent systems When and how to use them]] — cites Research as a parallelizable-tasks example
