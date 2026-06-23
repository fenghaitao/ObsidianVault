---
title: "Evals for Taste: Hill-Climbing a Slide-Generation Agent"
type: source
tags: [evals, grading, slide-generation, agent-improvement, quality]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London Day 2/04 - Evals for taste： Hill-climbing a slide-generation agent.md]
last_updated: 2026-06-23
---

## Core Summary

An Anthropic presenter demonstrates how to build and use evals to iteratively improve a slide-generation agent. Starting with a basic agent producing low-quality slides (emojis, cluttered layouts, small fonts), the session walks through defining code-based graders (deterministic checks like emoji count, slide count) and model-based judges (rubric-based scoring for color, layout, text quality). The agent is improved through systematic prompt engineering based on eval feedback, then further enhanced with a QA loop (self-critique and fix cycle). Finally, switching from Sonnet 4.6 to Opus 4.7 with just the basic prompt achieves better results, demonstrating that smarter models can internalize quality standards.

## Key Points

- **Evals defined:** Systematic tests measuring AI system performance on specific domains, made of tasks (scenarios) and graders (expectation encoding).
- **Grader types:** Code-based (fast, deterministic, brittle — e.g., emoji count, slide count, font size checks) and model-based (flexible, nuanced, non-deterministic — rubric scoring for color contrast, layout, text quality).
- **Model grader calibration is critical:** LLM judges need anchoring with examples of good/bad outputs. Ask for reasoning BEFORE the score to avoid auto-regressive justification bias.
- **QA loop pattern:** Agent creates slides → converts to images → self-inspects → finds issues → fixes → re-renders → re-inspects. "Approach QA as a bug hunt, not a confirmation step."
- **Smarter models reduce prompt engineering:** Opus 4.7 with a minimal prompt outperformed Sonnet 4.6 with extensive typography/layout instructions, showing that model intelligence can substitute for detailed configuration.
- **Evals are living artifacts:** They must evolve as product capability expands; saturation (no more useful information) signals need for refinement.
- **Human review remains essential:** Spot-checking eval results catches grader miscalibration (e.g., scoring a slide deck with no images as 5/5 for image quality).
- **Multi-judge consensus:** Running multiple judge evaluations and taking majority vote adds determinism to non-deterministic model graders.

## Related

- [[ClaudeManagedAgents]] — platform for deploying the slide-generation agent
- [[ClaudeFable5]] — Opus 4.7 model that outperformed with minimal prompting
- [[PromptEngineering]] — the iterative prompt refinement demonstrated
