---
title: "Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google.md"
author: "Michael Hablich"
company: "Google"
date: 2026-06-05
ingested: 2026-06-30
tags: [mcp, agent-interface, chrome-devtools, agent-experience, tool-design, security, agent-efficiency]
---

# Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google

## Core Thesis
Michael Hablich presents four engineering lessons from building Chrome DevTools for Agents, an MCP server that lets coding agents debug web pages. The central insight: agents are a fundamentally different user class from humans — they share goals but have different cognitive bottlenecks (visual complexity for humans, context window limits for agents). The four lessons cover measuring fuel efficiency (tokens per successful outcome), error recovery (useful messages, proactive detours, diagnostic playbooks), discoverability (tool descriptions are the UI for agents), and trust (friction by design, never compromise trust for convenience).

## Key Points
- **Agents as Different User Class**: Agents and humans share intent and goals but think differently. Humans are visual creatures needing layout and color; agents choke on raw data dumps. Chrome DevTools was built because coding agents were "flying blind" — they could generate code but not validate it.
- **Semantic Summaries Over Raw Data**: Throwing 50K lines of JSON (trace files) at agents blew through context windows. Instead, Chrome DevTools MCP returns markdown and semantic summaries (e.g., LCP, INP, CLS metrics) — "don't force the agent to read the entire book, point it at the right sentence."
- **Tokens Per Successful Outcome**: The fuel efficiency metric for agent interfaces. Effectiveness = does the agent complete the user journey? Efficiency = token cost, tool calls, duration. Tokens per successful outcome (not per outcome) matters because "fuel efficiency is worthless if you can't reach your destination." Cannot be measured globally — different task classes have dramatically different costs.
- **Error Recovery Spectrum**: Three layers: (1) useful error messages that enable self-healing by suggesting next steps, (2) proactive detours that counteract model training biases (e.g., steering toward start performance trace instead of Lighthouse audit), (3) diagnostic playbooks (troubleshooting skills) that help agents fix setup issues.
- **Discoverability: Schema is the UI**: 97% of MCP tool descriptions have quality smells. Moving from one monolithic "debug webpage" tool to 25 decomposed tools shifted the problem. Fixes: define purpose clearly, provide usage guidelines/activation criteria, use domain terminology agents understand (e.g., LCP/INP/CLS for performance tools). Trade-off: better descriptions consume more context window.
- **Tool Categorization and Slim Mode**: Hide niche tools behind CLI parameters (e.g., Chrome extension debugging). Slim mode exposes only 3 tools: select page, navigate page, evaluate script. Trade-off: fewer tools = less context, but agents may need more turns to achieve goals.
- **CLI Interface for Agents**: Alongside MCP, a CLI interface enables agents to chain commands together for post-processing (e.g., pipe grep output into click), saving tokens since the model doesn't process intermediate results.
- **Trust: Friction by Design**: Autoconnect feature lets humans share their screen with agents. Users wanted "remember my choice" but the team refused — friction is intentional. Based on Simon Willison's Lethal Trifecta: local agents (tier 1) need human consent every time; CI/CD agents (tier 2) need data separation; full internet agents (tier 3) need domain allowlists and prompt injection mitigations.
- **Skills Are Not Free Lunch**: Skills supercharge discoverability but pile on too many and the problem shifts — agents call skills when they shouldn't, context window grows.
- **Agent Experience (AX)**: User experience is evolving to incorporate agent experience. Agents are "our next users — let's help them help us."

## Entities
- [[Michael Hablich]] — Product Manager for Chrome DevTools at Google, guest lecturer, 20 years in tech
- [[Chrome DevTools]] — Browser developer tools built into Chrome, used by millions of web developers
- [[Chrome DevTools MCP]] — Purpose-built MCP server for agents to debug, profile, and audit web pages
- [[Google]] — Company behind Chrome DevTools
- [[Gemini CLI]] — MCP-capable agent harness used in the demo
- [[SimonWillison]] — Security researcher; Lethal Trifecta model referenced for trust design
- [[ClaudeCode]] — Referenced as an MCP-capable agent harness
- [[Codex]] — Referenced as an MCP-capable agent harness (OpenAI)
- [[OpenClaw]] — Referenced as an MCP-capable agent harness

## Concepts
- [[Agents As Different User Class]] — Agents share goals with humans but have different cognitive bottlenecks
- [[Tokens Per Successful Outcome]] — Fuel efficiency metric for agent interfaces
- [[Semantic Summaries]] — Returning structured summaries instead of raw data to agents
- [[Error Recovery For Agents]] — Spectrum of error recovery: messages, detours, playbooks
- [[Proactive Detours]] — Counteracting model training biases by steering agents to correct tools
- [[Diagnostic Playbooks]] — Troubleshooting skills enabling agent self-healing
- [[Agent Discoverability]] — Making tools findable for agents; schema as UI
- [[MCP Tool Description Quality]] — 97% of descriptions have quality smells; trade-offs in fixing them
- [[Slim Mode]] — Exposing minimal tools to save context window at cost of extra turns
- [[Tool Categorization]] — Hiding niche tools behind CLI parameters
- [[CLI For Agents]] — Command-line interface for token-efficient post-processing
- [[Trust Boundaries For Agents]] — Friction by design; never compromise trust for convenience
- [[Browser Agent Security Tiers]] — Three-tier security model: local, CI/CD, full internet
- [[Agent Experience]] — UX evolving to incorporate agent experience (AX)
- [[LethalTrifecta]] — Simon Willison's security model referenced for trust design
- [[Agent Skills]] — Skills supercharge discoverability but are not free lunch
- [[Tool Description]] — Schema is the UI for agents
- [[AgenticProductDesign]] — Designing interfaces optimized for agents

## Related
- [[MCP]] — Model Context Protocol
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — complementary MCP design advice
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — MCP protocol future
- [[summary-20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz]] — MCP server security
- [[summary-20260523 - Introducing WebMCP： Agents in the Browser — RL Nabors]] — browser agent MCP
