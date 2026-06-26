---
title: "SandboxingAndPermissions"
type: concept
tags: [security, coding-agents, bash, prompt-injection, agent-architecture]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer.md"]
last_updated: 2026-06-25
---

## Definition
Sandboxing and permissions is the security layer in coding agents that gates what commands an agent can execute, particularly bash commands. It addresses the prompt injection attack vector from internet-connected agents with shell access, and is where most of the complex code in agents like Claude Code resides.

## Key Information
- Claude Code has a pipeline to gate bash commands based on command prefix, routing through the sandboxing environment
- Major attack vector: agents with shell access that can web fetch — prompt injection from the internet becomes dangerous
- Mitigations include containerization, URL blocking, and running web fetches in sub-agents
- Claude Code is "pretty annoying" about asking permission: "Can I fetch from this URL? Can I do this?"
- Different agents handle sandboxing differently: Claude Code uses containerization, Codex uses kernel-based sandboxing (macOS Seatbelt, Linux Land)
- Jared Zoneraich admits he runs Claude Code on "YOLO mode" half the time, but acknowledges some team members have dropped all their local databases
- Described as "the most boring part" but also where most of the complex code lives
- Predicted that all chat windows will come with sandboxes in the near future, enabling long-term memory via file system storage

## Related
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — source
- [[ClaudeCode]] — primary example
- [[Codex]] — different sandboxing approach
- [[BashAsUniversalAdapter]] — the capability that requires sandboxing
- [[PromptInjection]] — the attack vector sandboxing addresses
