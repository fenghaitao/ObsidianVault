---
title: "MCP Apps UI Spectrum"
type: concept
tags: [mcp, mcp-apps, ui, protocol, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps.md"]
last_updated: 2026-06-29
---

## Definition
The MCP Apps UI Spectrum represents the three levels of control a UI chunk can have when communicating back to the host, ranging from the UI retaining maximum control (notification) to releasing all control to the host (prompt).

## Key Information
- **Notification**: The highest level of UI control. The UI just notifies the host that something happened. Example: increasing the number of items in a cart — the action goes directly to the backend (e.g., Shopify), and the host is simply informed.
- **Tool Call**: The UI tells the host to call a specific tool. The host decides whether to execute it. This keeps the model in the loop while the UI specifies what should happen.
- **Prompt**: The UI releases all control and tells the host to run a prompt and see what happens. The host/model has full autonomy over the response.
- This spectrum represents a new philosophy in software design: how much control does the UI give to the host vs. retain for itself?
- Standardized as part of the MCP Apps spec

## Related
- [[summary-20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps]] — source transcript
- [[MCP Apps]] — the protocol defining this spectrum
- [[MCP Apps Message Passing]] — the underlying message passing mechanism
- [[MCP]] — the underlying protocol
