---
title: "Agents As Different User Class"
type: concept
tags: [agents, ux, agent-experience, design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google.md"]
last_updated: 2026-06-30
---

## Definition
Agents as Different User Class is the insight that AI agents are a fundamentally separate user segment from humans — they share intent and goals but have different cognitive bottlenecks (context window limits vs. visual complexity), requiring purpose-built interfaces rather than repurposed human UIs.

## Key Information
- Core insight from Michael Hablich's Chrome DevTools for Agents work
- Agents and humans share intent and goals (e.g., both want to identify and fix page errors) but think differently
- Human cognitive bottleneck: visual complexity — humans need layout, color, and visual signal to process information
- Agent cognitive bottleneck: context window limits — agents cannot process raw data dumps (e.g., 50K lines of JSON)
- This insight drove Chrome DevTools MCP to return semantic summaries instead of raw trace files
- Led to decomposing one monolithic "debug webpage" tool into 25 purpose-built tools optimized for agent cognition
- Connects to [[AgenticProductDesign]] — designing interfaces for agents, not humans
- "Agents are our next users — let's help them help us"

## Related
- [[summary-20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google]] — source
- [[AgenticProductDesign]] — related design philosophy
- [[Agent Experience]] — broader UX framework
- [[Semantic Summaries]] — technique for bridging the cognitive gap
- [[Chrome DevTools MCP]] — practical application
