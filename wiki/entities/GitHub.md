---
title: "GitHub"
type: entity
category: platform
tags: [platform, code-hosting, version-control, microsoft, agent-integration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps.md"]
last_updated: 2026-06-29
---

## Definition
GitHub is a code hosting and version control platform. In the context of n8n agent workflows, GitHub issues and PRs are mentioned as use cases for sub-agents. In Demand-Driven Context, GitHub is the preferred storage location for curated knowledge bases.

## Key Information

- **Agent Use Case**: GitHub issues and PR management via specialized sub-agents
- **Human-in-the-Loop Pattern**: Agent scans code, drafts messages to contributors, but routes through human review before sending — "I don't want to AI message co-workers or clients or anything without seeing it first"
- **Enterprise Git Integration**: n8n enterprise plans include git integration for workflow versioning with dev/staging/prod environments
- **MCP Server**: GitHub provides an MCP server for interacting with the GitHub API (pull requests, issues), though it reportedly ships ~200K tokens on handshake
- **Demand-Driven Context**: Raj prefers GitHub repositories as the storage location for curated knowledge bases because GitHub provides built-in PR processes, review workflows, and conflict resolution for multi-agent, multi-team contributions. Curated knowledge can also be published to Confluence or Slack from GitHub. The file structure of the knowledge base serves as a meta model for agent navigation.

## Related

- [[n8n]] — platform for GitHub agent workflows
- [[Jira]] — alternative ticketing system for sub-agents
- [[summary-20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle]] — source
- [[summary-20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure]] — source
- [[Sub-agent Orchestration]] — pattern for GitHub issues sub-agent
- [[MCP]] — GitHub MCP server
- [[HumanInTheLoopWorkflows]] — review before messaging contributors
- [[Demand-Driven Context]] — methodology using GitHub for knowledge storage
- [[Meta Model]] — file structure as navigation map
- [[Knowledge Curation]] — agents curating knowledge into GitHub repos
