---
title: "Inference-Time Interrogation"
type: concept
tags: [agents, feedback-loops, debugging, agent-observability, quality]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - LLM codegen fails and how to stop 'em — Danilo Campos, PostHog.md"]
last_updated: 2026-06-29
---

## Definition
Inference-time interrogation is the practice of asking an autonomous coding agent at the end of every run what could have been done better to set it up for success. It functions as user research where the user is the agent itself, surfacing human errors in prompt design, tool configuration, and instruction quality.

## Key Information
- Introduced by Danilo Campos (PostHog) for the PostHog Wizard
- Implemented at the stop hook of every agent run with a simple question: "What could we have done better to set you up for success in this run?"
- Discovered critical issues that would otherwise have gone unnoticed:
  - Contradictory MCP tool instructions ("you're putting me into an impossible spot")
  - Missing tools referenced in instructions (hundreds of runs with a non-existent tool)
  - Language mismatches (JavaScript instructions for Python projects)
  - Missing tool access permissions
- "If we didn't ask, we wouldn't know" — human error is the biggest threat to agent outcomes
- Human context is limited and fragmentary; we forget what we implemented last month
- Described as "fairly cheap" to implement — a small prompt at the end of each run
- Enables continuous improvement of the agent harness through systematic feedback collection

## Related
- [[summary-20260430 - LLM codegen fails and how to stop 'em — Danilo Campos, PostHog]] — source
- [[DaniloCampos]] — introduced the concept
- [[PostHogWizard]] — product that uses this technique
- [[AgentHooks]] — the stop hook mechanism
- [[ContinuousImprovement]] — broader practice
- [[Feedback Loops as AI Speed Limit]] — related concept
- [[AgentObservability]] — broader category
- [[LLMAsJudge]] — related pattern for agent evaluation
