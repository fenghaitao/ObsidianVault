---
title: "AgenticSearchInterface"
type: concept
tags: [agents, search, design, context]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md"]
last_updated: 2026-06-25
---

## Definition
Agentic search interface is the design pattern of creating search mechanisms that make a problem as in-distribution as possible for the agent. It involves translating data into interfaces the model already knows well (SQL, XML, range strings) rather than forcing the model to learn custom search paradigms.

## Key Information
- Core principle: the model knows certain interfaces extremely well (SQL, spreadsheet range syntax like B3:B5, XML). Translate your data into one of these interfaces.
- Example: convert a CSV spreadsheet into a SQLite database so the agent can query it with SQL, which it knows deeply
- Example: use Excel/Sheets range syntax (B3:B5) as a search interface since the model is familiar with spreadsheet formulas
- Example: use XML search queries since .xlsx files are XML under the hood
- Preprocessing is a powerful technique: have another agent annotate or transform data before the main agent searches it
- For large datasets: never load everything into context. Let the agent navigate incrementally, keeping a scratch pad, just as a human would
- The gathering context step of the agent loop is often underthought; creative search interface design can dramatically improve agent performance
- "Try as many different ways as you can" — test SQL, grep, awk, XML, range strings across the same problem and see what the agent prefers

## Related
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[AgentLoop]] — the gather context step
- [[SQLite]] — one translation target
- [[BashTool]] — mechanism for grep/awk approaches
