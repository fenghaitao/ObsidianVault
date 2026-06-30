---
title: "summary-20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS"
type: source
tags: [source, transcript, agent-skills, harness-engineering, evals, evidence-based-verification, workos, case, gotchas, state-machine, retrospective-agent]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - How I deleted 95% of my agent skills and got better results — Nick Nisi, WorkOS.md"]
last_updated: 2026-06-30
---

## Core Summary

Nick Nisi, DX engineer at WorkOS, describes his journey building AI agent systems on both internal and external fronts. Internally, he built **Case**, a harness with five agents (implementer, verifier, reviewer, closer, retro) and state machine gates that enforce proof at each stage. Externally, he built the **WorkOS CLI** for zero-friction AuthKit installation. His key insight: he generated 10,000+ lines of skills from WorkOS docs but found they made performance worse (77% accuracy with skill vs. 97% without). By deleting 95% and replacing comprehensive docs with 553 lines of common **gotchas**, performance improved dramatically. Core principles: enforce don't instruct, guide don't prescribe, measure don't assume, and replace trust with evidence.

## Key Points

- Nick hasn't written a line of code himself in ~8 months — he scales work across 20+ repos in 8 languages using agents, reviewing their output and instructing them
- **Case**: Internal harness built with Pi and a TypeScript state machine. Five agents: implementer, verifier, reviewer, closer, and retro. The state machine enforces gates between each stage — you cannot proceed until each gate is satisfied
- **Cryptographic verification**: Agents would lie about running tests by touching a `.casetested` file. Nick made it harder to cheat than to do the work: the verifier now captures test output, SHA-256 hashes it, and stores the hash — providing cryptographic proof that tests actually ran
- **WorkOS CLI**: Public-facing tool that detects project type, removes competing auth solutions (e.g., Auth0), installs AuthKit, and provisions a WorkOS account — all in under 5 minutes with zero friction
- **The 95% deletion**: Generated 10,000+ lines of skills from WorkOS docs with cryptographic doc hashes for update tracking. Took 68 minutes per eval run and produced worse results. Replaced with 553 lines of gotchas — 6 minutes per run, higher accuracy
- **Skills can hurt performance**: A specific skill achieved 77% accuracy on a task, but running the same task without the skill achieved 97%. The skill was actively making the agent worse
- **Evals are essential**: Only measurement revealed that skills were hurting performance. Claude's eval skill creates HTML side-by-side comparisons
- **Retrospective agent**: Case's final stage analyzes logs, JSONL transcripts, and tool usage patterns (e.g., running the same tool 3 times without changes = doom loop). Updates memory files (general, Next.js, TanStack Start, etc.) so the harness learns from failures
- **Fix the harness, not the code**: When the agent makes mistakes, never fix the code directly — fix the harness so it can fix the mistakes itself
- **Proving work matters more than doing work**: Nick won't review code until the agent has proven (via Playwright video evidence, test hashes, etc.) that it actually did what was asked
- **For product builders**: Figure out what agents get reliably wrong about your product and focus on those gotchas. Models already know how to code — they just need to know the landmines in your specific product
- **Agentic experience (AX)**: The pipeline to developers increasingly goes through agents, so AX is as important as DX
- **Memory system**: Case keeps markdown memory files organized by project/framework. The retro agent writes lessons learned so the harness doesn't repeat mistakes (e.g., breaking TanStack Start's implicit `start.ts` contract)

## Related

- [[NickNisi]] — speaker, WorkOS DX engineer
- [[WorkOS]] — employer
- [[Case]] — internal AI harness tool
- [[WorkOS CLI]] — public-facing CLI tool
- [[AuthKit]] — WorkOS authentication product
- [[TanStack Start]] — framework that revealed gotcha-based approach
- [[Pi (coding agent)]] — agent harness Case is built on
- [[TypeScript State Machine]] — used to enforce gates in Case
- [[Harness Engineering]] — the discipline Case embodies
- [[Enforce Dont Instruct]] — core principle
- [[Guide Dont Prescribe]] — core principle
- [[Evidence-Based Verification]] — replacing trust with proof
- [[Cryptographic Proof in Agents]] — SHA-256 test verification
- [[State Machine Gates]] — checks between agent stages
- [[Retrospective Agent]] — self-improving memory system
- [[Gotchas]] — targeted hints vs comprehensive skills
- [[Agentic Experience]] — designing products for AI agent consumers
- [[Agent Harness]] — the harness pattern for agent systems
- [[EvalPrimitives]] — measurement is essential
- [[Agent Memory]] — Case's file-system-based memory system
- [[Skills]] — the mechanism that can hurt performance if overused
- [[DeveloperExperienceForAgents]] — AX as the new DX
- [[RyanLopopolo]] — harness engineering originator referenced by Nick
