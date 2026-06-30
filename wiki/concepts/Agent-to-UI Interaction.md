---
title: "Agent-to-UI Interaction"
type: concept
tags: [mcp, mcp-apps, ui, agents, interaction]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps.md"]
last_updated: 2026-06-29
---

## Definition
Agent-to-UI Interaction is an upcoming MCP Apps feature that standardizes how AI models can interact with UI views — clicking buttons, filling forms, and performing actions within MCP App interfaces. It reverses the existing flow (user interacts with UI → UI sends message to model) to also allow model → UI interaction.

## Key Information
- Currently, MCP Apps supports user-to-UI-to-model interaction only
- Agent-to-UI Interaction would allow the model to click buttons, fill forms, and interact with the UI directly
- Apps would expose tools specifically for the model to interact with the view
- Existing solutions like WebMCP already do this, but MCP Apps is working on a standardized approach
- Still an open PR as of the talk, under active development in the MCP Apps committee
- Closes the loop: user ↔ UI ↔ model becomes fully bidirectional

## Related
- [[summary-20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps]] — source transcript
- [[MCP Apps]] — the protocol
- [[WebMCP]] — existing solution in the same space
- [[Computer Use]] — related capability for model-driven UI interaction
