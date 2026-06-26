---
title: "AgentBudgets"
type: concept
tags: [ai, agents, cost-management, budgeting, paperclip]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa.md"]
last_updated: 2026-06-26
---

## Definition
Agent budgets are per-agent and per-project spending limits in Paperclip that track monthly inference costs. They enable cost control across an organization of AI agents, allowing users to manage spend as agent teams scale.

## Key Information
- Paperclip tracks monthly spend at both the agent level and project level
- Users can set budgets per agent and per project to control costs
- Supports subscription-based models (e.g., Claude and Codex subscriptions) where costs may not immediately appear
- As teams scale, subscription-based pricing may give way to usage-based costs
- Enables cost-conscious agent selection: cheaper models (e.g., Qwen 3.6+ via OpenRouter, free tier) can be used for simpler tasks
- Practical advice: not every agent needs frontier model pricing — match model cost to task complexity
- Part of the broader vision of running a zero-human company with financial controls

## Related
- [[Paperclip]] — the orchestrator implementing agent budgets
- [[summary-20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa]] — source transcript
- [[BringYourOwnAgent]] — budget considerations drive model selection
- [[ZeroHumanCompany]] — financial controls for AI-run businesses
- [[OpenRouter]] — provides access to free and cheap models
