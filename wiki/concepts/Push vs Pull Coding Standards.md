---
title: "Push vs Pull Coding Standards"
type: concept
tags: [ai, coding-standards, agents, code-review, skills]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock.md"]
last_updated: 2026-06-29
---

## Definition
Push vs Pull describes two strategies for enforcing coding standards on AI agents. Push means always sending coding standards to the agent (e.g., via Claude.md). Pull means letting the agent retrieve standards via skills only when needed. Matt Pocock recommends pull for implementers and push for automated reviewers.

## Key Information
- Push: instructions are always sent to the agent. Example: putting "talk like a pirate" in Claude.md pushes that instruction to every session
- Pull: the agent has access to skills with description headers that say "you may pull this when you want to." The agent decides when to retrieve the information
- Pocock's recommendation: use pull for implementers (let them pull coding standards via skills when they have questions) and push for automated reviewers (push the full coding standards so the reviewer can compare code against them)
- This separation means implementers don't waste tokens on standards they don't need, while reviewers have full context to evaluate compliance
- Pocock uses Sonnet for implementation (where pull is used) and Opus for reviewing (where push is used), because reviewing needs more "smarts"
- Skills are the primary pull mechanism: they sit in the repo with description headers

## Related
- [[summary-20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock]] — source transcript
- [[MattPocock]] — advocates this approach
- [[Skills]] — the pull mechanism
- [[AgentReviewerApprover]] — where push is used
- [[Ralph Loop]] — where pull is used for implementers
- [[Sandcastle]] — implements this pattern with separate implementer and reviewer agents
- [[ClaudeCode]] — where Claude.md provides push
- [[AgentsDotMd]] — push mechanism
