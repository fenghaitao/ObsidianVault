---
title: "Application Capabilities"
type: concept
tags: [tailscale, networking, identity, acl, metadata]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - What if the network was the sandbox — Remy Guercio, Tailscale.md"]
last_updated: 2026-06-30
---

## Definition
Application Capabilities are a [[Tailscale]] ACL (Access Control List) feature that allows attaching arbitrary metadata to network connections alongside the standard identity information (user, groups, tags). This metadata is guaranteed by the Tailscale control plane and travels with every network connection, enabling applications to make authorization decisions based on custom, application-specific attributes.

## Key Information
- **Part of Tailscale ACL policy**: Defined in the same policy file (JSON) that controls who can access what on the network
- **Arbitrary metadata**: Can carry any custom key-value data relevant to the application — not limited to user/group/tag
- **Guaranteed by control plane**: The Tailscale control plane ensures the metadata is authentic and attached to the correct identity
- **Sent with every connection**: Application capabilities are present on every network connection, not just at initial handshake
- **GitOps-friendly**: Can be managed as JSON in ACL files, via visual editor, or via API
- **Used by Aperture**: [[Aperture (Tailscale)]] uses application capabilities to carry fine-grained permission information for AI gateway access control
- **Enables custom authorization**: Applications built with [[TS Net]] can read application capabilities to implement domain-specific authorization without building separate auth systems

## Related
- [[Tailscale]] — platform providing this feature
- [[Network-Level Identity]] — broader concept; application capabilities are a component
- [[Aperture (Tailscale)]] — uses application capabilities
- [[TS Net]] — library for reading application capabilities
- [[summary-20260601 - What if the network was the sandbox — Remy Guercio, Tailscale]] — source
