---
title: "Keyless Agent Sandbox"
type: concept
tags: [security, agents, sandbox, networking, identity, api-keys]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - What if the network was the sandbox — Remy Guercio, Tailscale.md"]
last_updated: 2026-06-30
---

## Definition
A Keyless Agent Sandbox is an agent execution environment that contains zero API keys, OAuth tokens, or other credentials. Instead of carrying credentials inside the sandbox, the agent's identity and permissions are provided by the network connection itself via [[Network-Level Identity]]. This eliminates the risk of credential exfiltration, misuse, or the agent "going beyond its boundaries" using stolen keys.

## Key Information
- **The problem it solves**: Traditional agent sandboxes (VMs, containers, GitHub Actions runners) require API keys or OAuth tokens to be placed inside the sandbox. These can be exfiltrated, shared, or misused by agents — especially clever models running in long loops
- **How it works**: The sandbox (e.g., a GitHub Actions runner) joins a tailnet via federated OIDC, receives a tag (e.g., "PR review bot for project X"), and connects to services using only its network identity. The tag determines what the agent can access
- **No keys to leak**: The agent has no API key — just a dummy placeholder (e.g., `-`) to satisfy tool requirements. If the agent tries to exfiltrate credentials, there is nothing to steal
- **Revocation is absolute**: Cutting off network access (removing the tag, revoking the connection) immediately stops the agent. Unlike API key revocation, the agent cannot try alternative endpoints or work around the restriction
- **Implementation via Aperture**: [[Aperture (Tailscale)]] is the reference implementation — agents connect to the AI gateway with network identity, not API keys
- **Setup simplicity**: In coding agents (Claude Code, Codex, Gemini CLI), just set a dummy API key and point the base URL to the gateway node
- **All providers, one identity**: A single network identity works across all LLM providers through the gateway — no per-provider key management

## Related
- [[Network as Sandbox]] — architectural pattern
- [[Network-Level Identity]] — mechanism that enables keyless sandboxes
- [[AI Gateway]] — gateway pattern used with keyless sandboxes
- [[Agent Sandboxing]] — traditional sandboxing approaches
- [[Aperture (Tailscale)]] — reference implementation
- [[summary-20260601 - What if the network was the sandbox — Remy Guercio, Tailscale]] — source
