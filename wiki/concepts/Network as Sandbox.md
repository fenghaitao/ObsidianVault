---
title: "Network as Sandbox"
type: concept
tags: [security, networking, agents, sandbox, identity, architecture]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - What if the network was the sandbox — Remy Guercio, Tailscale.md"]
last_updated: 2026-06-30
---

## Definition
The Network as Sandbox is an architectural pattern where the network layer serves as the boundary and permissioning mechanism for AI agent execution, rather than traditional sandbox approaches (VMs, containers, API keys). The two fundamental components of a sandbox — a boundary (inside vs. outside) and a set of permissions (identity-based access) — are implemented at the network connection level instead of inside the execution environment.

## Key Information
- **Core insight**: Sandboxes have two components: a boundary and permissions. Both can be implemented at the network layer using identity-carrying connections.
- **Contrast with traditional approaches**: VM/container sandboxes still require credentials (API keys, OAuth tokens) to live inside the boundary, creating exfiltration risk. Network-level identity eliminates this by making the connection itself carry authorization.
- **Implementation via WireGuard + Tailscale**: [[WireGuard]] provides cryptographic connections; [[Tailscale]] adds identity (user, groups, tags) to every connection. The network becomes the sandbox boundary.
- **Keyless execution**: Agents inside the sandbox have zero credentials — their network identity (tag on the tailnet) determines what they can access. No API keys to leak, exfiltrate, or misuse.
- **Guaranteed observability**: Because all tool calls must pass through the network-layer gateway, you have a guarantee of seeing everything. Unlike container-level observation, the agent cannot bypass the network layer.
- **Revocation is immediate and absolute**: Cutting off network access stops the agent completely — it cannot try alternative endpoints or work around the restriction because it has no keys, only a network identity.
- **Application**: [[Aperture (Tailscale)]] is the primary example — an AI gateway where agents connect via network identity with no API keys.

## Related
- [[Network-Level Identity]] — the identity mechanism that enables this pattern
- [[Keyless Agent Sandbox]] — the agent-side benefit of this approach
- [[AI Gateway]] — the gateway pattern that implements network-as-sandbox for LLMs
- [[Agent Sandboxing]] — traditional sandboxing approaches
- [[Aperture (Tailscale)]] — reference implementation
- [[Tailscale]] — platform enabling this pattern
- [[summary-20260601 - What if the network was the sandbox — Remy Guercio, Tailscale]] — source
