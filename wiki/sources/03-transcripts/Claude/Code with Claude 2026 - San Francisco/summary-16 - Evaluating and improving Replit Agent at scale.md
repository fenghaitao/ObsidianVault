---
title: "Evaluating and Improving Replit Agent at Scale"
type: source
tags: [replit, evals, benchmarks, agent-improvement, vibe-coding, AB-testing]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - San Francisco/16 - Evaluating and improving Replit Agent at scale.md]
last_updated: 2026-06-23
---

## Core Summary

Michele Catasta, President and Head of AI at Replit, presents their approach to continuously evaluating and improving the Replit Agent, a vibe-coding platform for knowledge workers who start from natural language with no code, tests, or framework specifications. He launches VibeBench, a new open-source benchmark for end-to-end vibe coding with 20 real-world PRDs and automated AI evaluators. The talk also introduces Telescope, an internal system that clusters millions of production traces nightly to identify failure modes, automatically generates PRs with fixes, validates against VibeBench, and runs AB tests before shipping. Key insight: evals should be a continuous engine for daily improvement, not just a pre-release gate.

## Key Points

- **Vibe coding challenge:** Users start from natural language only — no framework choice, no tests, no existing code. Traditional benchmarks like SWE-bench don't capture this.
- **VibeBench:** Open-source benchmark with 20 real-world PRDs, automated AI evaluators that read code, open browsers, and step through natural-language test plans. Available at bybench.ai.
- **Five evaluation pairings:** Single-shot (PRD → app), reference implementation (add feature to working app), vibe-on-vibe (agent-built MVP + new feature), parallel decomposition (task split + merge), buggy base + feature.
- **Key findings:** ~2x gap between frontier and open-weight models. Most models perform worse when extending their own code (slop-on-slop).
- **Telescope system:** Nightly trace clustering → semantic failure grouping → LLM classification → automated PR generation → VibeBench validation → AB testing → ship or iterate.
- **AB testing infrastructure:** Essential for steady progress. Tracks run duration, cost, user sentiment, and publish rate. Results are rarely crystal clear — human taste and product philosophy still drive decisions.
- **Agent self-fixing example:** Replit Agent tried to debug environment setup issues before the environment was ready. Semantic clustering revealed the pattern despite non-deterministic traces.
- **Human role:** Formulating hypotheses about failure clusters, providing guidance to agent-generated PRs, making ship/no-ship decisions on ambiguous AB tests, and shaping which "hill" to optimize.

## Related

- [[Replit]] — the company and platform
- [[ClaudeCode]] — the coding agent used in the pipeline
- [[ClaudeFable5]] — Opus 4.7 enabling sophisticated trace analysis
- [[PromptEngineering]] — the continuous prompt refinement cycle
