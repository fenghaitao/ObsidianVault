---
title: "LibrariesVsProducts"
type: concept
tags: [agent-engineering, codebase-design, libraries, products]
sources:
  - "raw/03-transcripts/aiDotEngineer/Channel Only/20260418 - The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil.md"
last_updated: 2026-06-26
---

## Definition
Libraries vs. Products is an observation by Armin Ronacher and Cristina Poncela Cubeiro that AI coding agents perform significantly better on libraries than on products. Libraries have clearly defined problems, tight API constraints, and simple cores — making them legible to agents. Products have many interacting concerns (UI, permissions, billing, feature flags) that don't fit in context windows, causing agents to be locally reasonable but globally "demented."

## Key Information
- **Libraries**: Agents excel because the problem is clearly defined, features map to API surfaces, constraints are tight, and the core is simple with complexity pushed to abstraction layers
- **Products**: Agents struggle because of heavy intertwining between components — UI, API responses, permissions, feature flags, billing — all interacting in ways the agent cannot fit in its context window
- The agent has "no way to actually understand the entire global structure"
- Locally, the agent tends to be very reasonable; globally, it becomes "a bit demented"
- Implication: product codebases need even more deliberate design for agent legibility — modularization of both components and code flow
- This distinction helps teams decide where to deploy agents most effectively

## Related
- [[summary-20260418 - The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil]] — source transcript
- [[AgentLegibleCodebase]] — design approach to make products more agent-friendly
- [[Modularity]] — key principle for making products work with agents
- [[ArminRonacher]] — key proponent
- [[CristinaPoncelaCubeiro]] — key proponent
