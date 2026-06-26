---
title: "ThreePhaseApproach"
type: concept
tags: [methodology, ai, workflow, software-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251220 - The Infinite Software Crisis – Jake Nations, Netflix.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary.md"]
last_updated: 2026-06-25
---

## Definition
A structured three-phase workflow for AI-assisted software development proposed by Jake Nations: Phase 1 (Research) — feed context, probe, validate; Phase 2 (Planning) — create a detailed implementation plan any developer could follow; Phase 3 (Implementation) — let AI execute the clean spec.

## Key Information
- **Phase 1 — Research**: Feed everything upfront (architecture diagrams, documentation, Slack threads). Use AI to analyze the codebase and map components and dependencies. Probe with questions ("What about caching? How does this handle failures?"). Correct wrong analysis, provide missing context. Output: a single research document mapping what exists, what connects to what, and what the change will affect. The human checkpoint at the end of this phase is the highest-leverage moment in the entire process.
- **Phase 2 — Planning**: Create a detailed implementation plan with real code structure, function signatures, type definitions, data flow. Should be so detailed any developer could follow it — "paint by numbers." This is where architectural decisions are made: service boundaries, clean separation, preventing unnecessary coupling. Review speed is the magic: validate the plan in minutes and know exactly what will be built.
- **Phase 3 — Implementation**: With a clear plan backed by validated research, this phase should be simple. AI has a clear specification to follow, context remains clean and focused. Instead of 50 messages of evolutionary code, three focused outputs each validated before proceeding. Background agents can do the work while the developer works on something else.
- The approach prevents the complexity spiral of long AI conversations: no abandoned approaches, no conflicting patterns, no "wait actually" moments leaving dead code
- Key principle: not using AI to think for us, but to accelerate mechanical parts while maintaining human understanding

## Related
- [[summary-20251220 - The Infinite Software Crisis – Jake Nations, Netflix]] — source transcript
- [[JakeNations]] — creator of the approach
- [[ContextCompression]] — the broader methodology this workflow implements
- [[InfiniteSoftwareCrisis]] — the problem this approach addresses
- [[summary-20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary]] — source (related Research-Plan-Implement variant)
- [[ResearchPlanImplement]] — Brendan O'Leary's variant with agent modes and fresh sessions per phase
