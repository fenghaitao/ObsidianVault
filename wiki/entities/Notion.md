---
title: "Notion"
type: entity
tags: [platform, knowledge-management, integration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - The End of Apps — Kitze, Sizzy.co.md"]
last_updated: 2026-06-26
---

## Definition
Notion is a knowledge management platform that integrates with Manus AI via pre-configured connectors, enabling agents to read company policies, update pages, and process structured data within Notion workspaces. It is also a Braintrust customer that sends large volumes of unstructured trace data.

## Key Information
- Manus provides a Notion connector that works out of the box via a connector UID
- Demonstrated in an expense claims workflow: Manus read company policies from Notion, analyzed receipt images via OCR, and updated expense tracking pages
- Connectors are configured in the Manus web app and referenced by UID in API calls
- Enables internal deep research agents that reference company knowledge bases
- Accessible to anyone in a company who can edit Notion pages
- **Braintrust Customer**: Notion sends large volumes of unstructured trace data to Braintrust, exposing limitations in the original data architecture — specifically the need for full-text search across traces, which existing technologies (open-source data warehouse, BTQL, DuckDB) couldn't handle. This drove Braintrust's evolution toward a more capable data platform for traces.

## Related
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source (Manus connector)
- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — source (Braintrust customer)
- [[ManusAI]] — platform providing the connector
- [[Braintrust]] — eval/observability platform
- [[TraceDataChallenges]] — data problems surfaced by Notion's usage
- [[Agent Connectors]] — general connector concept
- [[ManusAPI]] — API that uses connector UIDs
