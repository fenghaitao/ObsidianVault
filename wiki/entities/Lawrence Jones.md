---
title: "Lawrence Jones"
type: entity
tags: [person, ai-engineering, incident-response, sre, speaker]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260517 - Fighting AI with AI — Lawrence Jones, Incident.md"]
last_updated: 2026-06-30
---

## Definition

Lawrence Jones is a founding engineer at incident.io, where he builds AI-powered SRE (Site Reliability Engineering) automation. He speaks on the practical challenges of building and debugging complex AI systems, advocating for using AI itself as the primary tool for understanding and improving AI products.

## Key Information

- **Role**: Founding engineer at [[IncidentIo]]
- **Product focus**: Building an AI SRE product that automates production investigations — running hundreds of telemetry queries, cross-referencing logs, metrics, traces, and historical incident data against codebases
- **Engineering philosophy**: AI systems have become too complex for humans to debug directly; the only scalable approach is to use AI in internal tooling to understand and improve AI products
- **Key patterns developed**:
  - Agent-accessible eval tooling (CLI tools for coding agents to interact with eval suites)
  - File system downloads of AI traces for agent debugging
  - Repeatable analysis pipelines with parallel sub-agents and cohort clustering
- **Previous talks**: Spoke at LDX (London Developer Experience) a year prior on core AI engineering constructs (prompts, evals, scorecards, traces, datasets, backtests)
- **Hiring**: incident.io is expanding its team in London following a significant fundraise

## Related

- [[summary-20260517 - Fighting AI with AI — Lawrence Jones, Incident]] — primary source (talk transcript)
- [[IncidentIo]] — company he co-founded
- [[Eval Red Green Cycle]] — pattern he described
- [[Agent-Ready Eval Tooling]] — CLI tool pattern from incident.io
- [[File System Downloads for Agent Debugging]] — debugging pattern from incident.io
- [[AI Analysis Pipelines]] — analysis pattern from incident.io
- [[Backtesting for AI Systems]] — evaluation pattern from incident.io
- [[ClaudeCode]] — coding agent used in incident.io's workflow
