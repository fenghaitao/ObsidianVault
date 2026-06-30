---
title: "Agentic Experience"
type: concept
tags: [agentic-engineering, developer-experience, product-design, workos]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS.md"]
last_updated: 2026-06-30
---

## Definition

Agentic Experience (AX) is the discipline of designing products and developer tools to be consumed by AI agents, not just human developers. As the pipeline to developers increasingly goes through agents, AX becomes as important as Developer Experience (DX).

## Key Information

- Articulated by Nick Nisi (WorkOS) as a strategic product philosophy
- Core premise: the developer is still the most important user, but increasingly the pipeline to reach developers goes through AI agents
- Two directions for AI-native development: internal (building tools like Case for your own agents) and external (making your product work for customer agents)
- WorkOS CLI example: designed for zero-friction installation by both humans and agents — detects project type, removes competitors, provisions accounts automatically
- Key product design considerations for AX:
  - Figure out what agents get reliably wrong about your product and focus on those gotchas
  - Don't rely on comprehensive docs — models can read tutorials but need to know the landmines
  - Measure what you're shipping with evals — otherwise you may be adding noise that sends models on wild goose chases
  - Think about agents the same way you think about developers: what do they want to know? How can you make things better for them?
  - Consider how page content loads — JavaScript-heavy pages may lose context when agents summarize them
- The WorkOS CLI's AuthKit installation can provision an account that users claim later — designed for agent-driven onboarding

## Related

- [[summary-20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS]] — source
- [[NickNisi]] — articulated the concept
- [[WorkOS]] — company implementing AX
- [[WorkOS CLI]] — product designed for AX
- [[AuthKit]] — product with AX considerations
- [[Gotchas]] — the guidance approach for AX
- [[Guide Dont Prescribe]] — the design principle for AX
- [[DeveloperExperienceForAgents]] — related concept
- [[AgentReadyCodebases]] — related concept
