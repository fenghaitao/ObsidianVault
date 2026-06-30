---
title: "Andrew Wilson"
type: entity
tags: [person, solution-architect, anthropic, applied-ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson.md"]
last_updated: 2026-06-30
---

## Definition
Andrew Wilson is a Solution Architect on Anthropic's Applied AI team based in London, working with digital native and industries customers. He presented the historical evolution of Claude models and harnesses for long-running agents at the 2026 AI Engineer conference.

## Key Information
- Solution Architect on Anthropic's Applied AI team, based out of London
- Works with digital native and industries customers
- Presented the history tour of Claude model and harness evolution: from Sonnet 3.5 (20-minute runs, struggling with bash) through Opus 4.6 (12+ hours on minimal scaffold)
- Covered key releases: computer use, MCP spec, Claude Code (Feb 2025), Claude Code SDK → Agent SDK, skills with progressive disclosure, programmatic tool calling, agent teams, server-side compaction, 1M context GA
- Explained the three challenges for long-running agents: context (finite windows, amnesia, context rot, context anxiety), planning (models aren't great planners, build half-features), verification (models bad at judging own output due to sycophancy)
- Described Anthropic's first blog post harness (Nov 2025): initializer agent, featurelist.json, progress file, fresh context windows per feature, Puppeteer verification
- Emphasized that harnesses don't disappear as models improve — they co-evolve, filling model gaps then being trained into the model
- Co-presented with Ash Prabaker

## Related
- [[summary-20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson]] — source
- [[Ash Prabaker]] — co-presenter
- [[Anthropic]] — company
- [[ClaudeCode]] — coding agent discussed
- [[ClaudeAgentSDK]] — agent framework discussed
- [[RALPH Loop]] — pattern discussed in history
- [[Context Rot]] — challenge for long-running agents
- [[Context Anxiety]] — model behavior discussed
- [[Harness Evolution]] — co-evolution of models and harnesses
- [[Agent Teams]] — sub-agent communication feature
- [[Server-Side Compaction]] — feature enabling indefinite runs
- [[One Million Context Window]] — 1M context GA release
- [[Checkpoints]] — Claude Code 2.0 feature
- [[ProgressiveDisclosure]] — skills mechanism for context efficiency
- [[ProgrammaticToolCalling]] — on-the-fly code for tool calls
