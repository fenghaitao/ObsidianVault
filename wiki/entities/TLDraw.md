---
title: "TLDraw"
type: entity
tags: [tool, canvas, drawing, whiteboard]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare.md"]
last_updated: 2026-06-26
---

## Definition
TLDraw is a canvas/drawing library for building whiteboard-style applications. It was used in Kenton's tic-tac-toe demo to demonstrate the concept of inhabiting the state machine, where the canvas state (an array of strokes) served as the system state that the AI agent could read and write.

## Key Information
- Canvas/drawing library for whiteboard-style applications
- Used in Kenton's demo alongside Excalidraw as a reference for the canvas style
- The canvas state is represented as an array of strokes (points, grid lines, shapes)
- The AI agent was able to read this stroke array, recognize a tic-tac-toe board, and draw a response
- Demonstrates how AI agents can interact with existing application state rather than generating new applications

## Related
- [[summary-20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare]] — source
- [[Excalidraw]] — similar drawing tool referenced alongside TLDraw
- [[Kenton]] — used TLDraw in his demo
- [[InhabitingTheStateMachine]] — concept demonstrated using TLDraw
