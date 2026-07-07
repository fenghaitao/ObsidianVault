---
title: "VirtualPuppetTheater"
type: entity
tags: [hackathon, interactive-play, claude-code, spatial-reasoning, webcam, three-js]
sources: ["raw/01-articles/claude/2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon.md"]
last_updated: 2026-07-07
---

## Definition

Virtual Puppet Theater is a browser-based interactive puppet show app built by Rene Hangstrup Møller. It turns webcam video and voice into a dynamic puppet show where a real-time animated puppet mirrors the user's movements while an AI-driven companion puppet banters with them. Spoken prompts can transform scenery and spawn 3D props on the fly.

## Key Information

- **Creator**: Rene Hangstrup Møller, a full-stack developer intrigued by Opus 4.7's spatial reasoning capabilities.
- **Tech stack**: Built on [[Bun]], [[Vite]], and [[TypeScript]], using MediaPipe hand tracking (running in WASM) and Three.js to render the puppet stage in 3D at 60 fps. A WebSocket server connects to Claude Opus 4.7 via the Anthropic SDK to drive the AI puppet's dialogue and generate 3D props. Voice handled by Web Speech API (input) and ElevenLabs (output), with browser speech synthesis as a fallback.
- **Spatial reasoning**: Opus's spatial reasoning capabilities, refined through a screenshot-based feedback loop, handle the visual output.
- **Purpose**: Open-ended play with no objective. Rene has no product plans — it was about learning and fun.
- **Licensing**: Source code available on GitHub under MIT licensing.

## Related

- [[summary-2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon]] — source summary
- [[ClaudeCode]] — development environment
- [[Claude4.7Opus]] — model providing spatial reasoning capabilities
- [[Bun]] — JavaScript runtime used
- [[TypeScript]] — primary language
