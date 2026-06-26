---
title: "Stateless Transport Protocol"
type: concept
tags: [mcp, protocol, transport, scalability, infrastructure]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - The Future of MCP — David Soria Parra, Anthropic.md"]
last_updated: 2026-06-26
---

## Definition
The Stateless Transport Protocol is a proposed MCP transport layer from Google that replaces the current streamable HTTP transport, making MCP servers easier to deploy and scale on standard cloud infrastructure like Cloud Run and Kubernetes.

## Key Information
- Current streamable HTTP transport is "very hard to scale if you're a large hyperscaler"
- Proposal from Google to make MCP servers treatable like stateless REST servers
- Enables standard deployment patterns: cloud runs, Kubernetes, and other familiar infrastructure
- Announced as coming down in June 2026, with SDK support to follow
- Part of the MCP core improvements alongside async task improvements and SDK v2 releases
- Addresses a fundamental scaling limitation identified as the protocol has matured over the past year

## Related
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — source
- [[MCP]] — protocol
- [[GoogleDeepMind]] — contributor of the proposal
- [[Kubernetes]] — deployment target
- [[Cloud Run]] — deployment target
- [[DavidSoriaParra]] — presenter
