---
title: "Writing Profiles"
type: concept
tags: [content-generation, prompt-engineering, style, linkedin]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi.md"]
last_updated: 2026-06-26
---

## Definition
Writing Profiles are static markdown files that define how an LLM should write content. They form the styling layer of a content generation system, separate from the dynamic user input (guideline). Three profile types are used: structure (format, character counts, core sections), terminology (banned AI slop words and expressions), and character (author personality and biography).

## Key Information
- **Three profile types**: Structure profile (LinkedIn post format, hook/body/CTA, character counts), terminology profile (banned words like "delve," "vibrant," "game-changing," active voice enforcement), character profile (author bio, writing style, personality)
- **Static vs dynamic**: Profiles are defined once and reused across all posts. Only the guideline.md (user input) changes per post
- **Overridable**: The guideline can override default profile settings (e.g., a specific character count constraint for a particular post)
- **Terminology management**: Maintain a list of banned AI slop words and expressions. The LLM is instructed not to use them
- **Character profile**: Includes the author's biography and writing style preferences to inject personality into generated content
- **Part of system prompt**: Profiles are loaded into the system prompt alongside the guideline and few-shot examples
- **Used by both writer and reviewer**: The reviewer checks adherence against all three profiles
- **Result**: Generated posts pass AI slop detectors with scores lower (less sloppy) than human-written content

## Related
- [[summary-20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi]] — source
- [[EvaluatorOptimizer Pattern]] — workflow using these profiles for review
- [[Slop]] — the AI-generated low-quality content profiles aim to avoid
- [[FewShotExamples]] — complementary technique for controlling generation
- [[Paul Iusztin]] — presenter who designed the profile system
- [[LinkedIn]] — target platform for the writing workflow
