---
title: "Giving Coding Agents Their Own Computers: How Cursor Built Cloud Agents"
type: source
tags: [cursor, cloud-agents, computer-use, autonomy, agent-experience, self-improving]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - San Francisco/17 - Giving coding agents their own computers： How Cursor built cloud agents.md]
last_updated: 2026-06-23
---

## Core Summary

A Cursor presenter describes their three-stage journey to giving coding agents their own cloud computers for autonomous work. Stage 1: Build an onboarding agent that explores codebases to figure out how to run them, plus dev tools (anydev CLI) for service management, test accounts, and documentation. Stage 2: Learn to leverage more capable agents by kicking off prompts instead of filing issues, giving agents larger units of work, and using computer-use demos as high-bandwidth review. Stage 3: Build the system that builds the system — agents report their own issues (WCF skill: "Work on the Factory"), validate fixes across eval sets, and iteratively improve their own workflows. The Claude onboarding agent is publicly available at cursor.com/onboard.

## Key Points

- **Onboarding agent:** Explores codebase to figure out how to run it, discovers environment variables, permissions, and services. Produces a demo. Available at cursor.com/onboard.
- **Principles of autonomy:** Give agents eyes (see everything you can see), give agents tools (run apps, use services), ensure high-quality inputs (auto-regressive nature).
- **Computer use as foundational primitive:** Raw pixels in, mouse/keyboard out. Claude 4.7 is the computer use model. Hard part is not clicking correctly but navigating one-way doors and game-over states — requires metacognition and backtracking.
- **Computer use demos as review:** Agents record demos of implemented features, providing high-bandwidth human review before code review. Critical when running many agents simultaneously.
- **Security through freedom:** Cloud agents free developers from resource management, context switching, and environment variable concerns. Made programming more enjoyable.
- **Agent Experience (AX):** Care as much about agent dev experience as human dev experience. Agents report issues via WCF skill, issues are categorized (technical, permission, ignorance), fixed by agents and humans.
- **Validated fixes:** Agents don't one-shot fixes — they kick off multiple cloud agents to validate the fix across an eval set before submitting the PR.
- **Self-improving systems:** The goal is decreasing human involvement as agents gain trust, context, and capability to solve issues end-to-end.

## Related

- [[ClaudeCode]] — the coding agent foundation
- [[ClaudeFable5]] — Claude 4.7 as the computer use model
- [[Cursor]] — the company building cloud agents
- [[ClaudeCodeSkills]] — WCF skill for self-reporting issues
