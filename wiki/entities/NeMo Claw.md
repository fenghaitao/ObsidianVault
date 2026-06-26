---
title: "NeMo Claw"
type: entity
tags: [tool, security, sandbox, nvidia, open-claw]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - State of the Claw — Peter Steinberger.md"]
last_updated: 2026-06-26
---

## Definition
NeMo Claw is a security layer and sandbox plugin for OpenClaw, launched by Nvidia. It provides an additional security boundary around OpenClaw agents to prevent sandbox breakouts and limit the blast radius of compromised agents.

## Key Information
- Launched by Nvidia as a plugin and security layer for OpenClaw
- Nvidia's keynote was on Monday; they invited Peter Steinberger on Sunday to work with them
- Peter hooked NeMo Claw to Codex security and found 5 different ways to break out of the secure sandbox within 30 minutes
- The breakouts were found using Nvidia's internal model which is "quite a bit smarter in terms of cyber than what the public has access to" — "because it's dangerous"
- Part of Nvidia's broader contribution to OpenClaw security, alongside providing engineers who "basically work full-time going through the slop and hardening the code base"
- Represents the industry trend of companies building security layers around OpenClaw

## Related
- [[summary-20260417 - State of the Claw — Peter Steinberger]] — source
- [[Nvidia]] — creator
- [[OpenClaw]] — project it secures
- [[PeterSteinberger]] — tested its security
- [[Codex]] — used to test sandbox breakouts
- [[Sandboxing]] — the security approach it implements
