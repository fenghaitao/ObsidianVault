---
title: "Network-Level Observability"
type: concept
tags: [observability, networking, agents, security, monitoring, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - What if the network was the sandbox — Remy Guercio, Tailscale.md"]
last_updated: 2026-06-30
---

## Definition
Network-Level Observability is the practice of observing and logging all agent tool calls, model requests, and responses at the network layer — at the point where traffic passes through a gateway — rather than from inside the agent's execution environment (container, harness, or application code). This provides a guarantee of completeness that in-process observation cannot match, because the agent cannot bypass the network layer.

## Key Information
- **Guaranteed completeness**: Because all LLM requests and tool calls must pass through the network-layer gateway, observation is guaranteed — unlike container-level or harness-level observation which the agent could potentially circumvent
- **Cannot be bypassed**: An agent cannot "be helpful" and route around the gateway because it has no API keys — only network identity. If the network connection is cut, the agent stops completely
- **Sees everything**: Tool calls (bash commands, MCP calls, grep, file operations), request headers, request bodies, response bodies — all visible at the gateway level
- **Per-identity views**: Observability is broken down by user, tag, group — see exactly what each agent/identity is doing
- **Webhook integration**: Gateway can fire webhooks with full tool call information to external systems, guaranteed to execute
- **Contrast with in-process observation**: Observing from inside the container or harness can miss things if the agent finds workarounds. Network-level observation is outside the agent's control
- **Implementation via AI Gateway**: [[Aperture (Tailscale)]] is the reference implementation — all traffic passes through the gateway at the network layer
- **Use cases**: Debugging agent behavior, auditing tool usage, cost tracking per identity, security monitoring for dangerous commands, compliance logging

## Related
- [[AI Gateway]] — the gateway pattern that enables network-level observability
- [[Network as Sandbox]] — architectural pattern
- [[AgentObservability]] — broader agent observability concept
- [[Aperture (Tailscale)]] — reference implementation
- [[summary-20260601 - What if the network was the sandbox — Remy Guercio, Tailscale]] — source
