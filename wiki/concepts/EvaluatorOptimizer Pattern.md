---
title: "Evaluator-Optimizer Pattern"
type: concept
tags: [workflows, content-generation, llm, structured-outputs, quality]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic.md"]
last_updated: 2026-06-29
---

## Definition
The Evaluator-Optimizer Pattern is a content refinement workflow where a writer LLM generates a draft, a reviewer LLM (with a separate context window) evaluates it against guidelines and profiles, and an editor (often the writer itself) applies the prioritized reviews. The loop iterates a fixed number of times (typically 3-4) to progressively improve output quality.

## Key Information
- **Two separate context windows**: Writer and reviewer use different contexts to avoid bias — LLMs tend to be biased in liking what they already wrote
- **Reviewer outputs**: Structured Pydantic objects with profile (which rule was violated), location (where in the content), and comment (what the issue is). Structured outputs are more performant than free-form LLM responses
- **Review prioritization**: Reviews are not created equal. Priority order: guideline (user input) first, then research (factual accuracy), then profiles (style). This resolves conflicts when reviews clash on the same content
- **Fixed iterations over score-based**: For creative/subjective work, score-based thresholds are unreliable because quality is hard to quantify. Fixed iterations (3-4) are more practical, and users can run additional iterations manually
- **Version preservation**: All intermediate versions (V0 through V4) are saved so users can pick their preferred version, since writing is subjective
- **Inputs to reviewer**: Current post state + guideline + research + profiles (structure, terminology, character)
- **Inputs to editor**: List of Pydantic review objects + current post state + all original writer context
- **Applicability**: Works for any content type (LinkedIn posts, articles, reports, video transcripts, book chapters) — just adapt the profiles and examples
- **Pydantic as prompt engineering**: Pydantic field descriptions serve as prompts explaining to the LLM what each attribute should contain

## Related
- [[summary-20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi]] — source
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — source (GEPA proposer agent as evaluator-optimizer)
- [[Writing Profiles]] — static styling layer used by the reviewer
- [[Structured Outputs]] — Pydantic objects for reviewer feedback
- [[Pydantic]] — library used for structured reviewer output
- [[LLMAsJudge]] — related evaluation technique
- [[FewShotExamples]] — used in both writer and evaluator prompts
- [[Paul Iusztin]] — presenter who designed this pattern
- [[Deep Research Agent]] — produces the research input for the writer
- [[GEPA]] — genetic algorithm using evaluator-optimizer meta-pattern
- [[Agentic Optimization]] — meta-agent optimization pattern
