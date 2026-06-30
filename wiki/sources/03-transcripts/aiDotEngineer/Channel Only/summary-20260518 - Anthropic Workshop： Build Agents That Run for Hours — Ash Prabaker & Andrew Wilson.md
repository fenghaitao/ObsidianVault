---
title: "summary-20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson"
type: source
tags: [source, transcript, anthropic, agents, harness, workshop]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson.md"]
last_updated: 2026-06-29
---

## Core Summary

Ash Prabaker and Andrew Wilson from Anthropic's Applied AI team present a workshop on building agents that run for hours or days. They trace Claude Code's evolution from 20-minute sessions to multi-day runs, covering the three challenges (context rot, planning failures, self-judgment bias) and how model improvements plus harness changes co-evolved. Key primitives: agent loop, sub-agents, MCP tools, skills, permissions, and the Claude Code SDK.

## Key Points

- Three challenges for long-running agents: (1) Context — finite windows, context rot, context sense anxiety. (2) Planning — models try one-shot, build half features, run out of context. (3) Verification — models are bad at judging their own output (sycophancy, superficial completeness).
- Model evolution: Opus 3.7 (~1 hour) to Opus 4.6 (~12 hours) on minimal scaffold; harness changes extend this further.
- Harness primitives: agent loop (model decides what to do, what tools to run), sub-agents for delegation, MCP for tools, skills/claude.md for context, permissions for safety.
- Claude Code was released as research preview (Feb 2025) to inform model improvements; later became GA with SDK.
- Ralph Wiggum technique (July 2025): gained traction as a verification technique for agent output.
- Co-evolution: every model release accompanied by harness changes; as models improve, harness components evolve or become less necessary.

## Related

- [[Anthropic]] — company
- [[ClaudeCode]] — coding agent and harness
- [[AgentHarness]] — core concept
- [[ClaudeAgentSDK]] — SDK for building harnesses
- [[AgentLoop]] — core primitive
- [[SubAgents]] — delegation pattern
- [[RalphWiggum]] — verification technique
