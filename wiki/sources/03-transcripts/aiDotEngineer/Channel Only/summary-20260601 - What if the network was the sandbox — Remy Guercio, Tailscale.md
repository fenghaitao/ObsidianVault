---
title: "What if the network was the sandbox? — Remy Guercio, Tailscale"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - What if the network was the sandbox — Remy Guercio, Tailscale.md"
author: "Remy Guercio"
date: 2026-06-01
ingested: 2026-06-30
---

## Core Thesis

What if authentication (authN) and authorization (authZ) moved from the application layer to the network layer? A sandbox has two fundamental components: a boundary and a set of permissions. By using WireGuard plus Tailscale's identity primitives, every network connection carries identity (user, groups, tags), eliminating the need for API keys inside agent sandboxes. This enables applications like an AI gateway (Aperture) where agents have zero keys to accidentally exfiltrate or misuse, all tool calls are observable at the network layer with guaranteed completeness, and permissions, budgets, and quotas can be governed centrally. The key insight: if you can see and control everything at the network layer, you don't need keys in the sandbox at all.

## Key Points

- **Two components of a sandbox**: (1) a boundary (inside vs. outside) and (2) a set of permissions (identity-based access to tools/resources). Without permissions, a sandbox is "a sandbox without any toys."
- **Current agent auth approaches are flawed**: API keys live inside the sandbox where agents can exfiltrate or misuse them; OAuth/OIDC requires logging the agent into an account that's "hanging out over there." Both put credentials inside the boundary.
- **WireGuard + Tailscale identity**: WireGuard gives every node on a network a set of keys. Tailscale adds identity on top — with each connection, you get the user (if logged in), all groups (from SCIM syncing, e.g., engineering org), and arbitrary tags (e.g., "PR review bot for this project"). This identity is present on every single network connection.
- **Network-level governance**: You can govern network access based on identity — a node cannot even talk to something without the right permissions. The receiving side also gets all identity information, enabling fine-grained access control at the network layer rather than the application layer.
- **Aperture — Tailscale's AI gateway**: A single key from any provider (Anthropic, OpenAI, Gemini, Vertex AI, Bedrock, etc.) goes on Aperture, which is a node on the tailnet. Aperture sees the identity of everything connecting to it. Agents connect with zero keys — just a tag on the tailnet determines what they can do. Rules, budgets, and quotas are configured in Aperture and work across all providers.
- **Keyless sandbox**: A GitHub Actions runner acting as an agent sandbox gets access to the tailnet via federated OIDC from GitHub, receives a tag, and connects to Aperture with no API key whatsoever — "there's just no key whatsoever in that sandbox." No key to accidentally exfiltrate, share, or use to go beyond boundaries.
- **Complete observability at the network layer**: Because all tool calls must go through Aperture at the network layer, you have a guarantee of seeing every tool call an agent has ever made. Unlike container-level or harness-level observation, this cannot be bypassed — the moment you revoke access, the connection simply stops. "It's not like it has a key and it can be like, 'Oh, I see the key no longer works. Let me go to this other endpoint.' It literally is like, 'Oh, key no longer works.' It's just a dash."
- **Live demo of Aperture**: Remy demonstrated Aperture showing per-user/per-identity usage metrics (tokens, models, cost), per-request inspection (full request/response bodies), per-tag views for bot agents (e.g., dog food PR review bot with all bash commands and tool calls visible), and Claude Code's complete initial request payload — all visible because everything goes through the gateway.
- **Setup simplicity**: In Claude Code (or Codex, Gemini CLI), just set API key mode with a dummy key (`-`) and point the base URL to the Aperture node. That's all that's required.
- **Cost controls across providers**: Set a single budget in Aperture (e.g., $5/day per user) that works across all providers — not per-provider budgets. Can also set team-level budgets with individual sub-budgets, and differentiate between free internal GPU endpoints vs. paid external models (e.g., unlimited internal, capped Opus 4.6).
- **Webhooks for tool calls**: Aperture offers webhooks that fire on each tool call with full information, guaranteed to run because everything must pass through the gateway.
- **Application capabilities in Tailscale ACL**: Beyond user/tag/group identity, Tailscale's ACL policy file supports "application capabilities" — arbitrary metadata sent alongside the identity, guaranteed by the Tailscale control plane. This can be managed via visual editor, JSON in GitOps workflows, or API.
- **TS Net — build your own**: Aperture is built entirely on public Tailscale identity primitives available via TS Net, an open source Go library. You can write your own Go program that puts itself on the tailnet and reads all the same identity information. The challenge to the Aperture team was: it had to be built using only public APIs, no private endpoints. In theory, you could build Aperture yourself.
- **Internal MCP servers and APIs**: Using TS Net, you can build internal MCP servers or API endpoints that don't need OAuth — just check "who made this request" via the network-level identity and proxy accordingly.
- **Permissioning model**: Today Aperture controls access by model and provider, with quotas also permissioned the same way. More granular controls (e.g., restricting specific tools or bash commands) are being added, including guardrails like blocking `rm -rf /`.
- **Why the LLM layer, not just MCP**: Tailscale considered building this at the MCP layer but realized the LLM layer is more valuable — even when agents move away from structured tool calls toward code execution, you still see the bash commands and other activity passing through the gateway. Internally at Tailscale, bash dominates all other tool usage.
- **No transparent proxy (intentional)**: When asked if Aperture could transparently intercept traffic without changing the base URL, Remy said this was discussed but rejected as "not the Tailscale way." The goal is to make LLM access easy and explicit for developers while giving security/IT admins easy controls — doing the best of both worlds without hidden magic.

## Entities Mentioned

- [[Remy Guercio]] — Speaker, from Tailscale
- [[Tailscale]] — Secure networking company built on WireGuard; provides identity primitives, ACL policy, TS Net library
- [[Aperture (Tailscale)]] — Tailscale's AI gateway product; built on Tailscale identity primitives
- [[WireGuard]] — VPN protocol that provides cryptographic key-based connections between nodes
- [[TS Net]] — Open source Go library by Tailscale for building applications that use Tailscale identity
- [[Claude Code]] — Anthropic's coding agent; demonstrated working with Aperture via dummy API key
- [[Anthropic]] — LLM provider; Claude models used via Aperture
- [[OpenAI]] — LLM provider supported by Aperture
- [[Google DeepMind]] — Provider of Gemini models supported by Aperture
- [[GitHub]] — GitHub Actions runners used as agent sandboxes; federated OIDC for tailnet access
- [[Vertex AI]] — Google Cloud AI platform supported by Aperture
- [[Amazon Bedrock]] — AWS AI platform supported by Aperture
- [[Codex]] — OpenAI coding agent; can connect to Aperture
- [[Gemini CLI]] — Google's CLI coding agent; can connect to Aperture

## Concepts Introduced

- [[Network as Sandbox]] — Using the network layer as the sandbox boundary, with identity and permissions enforced at the connection level rather than inside the sandbox
- [[Network-Level Identity]] — Carrying user, group, and tag identity on every network connection via WireGuard + Tailscale, enabling authN/authZ at the network layer
- [[Keyless Agent Sandbox]] — Agent sandboxes that contain zero API keys; identity is provided by the network connection itself, eliminating key exfiltration risk
- [[AI Gateway]] — An LLM gateway pattern where a single provider key is placed on a gateway node that sees all connecting identity and enforces permissions, budgets, and observability at the network layer
- [[Application Capabilities]] — Tailscale ACL feature for attaching arbitrary metadata to network identity, guaranteed by the control plane
- [[Network-Level Observability]] — Guaranteed visibility into all agent tool calls because every request must pass through the network-layer gateway; cannot be bypassed by the agent

## Related

- [[summary-20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0]] — agent identity topic
- [[summary-20260427 - Gateways are All You Need — Karan Sampath, Anthropic]] — AI gateway topic
- [[summary-20260526 - Run Frontier AI at Home — Alex Cheema, EXO Labs]] — also mentions Tailscale
