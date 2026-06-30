---
title: "Backtesting Agent Skills"
type: concept
tags: [agent-skills, validation, testing, quality-assurance, intercom]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260515 - How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom.md"]
last_updated: 2026-06-30
---

## Definition
Backtesting Agent Skills is the practice of validating agent skills against historical data — past code changes, incidents, and work artifacts — to measure and improve skill quality before deployment. Intercom uses this methodology to prove that skills operate at extremely high quality, including for automated code review where human-labeled historical outputs build confidence in auto-approval decisions.

## Key Information
- Uses historical work data: code changes, incidents, and past work artifacts
- Applied to validate skill quality before and during deployment
- For automated code review: backtesting with human-labeled outputs builds confidence in auto-approval
- Part of the Skills Flywheel: backtesting feeds into continuous improvement
- Combined with session transcript data pulled into S3 for analysis
- Enables data-driven skill development rather than manual authoring
- Example: flaky spec fixing skill was built through iterative feedback loops with the agent, not manually authored — the agent discovered patterns through guided iteration
- Used to shape pull requests toward safe, simple changes that should have always been auto-approved

## Related
- [[summary-20260515 - How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom]] — source
- [[Skills Flywheel]] — the broader improvement cycle
- [[Automated Code Review and Approval]] — application of backtesting
- [[Agent Skills]] — the skills being backtested
- [[Intercom]] — company using backtesting
- [[BrianScanlan]] — architect of the approach
- [[ContinuousImprovement]] — underlying methodology
