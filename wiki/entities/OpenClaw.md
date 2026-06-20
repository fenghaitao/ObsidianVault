---
title: "OpenClaw"
type: entity
tags: [tool, second-brain, agent, open-source, security, personal-assistant]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260402 - Full Guide - Build Your Own AI Second Brain with Claude Code.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260212 - I Built a Safer OpenClaw Alternative Using Claude Code.md"
last_updated: 2026-06-20
---

## Definition

OpenClaw is an open-source, out-of-the-box personal AI assistant / [[SecondBrain]] application that took the internet by storm in 2026 — **~185,000 GitHub stars** (surpassing even [[N8N]]), created by **Peter**. [[ColeMedin]] treats it as a key reference point: a beautifully-crafted app to *take inspiration from* but **not run directly** — because, as an out-of-the-box agent with broad permissions, it's exposed to the [[LethalTrifecta]] in ways you can't easily control or understand, on top of concrete code-level vulnerabilities.

> Note: **Nano Claw** is a *separate* lightweight, more-secure OpenClaw-style assistant Cole mentions — not a fork — which didn't meet his requirements, so he built his own. (An earlier note in this wiki called it "Nemo Claw"; the correct reference is Nano Claw.)

## Key Information

### Why it matters

OpenClaw is the foil in Cole's "build your own [[SecondBrain]]" argument. It's impressive enough that the obvious question is "why not just run OpenClaw?" — and Cole's answer frames the entire build-your-own thesis.

### Cole's critique (the [[LethalTrifecta]] argument)

OpenClaw has all three lethal-trifecta pillars (private data access, untrusted content, exfiltration) — unavoidable for a useful second brain. The problems:

- **Doesn't limit private-data-access and exfiltration well** — broad default permissions.
- **Huge code base you don't understand** — you can't reason about how the trifecta affects you, or easily adjust it.
- **Gives lots of control to an AI agent in ways that aren't transparent** to the operator.

Cole credits OpenClaw with real security progress (prompt-injection handling has improved) and calls it "constantly evolving" and "beautifully crafted" — but the fundamental issue of running a large opaque agent with broad permissions remains.

### The four "magical" components (what Cole borrows)

Per `summary-safer-openclaw-alternative`, four components make OpenClaw feel magical:

1. **Memory system** — entirely markdown-driven: `soul.md` (agent identity, evolves), `user.md` (model of the user), `memory.md` (core memories), `agents.md` (behavior / global rules), plus daily **session logs**; a SQLite DB adds light RAG for search.
2. **Heartbeat** — a `heartbeat.md` the agent consults on a schedule to act proactively (draft emails, open PRs) without being asked.
3. **Channel adapters** — talk to it from WhatsApp/Telegram/Slack/Discord with thread support.
4. **Skills registry** — add a capability with one file; shareable.

### Security problems (the concrete vulnerabilities)

Two lanes of risk, beyond the [[LethalTrifecta]]:

- **Codebase/architecture**: a **one-click remote code execution** vuln (a malicious link makes the victim's OpenClaw send an OAuth token to the attacker, who logs in and reads everything); **plaintext credential storage** (all API keys/tokens). A researcher hijacked an instance in **under 2 hours**. **ClawHub** (the public skills marketplace) was found to host **hundreds of malicious packages** stealing API keys, wallet private keys, and SSH credentials.
- **Fundamental**: a large opaque codebase you don't understand, handed enormous agent power — Cisco called it a "security nightmare." Cole credits creator **Peter** with keeping up on fixes but still considers it too risky to run.

### Anthropic ToS warning

Using your Anthropic **subscription** with OpenClaw violates Anthropic's terms and has gotten accounts **banned**. Using [[ClaudeCode]] / the [[ClaudeAgentSDK]] directly in your own environment (even on a VPS) is allowed and cost-effective.

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
- [[ClaudeAgentSDK]] — runs the proactive heartbeat in Cole's alternative
- [[ClaudeSkills]] — capability layer of the alternative
- [[Obsidian]] — canvas of the alternative
- [[N8N]] — OpenClaw surpassed its GitHub star count
- [[ColeMedin]] — the inspiration-not-execution stance
- [[summary-full-guide-ai-second-brain]] — primary source
- [[summary-safer-openclaw-alternative]] — security deep dive + clone-and-rebuild method
