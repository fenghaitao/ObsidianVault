---
title: "RL Environments"
type: concept
tags: [ai, reinforcement-learning, post-training]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/40 - The $1B Al company training ChatGPT, Claude & Gemini on the path to responsible AGI ｜ Edwin Chen.md"]
last_updated: 2026-07-12
---

## Definition

RL (reinforcement learning) environments, as described by [[Edwin Chen]] (CEO, [[Surge AI]]), are rich, game-like simulations of real-world work — complete with characters, businesses, tools, and interacting systems — used to train AI models on long-horizon, multi-step, ambiguous tasks that isolated single-step benchmarks fail to capture.

## Key Information

- Example given: a simulated startup with Gmail messages, Slack threads, GitHub PRs, and a full codebase — then AWS and Slack suddenly go down, and the model must figure out what to do, given rewards for good/bad handling.
- Rationale: models that look highly capable on isolated, single-step benchmarks (tool calling, instruction following) often "fail catastrophically" once dropped into messy, ambiguous, long-horizon environments where earlier actions affect much-later steps and unfamiliar tools must be navigated.
- Task design pattern: an expert (e.g., a financial analyst) doesn't just write grading rubrics anymore — they design an entire environment (e.g., an Excel spreadsheet, a Bloomberg-terminal-like tool the model must learn to call) with rewards defined by checking specific outcomes (e.g., does cell B22 contain the correct profit/loss figure).
- **Trajectories matter, not just final answers**: Chen stresses that a model can reach a correct result through wasteful, inefficient, or reward-hacked intermediate steps (e.g., 50 failed attempts before randomly landing on the right number); training only on final-answer correctness discards crucial information about *how* the model should behave along the way (e.g., reflecting vs. one-shotting).
- Positioned as the latest stage in an evolving sequence of post-training methods — SFT (mimicking a master) → RLHF (ranking many candidate outputs) → rubrics/verifiers (detailed graded feedback) → RL environments (learning by doing, in simulated real-world settings) — which Chen frames as complementary layers rather than a strict linear replacement, paralleling how humans learn a skill through many different, coexisting methods (reading, practicing, getting feedback, developing taste from exposure to good and bad examples).

## Related

- [[summary-40 - The $1B Al company training ChatGPT, Claude & Gemini on the path to responsible AGI ｜ Edwin Chen]] — source summary
- [[Edwin Chen]] — describes this framework in depth
- [[Surge AI]] — builds these environments as a core product
- [[LM Arena Gaming]] — contrasted flawed evaluation approach these environments aim to improve on
