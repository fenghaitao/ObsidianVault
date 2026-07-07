---
title: "Rakuten"
type: entity
tags: [company, e-commerce, claude-code, ai-adopter, agentic-coding]
sources: ["raw/01-articles/claude/2025-10-30 - Introduction to agentic coding.md", "raw/01-articles/claude/2025-12-01 - What are the key benefits of transitioning to agentic coding for software development.md", "raw/01-articles/claude/2026-01-21 - Eight trends defining how software gets built in 2026.md", "raw/01-articles/claude/2026-04-23 - Built-in memory for Claude Managed Agents.md", "raw/01-articles/claude/2026-06-09 - New in Claude Managed Agents run agents on a schedule and store environment variables in vaults.md"]
last_updated: 2026-07-07
---

## Definition

Rakuten is a company whose engineering team used [[ClaudeCode]] to autonomously implement a specific activation-vector extraction method in vLLM, an open-source library with 12.5 million lines of code across Python, C++, and CUDA.

## Key Information

- Claude Code completed the implementation in seven hours of sustained autonomous work.
- Achieved 99.9% numerical accuracy compared to the reference method.
- Kenta Naruse (Machine Learning Engineer): *"I didn't write any code during those seven hours, I just provided occasional guidance."*
- Yusuke Kaji (General Manager of AI for Business): *"You can have five tasks running in parallel by delegating four to Claude Code while focusing on the remaining one."*
- Also cited (April 2026) as a [[ClaudeManagedAgents]] customer shipping production agents "10x faster," separate from the earlier Claude Code/vLLM case study.
- The April 2026 memory-beta article specifies the use case behind that "10x faster" framing: Rakuten's task-based long-running agents use cross-session memory to learn from every session and avoid repeating past mistakes, cutting first-pass errors by 97%, within workspace-scoped, observable boundaries.
- Uses [[ScheduledDeployments|scheduled deployments]] (June 2026) to analyze spreadsheet data and produce reports and decks on a weekly or monthly schedule. Teams also monitor production logs and metrics, allowing product managers to see application health without creating a dashboard.

## Related

- [[ClaudeCode]] — the tool used for the vLLM implementation
- [[AgenticCoding]] — the practice this case study demonstrates
- [[summary-2025-10-30 - Introduction to agentic coding]] — source article
- [[summary-2025-12-01 - What are the key benefits of transitioning to agentic coding for software development]] — cross-referenced as a sustained-autonomy example
- [[summary-2026-01-21 - Eight trends defining how software gets built in 2026]] — cited in 2026 trends report
- [[ClaudeManagedAgents]] — production agents platform Rakuten also uses
- [[summary-2026-04-08 - Claude Managed Agents get to production 10x faster]] — customer mention
- [[summary-2026-04-23 - Built-in memory for Claude Managed Agents]] — memory public-beta article citing the 97% error-reduction figure
- [[AgenticMemory]] — concept page that also documents this same 97% statistic
- [[summary-2026-06-09 - New in Claude Managed Agents run agents on a schedule and store environment variables in vaults]] — scheduled deployments announcement citing Rakuten
- [[ScheduledDeployments]] — the scheduling feature used for reports and log monitoring
