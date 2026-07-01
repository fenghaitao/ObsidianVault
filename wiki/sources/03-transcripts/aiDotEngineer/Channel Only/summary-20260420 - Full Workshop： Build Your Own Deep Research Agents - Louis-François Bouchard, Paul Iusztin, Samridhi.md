---
title: "summary-20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi"
type: source
tags: [source, transcript, ai, deep-research, agents, mcp, fastmcp, linkedin, writing-workflow, evaluator-optimizer, observability, evals, llm-as-judge, towards-ai, gemini, claude-code]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - Full Workshop： Build Your Own Deep Research Agents - Louis-François Bouchard, Paul Iusztin, Samridhi.md"]
last_updated: 2026-06-26
---

## Core Summary
A 2-hour workshop by the Towards AI team (Louis-François Bouchard, Paul Iusztin, and Samridhi) demonstrating how to build an end-to-end deep research and technical writing system. The system takes a topic, performs deep web research using an MCP-based agent, and then uses a deterministic writing workflow with an evaluator-optimizer loop to produce polished LinkedIn posts that pass AI slop detectors. The workshop covers AI engineering fundamentals (workflows vs agents, autonomy slider, context budget), MCP server architecture with FastMCP, agent skills, writing profiles, few-shot examples, observability with Opic, and AI evals with LLM-as-judge calibration.

## Key Points
- **AI Engineering Problem Space**: All decisions are governed by cost-per-task, latency, quality, and data privacy constraints. An "autonomy slider" goes from simple prompting to agentic systems — more autonomy means less control and higher cost
- **Workflows vs Agents**: Workflows are predetermined step sequences (always same order, same steps). Agents need to take autonomous actions and react to environment changes. Most client requests for "agents" are actually simple workflows
- **Context Budget Management**: Context grows through system prompts, tool definitions, few-shot examples, retrieved data, and conversation history. Performance degrades well before context window limits due to the "lost in the middle" problem. Techniques include trimming, summarizing, retrieval, compaction, and delegation to tools/sub-agents
- **Multi-Agent Systems**: Used when context becomes too large (over 20 tools), when autonomous decision-making is needed across domains, or for security/compliance isolation. Real AI products combine workflows, tools, and agents
- **Deep Research Agent Architecture**: Uses MCP with FastMCP to expose three tools — deep research (Gemini grounded search), analyze YouTube video (Gemini multimodal, watches the video frame-by-frame), and compile research (assembles final research.md). Claude Code serves as the agent harness (brain) while the MCP server handles capabilities
- **Agent Skills**: Compact, concise way to tell agents about capabilities and workflows. Uses progressive disclosure — only the name and description load initially, full body loads on query execution, then wipes from context. More maintainable and shareable than inline prompts
- **Writing Workflow Architecture**: Three phases — build context (guideline + research + static profiles + few-shot examples → system prompt), generate first draft via LLM, apply evaluator-optimizer loop (writer → reviewer → editor, 3-4 iterations)
- **Writing Profiles**: Static markdown files defining structure (LinkedIn post format, character counts), terminology (banned AI slop words), and character profile (author personality/style). The guideline.md is the only dynamic user input
- **Few-Shot Examples**: High-quality, varied LinkedIn posts used in the system prompt. Start with a larger number and trim down to minimize context bloat. Three examples used as a starting point
- **Evaluator-Optimizer Pattern**: Writer and reviewer use separate context windows to avoid bias. Reviewer outputs structured Pydantic objects with profile, location, and comment attributes. Reviews are prioritized: guideline first, then research, then profiles. Fixed iteration count (3-4) instead of score-based thresholding
- **Observability with Opic**: Captures threads (full workflow conversations), traces (individual LLM/tool calls), latency, cost, token usage. Essential for debugging agentic systems beyond raw logs
- **AI Evals**: Build a labeled dataset (20 real LinkedIn posts, reverse-engineered guidelines, generated outputs, binary pass/fail labels with critiques), train/dev/test split, build LLM-as-judge evaluator, calibrate against dev split using F1 score, validate on test split. Treat evals like training a machine learning model
- **Technology Stack**: Python, UV for dependency management, Gemini (Pro and Flash) for all LLM calls, Firecrawl and Apify for web scraping, FastMCP for MCP server, Claude Code as agent harness, Opic for observability, Pydantic for structured outputs

## Related
- [[LouisFrançois Bouchard]] — speaker, CTO of Towards AI
- [[Paul Iusztin]] — speaker, author of LLM Engineer's Handbook
- [[Samridhi]] — speaker, ML engineer and technical writer
- [[Towards AI]] — educational company behind the workshop
- [[aiDotEngineer]] — conference/YouTube channel
- [[Deep Research Agent]] — core concept built in the workshop
- [[EvaluatorOptimizer Pattern]] — writing workflow refinement loop
- [[Writing Profiles]] — static styling layer for content generation
- [[Autonomy Slider]] — spectrum from prompting to agentic systems
- [[Context Budget]] — managing context window constraints
- [[Lost in the Middle]] — long-context model performance degradation
- [[Grounded Search]] — Gemini's search with source citations
- [[Agent Skills]] — progressive disclosure for agent instructions
- [[AgenticWorkflows]] — predetermined step sequences
- [[MultiAgentArchitecture]] — when to split into multiple agents
- [[AgentObservability]] — monitoring and tracing agent systems
- [[LLMAsJudge]] — evaluation technique used for post quality
- [[FewShotExamples]] — in-context learning for generation and evaluation
- [[Structured Outputs]] — Pydantic objects for reviewer feedback
- [[MCP]] — Model Context Protocol for tool exposure
- [[FastMCP]] — Python framework for building MCP servers
- [[ClaudeCode]] — agent harness used in the workshop
- [[Gemini3]] — LLM used for research and writing
- [[Firecrawl]] — web scraping service
- [[Apify]] — web scraping platform
- [[Opic]] — observability platform
- [[Pydantic]] — structured output library
- [[UV]] — Python package manager
- [[EvalEngineering]] — building and calibrating evaluation systems
- [[Slop]] — AI-generated low-quality content the system aims to avoid
- [[AgentHarness]] — the runtime that connects agent brain to tools
