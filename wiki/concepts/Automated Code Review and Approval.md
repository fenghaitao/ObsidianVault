---
title: "Automated Code Review and Approval"
type: concept
tags: [code-review, automation, agents, quality-assurance, intercom, compliance]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260515 - How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom.md"]
last_updated: 2026-06-30
---

## Definition
Automated Code Review and Approval is the practice of using AI agents to review pull requests and automatically approve them when confidence is high enough. Intercom achieved a 17.6% auto-approval rate using backtesting against historical data with human-labeled outputs, and worked with auditors to ensure SOC 2, ISO 27001, and HIPAA compliance without requiring humans in the loop.

## Key Information
- Intercom reached 17.6% auto-approval rate for pull requests
- Not simple "Claude, approve this" — detailed work using backtesting and human-labeled outputs to build confidence
- Shaped pull requests toward very safe and simple changes that should have always been auto-approved
- Worked with auditors to confirm SOC 2, ISO 27001, HIPAA compliance is achievable without humans in the loop
- Key requirement: know exactly what you're doing and have auditing controls in place
- Uses multimodal code reviews including Codex — "multimodal code reviews are okay"
- Believes automated review is removing risk, not adding it — humans aren't as good as well-defined agents
- Emerged as a solution to code review becoming the new bottleneck after AI dramatically increased PR throughput
- Confidence level shaped by backtesting against prior data with human-labeled outputs

## Related
- [[summary-20260515 - How Building with AI Can Double the Throughput of Your Engineering Team — Brian Scanlan, Intercom]] — source
- [[Intercom]] — company implementing it
- [[AgentReviewerApprover]] — related pattern in Paperclip
- [[Doubling Engineering Throughput]] — context where it emerged as a bottleneck solution
- [[Codex]] — used for multimodal code review
- [[CodeReviewAmplification]] — the problem it addresses
- [[CodeReviewVelocity]] — related concept
- [[SOC 2]] — compliance certification
- [[ISO 27001]] — compliance certification
- [[HIPAA]] — compliance certification
- [[Backtesting Agent Skills]] — methodology used to validate auto-approval
