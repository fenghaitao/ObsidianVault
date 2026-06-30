---
title: "GenMedia"
type: concept
tags: [google, deepmind, generative-media, image-generation, video-generation, music-generation, tts, multimodal, suite]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind.md"]
last_updated: 2026-06-29
---

## Definition
GenMedia is Google DeepMind's suite of generative media models encompassing image generation (Nano Banana), video generation (VEO), music generation (Lyria), and text-to-speech (TTS). The suite is unified by Gemini as the orchestrating foundation model that generates prompts, and all GenMedia models are trained with Gemini-written prompts.

## Key Information
- **Suite components**: Nano Banana (image), VEO (video), Lyria (music), TTS (speech)
- **Unifying model**: Gemini serves as the foundation — all GenMedia models are trained with Gemini-generated prompts
- **World model vision**: DeepMind's long-term goal is a single multimodal model ingesting and outputting across all modalities, but ships separate models for release safety
- **Release cadence**: New GenMedia features shipped more than once per month on average (all of DeepMind: every 5 days)
- **Prompt-first design**: Most GenMedia models rewrite short user prompts internally; longer, more detailed prompts produce better results
- **API access**: Available via Gemini Developer API and Vertex AI with the same SDK
- **Cost**: All paid models; VEO is the most expensive component (~$0.05/sec for Light variant)
- **European availability**: Preview model status blocks EU endpoint access (a known issue)
- **Cookbook**: GitHub repository with quick starts and full examples mixing multiple GenMedia capabilities

## Related
- [[summary-20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind]] — source
- [[GoogleDeepMind]] — creator
- [[Nano Banana 2]] — image generation
- [[Veo]] — video generation
- [[Lyria]] — music generation
- [[Lyria Real-Time]] — real-time music variant
- [[Gemini]] — foundation model
- [[Guillaume Vernade]] — Developer Advocate
- [[Media Prompt Generation]] — pattern for generating prompts
- [[WorldModels]] — broader vision
- [[MultimodalAI]] — underlying paradigm
