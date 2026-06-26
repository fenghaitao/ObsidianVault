---
title: "MinimalAgentDesign"
type: concept
tags: [agents, architecture, design, tools]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - Building pi in a World of Slop — Mario Zechner.md"]
last_updated: 2026-06-26
---

## Definition
Minimal agent design is the philosophy that coding agents should have tiny system prompts, few tools, and simple architectures because models are already reinforcement-trained to be coding agents. Mario Zechner's Pi embodies this with only 4 tools (read, write, edit, bash) and a system prompt that fits on a slide.

## Key Information
- Mario Zechner: "The models are actually reinforcement trained up to a zoo. So, they didn't know what a coding agent is, because the coding agent harness is basically what they're being trained when they are post-trained. You don't need 10,000 tokens to tell them, 'You're a coding agent.' They know, because they are coding agents now."
- Pi's system prompt is minimal — fits on a slide; later added a few lines for skills (markdown files)
- Only 4 tools: read, write, edit, bash — tool definitions are tiny compared to other harnesses
- Terminal Bench validates this: Terminus (only keystroke send + tmux read tools) tops the leaderboard regardless of model family
- Contrasts with Claude Code's complex system prompt, many tools, and hidden context manipulation
- Related to Anthropic's "give it tools and get out of the way" philosophy, but taken further

## Related
- [[summary-20260416 - Building pi in a World of Slop — Mario Zechner]] — source transcript
- [[Pi (coding agent)]] — implements minimal design
- [[Terminus]] — validates minimal design on Terminal Bench
- [[TerminalBench]] — benchmark showing minimal design wins
- [[MarioZechner]] — originator
- [[SimpleDesignPhilosophy]] — related Anthropic philosophy
- [[BashTool]] — one of the 4 core tools
