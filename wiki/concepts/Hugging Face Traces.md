---
title: "Hugging Face Traces"
type: concept
tags: [hugging-face, traces, agents, datasets, observability]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face.md"]
last_updated: 2026-06-30
---

## Definition
Hugging Face Traces is a new dataset repository type on the Hugging Face Hub for storing and exploring AI agent execution traces from Codex, Claude Code, Pi, and other coding agents. Traces are parsed and displayed in the dataset viewer with a dedicated traces column, enabling analysis and reuse as training data for self-training agents.

## Key Information
- New dataset repository type on Hugging Face Hub specifically for agent execution traces
- Supported agent sources: Codex, Claude Code, Pi traces (Hermes Agent support coming soon)
- Traces are parsed and rendered nicely in the dataset viewer with a dedicated traces column
- Push traces from standard session file paths — no additional configuration needed
- Enables exploration and analysis of agent behavior through structured trace data
- Forms the data layer of the self-training loop: capture traces → explore → fine-tune → improved agent
- Part of Hugging Face's broader agent ecosystem alongside Skills, MCP server, and inference providers

## Related
- [[Self-Training Agents]] — the paradigm enabled by traces
- [[HuggingFace]] — platform hosting traces
- [[Agent Traces]] — the captured execution data
- [[Hugging Face Skills]] — skills for training on trace data
- [[Hermes Agent]] — upcoming traces support
- [[summary-20260513 - Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face]] — source
