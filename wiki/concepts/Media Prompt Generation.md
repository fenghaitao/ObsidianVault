---
title: "Media Prompt Generation"
type: concept
tags: [prompt-engineering, genmedia, llm, image-generation, video-generation, music-generation, pattern]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind.md"]
last_updated: 2026-06-29

---

## Definition
Media Prompt Generation is the pattern of using an LLM (typically Gemini) to generate detailed prompts for generative media models (image, video, music). This pattern is particularly effective because Google DeepMind's GenMedia models are trained on prompts written by Gemini, creating a natural synergy between the prompt generator and the media generator.

## Key Information
- **Why it works**: All GenMedia models are trained with Gemini-written prompts, making Gemini especially effective at crafting prompts these models respond well to
- **Internal prompt rewriting**: GenMedia models internally rewrite short user prompts before generation; longer, detailed prompts bypass this and produce more controlled results
- **Workflow**: (1) Use Gemini with structured output to generate prompts for characters/scenes/chapters, (2) Feed those prompts to GenMedia models for generation
- **Structured output advantage**: Using JSON schema for prompt generation ensures consistent metadata (character names, chapter associations) alongside the prompts
- **Style specification**: Gemini can be directed to generate prompts in a specific artistic style (e.g., "colorful building block style"), and the style carries through to the generated media
- **Video-specific**: For video generation, a dedicated prompt describing what happens in the seconds after the still image produces better results than reusing the image prompt
- **Music-specific**: Gemini can generate instrument specifications, BPM, scale, structure (intro/verse/chorus/outro), and lyrics as part of the music prompt
- **Cross-modal**: The same Gemini instance can generate prompts for images, videos, and music, maintaining thematic consistency

## Related
- [[summary-20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind]] — source
- [[GenMedia]] — target models
- [[Gemini]] — LLM used for prompt generation
- [[Character Consistency]] — related goal
- [[Structured Outputs]] — used for prompt formatting
