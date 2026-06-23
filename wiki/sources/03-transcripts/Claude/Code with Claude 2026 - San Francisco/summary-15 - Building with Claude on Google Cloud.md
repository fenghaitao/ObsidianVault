---
title: "Building with Claude on Google Cloud"
type: source
tags: [google-cloud, claude-code, MCP, deployment, enterprise, workshop]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - San Francisco/15 - Building with Claude on Google Cloud.md]
last_updated: 2026-06-23
---

## Core Summary

Ivan Nardini from Google Cloud demonstrates an end-to-end workflow for building and deploying applications with Claude Code on Google Cloud, wearing five different persona hats (PM, UX designer, software engineer, security engineer, data analyst). The session showcases Claude Code's plan mode, MCP server integration for Google Cloud documentation (Developer Knowledge API), Google Cloud Skills for deployment, sub-agents for parallel implementation, and built-in security review. The demo builds a live feedback application deployed on Cloud Run with Firestore and BigQuery, demonstrating how non-Google Cloud experts can deploy production applications using Claude's agentic capabilities.

## Key Points

- **Five personas, one tool:** PM (wireframe from sketch), UX designer (plan mode with Figma MCP), software engineer (architecture design via documentation MCP + skills for Cloud Run/Firestore deployment), security engineer (built-in security review), data analyst (BigQuery MCP + Looker dashboard).
- **ADC setup:** Application Default Credentials automatically find user credentials; Claude Code wizard detects project, region, and available models.
- **Google Cloud advantages:** Per-token pricing (no message caps), provisioned throughput for production, no API key rotation, data stays in project, multiple regional endpoints, high availability SLAs.
- **Developer Knowledge API MCP:** Fresh Google Cloud documentation directly consumable by Claude Code for architecture design without prior GCP knowledge.
- **Google Cloud Skills:** Pre-built skills for specific deployment tasks (deploy on Cloud Run, connect to Firestore) complementing the architecture-level MCP server.
- **Sub-agents for parallel implementation:** Three sub-agents spun up simultaneously for API, ingestion pipeline, and dashboard — mirroring a team sprint.
- **Agent Platform:** Google Cloud's agent registry listing all natively supported MCP servers (Developer Knowledge, BigQuery) with tool descriptions and observability.
- **MCP Toolbox:** Open-source MCP server with Looker integration for dashboard creation from BigQuery data.

## Related

- [[ClaudeCode]] — the tool used throughout
- [[ModelContextProtocol]] — MCP servers for GCP documentation and BigQuery
- [[ClaudeCodeSkills]] — Google Cloud Skills for deployment
- [[ClaudeCodeSubagents]] — parallel implementation pattern
- [[GoogleCloud]] — the cloud platform
