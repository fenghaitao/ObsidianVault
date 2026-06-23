---
title: "summary-20260212 - I Built a Safer OpenClaw Alternative Using Claude Code"
type: source
tags: [source, original-material, openclaw, second-brain, security, claude-agent-sdk]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260212 - I Built a Safer OpenClaw Alternative Using Claude Code.md"]
last_updated: 2026-06-20
---

## Core Summary

[[ColeMedin]] dissects [[OpenClaw]] — the runaway-hit open-source personal AI assistant (185k GitHub stars, surpassing even [[N8N]]) — explaining both *why it feels magical* and *why it's too dangerous to run directly*, then shows how he replicated everything powerful about it in a couple of days (a few thousand lines of Python + markdown) using [[ClaudeCode]] and the [[ClaudeAgentSDK]]. The thesis: learn from powerful open-source assistants, but **build your own** so you understand, control, and customize it — and avoid OpenClaw's serious security problems.

## Key Points

- **Why OpenClaw is magical** — four core components:
  1. **Memory system** — entirely markdown-driven: `soul.md` (agent identity, evolves), `user.md` (model of the user), `memory.md` (core memories), `agents.md` (behavior/global rules), plus daily **session logs**; a SQLite DB adds a light RAG layer for search. Elegant but simple.
  2. **Heartbeat** — a `heartbeat.md` that the agent consults when it runs autonomously on a schedule ("what can I do for Cole right now that he'd appreciate?"); produces proactive output (drafted emails, opened PRs) without being asked.
  3. **Channel adapters** — talk to it from WhatsApp, Telegram, Slack, Discord, etc., with thread support (multiple simultaneous conversations).
  4. **Skills registry** — add a capability with a single file; shareable with others.
- **Security problems (two lanes)**:
  - *Codebase/architecture*: a **one-click remote code execution** vuln (a malicious link makes the victim's OpenClaw send an OAuth token to the attacker, who logs in and reads everything); **credentials stored in plain text** (API keys, tokens for all platform adapters). A researcher hijacked an instance in **under 2 hours**. **ClawHub** — the public skills marketplace — was found to contain **hundreds of malicious packages** stealing API keys, wallet private keys, and SSH credentials.
  - *Fundamental*: a large opaque codebase you don't understand, handed enormous agent power. Cisco called it a "security nightmare." Even if all architecture bugs were fixed, Cole considers it too risky. (Credit: creator **Peter** keeps up with fixes; [[LethalTrifecta]] still applies.)
- **The build-your-own method** — clone OpenClaw locally (MIT license), point [[ClaudeCode]] at it: *"explain how the memory system works, now build it into my own system adapted to my stack."* Coding agents thrive on a simple, elegant working example — it one-shotted his memory system. Repeat per component. When OpenClaw ships something great, pull the repo and re-point Claude Code at it.
- **Cole's stack**: [[Obsidian]] (storage + sync) + markdown (the database) + SQLite (local) / Postgres (remote VPS) + [[ClaudeAgentSDK]] (the heartbeat: a scheduled job every ~30 min that reads memory, email, calendar, Asana tasks and notifies him) + [[ClaudeCode]] as the primary driver. **Skills** come built into Claude Code / the Agent SDK, including a skill that creates more skills — so no public registry (and no risk of malicious downloaded skills).
- **Adapters, minimalist**: unlike OpenClaw's many adapters, Cole keeps just **Slack** + the terminal — most people only need one channel that works for them; he can one-shot another adapter (Discord/Teams) anytime by copying OpenClaw's architecture.
- **Anthropic ToS warning**: using your Anthropic *subscription* with OpenClaw violates the terms and has gotten people banned; using [[ClaudeCode]] / the [[ClaudeAgentSDK]] directly in your own environment (even on a VPS) is allowed and cost-effective.
- **Note on alternatives**: lightweight, more-secure OpenClaw alternatives exist (e.g. **Nano Claw**) but didn't meet Cole's requirements, so he built his own.

## Related

- [[OpenClaw]] — the tool dissected and used as a reference, not run
- [[SecondBrain]] — what Cole builds instead, on his own controlled stack
- [[LethalTrifecta]] — the security model; OpenClaw's vulnerabilities are concrete evidence
- [[ClaudeAgentSDK]] — runs the heartbeat / proactive layer
- [[ClaudeCode]] — clones-and-rebuilds OpenClaw's components; primary driver
- [[Obsidian]] — storage + sync layer
- [[N8N]] — star-count comparison (OpenClaw surpassed it)
