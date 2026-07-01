---
title: "TS Net"
type: entity
tags: [library, open-source, go, networking, tailscale]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - What if the network was the sandbox — Remy Guercio, Tailscale.md"]
last_updated: 2026-06-30
---

## Definition
TS Net is an open source Go library by [[Tailscale]] that allows developers to write programs that place themselves on a tailnet and read all Tailscale identity information (user, groups, tags, application capabilities) from incoming network connections. It exposes the same identity primitives that [[Aperture (Tailscale)]] is built on.

## Key Information
- Open source Go library from Tailscale
- Enables any Go program to join a tailnet as a node
- Programs can read the full identity (user, groups, tags, application capabilities) of connecting nodes
- Used to build internal MCP servers, API endpoints, or custom services that leverage network-level identity without needing OAuth
- [[Aperture (Tailscale)]] was built entirely using TS Net — the internal challenge was that Aperture had to use only public APIs, proving that anyone could build it
- Enables the pattern: "Hey, who made this request?" at the network layer, then proxy/authorize accordingly

## Related
- [[Tailscale]] — parent company/platform
- [[Aperture (Tailscale)]] — AI gateway built on TS Net
- [[NetworkLevel Identity]] — concept enabled by TS Net
- [[summary-20260601 - What if the network was the sandbox — Remy Guercio, Tailscale]] — source
