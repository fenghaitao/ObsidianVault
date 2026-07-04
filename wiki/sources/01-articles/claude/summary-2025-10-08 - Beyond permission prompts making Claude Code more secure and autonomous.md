---
title: "summary-2025-10-08 - Beyond permission prompts making Claude Code more secure and autonomous"
type: source
tags: [source, original-material, sandboxing, security, claude-code]
sources: ["raw/01-articles/claude/2025-10-08 - Beyond permission prompts making Claude Code more secure and autonomous.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic introduced [[Sandboxing]] in Claude Code as an alternative to constant permission-prompt approval, which causes "approval fatigue." Sandboxing defines OS-level boundaries (filesystem isolation and network isolation) within which Claude can act freely without asking permission each time, while remaining safe against prompt injection. This underlies two new features: a sandboxed bash tool (research preview, built on Linux bubblewrap and macOS Seatbelt) that runs commands within user-defined directory/network limits, and **Claude Code on the web**, which runs each session in an isolated cloud sandbox where sensitive credentials (git credentials, signing keys) never enter the sandbox — git operations are proxied through a scoped-credential service instead.

## Key Points

- **Problem**: Claude Code's default permission-based model requires explicit approval for most modifications/commands; constant approval clicking causes "approval fatigue" where users stop paying close attention.
- **Sandboxing** requires both pieces to be effective: filesystem isolation (restricts Claude to specific directories, preventing modification of sensitive system files) and network isolation (restricts connections to approved servers/domains, preventing exfiltration or malware download). Missing either lets a prompt-injected agent escape.
- **Sandboxed bash tool** (research preview, open source): lets developers define exactly which directories and network hosts an agent/MCP server can access, without spinning up a container; built on Linux bubblewrap and macOS Seatbelt; covers subprocesses spawned by commands too. Network access is only permitted through a unix domain socket connected to a proxy server that enforces domain restrictions and handles user confirmation for new domains; the proxy can be further customized for arbitrary outgoing-traffic rules. Enabled via `claude --sandbox`.
- **Claude Code on the web**: runs each session in an isolated cloud sandbox with full server access; sensitive credentials (git credentials, signing keys) never enter the sandbox. A custom proxy service handles git interactions — the sandboxed git client authenticates with a scoped credential, the proxy verifies it (e.g., ensuring pushes only go to the configured branch) and attaches the real authentication token before forwarding to GitHub.
- Anthropic open-sourced the sandboxing runtime so other teams/agent builders can adopt the same security posture.
- Framed explicitly as a [[PromptInjection]] mitigation: sandboxing ensures a successful prompt injection is fully isolated and cannot impact overall user security (e.g., cannot steal SSH keys or phone home to an attacker's server).

## Related

- [[Sandboxing]] — the core concept this article introduces
- [[ClaudeCode]] — the tool receiving these two new features
- [[PromptInjection]] — the threat model sandboxing is designed to mitigate
- [[GitHub]] — target of the scoped-credential git proxy used by Claude Code on the web
