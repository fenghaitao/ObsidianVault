---
title: "MCP Apps Message Passing"
type: concept
tags: [mcp, mcp-apps, ui, protocol, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps.md"]
last_updated: 2026-06-29
---

## Definition
MCP Apps Message Passing is the standardized mechanism by which interactive UI chunks in MCP Apps communicate back to the host. Instead of the UI talking directly to its backend, every user interaction sends a message to the host, which decides what to do — keeping the model in the loop and all context with the host.

## Key Information
- Every click, every interaction in an MCP App sends a message back to the host
- The host receives the message and decides what action to take (call a tool, run a prompt, etc.)
- This breaks the traditional model where apps own the user journey — in MCP Apps, control stays with the host
- If the UI spoke directly to its backend (e.g., favoriting a song on Spotify), the host/model wouldn't know about it
- Standardized message passing ensures everything stays in context
- This is a fundamental shift in software architecture: apps no longer own the interaction flow

## Related
- [[summary-20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps]] — source transcript
- [[MCP Apps]] — the protocol defining this mechanism
- [[MCP Apps UI Spectrum]] — the three message types (notification, tool call, prompt)
- [[MCP]] — the underlying protocol
