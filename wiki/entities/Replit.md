---
title: "Replit"
type: entity
tags: [company, coding-agents, ai, developer-tools]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260501 - Agents on the Canvas in tldraw — Steve Ruiz, tldraw.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure.md"]
last_updated: 2026-06-29
---

## Definition
Replit is a company building an autonomous coding agent (Replit Agent) designed for non-technical users, aiming to empower every knowledge worker to create software without needing to make technical decisions.

## Key Information
- Building a coding agent for non-technical users, launched first version in September 2024.
- The Replit Agent has gone through multiple generations: initial React-based agents, native tool calling agents, and autonomous agents (B3 launched a couple months before December 2025).
- Defaults to Gemini 3.1 Pro for its agent system, selected for performance and cost reasons.
- Focuses on a "Waymo experience" where users don't need a "driving license" (technical expertise) to use the agent.
- Key technical innovations include autonomous testing via Playwright code generation, sub-agent orchestration for context management, and the core loop as orchestrator for parallel agents.
- Found that over 30% of individual features built by agents are broken on first pass ("painted doors").
- Improved memories-per-compression from ~35 to ~45-50 through sub-agent orchestration.
- Uses tldraw SDK for its agent canvas, enabling spatial agent interaction.
- **Demand-Driven Context**: Referenced as an example of how far AI coding agents have come — "by the time you make instant noodles, you already have a million-dollar app already working on your laptop" using Replit. This highlights the gap between AI's code generation capabilities and enterprise delivery (Jira tickets not moving).

## Related
- [[summary-20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit]] — source
- [[summary-20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind]] — source
- [[summary-20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure]] — source
- [[MicheleCatasta]] — leader at Replit
- [[ReplitAgent]] — product
- [[Three Pillars of Autonomy]] — framework
- [[Autonomous Coding Agents]] — category
- [[Gemini 3.1 Pro]] — default model for agent system
- [[summary-20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop]] — source (referenced as scale where LLM-on-every-output becomes expensive)
- [[Raindrop]] — referenced Replit scale as example of why trained classifiers beat LLM-as-judge for observability
