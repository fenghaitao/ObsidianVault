---
title: "Hugging Face Skills"
type: concept
tags: [hugging-face, skills, agents, training, automation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face.md"]
last_updated: 2026-06-30
---

## Definition
Hugging Face Skills are a suite of agent skills that allow coding agents to manage Hugging Face Hub resources, train models, build demos, and explore datasets through natural language commands. They plug the Hub into any agent, enabling "vibe training" — telling an agent to train a model and having it handle the entire workflow.

## Key Information
- **HF CLI Skill**: Allows coding agents to manage repositories, run jobs, launch demos, and perform Hub operations
- **LLM Trainer Skill**: End-to-end fine-tuning automation — agent calculates VRAM requirements, selects instance types, determines batch sizes, handles validation splits, and launches training jobs. Works for LLMs, VLMs, object detectors, and segmentation models. Handles bounding box type variations automatically for vision tasks
- **Gradio Skill**: Builds and launches interactive demos from models
- **Dataset Skill**: Explores datasets through the Hugging Face dataset viewer API
- Skills can be installed by searching "HF skills" — simple CLI commands to add to any agent
- Plays nicely with Claude, Gemini, and other coding agent platforms
- Merve Noyan describes the LLM Trainer Skill as "absolute sci-fi" — the ability to fine-tune models by simply stating the intent, with the agent handling all infrastructure decisions
- Not limited to text models — supports vision tasks including object detection and segmentation
- New skill shipped for recommending models from benchmarks (e.g., "what is the best model on OCR for fine-tuning")

## Related
- [[HuggingFace]] — platform integrated via skills
- [[Self-Training Agents]] — training loop enabled by skills
- [[Hugging Face Traces]] — data source for training
- [[Hugging Face MCP Server]] — complementary MCP integration
- [[Agent Skills]] — broader skills concept
- [[FineTuning]] — the training technique automated by skills
- [[summary-20260513 - Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face]] — source
- [[summary-20260504 - Skill Issue： How We Used AI to Make Agents Actually Good at Supabase — Pedro Rodrigues, Supabase]] — skills for agents
- [[summary-20260506 - Full Walkthrough： Writing & Using Skills — Nick Nisi and Zack Proser]] — skills
