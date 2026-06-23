---
title: "Agent Battle: Mine the Most Diamonds in 45 Minutes"
type: source
tags: [workshop, managed-agents, agent-configuration, evals, minecraft]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London Day 2/03 - Agent Battle： Mine the most diamonds in 45 minutes.md]
last_updated: 2026-06-23
---

## Core Summary

Ben and Jeff from Anthropic's Applied AI team run a competitive workshop where participants configure Claude Managed Agents to mine diamonds in a Minecraft clone. The session teaches agent configuration (system prompt, model selection, skills, MCP servers) and hill climbing on evals through rapid iteration. The competition format emphasizes token efficiency alongside diamond count, rewarding participants who craft precise system prompts rather than just using the heaviest model. The top score reached 19 diamonds in a 5-minute run.

## Key Points

- **Agent configuration levers:** System prompt (initially empty), model selection, skills (pre-built or custom), MCP server connections.
- **Minecraft integration:** Agents connect via Mind Flare bot using MCP tools (mine block, jump, go near) rather than visual processing.
- **Shared starting conditions:** All participants start from the same seed and starter kit, making configuration the differentiator.
- **Token efficiency scoring:** Tiebreakers decided by diamonds-to-tokens ratio, incentivizing efficient prompts over brute-force model usage.
- **Iteration loop:** Run eval (~1 minute), observe results, adjust configuration, rerun — the same hill-climbing pattern used for production agents.
- **Workshop format:** 35-minute build window, 5-minute agent runs, leaderboard with live updates.

## Related

- [[ClaudeManagedAgents]] — the platform used for agent deployment
- [[ClaudeCodeSkills]] — skills as a configuration lever
- [[ModelContextProtocol]] — MCP tools for Minecraft interaction
