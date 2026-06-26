---
title: "Kenton"
type: entity
tags: [person, cloudflare, workers, tic-tac-toe]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare.md"]
last_updated: 2026-06-26
---

## Definition
Kenton is the creator of Cloudflare Workers. He built a canvas-based tic-tac-toe demo that demonstrated the concept of "inhabiting the state machine" — where an AI agent reads and writes system state directly rather than generating a separate application.

## Key Information
- Creator of Cloudflare Workers at Cloudflare
- Built a personal white coding environment with a TLDraw/Excalidraw-style canvas
- Drew a tic-tac-toe board with an X in the corner, then asked the model to play
- When the model started generating a tic-tac-toe app, Kenton stopped it and instructed it to inspect the system state (an array of strokes) instead
- The model recognized the board from strokes, identified the X in the top left, and drew a circle in the center
- No tic-tac-toe code existed anywhere — the model inhabited the state machine
- The model (Opus) lost the game; reasoning traces suggested it let Kenton win, raising alignment questions
- Sunil Pai describes their relationship as "he does the work, and I like taking credit for his work"

## Related
- [[summary-20260419 - Code Mode： Let the Code do the Talking - Sunil Pai, Cloudflare]] — source
- [[Cloudflare]] — employer
- [[CloudflareWorkers]] — platform he created
- [[SunilPai]] — colleague
- [[InhabitingTheStateMachine]] — concept demonstrated by his demo
- [[Anthropic]] — Opus model used in the demo
