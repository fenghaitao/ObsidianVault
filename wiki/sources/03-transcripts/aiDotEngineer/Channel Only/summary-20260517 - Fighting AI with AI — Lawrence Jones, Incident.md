---
title: "Fighting AI with AI — Lawrence Jones, Incident"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260517 - Fighting AI with AI — Lawrence Jones, Incident.md"
author: "Lawrence Jones"
company: "incident.io"
date: 2026-05-17
tags: [ai-engineering, evals, debugging, agents, file-system, analysis-pipelines, incident-response, sre]
---

# Fighting AI with AI — Lawrence Jones, Incident

## Core Thesis

As AI systems grow too complex for humans to debug — spanning dozens of agents, hundreds of prompts, and thousands of tool calls — the only scalable solution is to use AI itself to understand and improve these systems. Lawrence Jones presents three practical patterns from incident.io's experience building an AI SRE product: making eval suites accessible to coding agents via CLI tools, downloading AI interaction traces as self-documenting file systems for agent analysis, and building repeatable analysis pipelines with parallel sub-agents that cluster failures into actionable reports.

## Key Points

### The Complexity Problem

Modern AI systems are no longer single prompts. incident.io's chatbot alone involves 10+ agents, 50+ tools, and a deep hierarchy of prompts. Their automated investigation system runs hundreds of telemetry queries, cross-referencing logs, metrics, traces, and historical incident data against the codebase. When a customer reports a bad interaction, it is no longer obvious which part of the system is responsible. Humans simply do not have enough time to trace through all this complexity.

### Eval Red-Green Cycle with Coding Agents

incident.io built a small CLI tool called `eval tool` that allows coding agents (Claude Code, Codex) to programmatically interact with eval suites stored as YAML files. This solves the context-window problem: production evals can be 2MB+ of YAML containing full incident reports, making them unusable for agents. The CLI exposes commands to list, edit, replace, and add test cases. With this, a developer can ask a coding agent: "I have a problem. Look at this prompt, create an eval proving the failure, modify the prompt so the eval passes, and check that no other evals regressed." The agent also performs a final consolidation pass to prevent prompt bloat from repeated modifications.

### File System Downloads for Agent Debugging

Instead of building MCP servers or browser-use agents for their debugging UIs, incident.io made every AI interaction downloadable as a self-documenting file system. Traces, prompts, tool calls, and results are all rendered as text files in a sandbox directory. Point Claude Code at it and ask: "What went wrong? What would you change?" Because the agent has both the trace file system and access to the codebase, it can trace through the hierarchy of agents and prompts to identify the exact code location requiring modification. This approach has been far more effective than MCP-based or human-use-agent approaches.

### Repeatable Analysis Pipelines with Parallel Sub-Agents

For system-wide analysis (thousands of investigations across hundreds of customer accounts daily), incident.io downloads batches of investigations into a file system and runs a structured analysis pipeline via Claude Code. The pipeline spins up ~25 parallel sub-agents, each analyzing one investigation, then clusters failures into cohorts to identify common failure modes. Analysis is stored incrementally in files so the pipeline can be paused and resumed. The final output is a report that explains not just accuracy scores but why the system performs well or poorly on specific accounts and what to change.

### Closing the Loop: Analysis to Code Change

The pipeline integrates with the codebase: when an agent finds a problem, it can identify the relevant code, suggest a fix, make the change, and verify it using the eval red-green cycle. The end result is a PR that directly addresses issues surfaced by the analysis pipeline. This creates a complete feedback loop from production monitoring to code improvement.

## Entities

- [[Lawrence Jones]] — Speaker, founding engineer at incident.io
- [[IncidentIo]] — Incident response management platform, building AI SRE automation
- [[ClaudeCode]] — Anthropic's coding agent, used as the primary analysis tool
- [[Codex]] — OpenAI's coding agent, also used in the workflow
- [[Netflix]] — Customer of incident.io

## Concepts

- [[Eval Red Green Cycle]] — Coding agents modifying prompts through an automated eval pass/fail loop
- [[AgentReady Eval Tooling]] — CLI tools that enable coding agents to programmatically interact with eval suites
- [[File System Downloads for Agent Debugging]] — Downloading AI interaction traces as file systems for agent analysis
- [[AI Analysis Pipelines]] — Structured, repeatable agent-driven analysis with parallel sub-agents and cohort clustering
- [[Backtesting for AI Systems]] — Running batches of investigations to measure system accuracy over time
- [[Parallel Agents]] — Using multiple concurrent sub-agents for per-entity analysis

## Related

- [[EvalEngineering]] — the practice of crafting evaluation prompts
- [[EvalFlywheel]] — the continuous improvement loop evals enable
- [[AgenticEvaluations]] — evaluating agents holistically across their workflow
- [[FileSystemAsContextEngineering]] — file system as context for agents (related but distinct pattern)
- [[Malleable Evals]] — adaptive evaluations for evolving systems
- [[AgentObservability]] — prerequisite for analysis pipelines
