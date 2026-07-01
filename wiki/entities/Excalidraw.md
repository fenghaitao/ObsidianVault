---
title: "Excalidraw"
type: entity
tags: [tool, drawing, whiteboard, open-source, mcp, collaboration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - Beyond Components： Designing Generative UI for MCP Apps — Ruben Casas, Postman.md"]
last_updated: 2026-06-30
---

## Definition
Excalidraw is an open-source virtual whiteboard/drawing tool. It was referenced alongside TLDraw in Sunil Pai's talk as the style of canvas used in Kenton's tic-tac-toe demo demonstrating the inhabiting-the-state-machine concept. The Excalidraw MCP App extends it into a shared collaborative canvas for human-agent interaction.

## Key Information
- Open-source virtual whiteboard for sketching and diagramming
- Referenced alongside TLDraw as the style of canvas in Kenton's demo
- The canvas state (array of strokes) serves as system state that AI agents can read and write
- **Excalidraw MCP App**: creates a shared artifact where humans and agents collaborate bidirectionally — users can click around and modify UI while the agent also contributes
- Represented by Ruben Casas as the "beyond components" future of human-agent collaboration

## Related
- [[summary-20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare]] — source
- [[summary-20260603 - Beyond Components： Designing Generative UI for MCP Apps — Ruben Casas, Postman]] — source
- [[TLDraw]] — similar tool referenced alongside Excalidraw
- [[Kenton]] — used this style of canvas in his demo
- [[Excalidraw MCP App]] — MCP application built on Excalidraw
- [[AgentHuman Collaboration]] — paradigm enabled by the MCP app
- [[Agents on Canvas]] — related collaboration pattern
