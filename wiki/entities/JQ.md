---
title: "JQ"
type: entity
tags: [tool, json, cli, bash]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md"]
last_updated: 2026-06-25
---

## Definition
JQ is a lightweight command-line JSON processor. In the Claude Agent SDK context, it exemplifies how the bash tool lets agents compose functionality by piping data through existing CLI tools.

## Key Information
- Used as an example of how bash enables composability: agents can pipe tool results through JQ for analysis
- Example use case: after using FFmpeg to slice a video, the agent uses JQ to analyze the resulting structured information
- Demonstrates the "composability" advantage of bash over structured tools

## Related
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[BashTool]] — the mechanism that enables JQ usage
- [[FFmpeg]] — another CLI tool used in the same example pipeline
