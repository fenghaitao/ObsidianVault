---
title: "Sandboxing"
type: concept
tags: [security, sandboxing, claude-code, filesystem-isolation, network-isolation]
sources: ["raw/01-articles/claude/2025-10-08 - Beyond permission prompts making Claude Code more secure and autonomous.md"]
last_updated: 2026-07-04
---

## Definition

Sandboxing is a security approach that defines pre-set boundaries within which an AI agent can act freely, replacing per-action permission prompts with OS-level enforced limits on what the agent can touch — providing both more security and more autonomy than a manual-approval model.

## Key Information

- **Motivation**: [[ClaudeCode]]'s default permission-based model (ask before every modification or command) causes "approval fatigue," where constant clicking leads users to stop scrutinizing what they approve.
- **Two required components** — both are necessary, neither is sufficient alone:
  - **Filesystem isolation**: restricts an agent to specific directories, preventing a prompt-injected agent from modifying sensitive system files or escaping the sandbox.
  - **Network isolation**: restricts connections to approved servers/domains, preventing a prompt-injected agent from exfiltrating data (e.g., SSH keys) or downloading malware.
- **Sandboxed bash tool** (research preview): open-source runtime letting developers define exactly which directories and network hosts a process, agent, or MCP server can access, without managing containers. Built on OS-level primitives — Linux bubblewrap and macOS Seatbelt — covering not just direct commands but any spawned subprocesses. Network access is only permitted through a unix domain socket to a proxy server that enforces domain rules and handles user confirmation for new domains (further customizable for arbitrary traffic rules). Enabled via `claude --sandbox`.
- **Claude Code on the web**: runs each session in an isolated cloud sandbox; sensitive credentials (git credentials, signing keys) never enter the sandbox. Git operations are proxied through a service that authenticates a scoped credential, verifies the interaction (e.g., only pushing to the configured branch), then attaches the real token before forwarding to [[GitHub]].
- Anthropic open-sourced the sandboxing runtime to encourage other AI companies/agent builders to adopt the same approach.
- Directly framed as a [[PromptInjection]] mitigation: even a successful prompt injection is fully isolated and cannot affect overall user security.

## Related

- [[ClaudeCode]] — the tool implementing sandboxing via the sandboxed bash tool and Claude Code on the web
- [[PromptInjection]] — the threat model sandboxing mitigates
- [[CodeSecurity]] — broader security practices this complements
- [[GitHub]] — target of the scoped git-credential proxy in Claude Code on the web
- [[summary-2025-10-08 - Beyond permission prompts making Claude Code more secure and autonomous]] — source article
