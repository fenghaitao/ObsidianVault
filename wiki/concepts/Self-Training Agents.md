---
title: "Self-Training Agents"
type: concept
tags: [agents, training, traces, fine-tuning, self-improvement]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face.md"]
last_updated: 2026-06-30
---

## Definition
Self-Training Agents are AI agents that improve their own performance by capturing execution traces, analyzing them, and using that data to fine-tune the underlying model. The paradigm is enabled by Hugging Face Traces — a new dataset repository type that stores agent sessions — combined with Hugging Face Skills that automate the fine-tuning workflow.

## Key Information
- The self-training loop: run agent → capture traces to Hugging Face Traces → explore traces in dataset viewer → use traces as training data → fine-tune model via LLM Trainer Skill → improved agent
- Hugging Face Traces stores Codex, Claude Code, and Pi agent sessions as structured datasets with parsed trace columns
- Traces can be pushed from standard session paths with no additional configuration needed
- Hermes Agent support for traces is coming soon, closing the loop for personal agents
- The LLM Trainer Skill handles the full fine-tuning pipeline: VRAM calculation, instance selection, batch size determination, and job launching — all triggered by a natural language command
- Enables "vibe training" — tell the agent "train Qwen-2-VL on Lava-Instruct-MiX" and it handles everything
- Represents a shift from manual ML engineering to agent-driven model improvement
- Works for LLMs, VLMs, object detectors, and segmentation models

## Related
- [[Hugging Face Traces]] — dataset type for agent execution data
- [[Hugging Face Skills]] — skill suite for automated training
- [[Agent Traces]] — the captured execution data
- [[FineTuning]] — the training technique
- [[Hermes Agent]] — agent framework gaining traces support
- [[HuggingFace]] — platform enabling the workflow
- [[summary-20260513 - Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face]] — source
