---
title: "SQLite"
type: entity
tags: [tool, database, sql, cli]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful.md"]
last_updated: 2026-06-25
---

## Definition
SQLite is a self-contained SQL database engine. In the Claude Agent SDK workshop, it was suggested as a creative way to query CSV data by translating spreadsheets into a SQL interface that agents already know well.

## Key Information
- Can interpret CSV files directly, enabling SQL queries against spreadsheet data
- Represents the "translation" pattern: convert data into an interface (SQL) that the model is highly familiar with, making the problem more in-distribution
- Suggested by a workshop attendee as an alternative to grep/awk for spreadsheet search
- Exemplifies the creative thinking needed for designing agentic search interfaces

## Related
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[summary-20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful]] — source
- [[AgenticSearchInterface]] — the design pattern SQLite enables
- [[BashTool]] — the mechanism for invoking SQLite
- [[Effect]] — used with Effect SQL for persistence in the workshop
