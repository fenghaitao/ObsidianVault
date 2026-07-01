---
title: "summary-20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind"
type: source
tags: [source, transcript, google, deepmind, genmedia, image-generation, video-generation, music-generation, tts, multimodal, workshop]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind.md"]
last_updated: 2026-06-29
---

## Core Summary

Guillaume Vernade, Developer Advocate at Google DeepMind, delivers a hands-on workshop demonstrating how to compose Google's GenMedia suite (Nano Banana for images, VEO for video, Lyria for music, and TTS for speech) to illustrate a book end-to-end, with Gemini acting as the prompt-generation orchestrator. The talk covers practical API patterns, cost management, and the developer experience gap between consumer apps and enterprise Vertex AI.

## Key Points

- **Developer Advocate role**: Bridging developers and internal teams — ensuring released products make sense in the real world, not just "for Google by Google." Key win: Imagen brand consolidated after fighting for API consistency across models.
- **World model vision**: DeepMind's goal is a single multimodal model ingesting and outputting across all modalities (images, video, audio, sensors). Current approach ships separate GenMedia models for release safety, with Gemini as the unifying foundation.
- **GenMedia suite components**: Nano Banana 2 (image generation with search grounding, aspect ratios up to 4K), VEO 3.1 (video generation, $0.05/sec for Light variant), Lyria (music generation, 30s clips or 3min full songs), Lyria Real-Time (predictive model for live DJ-style music), TTS (text-to-speech with voice style control).
- **Service tiers**: Normal (standard queue), Flex (50% discount, possible delays up to minutes), Priority (2x price, guaranteed fast track). Shipped the week of the talk.
- **Gemini API vs Vertex AI**: Gemini Developer API simplifies Vertex complexity (no bucket/ACL management) via Client File Upload. Same SDK across both, allowing migration. AI Studio is the testing playground.
- **Chat mode and context**: Chat API maintains conversation history, enabling character consistency across generations. Downside: re-sends entire context (e.g., full book) on each call. New Interactions API (preview) solves this with stateful session IDs and automatic caching.
- **Structured output**: JSON schema constrained responses ensure consistent prompt generation for characters, chapters, and music.
- **Prompt generation via LLM**: Gemini generates prompts for GenMedia models. All GenMedia models are trained with Gemini-written prompts, making Gemini particularly effective as a prompt engineer for these models.
- **Character consistency strategies**: (1) Chat mode history for implicit consistency across generations, (2) Saving generated character images and passing them as references to later calls with generate_content for explicit consistency.
- **Video generation workflow**: Use VEO with reference image as first frame. Better results when Gemini generates a dedicated video prompt describing what happens in the seconds after the still image.
- **Lyria prompt-only control**: No parameters — everything (duration, instruments, BPM, scale, structure, lyrics, language) is controlled via natural language in the prompt. Supports intro/verse/chorus/outro structure, multi-language, and lyric timing metadata for karaoke.
- **TTS voice style trick**: Using a single TTS voice for multiple characters by embedding style instructions (e.g., "breathless and unbolstered" vs "long poetic pauses") in the transcript text, creating the illusion of distinct voices.
- **European data sovereignty**: Preview models only available on global endpoints, blocking EU-hosted access. A known pain point Vernade is actively fighting to change.
- **Cookbook**: GitHub repo (goo.gl/cookbook-illustration) with quick starts and full examples mixing multiple GenMedia capabilities.

## Related

- [[Guillaume Vernade]] — presenter, Developer Advocate at Google DeepMind
- [[GoogleDeepMind]] — organization
- [[GenMedia]] — suite of generative media models
- [[Nano Banana 2]] — image generation model
- [[Veo]] — video generation model
- [[Lyria]] — music generation model
- [[Lyria RealTime]] — real-time predictive music model
- [[NotebookLM]] — referenced for podcast-style TTS
- [[Gemini]] — foundation model used as orchestrator
- [[VertexAI]] — enterprise AI platform
- [[AI Studio]] — developer testing platform
- [[GoogleColab]] — notebook environment used for workshop
- [[GeminiInteractionsAPI]] — new stateful API
- [[Stadia]] — previous product, Vernade's background
- [[Project Gutenberg]] — source of open-source books
- [[Imagen]] — deprecated image generation brand
- [[Character Consistency]] — concept for multi-generation coherence
- [[Service Tiers]] — pricing and performance model
- [[Developer Advocate]] — role and function
- [[Media Prompt Generation]] — using LLMs to generate prompts for media models
- [[Client File Upload]] — simplified file upload API
- [[API Consistency]] — unified API design principle
- [[Model Preview vs GA]] — product lifecycle concept
- [[Voice Style Control]] — TTS voice manipulation technique
- [[Data Sovereignty]] — geographic data privacy concern
- [[Image Search Grounding]] — web image reference feature
