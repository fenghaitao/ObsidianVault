---
title: "Trust Boundaries For Agents"
type: concept
tags: [agents, security, trust, agent-interface, design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google.md"]
last_updated: 2026-06-30
---

## Definition
Trust Boundaries For Agents is the design principle that friction in agent interfaces can be intentional and should not be removed for convenience. In a world where work is delegated to agents, security requires deliberate trust boundaries — "never compromise trust for convenience."

## Key Information
- Core lesson from Chrome DevTools MCP's autoconnect feature design
- Autoconnect lets humans share their screen with agents for collaborative debugging
- Users requested "remember my choice" to avoid clicking "allow" every time — a traditional UX win
- The team refused: friction is by design because delegating work to agents requires thinking about trust boundaries
- Based on Simon Willison's [[LethalTrifecta]] security model
- In traditional UX design, removing friction is a clear win — but in agent UX, some friction is security-critical
- "A local agent (tier 1) and a browsing agent fleet (tier 3) might share a tool like Chrome DevTools for agents, but they shouldn't share nothing else about your security model"
- Contrasts with the general UX principle of reducing friction — introduces the concept of intentional friction

## Related
- [[summary-20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google]] — source
- [[Browser Agent Security Tiers]] — tiered security model
- [[LethalTrifecta]] — underlying security model from Simon Willison
- [[SimonWillison]] — security researcher whose work informed this design
- [[Chrome DevTools MCP]] — practical implementation
- [[Agent Experience]] — broader framework where trust boundaries are a non-functional requirement
