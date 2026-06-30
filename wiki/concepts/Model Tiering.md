---
title: "Model Tiering"
type: concept
tags: [agents, models, cost-optimization, scaling, fallback]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition
Model Tiering is the practice of mixing and matching AI models of different capabilities and costs within an agentic system, and seamlessly falling back to cheaper or local models when premium model quota is exhausted. The goal is to maintain agent workflow continuity while managing token costs at scale.

## Key Information
- **Mixing models by component**: Use cheaper models (e.g., Gemma 4 on local GPUs/TPUs) for routine agent operations and reserve advanced models for specific, high-value components of the agentic system
- **Seamless fallback**: When a user hits their token limit on a premium model, the harness should automatically switch to a fallback model (e.g., Flash instead of Pro, or a local model) without interrupting the workflow
- **Preference over hard limits**: Instead of the user returning to find their agent spent the last hour doing nothing because it hit a quota limit, the system should degrade gracefully
- **Gemma 4 as free tier**: Gemma 4 running on local GPUs/TPUs is effectively free from a quota perspective, making it an ideal fallback or primary model for less demanding agent operations
- **Workflow continuity**: The key insight is that interrupting a long-running agent task because of quota exhaustion is worse than completing it with a slightly less capable model — the notification should not be "we ran out of quota" but rather "task completed (using fallback model)"
- **Google context**: Within Google, engineers have worse rate limits than external customers because Google prioritizes customer access over internal usage

## Related
- [[Agent Quota Management]] — the problem model tiering helps solve
- [[Tokenomics]] — the economic motivation for tiering
- [[Gemma4]] — the "free tier" model for agent components
- [[HybridInference]] — related concept of mixing inference providers
- [[Local Models for Agents]] — running models locally for agents
- [[Credit-Based Pricing]] — pricing model that enables tiering
- [[AgentHarness]] — the harness must support model switching
- [[summary-20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind]] — source
