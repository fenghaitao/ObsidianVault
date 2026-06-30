---
title: "WireGuard"
type: entity
tags: [protocol, networking, vpn, security, cryptography]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - What if the network was the sandbox — Remy Guercio, Tailscale.md"]
last_updated: 2026-06-30
---

## Definition
WireGuard is a modern VPN protocol that uses cryptographic key pairs to establish secure, direct connections between nodes on a network. It is the foundational protocol that [[Tailscale]] is built on top of, providing the encrypted transport layer over which Tailscale adds identity, ACLs, and other management features.

## Key Information
- Provides cryptographic key-based connections between any nodes (containers, GPU servers, laptops, phones, etc.)
- Connections are direct peer-to-peer between nodes
- [[Tailscale]] builds on WireGuard by adding an identity layer (user, groups, tags) on top of the encrypted connections
- Enables the [[Network-Level Identity]] concept — every connection carries identity information
- Used as the foundation for [[Aperture (Tailscale)]], Tailscale's AI gateway

## Related
- [[Tailscale]] — built on WireGuard
- [[Network-Level Identity]] — concept enabled by WireGuard + Tailscale
- [[summary-20260601 - What if the network was the sandbox — Remy Guercio, Tailscale]] — source
