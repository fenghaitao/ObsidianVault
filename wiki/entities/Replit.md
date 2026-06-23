---
title: "Replit"
type: entity
tags: [company, coding-platform, vibe-coding, app-building, agents]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - San Francisco/16 - Evaluating and improving Replit Agent at scale.md, raw/03-transcripts/Claude/The Problem Solvers/04 - The Problem Solvers： Michele Catasta at Replit.md]
last_updated: 2026-06-23
---

## Definition

Replit is a vibe-coding platform that lets anyone build applications from natural language descriptions with no coding skills required. Users express ideas in natural language and see them turn into working applications and websites. Led by Michele Catasta, Replit has crossed 40 million registered users and pioneered automated evaluation systems for vibe-coding agents.

## Key Information

- **Natural language to app:** Users describe what they want; Replit Agent builds it — no framework choice, no tests, no code required.
- **VibeBench:** Open-source benchmark for end-to-end vibe coding with 20 real-world PRDs and automated AI evaluators.
- **Telescope:** Internal system clustering millions of production traces nightly to identify failure modes and auto-generate fixes.
- **Multi-agent system:** Refactoring agents, pre/post-deployment security agents, and long-term memory that learns across all apps.
- **Model choice:** Started with Sonnet 3.5 (early 2024); Anthropic has kept the lead in coding models since.
- **Deployment rates:** Improved from 84% to 98% through tightening feedback loops.
- **40 million users:** People who never felt permission to create software are now building businesses.

## Related

- [[summary-evaluating-replit-agent-at-scale]] — evals and Telescope talk
- [[summary-problem-solvers-replit]] — problem solvers profile
- [[ClaudeFable5]] — Opus as the workhorse model
- [[ClaudeCode]] — related coding agent
- [[Anthropic]] — model provider and partner
