---
title: "AgentBrittleSystems"
type: concept
tags: [agent-engineering, reliability, system-design, failure-modes]
sources:
  - "raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil.md"
last_updated: 2026-06-26
---

## Definition
Agent brittle systems are software systems built by AI coding agents that silently recover from local failures, creating an illusion of robustness while actually being highly fragile. Because agents optimize for making progress rather than correctness, they create many more failure conditions than human-written code, and their recovery paths mask problems until they cascade.

## Key Information
- Identified by Armin Ronacher and Cristina Poncela Cubeiro as a characteristic failure mode of agent-generated code
- Example: an agent writes code that reads a config file and silently falls back to defaults on failure — the engineer might not notice for hours, by which time database records have been written with wrong data
- Agents are willing to "hobble along" by recovering from local failures, creating services that appear to work but are actually very brittle
- Humans feel bad when writing code like this — there's an emotional brake. Agents don't feel anything, so they have no such brake
- Over time, these brittle recovery paths accumulate, making the system increasingly fragile
- The only solution is intentional friction: slowing down, reviewing critical paths, and using mechanical enforcement to catch these patterns

## Related
- [[summary-20260418 - The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil]] — source transcript
- [[AgentEntropy]] — the broader pattern of increasing disorder
- [[MechanicalEnforcement]] — linting rules to catch brittle patterns (e.g., no bare catch)
- [[IntentionalFriction]] — slowing down to prevent brittle systems
- [[HumanCallouts]] — review pattern to catch these issues
- [[ArminRonacher]] — key proponent
- [[CristinaPoncelaCubeiro]] — key proponent
