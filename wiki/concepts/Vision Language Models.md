---
title: "Vision Language Models"
type: concept
tags: [models, vision, multimodal, vlm, computer-use]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face.md"]
last_updated: 2026-06-30
---

## Definition
Vision Language Models (VLMs) are multimodal AI models that combine vision and language capabilities, enabling them to process images and text together. In the agentic context, VLMs can act as computer-use agents by analyzing screenshots and determining where to click, effectively driving GUI interactions.

## Key Information
- Two types of agentic models on Hugging Face Hub: VLMs and LLMs
- VLMs can act as computer-use agents over screenshots, knowing where to click and what actions to take
- Trend: labs are releasing LLMs with vision capabilities "day zero" — Gemini 4, Qwen 3.5, Chimera 2.5 are all VLMs with agentic capabilities
- Merve Noyan predicts all models will eventually be released with vision capabilities from day one
- VLMs can be fine-tuned using Hugging Face Skills (LLM Trainer Skill supports VLMs)
- Example: Qwen-2-VL trained on Lava-Instruct-MiX (vision-language dataset) via the LLM Trainer Skill
- Hugging Face Skills also support vision-specific tasks: object detection, segmentation, handling different bounding box types

## Related
- [[Computer Use]] — VLM-driven GUI interaction
- [[Qwen]] — example VLM with agentic capabilities
- [[Gemma4]] — model with vision capabilities
- [[Hugging Face Skills]] — skills supporting VLM fine-tuning
- [[Self-Training Agents]] — VLM agents can also self-train via traces
- [[summary-20260513 - Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face]] — source
