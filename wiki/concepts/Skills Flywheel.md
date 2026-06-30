---
title: "Skills Flywheel"
type: concept
tags: [agent-skills, continuous-improvement, backtesting, intercom, claude-code]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260515 - How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom.md"]
last_updated: 2026-06-30
---

## Definition
The Skills Flywheel is Intercom's approach to building and continuously improving agent skills through a feedback loop: write skills, use backtesting against historical data to validate quality, collect session data for analysis, and iteratively improve. The goal is to create small, high-quality, durable, testable skills that do one job extremely well and become self-updating over time.

## Key Information
- Encapsulates knowledge in engineering captures, skills, guidance, and hooks
- Focus on small, high-quality, durable, testable skills
- Uses backtesting against historical work (code changes, incidents) to validate skill quality
- Continuous improvement: skills become self-updating and increasingly high quality
- All session transcripts pulled into S3 for data mining and skill effectiveness analysis
- Internal Claude Code plugins pushed to all laptops, bypassing update mechanisms
- Hundreds of contributors, tens of thousands of lines of code in Claude Code plugins
- Skill invocation tracked via Honeycomb observability
- Example: flaky spec fixing skill built through feedback loops — the agent wrote the skill through guided iteration, not manual authoring
- Uses progressive disclosure and well-organized lookup tables for skill organization
- Everyone contributes to the flywheel: when an agent hits an issue or goes down the wrong path, update the guidance
- Avoid building everything in-house — use what others ship to avoid getting stuck behind the curve

## Related
- [[summary-20260515 - How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom]] — source
- [[Intercom]] — company implementing the flywheel
- [[BrianScanlan]] — architect of the approach
- [[Agent Skills]] — the skills being improved
- [[ContinuousImprovement]] — underlying methodology
- [[Backtesting Agent Skills]] — validation methodology
- [[ClaudeCode]] — platform where skills run
- [[Honeycomb]] — observability tool for skill tracking
- [[AmazonS3]] — session transcript storage
- [[ProgressiveDisclosure]] — skill organization technique
