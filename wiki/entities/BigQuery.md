---
title: "BigQuery"
type: entity
tags: [google-cloud, data-warehouse, analytics, enterprise]
sources: ["raw/01-articles/claude/2026-05-20 - How an Anthropic sales leader uses Claude Cowork to run a 4,000-account book.md"]
last_updated: 2026-07-07
---

## Definition

Google BigQuery is a fully-managed, serverless data warehouse and analytics platform on [[GoogleCloud|Google Cloud]]. In the context of [[ClaudeCowork]] sales workflows, it serves as a data source for token spend analysis and account-level usage metrics.

## Key Information

- **Provider**: [[GoogleCloud|Google Cloud Platform]]
- **Type**: Serverless data warehouse with built-in analytics and machine learning capabilities
- **Claude Cowork integration**: Used by [[TravisBryant]] in daily call prep (pulling token spend data) and weekly forecast rollups (pulling token spend alongside [[Salesforce]] opportunity data and internal documents) at [[Anthropic]].
- **Role in account propensity scoring**: One of three data sources (alongside [[Salesforce]] and deep web research) used by Claude Cowork to score each of 4,000 accounts overnight.

## Related

- [[GoogleCloud]] — the cloud platform
- [[ClaudeCowork]] — the product integrating BigQuery data
- [[Salesforce]] — complementary data source in sales workflows
- [[TravisBryant]] — sales leader using BigQuery in Cowork workflows
- [[summary-2026-05-20 - How an Anthropic sales leader uses Claude Cowork to run a 4,000-account book]] — source article
