---
title: "Reusable Views"
type: concept
tags: [mcp, mcp-apps, ui, performance, optimization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps.md"]
last_updated: 2026-06-29
---

## Definition
Reusable Views is an upcoming MCP Apps feature that allows the same UI view to be referenced and reused across multiple interactions, rather than re-rendering a new view from scratch each time. This addresses performance issues for heavy applications where re-rendering creates a poor user experience.

## Key Information
- Currently, MCP Apps renders a new view each time an app is used, even for the same app
- For heavy applications (e.g., Autodesk), re-rendering from scratch takes too long and degrades the user experience
- Reusable Views would allow referencing the same view and pushing new data into it
- A second approach being explored: "flipping the script" — instead of re-rendering, update the existing view in place
- Part of the MCP Apps roadmap and under active development
- Motivated by real-world use cases from companies with complex, heavy UIs

## Related
- [[summary-20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps]] — source transcript
- [[MCP Apps]] — the protocol
- [[Autodesk]] — example company with heavy apps needing this feature
