---
title: "CodeReviewVelocity"
type: concept
tags: [code-review, productivity, software-engineering, developer-experience]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251223 - Developer Experience in the Age of AI Coding Agents – Max Kanat-Alexander, Capital One.md"]
last_updated: 2026-06-25
---

## Definition
Code Review Velocity is the speed and efficiency at which code reviews are conducted, encompassing both the iterative review cycle between a developer and an AI agent and the formal PR review process within a team.

## Key Information
- Writing code has become reading code; every software engineer is now primarily a code reviewer
- Agentic coding generates far more PRs than traditional development, making code review a bottleneck
- Two levels of code review velocity: (1) the iterative loop between developer and agent, and (2) the formal PR review process
- For both levels, the goal is fast individual responses, not shortened overall timelines (quality must be maintained)
- Common anti-pattern: broadcasting PR review requests to a team channel results in one person doing all reviews
- Solution: assign reviews to specific individuals with a distribution system and SLOs with enforcement mechanisms
- GitHub does not clearly indicate whose turn it is to take action in a review cycle; teams often resort to Slack messages
- The best code reviewers are often stuck in meetings doing strategy work instead of reviewing code and mentoring juniors
- Apprenticeship-based code review (seniors reviewing with juniors) is the only known effective method for teaching code review skills
- Low-quality, overwhelmed code reviews lead to rubber-stamp approvals and declining codebase quality

## Related
- [[summary-20251223 - Developer Experience in the Age of AI Coding Agents – Max Kanat-Alexander, Capital One]] — source transcript
- [[AICodingAgents]] — primary driver of increased PR volume
- [[DeveloperExperience]] — field concerned with review processes
- [[CodebaseTestability]] — related quality concern
- [[NoRegretsInvestments]] — code review improvement as a no-regrets investment
