---
title: "summary-20260510 - Feedback Loops are All You Need — Mehedi Hassan, Granola"
type: source
tags: [source, transcript, feedback-loops, product-engineering, ai-tracing, observability, electron, granola, desktop-app, testing, web-shell]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - Feedback Loops are All You Need — Mehedi Hassan, Granola.md"]
last_updated: 2026-06-29
---

## Core Summary
Mehedi Hassan, Product Engineer at Granola, argues that the key to shipping great AI features is not "one-shotting better" but building tight feedback loops. Generic chatbots fail in predictable ways (wrong output style, web search issues, misinterpreted queries) because one prompt cannot serve all user personas (sales, engineering, HR). Granola's approach: (1) build custom tracing tools with full visibility over tool calls, reasoning, and costs, accessible to non-engineers; (2) turn their Electron desktop app's front-end into a web shell deployed online, enabling preview links per PR and allowing LLMs to self-verify work and upload screenshots. The philosophy is to make the feedback loop feel like "playing tennis with an LLM" — rapid iteration that builds conviction about what you're shipping.

## Key Points
- **Generic chatbot failure modes**: Web search too slow or costly (10 pence/chat at scale), wrong output style for different personas, misinterpreted queries ("coach me about meetings" → football coach results)
- **Web search complexity**: Token usage and costs balloon for complex queries; provider-side changes degrade quality overnight with no visibility or control; billion-dollar companies exist solely to do web search well
- **One prompt doesn't serve everyone**: Sales wants deal-focused summaries, engineering wants action items and Linear tickets, HR wants something different entirely
- **Custom tracing tools**: Granola built their own tracing system with full visibility on tool calls from start to end — why each tool call was made, search tools, reasoning tools, costs — structured exactly how they want it
- **UI built for non-engineers**: Product, data, and CX teams can use the tracing UI without writing complex CloudWatch queries; even the founder follows agent loops front-to-back to diagnose failures
- **LLMs made custom tooling viable**: Previously, building this kind of tracing tool would require a SaaS provider and too much time; now you can one-shot custom tracing tools that exactly serve your needs
- **Electron web shell**: Turned the Electron render process into a web shell deployed online, abstracting IPC APIs to fall back to web standards in web environments, and moving React routing/sessions to web standards
- **PR preview links**: CI generates preview links per PR, enabling parallel testing of multiple feature variants simultaneously
- **LLM self-verification**: Cursor goes into preview links, tests features, and uploads screenshots into PRs, dramatically speeding up testing
- **Rapid variant testing**: The web shell enables testing one feature in multiple variants so the team actually experiences products rather than just seeing them in Figma
- **Electron vs Tauri**: Granola tried Tauri but didn't see massive performance gains, which is what they care about most; Electron's APIs serve them well
- **Core philosophy**: The answer isn't to one-shot better — it's about making the feedback loop tight so the end product feels like magic rather than a black box, with conviction that what you're shipping connects with users

## Related
- [[Mehedi Hassan]] — speaker, Product Engineer at Granola
- [[Granola]] — meeting notes app with real-time transcription and AI-generated notes
- [[Feedback Loops as AI Speed Limit]] — related principle from Matt Pocock
- [[Product Feedback Loops]] — the core concept from this talk
- [[Web Shell Pattern]] — pattern for converting Electron apps to web for rapid testing
- [[Electron]] — desktop app framework used by Granola
- [[AI Observability]] — observability for AI systems
- [[AgentObservability]] — related concept in agent systems
- [[Custom Tracing Tools]] — Granola's approach to LLM observability
- [[aiDotEngineer]] — event host
