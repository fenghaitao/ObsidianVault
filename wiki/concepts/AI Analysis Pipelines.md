---
title: "AI Analysis Pipelines"
type: concept
tags: [analysis, agents, pipelines, parallelism, clustering, observability]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260517 - Fighting AI with AI — Lawrence Jones, Incident.md"]
last_updated: 2026-06-30
---

## Definition

AI analysis pipelines are structured, repeatable workflows where coding agents systematically analyze batches of AI system outputs using parallel sub-agents and cohort clustering. They transform raw accuracy metrics (e.g., "86% accurate RCA") into actionable reports that explain why performance changed and what to fix.

## Key Information

- **Origin**: Developed at [[IncidentIo]] to move beyond aggregate accuracy numbers from backtests and understand why their AI SRE system performed well or poorly on specific customer accounts
- **Pipeline structure**:
  1. **Download phase**: Batch-download investigations or interactions as [[File System Downloads for Agent Debugging|file systems]]
  2. **Parallel analysis**: Spin up ~25 parallel sub-agents, each analyzing one investigation independently
  3. **Cohort clustering**: Aggregate individual analyses and cluster failures into groups sharing common failure modes
  4. **Meta-analysis**: Identify patterns across cohorts — what types of failures are most common, which customer accounts are most affected
  5. **Codebase integration**: Cross-reference findings with the codebase to identify specific code locations and suggest fixes
- **Incremental storage**: All analysis is stored in files within the downloaded directories, enabling pause-and-resume and incremental refinement
- **Runbook-driven**: The pipeline is guided by a markdown playbook (stored in a repo called "scrapbook") that specifies each stage, expected outputs, and decision criteria — making the process repeatable and reliable
- **Key design principles**:
  - Leverage sub-agents for parallel per-entity analysis
  - Store all intermediate analysis in files for resumability
  - Combine analysis with codebase access so findings lead directly to fixes
  - End with the ability to make changes and verify via [[Eval Red Green Cycle]]
- **Output**: A report that explains not just "accuracy went from 84% to 86%" but which failure modes drove the change, on which accounts, and what code changes would address the gaps
- **Generalizability**: Lawrence Jones states this pattern "generalizes really well for anyone building this type of thing"

## Related

- [[summary-20260517 - Fighting AI with AI — Lawrence Jones, Incident]] — primary source
- [[File System Downloads for Agent Debugging]] — prerequisite for the download phase
- [[Parallel Agents]] — sub-agent parallelism pattern
- [[Eval Red Green Cycle]] — verification step after pipeline-identified fixes
- [[Backtesting for AI Systems]] — the data source for analysis pipelines
- [[IncidentIo]] — company that developed this pattern
- [[AgentObservability]] — prerequisite for generating analysis data
- [[SubAgent Orchestration]] — related orchestration pattern
- [[FailureModeAnalysis]] — analysis methodology
