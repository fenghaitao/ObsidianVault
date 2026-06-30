---
title: "File-over-App"
type: concept
tags: [local-first, philosophy, ai-agents, agency, security]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260501 - Agents on the Canvas in tldraw — Steve Ruiz, tldraw.md"]
last_updated: 2026-06-29
---

## Definition
File-over-App is a design philosophy that prioritizes local, file-based applications over cloud services. In the context of AI agents, it becomes a practical enabler: local file-based apps can safely expose themselves to AI agents for full script injection and modification, maximizing agency while containing risk to the user's own machine.

## Key Information
- Previously an idealistic philosophy — now validated by AI agent use cases
- **AI motivation**: If you want to maximize what an AI agent can do (full script injection, DOM access, code modification), you need to give it full access to a local app
- **Risk containment**: A local, file-based desktop app limits the blast radius to the user's own machine — "what's the worst that could happen? You could hurt yourself, I guess, but you're not going to hurt the rest of me"
- **Contrasts with web apps**: Web apps cannot safely expose themselves to arbitrary AI script injection because they affect all users
- **Sharp tools philosophy**: Like Claude Code's approach, the philosophy is to hand the user powerful but dangerous tools and say "good luck" — the user accepts the risk
- **Local-first movement**: Part of the broader local-first software movement that values user ownership of data and offline capability
- **Desktop app as sandbox**: The Electron desktop app acts as a natural sandbox boundary — the agent can modify the app but cannot reach beyond the local machine
- Enables use cases like: AI modifying Spotify's desktop app to remove podcasts, AI making canvas drawings interactive with script injection

## Related
- [[summary-20260501 - Agents on the Canvas in tldraw — Steve Ruiz, tldraw]] — source
- [[Script Injection by AI]] — the capability this philosophy enables
- [[Sandboxing]] — the security model this aligns with
- [[Self-Hosting for Agents]] — related concept
- [[ClaudeCode]] — shares the "sharp tools" philosophy
