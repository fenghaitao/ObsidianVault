---
title: "ResearchPlanImplement"
type: concept
tags: [ai, workflow, methodology, software-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary.md"]
last_updated: 2026-06-26
---

## Definition
The Research-Plan-Implement loop is a structured three-phase workflow for AI-assisted development promoted by Brendan O'Leary and Kilo Code. It front-loads human thinking into research and planning phases before letting AI generate code, preventing the common mistake of jumping straight to implementation with poor context.

## Key Information
- **Phase 1 — Research**: Use an ask-only mode (cannot write files) to understand the system — how it works, which files are involved, what paradigms to mirror, data flow, edge cases. AI is great at brainstorming. Output: a research document that the human reviews and agrees with before proceeding.
- **Phase 2 — Plan**: Outline explicit next steps — files to create/change, verification strategy, test changes, what is in/out of scope. Output: a clear plan file with step-by-step instructions, test commands, and scope boundaries. Can be executed by a smaller/faster/cheaper model because the hard thinking is done.
- **Phase 3 — Implement**: Start a fresh session with just the plan. Keep context low. Review each change carefully. Commit frequently. Use Git as a local first-pass PR review before sharing with human colleagues.
- Dex Horthy: "A bad line of research can potentially be hundreds of lines of bad code" — justifying the upfront investment in research
- Human time in research and planning phases is the highest-leverage use of time
- Contrasts with the common anti-pattern: "Hey, help me implement this feature" → garbage in, garbage out
- Related to but distinct from Jake Nations' ThreePhaseApproach — Brendan's version emphasizes agent modes (ask/code/architect) and fresh sessions per phase

## Related
- [[summary-20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary]] — source transcript
- [[BrendanOLeary]] — promoter of the workflow
- [[KiloCode]] — tool built around this workflow
- [[ThreePhaseApproach]] — related workflow from Jake Nations
- [[AgenticEngineering]] — the parent paradigm
- [[AgentModes]] — ask/code/architect modes that enable the workflow
- [[ContextEngineering]] — the skill needed to execute each phase effectively
