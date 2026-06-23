---
title: "The Thinking Lever (San Francisco)"
type: source
tags: [test-time-compute, thinking, reasoning, effort, adaptive-thinking]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - San Francisco/14 - The thinking lever.md]
last_updated: 2026-06-23
---

## Core Summary

Matt Bleifer from Anthropic's research team presents on test-time compute scaling, covering the same core concepts as the London version but with additional detail on adaptive thinking, task budgets, and practical effort level guidance. The talk explains three token types (thinking, tool calling, text), adaptive thinking as the evolution beyond interleaved thinking, and provides rules of thumb for effort level selection. Key additions include the concept of task budgets (upper bounds on token spend before checking in) and the Claude Plays Pokémon insight where low effort produced clever speedrun strategies.

## Key Points

- **Three token types:** Thinking (internal monologue), tool calling (interfacing with world), text (communicating with user). All three are fundamental to how Claude works.
- **Adaptive thinking:** Claude freely chooses when to think, call tools, or output text in any order. Not a model router — it's giving Claude the option to think at every step rather than mandating thinking at specific points.
- **Task budgets:** New feature allowing users to set upper bounds on tokens before Claude checks in. Can be expressed in tokens, time, or cost.
- **Effort level guidance:** Max (hardest tasks, diminishing returns), Extra High (default for Claude Code/Claude.ai, best for coding/agentic), High (good balance for intelligence-sensitive use cases), Medium (cost-sensitive), Low (latency-sensitive, short-scope).
- **Model size vs. effort:** Low effort on larger model often beats high effort on smaller model for intelligence-demanding tasks. Small models best for low time-to-first-token and bulk simple tasks.
- **Claude Plays Pokémon:** On low effort, Claude treated the game as a speedrun — skipping battles, using repels, stocking healing items — demonstrating clever strategy, not lower intelligence.
- **North Star:** Users set quality bar and budget; Claude autonomously allocates compute to maximize performance.

## Related

- [[summary-14 - The thinking lever]] — London version of the same talk
- [[ClaudeFable5]] — Opus 4.7 enabling these capabilities
- [[AdaptiveThinking]] — the concept of models choosing when to reason
- [[ClaudeCode]] — defaults to extra high effort
