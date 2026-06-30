---
title: "Gemma 4"
type: entity
tags: [model, google, deepmind, open-source, apache2, mobile, omnimodel]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Running LLMs on your iPhone： 40 tok⧸s Gemma 4 with MLX — Adrien Grondin, Locally AI.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - TLMs： Tiny LLMs and Agents on Edge Devices with LiteRT-LM — Cormac Brick, Google.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Why MLX — Prince Canuma, Neywa Labs.md"]
last_updated: 2026-06-29
---

## Definition
Gemma 4 is Google DeepMind's open model family, released under an Apache 2 license. The models punch above their weight in terms of parameter size and compute footprint, support multimodal understanding, and the smallest versions run on mobile devices. The "e" variants (E2B, E4B) are omnimodels accepting image, audio, and text input.

## Key Information
- Open model family from Google DeepMind with Apache 2 license
- Available via AI Studio API for free ("try before you buy" experience)
- Can be downloaded for self-hosted infrastructure use and fine-tuning
- Supports multimodal understanding (audio, video, images)
- "e" variants (E2B, E4B) are omnimodels: accept image, audio, and text as input or any combination
- Smallest versions run on mobile devices (e.g., Pixel phones)
- Day-zero support on MLX: Gemma 4 was available on MLX the day it was released
- Planned integration with Pixel 10 and Chrome browser
- Released shortly before April 2026 (after Gemini 3.1 training data cutoff)
- Presented by Ian from the Gemma team at AIE conference
- Runs on iPhone via MLX at 40 tokens/second with 4-bit quantization (demonstrated in Locally AI)
- Can run Gemma 4 26B on an iPhone using device storage with reasonable speeds
- Available in multiple quantization variants on Hugging Face MLX community (4-bit, 5-bit, 6-bit, 8-bit, BF16, MXFP4)

## Related
- [[summary-20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind]] — source
- [[summary-20260420 - Running LLMs on your iPhone： 40 tok⧸s Gemma 4 with MLX — Adrien Grondin, Locally AI]] — source
- [[summary-20260511 - Why MLX — Prince Canuma, Neywa Labs]] — source (omnimodel variants, day-zero support)
- [[Google DeepMind]] — creator
- [[AI Studio]] — platform for API access
- [[Gemini 3.1 Pro]] — larger sibling model family
- [[MLX]] — framework for running on iPhone
- [[Locally AI]] — iOS app running Gemma 4 on-device
- [[Omnimodels]] — model category for "e" variants
- [[Day Zero Support]] — MLX's commitment to day-zero availability
