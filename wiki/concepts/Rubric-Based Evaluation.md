---
title: "Rubric-Based Evaluation"
type: concept
tags: [ai, evaluation, quality, design, agents, grading, taste]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson.md"]
last_updated: 2026-06-30
---

## Definition
Rubric-Based Evaluation is a grading framework for AI-generated applications that uses explicit written criteria to evaluate output quality. Anthropic's approach uses four weighted criteria — design, originality, craft, and functionality — calibrated with few-shot examples on reference sites to converge the evaluator agent's taste with human taste. The core philosophy: subjective quality is gradable if you have a strong enough opinion and write it down.

## Key Information
- **Four Criteria**: Design, Originality, Craft, Functionality — weighted toward design and originality to prevent "AI slop" aesthetics (purple gradients, generic outputs)
- **Weighting Strategy**: Adjusted based on which model is in play. Opus 4.6 is already good at functionality, so design and originality get more weight to compensate for remaining gaps
- **Calibration**: Evaluator's taste is calibrated using few-shot examples on reference sites — showing examples of good design vs "AI slop" — so the evaluator's judgment converges with human taste
- **Anti-Slop Function**: Primary purpose is preventing generic AI aesthetics. "You can't grade taste" is rejected — "we think you can if you have a strong enough opinion on it and you just write it down"
- **Granularity**: Rubrics must be detailed and specific. Vague criteria produce vague critiques that the generator ignores; granular criteria tell the agent exactly which line to fix
- **Hill Climbing**: The harness uses rubrics as the fitness function — generator iterates to improve scores across criteria, evaluator provides specific critiques tied to each criterion
- **Reusability**: Aim is for rubrics to be reusable across projects, not per-project. Common patterns of what constitutes good design generalize well
- **Skills Packaging**: Rubrics can be packaged as Claude Code skills for reuse
- **Beyond Design**: Can be extended to API design, code quality, and other dimensions — just define criteria and calibrate with examples

## Related
- [[summary-20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson]] — source
- [[Generator-Evaluator Pattern]] — harness pattern that uses rubrics
- [[Contract Negotiation]] — complementary evaluation mechanism
- [[Self-Evaluation Trap]] — what rubric-based evaluation helps avoid
- [[AIAndTaste]] — related concept about AI and design taste
- [[Slop]] — what rubrics help prevent
- [[Skills]] — packaging mechanism for rubrics
- [[LLM-as-Judge]] — broader evaluation category
