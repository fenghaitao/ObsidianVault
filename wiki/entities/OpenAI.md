---
title: "OpenAI"
type: entity
tags: [company, ai-lab, gpt, llm-provider]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/01 - Build an ARMY of AI Agents on Autopilot with Archon, Here's How.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/02 - 10x Your AI Agents with this ONE Agent Architecture.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/03 - Coding Subagents - The Next Evolution of AI IDEs.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
last_updated: 2026-06-19
---

## Definition

OpenAI is the AI lab behind the GPT model family. Their models are the default LLM choice in many of [[ColeMedin]]'s demos.

## Key Information

### Models referenced in the playlist

| Model | Used for |
|---|---|
| **GPT-4o** | Default coder agent inside [[Archon]]; primary agent in MCP Agent Army demo |
| **GPT-4o-mini** | Lower-cost option; demonstrated to be sufficient for the MCP Agent Army demo despite being a smaller model |
| **o3-mini** | Reasoner agent inside Archon (the model that defines scope before code generation) |

### Notable usage patterns Cole demonstrates

- **Tier the LLM by role.** Use a stronger reasoning model (o3-mini) for high-level planning and a faster/cheaper model (GPT-4o or GPT-4o-mini) for the high-volume tool-calling and code-emission steps. Pattern visible in Archon's Reasoner → Coder split.
- **Even small models are enough for sub-agent armies.** In the MCP Agent Army demo, GPT-4o-mini orchestrates 6 sub-agents and chained tasks (search → Airtable → Slack) successfully.

### Adjacent context

- OpenAI's tool-calling API shape is the de facto standard that other providers (and MCP) emulate. PydanticAI's tool registration ultimately compiles down to OpenAI-style function-calling JSON.
- Cole references **DeepSeek R1** and **Qwen 2.5 Coder** alongside Claude 3.7 Sonnet as evidence that "every LLM lab is racing on coding" — context for why specialized agent-builders like Archon matter now.

## Related

- [[Archon]] — uses OpenAI models for both Reasoner and Coder roles by default
- [[ColeMedin]] — frequent OpenAI user
- [[Anthropic]] — competing lab, also widely used
- [[PydanticAI]] — emits OpenAI-compatible tool-call JSON under the hood
- [[ToolUse]] — standardized via OpenAI's function-calling spec
