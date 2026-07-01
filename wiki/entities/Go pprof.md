---
title: "Go pprof"
type: entity
tags: [tool, profiling, go, performance, debugging, mcp]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub.md"]
last_updated: 2026-06-30
---

## Definition
Go pprof is the built-in profiling tool for the Go programming language. It collects CPU, memory, and other performance data from running Go programs. Liam Hampton used it as the data source for his flame graph MCP App demo.

## Key Information
- Built-in Go profiling tool
- Used in the MCP Apps flame graph demo to profile a Go application over 5 seconds
- Profiled code included bubble sort algorithm and Fibonacci sequence
- The MCP server bundles the Go program, runs it, profiles it with pprof, and returns JSON data linked to a React flame graph UI
- Enables performance analysis directly within VS Code's chat via MCP Apps

## Related
- [[summary-20260606 - Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub]] — source
- [[Liam Hampton]] — Go engineer who used pprof in the demo
- [[Flame Graph Profiling]] — visualization technique fed by pprof data
- [[MCP Apps]] — protocol used to render the profiling UI
- [[Go]] — the programming language
