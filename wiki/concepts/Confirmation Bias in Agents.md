---
title: "Confirmation Bias in Agents"
type: concept
tags: [ai, agents, bias, validation, quality, sub-agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick.md"]
last_updated: 2026-06-29
---

## Definition
Confirmation Bias in Agents is the tendency for AI agents to validate their own work too favorably when reviewing it in the same context they created it. The agent "pats itself on the back" rather than finding real issues, because it shares the same assumptions and blind spots from the creation context.

## Key Information
- Observed behavior: when an agent validates its own work in the same session/context, it tends to approve it uncritically
- "As soon as I changed mine to use sub-agents for the validation step, it started finding things" — workshop attendee
- Root cause: the agent shares the same context, assumptions, and reasoning that produced the code, so it can't see its own blind spots
- Solution: use sub-agents with fresh, limited context for validation — they don't have the creation bias
- Using different models for creation vs validation further reduces bias
- Claude Code's `simplify` skill uses three sub-agents to find issues, leveraging this principle
- Related to the broader pattern of Adversarial Reviews

## Related
- [[Adversarial Reviews]] — the solution pattern
- [[SubAgents]] — implementation mechanism
- [[ChrisParsons]] — discussed in his workshop
- [[Simplify]] — Claude Code skill using this principle
- [[Audience Simulation]] — related pattern for content
- [[summary-20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick]] — source transcript
