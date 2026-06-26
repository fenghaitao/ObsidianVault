---
title: "Sandboxing"
type: concept
tags: [security, agents, infrastructure, deployment]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md"]
last_updated: 2026-06-25
---

## Definition
Sandboxing is the practice of running agents in isolated container environments with restricted network and file system access. It is the third and final layer of the Swiss cheese defense model for agent security.

## Key Information
- The Claude Agent SDK includes sandboxing capabilities: network requests can be restricted, file system operations outside the workspace can be blocked
- If an agent is compromised, sandboxing limits the blast radius — it prevents the lethal trifecta (execute code, change file system, exfiltrate data)
- Cloud sandbox providers (Cloudflare, Modal, DigitalOcean, AWS) add infrastructure-level security
- Cloudflare has an example integration with the Agent SDK using `sandbox.start`
- Agents should not run on personal computers or on machines with broad access to secrets
- Each agent typically runs in its own container with its own file system — a one-to-one architecture rather than traditional multi-tenant
- Sandboxing network access is particularly important for preventing data exfiltration

## Related
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[SwissCheeseDefense]] — the layered security model
- [[LethalTrifecta]] — what sandboxing defends against
- [[ClaudeAgentSDK]] — the framework with built-in sandboxing
- [[Cloudflare]] — sandbox provider
- [[Modal]] — sandbox provider
