---
title: "Salesforce"
type: entity
tags: [company, crm, enterprise-software, cloud]
sources: ["raw/01-articles/claude/2025-10-01 - Claude and Slack.md", "raw/01-articles/claude/2025-10-01 - How enterprises are driving AI transformation with Claude.md", "raw/01-articles/claude/2026-05-20 - How an Anthropic sales leader uses Claude Cowork to run a 4,000-account book.md"]
last_updated: 2026-07-07
---

## Definition

Salesforce is an enterprise cloud software company best known for its customer relationship management (CRM) platform. Salesforce is the parent company of [[Slack]], the business communication platform it acquired in 2021.

## Key Information

- **Industry**: Enterprise software, cloud computing, CRM
- **Notable subsidiary**: [[Slack]] (acquired 2021)
- **Relevance to Claude**: Salesforce's subsidiary Slack partnered with [[Anthropic]] in October 2025 to integrate Claude directly into Slack workspaces and as a Slack connector in Claude.ai. Rob Seaman (Chief Product Officer of Slack at Salesforce) described the integration as enabling an "agentic enterprise" where AI agents work alongside humans.
- **Agentforce Agents**: Salesforce integrated Claude models to power Agentforce Agents through Einstein 1 Studio, letting AI plan and execute on behalf of employees and customers. All Claude interactions flow through Salesforce's secure AI systems, with safeguards like dynamic grounding and toxicity detection via the Einstein Trust Layer. Customers deploy autonomous agents that orchestrate complete workflows end-to-end (analyzing data, executing transactions, updating records) without human intervention — described by Anthropic as a shift from AI-as-assistant to AI-as-autonomous-collaborator.
- Quote: *"Through our partnership with Anthropic, customers gain the flexibility to integrate their own LLMs, introducing Claude models with diverse levels of intelligence, speed, and cost-effectiveness. This empowers users to tailor their CRM applications to their unique requirements."* — Kaushal Kurapati, Senior Vice President of Product for AI at Salesforce.

- **Claude Cowork integration**: [[TravisBryant]] (Head of US Mid-Market GTM at [[Anthropic]]) uses Salesforce as a primary data source in [[ClaudeCowork]] sales workflows — pulling opportunity records and submitted commits from the Forecast tab for weekly forecast rollups, and account and pipeline data for overnight [[AccountPropensityScoring]] across a 4,000-account book. Salesforce data is combined with [[BigQuery]] spend data and deep web research to produce account scores and rationales.

## Related

- [[Slack]] — Salesforce subsidiary that integrated with Claude
- [[Anthropic]] — Partner for the Claude–Slack integration and Agentforce
- [[Integrations]] — Category of Claude connectors including the Slack connector
- [[Claude4.5Sonnet]] — model powering Agentforce Agents as of October 2025
- [[AIAgent]] — the autonomous-agent pattern Agentforce implements
- [[summary-2025-10-01 - Claude and Slack]] — Source article
- [[summary-2025-10-01 - How enterprises are driving AI transformation with Claude]] — Agentforce Agents case study
- [[ClaudeCowork]] — product using Salesforce as a data source for sales workflows
- [[TravisBryant]] — sales leader using Salesforce in Cowork workflows
- [[AccountPropensityScoring]] — AI-driven scoring methodology using Salesforce account data
- [[BigQuery]] — complementary data source in Cowork sales workflows
- [[summary-2026-05-20 - How an Anthropic sales leader uses Claude Cowork to run a 4,000-account book]] — source article for Cowork + Salesforce sales workflows
