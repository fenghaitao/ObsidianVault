---
title: "Flame Graph Profiling"
type: concept
tags: [profiling, performance, visualization, mcp-apps, go, debugging]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub.md"]
last_updated: 2026-06-30
---

## Definition
Flame graph profiling is a performance analysis technique that visualizes where a program spends its CPU time. In the MCP Apps context, flame graphs are rendered as interactive UI components in VS Code's chat, allowing developers to explore profiling data without leaving the conversational interface.

## Key Information
- **Traditional format**: Flame graphs produce complex, dense data that is difficult to parse as raw text
- **MCP App integration**: Liam Hampton built an MCP App that profiles Go application code using Go pprof, then renders the results as an interactive flame graph in VS Code's chat
- **Interactive features**: Users can view top functions, summary statistics, and interact with the flame graph directly in the chat — clicking, exploring, and editing the view
- **Workflow improvement**: Instead of asking AI models "is this good? Is this bad? Where am I spending my time?" through text, the interactive UI eliminates back-and-forth by presenting all profiling data visually
- **Architecture**: The MCP server bundles the Go program, runs it, profiles it with Go pprof, returns JSON data with a UI resource reference, and the React-based flame graph UI renders in a sandboxed iframe
- **Demo code**: Used bubble sort algorithm and Fibonacci sequence as the profiled Go application

## Related
- [[summary-20260606 - Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub]] — source
- [[Liam Hampton]] — builder of the flame graph MCP App demo
- [[MCP Apps]] — protocol enabling the interactive visualization
- [[Go pprof]] — Go profiling tool that generates the data
- [[Sandboxed Iframe]] — rendering mechanism
- [[VisualStudioCode]] — host rendering the flame graph
- [[MCPApplications]] — the broader MCP Applications feature
