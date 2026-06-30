---
title: "Hugging Face MCP Server"
type: concept
tags: [hugging-face, mcp, agents, integration, spaces]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face.md"]
last_updated: 2026-06-30
---

## Definition
The Hugging Face MCP Server is an MCP (Model Context Protocol) integration that exposes Hugging Face Hub resources — models, datasets, spaces, semantic search, and jobs — to AI agents. It allows agents to query and interact with Hugging Face infrastructure through standard MCP tool calls.

## Key Information
- Exposes Hugging Face Hub resources via MCP: models, datasets, spaces, semantic search for spaces, and jobs
- Jobs feature allows agents to kick off one-off compute tasks that end on success or failure, with pay-per-use pricing
- Semantic search for spaces enables agents to discover relevant AI applications from the Hub's app store
- "Dynamic Spaces" setting (experimental) exposes all spaces for broader agent querying
- Plays nicely with all major platforms (Claude, Gemini, etc.)
- Example use case: agent queries the Qwen image generation space to produce images on demand
- Enables agents to search for models by task and compare options directly
- Complement to Hugging Face Skills — MCP for discovery and querying, Skills for training and deployment

## Related
- [[HuggingFace]] — platform
- [[MCP]] — the Model Context Protocol standard
- [[Hugging Face Skills]] — complementary integration for training and deployment
- [[Hugging Face Spaces]] — AI apps queriable via MCP
- [[Hugging Face Jobs]] — compute jobs accessible via MCP
- [[summary-20260513 - Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face]] — source
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — MCP ecosystem
