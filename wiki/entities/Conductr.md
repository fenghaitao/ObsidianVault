---
title: "Conductr"
type: entity
tags: [hackathon, claude-code, music, real-time, webassembly]
sources: [raw/01-articles/claude/2026-04-20 - Meet the winners of our Built with Opus 4.6 Claude Code hackathon.md]
last_updated: 2026-07-04
---

## Definition

Conductr is a browser-based MIDI instrument built by electronic musician Asep Bagja Priandana, a winner of Anthropic's "Built with Opus 4.6" Claude Code hackathon, that turns Claude into a live virtual bandmate.

## Key Information

- Listens as the user plays chords on a MIDI controller, analyzes the performance, and generates four tracks (drums, bass, melody, harmony) in real time; natural-language prompts like "make it funky" or "build to a climax" change the arrangement mid-jam.
- Technical challenge was keeping the music uninterrupted: a C engine compiled to WebAssembly generates notes every 15 milliseconds, so Claude's arrangement decisions reshape the music without breaking the flow ("musically invisible" latency).
- Runs on about 4,800 lines of JavaScript and WebAssembly.

## Related

- [[summary-2026-04-20 - Meet the winners of our Built with Opus 4.6 Claude Code hackathon]] — source summary
- [[ClaudeCode]] — tool used to build Conductr
