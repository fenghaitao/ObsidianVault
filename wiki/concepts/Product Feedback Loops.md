---
title: "Product Feedback Loops"
type: concept
tags: [ai, product-engineering, feedback-loops, iteration, testing, observability]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - Feedback Loops are All You Need — Mehedi Hassan, Granola.md"]
last_updated: 2026-06-29
---

## Definition
Product Feedback Loops are the rapid iteration cycles that product teams use to observe, trace, diagnose, and improve AI features. The core insight from Granola is that the answer to shipping great AI isn't "one-shotting better" — it's tightening the feedback loop until AI development feels like "playing tennis with an LLM," where each return gives immediate information to adjust the next shot.

## Key Information
- **Core thesis**: Building fast, tight feedback loops is more important than getting LLM prompts right in one shot
- **Two complementary loops**: (1) Tracing/observability — custom tools that give full visibility into LLM tool calls, reasoning, and costs; (2) Testing/experimentation — infrastructure that enables rapid parallel testing of multiple feature variants
- **Tracing loop**: Custom-built tracing tools with full visibility over individual tool calls, why they were made, search tools, reasoning tools, and costs — structured data served through a UI accessible to non-engineers (product, data, CX)
- **Testing loop**: Converting desktop app front-ends to web shells deployed online, generating preview links per PR, enabling LLMs to self-verify and upload screenshots into PRs
- **Multi-persona problem**: One prompt cannot serve all users — sales wants deal-focused summaries, engineering wants action items and Linear tickets, HR wants something different; feedback loops enable testing variants for each persona
- **Web search as a cautionary tale**: Adding web search to an LLM looks like one line of code but has hidden complexity (token costs balloon, provider changes degrade quality, billion-dollar companies exist solely for web search)
- **LLMs enabled custom tooling**: Previously, building custom tracing tools required a SaaS provider and too much time; now teams can one-shot custom tools that exactly serve their needs
- **Conviction through iteration**: The end goal is having conviction that what you're shipping connects with users — achieved by experiencing many variants in practice, not just seeing them in Figma
- **Non-engineer accessibility**: Tracing UIs should be built for product, data, and CX teams, not just engineers, so the entire organization can participate in the feedback loop

## Related
- [[Mehedi Hassan]] — speaker who presented this concept
- [[Granola]] — company that implements product feedback loops
- [[Feedback Loops as AI Speed Limit]] — related concept from Matt Pocock about codebase feedback loops
- [[Web Shell Pattern]] — the testing half of the feedback loop
- [[Custom Tracing Tools]] — the observability half of the feedback loop
- [[AI Observability]] — broader observability category
- [[AgentObservability]] — related concept in agent systems
- [[EvalFlywheel]] — continuous improvement via eval feedback
- [[summary-20260510 - Feedback Loops are All You Need — Mehedi Hassan, Granola]] — source transcript
