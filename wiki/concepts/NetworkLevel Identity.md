---
title: "Network-Level Identity"
type: concept
tags: [security, networking, identity, authn, authz, tailscale, wireguard]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - What if the network was the sandbox — Remy Guercio, Tailscale.md"]
last_updated: 2026-06-30
---

## Definition
Network-Level Identity is the practice of attaching authentication (authN) and authorization (authZ) information directly to network connections, so that every connection carries the identity of who or what is connecting. This moves identity from the application layer (API keys, OAuth tokens inside the sandbox) to the network layer, where it can be enforced before any application-level communication occurs.

## Key Information
- **What it carries**: Each network connection includes user identity (if logged into the device), group membership (from SCIM syncing, e.g., engineering org), tags (e.g., "PR review bot for project X"), and application capabilities (arbitrary metadata)
- **Enabled by WireGuard + Tailscale**: [[WireGuard]] establishes cryptographic connections; [[Tailscale]] adds the identity layer on top
- **Enforcement at connection time**: A node cannot even establish a connection to a service without the right identity/permissions — this is network-level access control, not application-level
- **Receiver sees identity**: The receiving service gets all identity information on every connection, enabling fine-grained authorization decisions without separate auth handshakes
- **Application capabilities**: Beyond user/group/tag, Tailscale's ACL policy supports arbitrary metadata ("application capabilities") guaranteed by the control plane
- **Eliminates key-in-sandbox problem**: Because identity is at the network layer, agents don't need API keys or OAuth tokens inside their execution environment
- **GitOps-friendly**: Identity and access policies can be managed as JSON in ACL files, via visual editor, or via API — all suitable for GitOps workflows
- **TS Net for custom applications**: The [[TS Net]] open source Go library lets any program read network-level identity, enabling custom services that use network identity instead of OAuth

## Related
- [[Network as Sandbox]] — architectural pattern this enables
- [[Keyless Agent Sandbox]] — agent benefit of network-level identity
- [[WireGuard]] — cryptographic foundation
- [[Tailscale]] — identity layer implementation
- [[TS Net]] — library for building on network-level identity
- [[Application Capabilities]] — Tailscale feature for arbitrary identity metadata
- [[summary-20260601 - What if the network was the sandbox — Remy Guercio, Tailscale]] — source
