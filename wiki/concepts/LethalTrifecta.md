---
title: "LethalTrifecta"
type: concept
tags: [security, agents, threats]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google.md"]
last_updated: 2026-06-30
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
- [[summary-20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google]] — applied to Chrome DevTools autoconnect friction-by-design
- [[Trust Boundaries For Agents]] — design principle informed by Lethal Trifecta
- [[Browser Agent Security Tiers]] — tiered model based on Lethal Trifecta risks
- [[SimonWillison]] — creator of the model
