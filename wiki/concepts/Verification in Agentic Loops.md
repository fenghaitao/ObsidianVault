---
title: "Verification in Agentic Loops"
type: concept
tags: [testing, agents, verification, quality-assurance]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md"]
last_updated: 2026-06-25
---

## Definition
Verification in agentic loops is the practice of testing for local correctness at every step an agent takes, to prevent compounding errors and ensure that agent outputs are truthful rather than hallucinated. It is the second pillar of Replit's autonomy framework.

## Key Information
- Without verification, agents build "painted doors" — features that appear complete but are broken (e.g., buttons without handlers, mock data instead of real data).
- Replit found over 30% of individual features are broken on first pass, and nearly every application has at least one broken feature.
- Spectrum of verification: static code analysis (LSPs) → code execution/debugging → unit test generation → API testing → browser-based autonomous testing.
- Autonomous testing breaks the feedback bottleneck: agents no longer need to wait for human QA feedback.
- Replit's approach uses Playwright code generation for programmatic testing, with computer use as a fallback.
- Playwright-based testing is roughly an order of magnitude cheaper and faster than computer-use approaches.
- Tests written in Playwright become reusable regression test suites.
- Thariq Shihipar emphasizes verification should happen "everywhere you can, just constantly" — not just at the end of the loop
- Deterministic verification is preferred: rules and heuristics (null checks, lint, compile, read-before-write checks) are more reliable than model-based verification
- Claude Code example: if the agent tries to write to a file it hasn't read yet, a hook throws an error telling it to read first
- Hooks are the mechanism for inserting deterministic verification at event boundaries in the Agent SDK
- Sub-agents can be used for adversarial verification: start a fresh context, feed it the output, and tell it to critique
- Verification strength determines how general an agent can become — agents with strong verification (like code with compile/lint) are better candidates for autonomy
- State reversibility matters: code is highly reversible (git undo), computer use is not (complex state machines compound errors)

## Related
- [[summary-20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit]] — source
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[Three Pillars of Autonomy]] — parent framework
- [[Painted Doors]] — problem this solves
- [[Browser-based Autonomous Testing]] — implementation approach
- [[Playwright]] — key tool
- [[AgentLoop]] — the three-part loop where verification fits
- [[Hooks]] — mechanism for deterministic verification
- [[SwissCheeseDefense]] — security model with verification layer
