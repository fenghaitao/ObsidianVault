---
title: "IncidentIo"
type: entity
tags: [company, incident-response, sre, ai, platform]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260517 - Fighting AI with AI — Lawrence Jones, Incident.md"]
last_updated: 2026-06-30
---

## Definition

incident.io is an incident response management platform used by companies like Netflix, Etsy, and Skyscanner. The platform pages teams when things go wrong, helps run incidents, and facilitates customer communication during outages. The company is building toward fully automated production investigations using AI.

## Key Information

- **Domain**: Incident response management and AI-powered SRE automation
- **Customers**: [[Netflix]], Etsy, Skyscanner, and many others
- **AI product**: Automated production investigations that run hundreds of telemetry queries across logs, metrics, traces, and historical incident data, cross-referenced against the codebase
- **Tech stack**: All AI work is done in Go, with prompts and evals living in YAML files alongside Go code
- **AI system complexity**: Their chatbot involves 10+ agents and 50+ tools; their investigation system unpacks into hundreds of prompts and tool calls per investigation
- **Scale**: Runs thousands of investigations daily across hundreds of customer accounts
- **Founded by**: [[Lawrence Jones]] (founding engineer) and team
- **Location**: London, UK
- **Funding**: Completed a significant fundraise and is actively hiring to expand the engineering team

## Related

- [[summary-20260517 - Fighting AI with AI — Lawrence Jones, Incident]] — primary source
- [[Lawrence Jones]] — founding engineer and speaker
- [[Eval Red Green Cycle]] — eval workflow used at incident.io
- [[AgentReady Eval Tooling]] — CLI tool pattern from incident.io
- [[File System Downloads for Agent Debugging]] — debugging pattern from incident.io
- [[AI Analysis Pipelines]] — analysis pattern from incident.io
- [[Backtesting for AI Systems]] — evaluation pattern from incident.io
- [[Netflix]] — customer
