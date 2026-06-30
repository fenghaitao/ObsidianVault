---
title: "TLDraw"
type: entity
tags: [tool, canvas, drawing, whiteboard, company, sdk, ai-agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260501 - Agents on the Canvas in tldraw — Steve Ruiz, tldraw.md"]
last_updated: 2026-06-29
---

## Definition
TLDraw is a London-based startup that makes an online whiteboard, a whiteboard SDK used by products like Replit and Luma AI, and experimental AI-on-canvas projects. The canvas is built with React components, making it hackable and extensible for AI agent integration.

## Key Information
- Three things in one: online whiteboard (free, at tldraw.com), startup (London-based), and SDK for building other products
- Canvas is built entirely with React components — "component component component" — making it highly hackable
- SDK used by Replit (agent canvas), Luma AI (canvas), Stitches (annotate mode), Lovelace, and Magic Path
- Canvas state is represented as an array of strokes (points, grid lines, shapes) that AI agents can read and write
- Pioneered AI-on-canvas experiments: Make Real (2023), AI collaborator, Fairies multi-agent canvas (2024), desktop app with script injection
- Desktop app (Electron wrapper) exposes an HTTP endpoint for AI agents to execute JavaScript directly on the canvas
- The hackable nature creates a tension: agents want full access, but safety concerns arise with web-based deployments
- Active on Twitter/X at @tldraw; founder Steve Ruiz at @steveruizok

## Related
- [[summary-20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare]] — source (Kenton's state machine demo)
- [[summary-20260501 - Agents on the Canvas in tldraw — Steve Ruiz, tldraw]] — source
- [[Steve Ruiz]] — founder
- [[Make Real]] — 2023 AI-on-canvas project
- [[Fairies]] — multi-agent canvas project
- [[Replit]] — uses tldraw SDK for agent canvas
- [[Luma AI]] — uses tldraw canvas
- [[Stitches]] — uses tldraw in annotate mode
- [[Lovelace]] — design app using tldraw
- [[Magic Path]] — design app using tldraw
- [[Excalidraw]] — similar drawing tool
- [[Kenton]] — used TLDraw in his demo
- [[InhabitingTheStateMachine]] — concept demonstrated using TLDraw
- [[Agents on Canvas]] — paradigm pioneered by tldraw
- [[Canvas as Agent Workspace]] — spatial shared state concept
