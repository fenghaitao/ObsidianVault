---
title: "OpenClaw"
type: entity
tags: [tool, second-brain, agent, open-source, security, personal-assistant]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260402 - Full Guide - Build Your Own AI Second Brain with Claude Code.md"
last_updated: 2026-06-20
---

## Definition

OpenClaw is an open-source, out-of-the-box personal AI assistant / [[SecondBrain]] application that took the internet by storm in 2026. [[ColeMedin]] treats it as a key reference point: a beautifully-crafted app to *take inspiration from* but **not run directly** — because, as an out-of-the-box agent with broad permissions, it's exposed to the [[LethalTrifecta]] in ways you can't easily control or understand.

> Note: also referenced as "Nemo Claw" in Cole's content as a related/forked solution. Treat as the same family of out-of-the-box second-brain agents.

## Key Information

### Why it matters

OpenClaw is the foil in Cole's "build your own [[SecondBrain]]" argument. It's impressive enough that the obvious question is "why not just run OpenClaw?" — and Cole's answer frames the entire build-your-own thesis.

### Cole's critique (the [[LethalTrifecta]] argument)

OpenClaw has all three lethal-trifecta pillars (private data access, untrusted content, exfiltration) — unavoidable for a useful second brain. The problems:

- **Doesn't limit private-data-access and exfiltration well** — broad default permissions.
- **Huge code base you don't understand** — you can't reason about how the trifecta affects you, or easily adjust it.
- **Gives lots of control to an AI agent in ways that aren't transparent** to the operator.

Cole credits OpenClaw with real security progress (prompt-injection handling has improved) and calls it "constantly evolving" and "beautifully crafted" — but the fundamental issue of running a large opaque agent with broad permissions remains.

### How Cole uses it: inspiration, not execution

The key move in `summary-full-guide-ai-second-brain`: Cole pointed [[ClaudeCode]] at OpenClaw's open-source repo and said "see how they implement the memory layer (`soul.md`, `user.md`, `memory.md`) and the heartbeat (proactive part), and bring those ideas into my own version." So he:

- **Takes** OpenClaw's good architecture (memory layer files, heartbeat for proactivity).
- **Leaves** the parts he can't control / that create security risk.
- **Builds his own** on [[ClaudeCode]] + [[ClaudeSkills]] + [[Obsidian]] with zero-trust permissions he layers deliberately.

"Stand on the shoulders of giants" — without running the giant.

### What Cole borrowed specifically

- **Memory layer**: `soul.md` (personality), `user.md` (facts about the user), `memory.md` (key decisions) — loaded at session start.
- **Heartbeat**: the proactive loop that gathers context and acts without explicit prompting.

These appear in Cole's [[SecondBrain]] architecture, reimplemented on his own controlled stack.

## Related

- [[SecondBrain]] — the category OpenClaw belongs to; Cole's build-your-own alternative
- [[LethalTrifecta]] — the security model Cole uses to critique running OpenClaw directly
- [[ClaudeCode]] — what Cole builds his alternative on
- [[ClaudeSkills]] — capability layer of the alternative
- [[Obsidian]] — canvas of the alternative
- [[ColeMedin]] — the inspiration-not-execution stance
- [[summary-full-guide-ai-second-brain]] — primary source
