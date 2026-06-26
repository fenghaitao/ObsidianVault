---
title: "LethalTrifecta"
type: concept
tags: [security, agents, threats]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md"]
last_updated: 2026-06-25
---

## Definition
The lethal trifecta refers to the three most dangerous capabilities a compromised agent could have: the ability to execute arbitrary code in its environment, the ability to change the file system, and the ability to exfiltrate data over the network. Together, these three capabilities represent the maximum threat surface for an agent.

## Key Information
- If an attacker controls an agent with all three capabilities, they can run malicious code, modify or destroy data, and steal sensitive information
- Sandboxing the network is a key defense against the exfiltration component
- Sandboxing file system operations outside the workspace defends against the file system change component
- The concept is part of the Swiss cheese defense model: each layer addresses different parts of the trifecta
- Thariq Shihipar noted he might have gotten the exact formulation slightly wrong, but the core idea is sound

## Related
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[SwissCheeseDefense]] — the layered defense model
- [[Sandboxing]] — primary mitigation
