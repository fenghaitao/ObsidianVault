---
title: "Proof"
type: entity
tags: [product, tool, every, writing, open-source]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/08 - AI predictions： Job markets, Codex beats Claude, and the death of org charts ｜ Dan Shipper.md"]
last_updated: 2026-07-10
---

## Definition

Proof is an online markdown editor built by [[Dan Shipper]] at [[Every]], used as his primary writing surface and as the codebase behind his "[[Senior Engineer Benchmark]]."

## Key Information

- Dan writes documents in Proof with [[Codex]]'s in-app browser open on the page, watching and editing alongside him — his core example of an agent-plus-browser work surface.
- Deliberately simplified relative to legacy word processors (e.g., skips manual formatting/page-break/table tooling) because the agent handles that; Dan argues this lets agent-native products start simpler and faster than legacy productivity software.
- Users bring their own AI tokens by running their own agent against Proof rather than Proof having to pay for AI tokens itself — cited as an example of SaaS margins improving rather than eroding in an agent-heavy world.
- Proof is open source; when users' agents encounter a bug, the agent files a structured bug report (exact repro steps, and even suggested code-base fixes) directly as a GitHub issue, which Every can then hand to an agent to fix.
- Was originally vibe-coded by Dan on the side while running the rest of Every; broke repeatedly in production right after launch (a formative, embarrassing experience that led him to get two senior engineers to independently rewrite the codebase, which became the basis of the Senior Engineer Benchmark). Dan says he got "vibe coder elbow" (a repetitive-strain injury) from over-working the launch.

## Related

- [[summary-08 - AI predictions： Job markets, Codex beats Claude, and the death of org charts ｜ Dan Shipper]] — source summary
- [[Dan Shipper]] — builder of Proof
- [[Every]] — company that owns Proof
- [[Codex]] — agent Dan uses inside Proof via its in-app browser
- [[Senior Engineer Benchmark]] — benchmark built on Proof's codebase
- [[Vibe Coding]] — how Proof was originally built
- [[GitHub]] — where agent-filed bug reports on Proof become issues
