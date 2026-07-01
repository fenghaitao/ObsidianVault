---
title: "AgenticWorkflows"
type: concept
tags: [agents, automation, workflows, function-calling]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240724 - From Software Developer to AI Engineer： Antje Barth.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure.md"]
last_updated: 2026-06-29
---

## Definition
Agentic Workflows are autonomous task execution patterns where AI models independently perform multi-step operations, supported by Gemma 4's larger models through native thinking, function calling, and structured JSON outputs.

## Key Information
- Gemma 4's 31B model is purpose-built for autonomous workflows with 256K context length
- Native support for thinking, function calling, and structured JSON outputs
- 26B and 31B models are designed for complex reasoning and agentic tasks
- Cloud-hosted via AI Studio and Vertex AI for prototyping and building agentic workflows
- Supported alongside coding capabilities in the larger models
- Amazon Bedrock agents can be built with custom instructions (prompt engineering), action groups, and tools that the agent reasons through and orchestrates autonomously
- Demonstrated with a Minecraft-playing agent using Claude 3 Haiku that chains tool calls (get player location, move to location) to solve multi-step problems without explicit programming
- **Demand-Driven Context**: The Demand-Driven Context cycle (problem → failure → gap identification → human input → resolution → curation) is a specific type of agentic workflow designed for knowledge base improvement rather than task execution.

## Related
- [[Gemma4]] — 31B and 26B support agentic workflows
- [[AIStudio]] — prototyping platform for agentic workflows
- [[VertexAI]] — production platform for agentic workflows
- [[summary-20260427 - Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind]] — source
- [[summary-20240724 - From Software Developer to AI Engineer： Antje Barth]] — source (Bedrock agents with Claude)
- [[summary-20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure]] — source
- [[AmazonBedrock]] — platform for building agents
- [[Anthropic]] — Claude models used in agent demos
- [[Function Calling]] — core capability for agentic workflows
- [[DemandDriven Context]] — a knowledge-improvement agentic workflow
