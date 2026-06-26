---
title: "BringYourOwnAgent"
type: concept
tags: [ai, agents, vendor-neutral, integration, paperclip]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa.md"]
last_updated: 2026-06-26
---

## Definition
Bring Your Own Agent (BYOA) is a vendor-neutral approach to agent orchestration where any AI agent model or provider can be integrated into the system as an employee. Rather than being locked into a single model provider, users can select the best model for each role based on capability and cost.

## Key Information
- Core design principle of Paperclip: any agent can be brought in as an employee
- Supported agents include: Claude Code, Codex, Gemini, Pi, Hermes, OpenClaw, OpenRouter, Cursor, and more
- Via OpenRouter integration, users can access many models including free ones like Qwen 3.6+
- Different agents in the same org chart can use different models — e.g., Claude for the CEO, cheaper models for simpler tasks
- Not every agent needs frontier model pricing; match model capability to task complexity
- Addresses the problem that different coding agents (Claude, Codex, etc.) have different personalities and hook mechanisms
- Provides a vendor-neutral harness where higher-level workflows (reviewer, approver) work consistently regardless of the underlying agent model
- Enables using the best model from each lab for different purposes within the same organization

## Related
- [[Paperclip]] — the orchestrator implementing BYOA
- [[summary-20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa]] — source transcript
- [[AgentOrgChart]] — each node can use a different agent model
- [[AgentBudgets]] — cost management across different model providers
- [[OpenRouter]] — model router enabling access to many models
- [[ClaudeCode]] — one of the supported agents
- [[Codex]] — one of the supported agents
