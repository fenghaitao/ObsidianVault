---
title: "Samridhi"
type: entity
tags: [person, towards-ai, machine-learning, technical-writing, deep-research]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi.md"]
last_updated: 2026-06-26
---

## Definition
Samridhi is a machine learning engineer, technical writer, and consultant who helps Towards AI grow. She presented the deep research agent portion of the workshop, covering MCP server architecture with FastMCP, tool registration, and agent skills.

## Key Information
- Machine learning engineer and technical writer
- Consultant helping Towards AI grow
- Presented the deep research agent architecture in the workshop: MCP server with three tools (deep research, analyze YouTube video, compile research)
- Demonstrated how FastMCP simplifies MCP server creation by hiding protocol complexities
- Explained the three MCP primitives: tools (actions), prompts (instructions), and resources (static data)
- Showed how Claude Code serves as the agent harness (brain/reasoning) while the MCP server handles capabilities
- Demonstrated agent skills as a replacement for inline prompts, using progressive disclosure to manage context
- Highlighted how the agent identifies research gaps and runs additional queries autonomously
- Showed Gemini's multimodal YouTube analysis: sending video URL as file URI, Gemini watches frame-by-frame

## Related
- [[summary-20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi]] — source
- [[Towards AI]] — company she consults for
- [[LouisFrançois Bouchard]] — co-presenter
- [[Paul Iusztin]] — co-presenter
- [[aiDotEngineer]] — conference where the workshop was presented
- [[Deep Research Agent]] — system she presented
- [[MCP]] — protocol used for tool exposure
- [[FastMCP]] — Python framework for building MCP servers
- [[Agent Skills]] — progressive disclosure pattern for agent instructions
- [[ClaudeCode]] — agent harness used in the demo
- [[Gemini3]] — LLM used for research and YouTube analysis
- [[Grounded Search]] — Gemini search with source citations
