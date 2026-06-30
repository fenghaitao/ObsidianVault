---
title: "Agent-to-Agent Communication"
type: concept
tags: [mcp, protocol, agents, async, tasks]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - The Future of MCP — David Soria Parra, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition
Agent-to-Agent Communication is an MCP protocol capability enabled by the asynchronous task primitive, allowing agents to communicate and coordinate with each other through the protocol rather than only interacting with tools and humans.

## Key Information
- Built on MCP's async task primitive — "a very fancy way to say we just want to have agent-to-agent communication"
- Currently exists as a very experimental version of the protocol with limited client support
- Anthropic plans to build more client support for this feature
- Part of the MCP core improvements roadmap
- Enables agents to delegate work to other agents through the protocol
- Represents a step beyond simple tool calling toward multi-agent orchestration

## Related
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — source
- [[MCP]] — protocol
- [[MultiAgentArchitecture]] — architectural pattern this enables
- [[AgentHandoffs]] — related concept
- [[SubAgents]] — related pattern in Claude Code
- [[DavidSoriaParra]] — presenter
- [[summary-20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind]] — source (future vision: efficient agent-to-agent communication, human as supervisor on digital assembly line)
- [[Antigravity]] — platform where agent-to-agent coordination is being explored
- [[Agent Workspaces]] — shared workspace as collaboration medium
