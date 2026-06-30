---
title: "Tailscale"
type: entity
tags: [tool, networking, security, vpn, remote-access, identity, ai-gateway]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - What if the network was the sandbox — Remy Guercio, Tailscale.md"]
last_updated: 2026-06-30
---

## Definition
Tailscale is a secure networking platform built on [[WireGuard]] that provides encrypted, identity-aware connections between devices. Beyond VPN functionality, it adds an identity layer (users, groups, tags, application capabilities) to every network connection, enabling network-level authentication and authorization. This makes it a foundation for building applications like [[Aperture (Tailscale)]], an AI gateway where agents connect with zero API keys and all tool calls are observable at the network layer.

## Key Information
- Built on [[WireGuard]] for secure, encrypted peer-to-peer networking
- **Identity primitives**: Every network connection carries identity — user (if logged in), groups (from SCIM syncing), tags (e.g., "PR review bot for project X"), and application capabilities (arbitrary metadata guaranteed by the control plane)
- **ACL policy**: Access control file (JSON) defines who can access what on the network; supports GitOps workflows and API management
- **TS Net**: Open source Go library that lets any program join a tailnet and read identity information from connections — used to build [[Aperture (Tailscale)]] and custom internal services
- **Aperture**: Tailscale's AI gateway — agents connect with no API keys, identity is network-level, all tool calls observable
- EXO Labs uses Tailscale to access local inference clusters remotely (e.g., from a conference venue back to a home cluster)
- Solves the problem of securely accessing local devices without complex network configuration
- Enables both developer ease (simple LLM access) and security/IT control (network-level observability and permissions)

## Related
- [[summary-20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs]] — source (EXO Labs usage)
- [[summary-20260601 - What if the network was the sandbox — Remy Guercio, Tailscale]] — source (identity primitives, Aperture)
- [[WireGuard]] — underlying protocol
- [[Aperture (Tailscale)]] — AI gateway built on Tailscale
- [[TS Net]] — open source library for building on Tailscale
- [[Network as Sandbox]] — concept presented by Remy Guercio
- [[Network-Level Identity]] — core Tailscale capability
- [[EXO]] — app that integrates with Tailscale
- [[EXO Labs]] — uses Tailscale for remote access
