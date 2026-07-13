---
title: "Multi-Model Peer Review"
type: concept
tags: [vibe-coding, code-review, ai]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz.md"]
last_updated: 2026-07-11
---

## Definition

[[Zevi Arnovitz]]'s practice of having multiple AI models independently review the same code, then feeding each model's findings back to the primary agent to accept or rebut — a workaround for his own inability, as a non-technical builder, to catch mistakes in AI-written code himself.

## Key Information

- Process: after manually QA-ing a feature, Zevi first has the primary agent ([[Claude Code]]) review its own code (`/review`). He then runs the same review independently with [[Codex]] (built-in code review) and Cursor's Composer model on the same branch.
- The `/peer review` command then feeds the other models' findings back to the primary agent, framed as: "other team leads within the company have looked at your code and reviewed it and found these issues... you need to either explain why the stuff they found are not real issues... or fix them yourself" — deliberately not taking secondary findings at face value, since the primary agent has the most context on the project.
- Zevi personifies each model with a distinct "personality" to reason about their different strengths: Claude as a communicative, opinionated, collaborative "dev lead" who pushes back rather than just complying; [[Codex]] as an uncommunicative but highly effective solo problem-solver ("closes the door for two hours and comes out and says I fixed it"); Gemini (used inside Google's Antigravity IDE) as a talented but erratic "crazy scientist" whose visible step-by-step reasoning (e.g., "first things first, I'll delete the dashboard... nope, that was a mistake, I'll bring it back") is alarming to watch even though the end design output is excellent.
- Outcome dynamic: sometimes the primary agent will repeatedly and firmly reject a flagged issue across multiple review rounds ("this has been raised for the third time and for the third time I'm telling you this is not an issue. This is by design") — treated by Zevi as a feature of the process, since it forces an explicit justification rather than silent compliance.
- Motivation: framed as compensating for his own lack of technical review ability — "it's very difficult for me to catch mistakes" — by having models check each other rather than relying on a single model's self-assessment.

## Related

- [[summary-31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz]] — source summary
- [[Zevi Arnovitz]] — originates this practice
- [[Slash Command Development Workflow]] — the broader workflow this is stage 5 of
- [[CTO Persona Pattern]] — the personification approach this extends to multiple models
- [[Claude Code]] / [[Codex]] / [[Cursor]] / [[Gemini]] — the models used in review rotation
