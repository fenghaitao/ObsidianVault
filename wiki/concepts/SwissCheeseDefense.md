---
title: "SwissCheeseDefense"
type: concept
tags: [security, agents, sandboxing, permissions]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md"]
last_updated: 2026-06-25
---

## Definition
The Swiss cheese defense is Anthropic's layered security model for agents. Each layer has holes, but together the layers block all attack vectors. The three layers are: model alignment, harness permissions, and sandboxing.

## Key Information
- **Layer 1 — Model alignment**: Claude models are trained to be aligned and resist malicious instructions. Anthropic published research on reward hacking relevant to this layer.
- **Layer 2 — Harness permissions**: The agent harness itself has permissioning, prompting, and an AST parser for the bash tool that reliably understands what commands are doing. "Definitely not something you want to build yourself."
- **Layer 3 — Sandboxing**: The execution environment is sandboxed — network requests can be restricted, file system operations outside the workspace can be blocked. If an agent is compromised, sandboxing limits what it can actually do.
- The "lethal trifecta" of dangerous agent capabilities: execute code, change the file system, exfiltrate data. Sandboxing the network is a key defense against exfiltration.
- Cloud sandbox providers (Cloudflare, Modal, DigitalOcean, AWS) add additional security at the infrastructure level
- Agents should not run on personal computers or on machines with broad access to secrets

## Related
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[LethalTrifecta]] — the three dangerous capabilities this defends against
- [[Sandboxing]] — the third layer
- [[BashTool]] — the AST parser is part of layer 2
