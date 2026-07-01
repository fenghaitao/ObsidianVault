---
title: "Browser Agent Security Tiers"
type: concept
tags: [agents, security, browser, trust, agent-interface]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google.md"]
last_updated: 2026-06-30
---

## Definition
Browser Agent Security Tiers is a three-tier security model for browser-based AI agents, ranging from local development (human in the loop) to CI/CD environments (controlled, separated) to full internet access (YOLO mode). Each tier has progressively stricter security requirements.

## Key Information
- Presented by Michael Hablich as the security framework for Chrome DevTools MCP
- **Tier 1 — Local Development**: Human in the loop, human grants time-bound access to default Chrome profile and data the human already has access to. Autoconnect requires consent every time.
- **Tier 2 — CI/CD Environments**: Controlled but separated environments. Requires data separation (containers, separate Chrome profiles). Remote debugging port for connections.
- **Tier 3 — Full Internet Access (YOLO Mode)**: Every webpage can potentially prompt-inject the agent. Requires domain allowlists, prompt injection mitigations, and data separation.
- Based on Simon Willison's [[LethalTrifecta]] — tier 1 is where all three lethal factors collide, hence the intentional friction
- "A local agent (tier 1) and a browsing agent fleet (tier 3) might share a tool like Chrome DevTools for agents, but they shouldn't share nothing else about your security model"
- Informs [[Trust Boundaries For Agents]] — the friction-by-design principle

## Related
- [[summary-20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google]] — source
- [[Trust Boundaries For Agents]] — design principle based on these tiers
- [[LethalTrifecta]] — underlying security model from Simon Willison
- [[SimonWillison]] — security researcher
- [[Chrome DevTools MCP]] — implementation
- [[YOLOMode]] — tier 3 operating mode
- [[Agent Sandboxing]] — tier 2 requirement
