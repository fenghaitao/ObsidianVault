---
title: "Reversible Without Embarrassment"
type: concept
tags: [ai, agents, autonomy, safety, decision-making]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick.md"]
last_updated: 2026-06-29
---

## Definition
"Reversible Without Embarrassment" is Chris Parsons' core rule for determining what AI agents are allowed to do autonomously. If an action can be reversed without causing embarrassment to the human, the AI can do it. If not, the AI should prepare the work for human review instead.

## Key Information
- Chris Parsons' fundamental rule for agent autonomy
- Examples of allowed actions (reversible): creating slide decks, drafting emails, writing code in sandboxed projects
- Examples of disallowed actions (not reversible without embarrassment): sending emails, posting on LinkedIn, sending messages, running production database migrations
- The AI can draft replies and prepare everything for review, but the human makes the final send decision
- Parsons describes his role as becoming "the email person who just checks emails and send, check email, send" — which he finds unsatisfying, leading to the question of what work he uniquely wants to do
- This rule forces a conscious decision about which work the human keeps vs delegates

## Related
- [[ChrisParsons]] — creator of the rule
- [[Agent Permission Management]] — implementation of such rules
- [[Agent Sandboxing]] — technical enforcement
- [[AgentHuman Collaboration]] — the balance this rule creates
- [[summary-20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick]] — source transcript
