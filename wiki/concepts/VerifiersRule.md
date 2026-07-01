---
title: "VerifiersRule"
type: concept
tags: [agents, verification, ai, economics, rl]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora.md"]
last_updated: 2026-06-26
---

## Definition
Verifier's Rule is a principle coined by Jason Warner (Poolside) stating that if a task is solvable and easy to verify, AI will solve it. It applies to both foundation models (where easy verification enables RL and post-training) and agents (where easy verification enables running an agent in a loop until it gets the right answer).

## Key Information
- Coined by Jason Warner, co-founder of Poolside and former CTO of GitHub
- Originally about foundation models: if you can make a task easy to verify, you can set up an RL environment and post-train the model to solve it
- Extended to agents: if a task is verifiable, you can run an agent in a loop telling it "you did this wrong, please fix it" until it succeeds
- Different industries and tasks fall at different points on the solvability/verifiability spectrum
- Legal examples: checking contract definitions (easy to verify, easy to solve), writing contracts (easy to solve, hard to verify — only a judge can truly verify), litigation strategy (impossible to verify — no objective truth)
- Coding examples: some parts are easy to verify, building a successful consumer app is very difficult to verify
- Strategies to bring tasks down the verifiability spectrum: use TDD (coding), use proxy verification (compare against golden contracts in legal), decompose tasks into verifiable sub-tasks, add guardrails
- The rule drives the design of agent-human collaboration: involve humans where verification is hard, let agents handle what's verifiable

## Related
- [[summary-20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora]] — source
- [[JasonWarner]] — coined the rule
- [[Poolside]] — Jason Warner's company
- [[AgentHuman Collaboration]] — trust and control framework derived from this rule
- [[Task Decomposition]] — strategy for making tasks more verifiable
- [[Guardrails]] — limiting scope to increase verifiability
- [[JacobLauritzen]] — presented the rule in context of legal AI
