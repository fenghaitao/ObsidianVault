---
title: "What the Best Agents Share — Mardu Swanepoel, Flinn AI"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260526 - What the Best Agents Share — Mardu Swanepoel, Flinn AI.md"
date: 2026-05-26
author: "Mardu Swanepoel"
organization: "Flinn AI"
conference: "aiDotEngineer"
playlist: "Channel Only"
tags: [agents, design-patterns, UX, agent-architecture]
---

# What the Best Agents Share — Mardu Swanepoel, Flinn AI

## Core Summary

Mardu Swanepoel (Flinn AI) distills four design patterns shared by the best AI agents, drawn from studying [[Cursor]], [[ClaudeCode]], [[Harvey]], and [[Manifold]]. Opening with Picasso's quote about stealing (deeply studying to make something your own), he argues that agent builders should learn from these exemplars. The four patterns are: **Focus Modes** (constraining action and input space per mode for better quality and aligned user expectations), **Transparent Execution** (showing tool calls, reasoning, and progress to shift from delegation to collaboration), **Personalization** (encoding user principles, playbooks, and memory to accelerate speed-to-understanding), and **Reversibility** (undo capabilities at line, file, and conversation-state granularity to bound the cost of mistakes and encourage bolder use). Each pattern is illustrated with concrete examples from leading agent products.

## Key Points

1. **Focus Modes** — Put the agent in a specific mode (planning, debug, research) that constrains its action and input space. This improves output quality on a smaller, optimized surface and aligns user expectations. Cursor exemplifies this with its drop-down mode selector: planning mode produces no code, debug mode follows a hypothesis-driven approach.

2. **Transparent Execution** — Make the agent's thinking, tool calls, and progress fully visible to the user. This shifts the dynamic from delegation to collaboration, builds trust in outputs, and lets users intervene early if the agent goes wrong. Claude co-work shows a progress list, tool call inputs/outputs, and skills in use. Manifold similarly exposes task progress and what it examined.

3. **Personalization** — Encode the user's thoughts, systems, knowledge, principles, and patterns into the agent. The goal is speed-to-understanding (not just speed-to-outcome): the agent must grasp what the user would have done and how. Harvey uses playbooks (legal firm methods for contract review) and memory that persists across interactions. Claude uses skills, connectors, and systems for personalization.

4. **Reversibility** — Give users the ability to undo agent actions at multiple levels of granularity. This bounds the cost of mistakes, making the ROI calculation easier and encouraging bolder, higher-value use. Cursor offers line-level accept/reject, file-level accept, conversation-state rollback, and parallel outputs from different models. Harvey integrates with native Microsoft Word change tracking for reviewer-style acceptance.

5. **Picasso's "Steal"** — The talk's framing principle: studying agents deeply, understanding what they do, and making it your own to build something better and unique.

## Related

### Entities
- [[MarduSwanepoel]] — Speaker, founder of Flinn AI.
- [[FlinnAI]] — Mardu Swanepoel's company.
- [[Cursor]] — AI-powered code editor with focus modes and reversibility.
- [[ClaudeCode]] — Anthropic's coding agent with transparent execution.
- [[Harvey]] — Legal AI with playbooks and memory for personalization.
- [[Manifold]] — AI coding agent with transparent task progress.
- [[PabloPicasso]] — Artist quoted on stealing as deep study and remixing.

### Concepts
- [[FocusModes]] — Constraining agent action/input space per mode for quality and aligned expectations.
- [[TransparentExecution]] — Making agent thinking, tool calls, and progress visible for trust and collaboration.
- [[AgentPersonalization]] — Encoding user principles and patterns into agents for speed-to-understanding.
- [[Reversibility]] — Undo capabilities at multiple granularities to bound mistake cost.
