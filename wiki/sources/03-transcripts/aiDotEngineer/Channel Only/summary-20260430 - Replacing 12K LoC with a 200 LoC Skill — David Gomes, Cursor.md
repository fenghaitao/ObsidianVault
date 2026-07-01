---
title: "summary-20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor"
type: source
tags: [source, transcript, cursor, skills, worktrees, agent-isolation, best-of-n, evals]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor.md"]
last_updated: 2026-06-29
---

## Core Summary

David Gomes from Cursor describes how they replaced a ~15,000-line code implementation of Git work trees and "best of N" features with a ~200-line markdown skill/command. By leveraging two existing primitives — agent skills and sub-agents — they re-implemented the entire feature in markdown instructions. The new approach reduces maintenance burden for a power-user feature, enables mid-chat work tree switching, and works across multi-repo setups. The main trade-off: trusting the model to stay within its work tree (vibes-based safety) instead of mechanical enforcement. Future improvements focus on evals (using Braintrust and Cursor CLI) and RL training for Cursor's in-house Composer model.

## Key Points

- Work trees in Cursor are separate Git checkouts that let agents work in parallel without interfering with each other. They shipped in October 2025 alongside Cursor 2.0.
- The "best of N" feature lets users give the same task to different models simultaneously and compare their implementations, with a judge model picking the best one.
- The original implementation was ~15,000 lines of code with complex logic for creating, managing, scoping, and cleaning up work trees.
- The new implementation uses two primitives: agent skills (markdown instructions loaded on demand) and sub-agents (specialized agents for bounded subtasks).
- The /worktree command is ~200 lines of markdown; the /bestofn command is ~40 lines. They are server-controlled commands (not local skills) so Cursor can iterate prompts without user updates.
- Commands include: /worktree (isolated agent), /bestofn (competing models), /applyworktree (merge changes), /deleteworktree (cleanup).
- Pros of the new approach: dramatically less code to maintain, mid-chat work tree switching, multi-repo support, superior judging experience where the parent agent can stitch together pieces from different implementations.
- Cons: agents sometimes forget to stay in their work tree (especially over long sessions or with weaker models like Haiku), it feels slower (agent visibly creates work trees in chat), and discoverability is worse (no UI dropdown — users must know the slash command exists).
- Cursor is improving the skill through evals (using Braintrust and headless Cursor CLI with two scorers: "did work in work tree" and "did work in primary checkout") and RL training for Composer.
- Cursor 3.0 will have a more native work trees implementation in its new agentic interface, plus exploration of non-Git parallelization primitives.

## Related

- [[DavidGomes]] — speaker, Cursor engineer
- [[Cursor]] — the product
- [[Cursor3]] — announced agentic interface rewrite
- [[Composer]] — Cursor's in-house trained model
- [[Braintrust]] — eval platform used for work tree evals
- [[GitWorktrees]] — the Git feature underlying Cursor's parallel agent pattern
- [[BestOfN]] — competing multiple models on the same task
- [[Skills]] — markdown-based agent instructions
- [[SubAgents]] — specialized agents for bounded subtasks
- [[MarkdownAsCode]] — using markdown prompts instead of traditional code
- [[AgentIsolation]] — ensuring agents stay within their designated work scope
- [[VibesBasedSafety]] — trusting the model instead of mechanical enforcement
- [[FeatureDiscoverability]] — trade-off between simplicity and user discoverability
- [[CrossPlatformCompatibility]] — skills needing platform-specific instructions
- [[AgentCommandsVsSkills]] — server-controlled prompts vs local skills
- [[LLMAsJudge]] — judging best-of-N outputs
- [[HeadlessEvals]] — using CLI for agent evaluation
- [[Parallel Agents]] — multiple agents working concurrently
- [[MultiRepoWorktrees]] — work trees spanning multiple repositories
- [[ReinforcementLearningWithLLMs]] — RL training for Composer
- [[ModelBehavior]] — model deviation from work tree instructions
