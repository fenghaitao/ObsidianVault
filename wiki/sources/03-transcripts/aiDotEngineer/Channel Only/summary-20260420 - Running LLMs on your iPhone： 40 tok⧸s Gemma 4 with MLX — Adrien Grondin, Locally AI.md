---
title: "summary-20260420 - Running LLMs on your iPhone： 40 tok⧸s Gemma 4 with MLX — Adrien Grondin, Locally AI"
type: source
tags: [source, transcript]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Running LLMs on your iPhone： 40 tok⧸s Gemma 4 with MLX — Adrien Grondin, Locally AI.md"]
last_updated: 2026-06-26
---

## Core Summary

Adrien Grondin, developer of Locally AI, presents how to run Gemma 4 on iPhone using MLX, Apple's framework optimized for Apple Silicon. He demonstrates 40 tokens/second on-device inference with 4-bit quantized Gemma 4, walks through the MLX Swift LM GitHub repo for iOS/macOS integration, and explains how to source quantized models from the MLX community on Hugging Face. He also announces that Locally AI has been acquired by LM Studio, a local AI studio for running models with multiple engines including MLX and Llama CPP.

## Key Points

- Locally AI is a fully native iOS chatbot that runs on-device models with MLX, also available on iPad and macOS
- MLX is Apple's framework optimized for Apple Silicon (iPhone and Mac chips), with a growing ecosystem including MLX VLM, MLX Audio, and MLX Video
- MLX Swift LM is the GitHub repo for integrating MLX into iOS/macOS/iPadOS apps — can have a model running in under 10 minutes
- The MLX community on Hugging Face has 4,000-5,000 quantized models uploaded, often within 30 minutes of a model's release
- Recommended quantization range for iPhone: 4-bit (minimum for quality) to 8-bit (for very small models); below 4-bit significantly degrades output
- Gemma 4 4-bit quantized runs at 40 tokens/second on latest iPhones; even 20 tokens/second on older devices is useful
- MLX Swift LM supports tool calling; structured generation is not yet natively supported but packages are emerging
- Locally AI was acquired by LM Studio, which allows downloading and running models from Hugging Face with multiple engines (MLX, Llama CPP) and supports OpenAI/Anthropic-compatible local server APIs
- The biggest barrier to on-device AI is model size (1-3 GB), but models are getting smaller and smarter while iPhones improve

## Related

- [[Adrien Grondin]] — presenter, developer of Locally AI
- [[Locally AI]] — on-device iOS chatbot app
- [[MLX]] — Apple's framework for Apple Silicon
- [[MLX Swift LM]] — GitHub repo for iOS/macOS MLX integration
- [[LM Studio]] — local AI studio that acquired Locally AI
- [[Gemma 4]] — model demonstrated running on iPhone
- [[HuggingFace]] — source for MLX community quantized models
- [[OnDeviceAI]] — concept of running models on mobile devices
- [[Quantization]] — technique for reducing model size for on-device inference
- [[ToolCalling]] — supported by MLX Swift LM
