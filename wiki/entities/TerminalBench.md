---
title: "TerminalBench"
type: entity
tags: [benchmark, coding-agents, evaluation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - Building pi in a World of Slop — Mario Zechner.md"]
last_updated: 2026-06-26
---

## Definition
Terminal Bench is a benchmark for coding agent harnesses that Mario Zechner cited as evidence that minimal agent design can outperform complex harnesses. It gives the model only a tool to send keystrokes to a tmux session and read the output — no file tools, no sub-agents, nothing else.

## Key Information
- "Pretty good benchmark, all things considered" per Mario Zechner
- Most minimal design possible: only keystroke send + tmux read tools
- No file tools, no sub-agents, no other tooling
- Terminus (the harness using this approach) scores highest on the leaderboard regardless of model family
- Terminus scores higher than the native harness of the same model
- Leaderboard from December 2025 showed Terminus outperforming across model families
- Key implication: current agent harness form is not the final form; we need better ways to "around and find out"
- Pi scored 6th on Terminal Bench before compaction was added
- Pi's ranking improved after compaction was added (for Peter's Open Claw integration)

## Related
- [[summary-20260416 - Building pi in a World of Slop — Mario Zechner]] — source transcript
- [[Terminus]] — the harness that tops Terminal Bench
- [[Pi (coding agent)]] — scored 6th on this benchmark
- [[MinimalAgentDesign]] — design philosophy supported by Terminal Bench results
