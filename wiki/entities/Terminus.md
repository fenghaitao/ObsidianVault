---
title: "Terminus"
type: entity
tags: [tool, coding-agent, benchmark, minimal-design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - Building pi in a World of Slop — Mario Zechner.md"]
last_updated: 2026-06-26
---

## Definition
Terminus is a minimal coding agent harness that tops the Terminal Bench leaderboard. It provides the model with only two tools: send keystrokes to a tmux session and read the tmux session output. Despite (or because of) its minimalism, it outperforms more complex harnesses including the native harnesses of the models it uses.

## Key Information
- Tops the Terminal Bench leaderboard as of December 2025
- Only two tools: keystroke send to tmux + read tmux output
- No file tools, no sub-agents, no other tooling
- Scores higher than the native harness of the same model family
- Outperforms regardless of model family
- Key implication for Mario Zechner: minimal agent design can be more effective than complex harnesses
- Influenced Pi's design philosophy of minimal tools and system prompts

## Related
- [[summary-20260416 - Building pi in a World of Slop — Mario Zechner]] — source transcript
- [[TerminalBench]] — the benchmark Terminus tops
- [[Pi (coding agent)]] — influenced by Terminus's minimal design
- [[MinimalAgentDesign]] — design philosophy validated by Terminus
