---
title: "Three Pillars of Autonomy"
type: concept
tags: [framework, autonomy, agent-architecture, replit]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit.md"]
last_updated: 2026-06-25
---

## Definition
The Three Pillars of Autonomy is a framework presented by Michele Catasta of Replit for building fully autonomous coding agents. The three pillars are: (1) frontier model capabilities (baseline IQ), (2) verification (autonomous testing for local correctness at every step), and (3) context management (maintaining global coherence and managing high-level goals alongside individual tasks).

## Key Information
- **Pillar 1 — Frontier Model Capabilities**: The baseline intelligence injected into the main agentic loop. Catasta leaves this largely to model providers.
- **Pillar 2 — Verification**: Testing for local correctness at every step to prevent compounding errors. Without it, agents build "painted doors" (broken features). Replit found over 30% of individual features are broken on first pass.
- **Pillar 3 — Context Management**: Ensuring the agent is globally coherent and aligned with user intent while managing both high-level goals and individual tasks. Achieved through sub-agent orchestration, codebase-as-state, and file-system memory offloading.
- The framework targets non-technical users who cannot make technical decisions or provide technical feedback.

## Related
- [[summary-20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit]] — source
- [[Autonomous Coding Agents]] — application domain
- [[Verification in Agentic Loops]] — pillar 2 detail
- [[Context Management]] — pillar 3 detail
- [[Replit]] — company applying this framework
- [[MicheleCatasta]] — presenter
