---
title: "AgentEntropy"
type: concept
tags: [agent-engineering, code-quality, technical-debt, entropy]
sources:
  - "raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil.md"
last_updated: 2026-06-26
---

## Definition
Agent entropy is the tendency of AI coding agents to increase codebase disorder over time. Because agents optimize for making progress and unblocking themselves (via reinforcement learning), they create more failure conditions, duplicate code, and brittle recovery paths than human-written code would. Over time, the codebase becomes too large and complex for the agent itself to navigate.

## Key Information
- Agents are optimized by reinforcement learning to write code that runs and makes progress — not code that is correct, maintainable, or safe
- Example: an agent might write code that silently falls back to defaults when a config file can't be read — the engineer might not notice until 2 hours later when database records have been written with wrong data
- Humans feel bad when writing fragile code; agents don't feel anything, so they have no emotional brake on creating brittle systems
- Agents create services that "hobble along" by recovering from local failures, creating very brittle systems overall
- Over time, the codebase grows to a size and complexity where the agent can no longer read all relevant files — it starts creating duplicate code in new files
- This creates "months and months of technical debt in weeks, in days sometimes"
- When understanding of your own code drops, it becomes psychologically hard to judge the state of the codebase objectively

## Related
- [[summary-20260418 - The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil]] — source transcript
- [[AgentLegibleCodebase]] — design approach to combat agent entropy
- [[MechanicalEnforcement]] — linting rules to catch entropy-inducing patterns
- [[CodeSlop]] — related concept
- [[Slop]] — broader concept
- [[IntentionalFriction]] — slowing down to prevent entropy
- [[CristinaPoncelaCubeiro]] — identified the problem
