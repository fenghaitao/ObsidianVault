---
title: "MLX VLM"
type: entity
tags: [tool, mlx, vision, on-device-ai, apple-silicon, object-detection]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Why MLX — Prince Canuma, Neywa Labs.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Running LLMs on your iPhone： 40 tok⧸s Gemma 4 with MLX — Adrien Grondin, Locally AI.md"]
last_updated: 2026-06-29
---

## Definition
MLX VLM is a vision-language model framework built on MLX for Apple Silicon. It enables real-time image analysis, object detection, grounded visual reasoning, and multimodal chat with vision models — all running completely on-device on Mac, iPhone, and iPad.

## Key Information
- Built by Prince Canuma (Neywa Labs) on top of MLX
- Supports real-time object detection using models like Roboflow's RFDetector
- Enables background blurring/segmentation for video conferencing natively on-device
- Provides a Gradio chat UI for interacting with vision models (`mlx_vlm.chat_ui`)
- Can run large models like Gemma 4 on devices with sufficient VRAM (e.g., 96GB Mac)
- Powers LM Studio's vision capabilities
- Supports grounded visual reasoning: detecting specific items in video and reasoning about them
- Community use cases: security systems, dashcam analysis, real-time scene understanding
- Originally motivated by building accessibility tools for blind users (phone-based scene description)
- Available in Python; Swift support planned

## Related
- [[summary-20260511 - Why MLX — Prince Canuma, Neywa Labs]] — primary source
- [[summary-20260420 - Running LLMs on your iPhone： 40 tok⧸s Gemma 4 with MLX — Adrien Grondin, Locally AI]] — secondary source
- [[MLX]] — underlying framework
- [[Prince Canuma]] — creator
- [[Neywa Labs]] — company behind it
- [[MLX Audio]] — companion audio framework
- [[MLX Video]] — companion video framework
- [[Roboflow]] — provider of RFDetector model
- [[Gradio]] — UI framework used for chat interface
- [[LM Studio]] — app using MLX VLM as engine
- [[Grounded Visual Reasoning]] — key capability enabled
- [[OnDeviceAI]] — core concept
