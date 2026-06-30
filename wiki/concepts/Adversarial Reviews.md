---
title: "Adversarial Reviews"
type: concept
tags: [ai, agents, code-review, quality, sub-agents, validation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick.md"]
last_updated: 2026-06-29
---

## Definition
Adversarial Reviews is a pattern where a separate AI agent (or sub-agent) with fresh, limited context reviews work done by another agent, specifically looking for issues. This addresses the confirmation bias problem where agents tend to validate their own work too favorably.

## Key Information
- Pattern discussed in Chris Parsons' workshop Q&A
- A dev agent develops code, a reviewer agent does an adversarial review with fresh context, the dev agent iterates on feedback
- The key insight: sub-agents start with only a small chunk of context, not the full conversation history, so they're not biased by having written the code
- "As soon as I changed mine to use sub-agents for the validation step, it started finding things" — workshop attendee observation
- Contrasts with same-context validation where the agent "just pats itself on the back and like, 'Yeah, you did good'"
- Claude Code's built-in `simplify` skill uses this pattern — it runs three sub-agents to find improvement opportunities in recent changes
- Can use different models for different perspectives to further reduce bias
- Generally catches more issues and increases confidence before shipping

## Related
- [[Confirmation Bias in Agents]] — the problem it addresses
- [[SubAgents]] — implementation mechanism
- [[Audience Simulation]] — related pattern for content
- [[ChrisParsons]] — discussed in his workshop
- [[Simplify]] — Claude Code skill using this pattern
- [[summary-20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick]] — source transcript
