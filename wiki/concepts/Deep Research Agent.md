---
title: "Deep Research Agent"
type: concept
tags: [agents, deep-research, mcp, web-search, content-synthesis]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition
A Deep Research Agent is an agentic system that autonomously researches a topic by planning, searching the web, analyzing sources (including YouTube videos and GitHub repositories), identifying knowledge gaps, running additional queries, and synthesizing findings into a cited research report. It is goal-driven — given an objective, it decides how to achieve it without explicit step-by-step instructions.

## Key Information
- **Core capabilities**: Plans research approach, searches the web, scrapes provided links, analyzes YouTube videos (via multimodal LLM), inspects GitHub repositories, identifies gaps and pivots, synthesizes information into a cited report
- **Architecture**: Uses MCP (Model Context Protocol) with FastMCP to expose tools. The agent harness (e.g., Claude Code) serves as the "brain" doing reasoning, while the MCP server handles capabilities (tools)
- **Three tools**: Deep research (Gemini grounded search with source citations), analyze YouTube video (Gemini multimodal — watches video frame-by-frame via file URI), compile research (assembles final research.md from .memory folder)
- **Agent reasoning**: The agent identifies gaps in research output and autonomously runs additional queries to fill them, similar to how a human researcher would notice missing information and search again
- **Memory folder**: All intermediate results are written to a .memory folder for logging, debugging, and verification before final compilation
- **Human guidance**: A guideline.md file provides the topic, key points to cover, and useful links. The more specific the guideline, the better the results
- **Content ingestion**: Uses Firecrawl and Apify for web scraping, Gemini for YouTube transcription (multimodal, not just transcript extraction), Git library for GitHub content
- **Separation from writing**: The research agent is exploratory and agentic, while the writing workflow is deterministic. They run sequentially, communicating through shared files (research.md)
- **Output**: A research.md file with cited sources, comparison tables, and synthesized findings that feeds into the writing workflow

## Related
- [[summary-20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi]] — source
- [[MCP]] — protocol used for tool exposure
- [[FastMCP]] — Python framework for building the MCP server
- [[ClaudeCode]] — agent harness used in the implementation
- [[Gemini3]] — LLM powering the research and YouTube analysis
- [[Grounded Search]] — Gemini's search with source citations
- [[Agent Skills]] — progressive disclosure pattern for agent instructions
- [[AgentHarness]] — the runtime connecting agent brain to tools
- [[EvaluatorOptimizer Pattern]] — writing workflow that consumes the research output
- [[Firecrawl]] — web scraping service used for content ingestion
- [[Apify]] — web scraping platform used for content ingestion
- [[Towards AI]] — company that built the system
- [[summary-20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind]] — source (DeepMind re-architecting with shared workspace)
- [[KP Sawhney]] — engineer who worked on the DeepMind deep research agent
- [[Antigravity]] — harness being used to re-architect deep research with shared file system collaboration
- [[Agent Workspaces]] — shared workspace collaboration pattern
- [[GeminiInteractionsAPI]] — API through which the DeepMind deep research agent is available
