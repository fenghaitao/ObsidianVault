---
title: "Closed-Loop Evaluation"
type: concept
tags: [eval, automation, self-improvement, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize.md"]
last_updated: 2026-06-30
---

## Definition
Closed-loop evaluation is an advanced pattern where eval results are fed as feedback to a coding agent (like Claude Code) that automatically improves the application without human involvement. It closes the loop between evaluation and improvement.

## Key Information
- The vision: write the initial version of an app, use evals as the feedback mechanism for a coding agent, let the agent automatically improve the app
- Currently aspirational — Laurie Voss described it as "very exciting and it's definitely going to happen as the models get better"
- Builds on the existing eval-iterate cycle: instrument → trace → eval → annotate → analyze → improve → repeat
- Replaces the manual "change prompt, run experiment, check scores" loop with an automated one
- Arize hinted at presenting working closed-loop evaluation at an upcoming AIE World's Fair
- Represents the frontier of eval automation beyond what was demonstrated in the workshop
- Requires highly reliable evals — if the feedback loop is automated, the evals must be trustworthy (validated via meta-evaluation)

## Related
- [[EvalEngineering]] — practice of crafting reliable eval prompts
- [[MetaEvaluation]] — validating evals before closing the loop
- [[Agentic Optimization]] — related meta-agent optimization pattern
- [[summary-20260514 - Ship Real Agents： Hands-On Evals for Agentic Applications — Laurie Voss, Arize]] — source
