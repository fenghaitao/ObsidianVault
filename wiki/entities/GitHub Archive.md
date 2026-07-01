---
title: "GitHub Archive"
type: entity
tags: [data-source, github, benchmark, dataset]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260604 - SWE-rebench： Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius.md"]
last_updated: 2026-06-30
---

## Definition
GitHub Archive is a project that records and archives public GitHub activity. It is used by SWE-rebench as the primary data source for collecting pull requests and issues to build coding agent benchmark tasks.

## Key Information
- Used as the main source of pull requests and issues for large-scale projects in [[SWERebench]]
- GitHub API is used as a complementary source for smaller repositories
- 100% of pull requests are linked with some issues, providing an 8x larger dataset compared to using issues alone
- Enables collection of fresh, real-world software engineering tasks on a monthly cadence

## Related
- [[SWERebench]] — benchmark using GitHub Archive as data source
- [[GitHub]] — the platform being archived
- [[Nebius]] — company using GitHub Archive for benchmark construction
- [[summary-20260604 - SWE-rebench： Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius]] — source transcript
