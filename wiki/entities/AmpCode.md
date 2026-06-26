---
title: "AmpCode"
type: entity
tags: [product, coding-agent, terminal, editor]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - Amp Code： Next Generation AI Coding – Beyang Liu, Amp Code.md"]
last_updated: 2026-06-25
---

## Definition
Amp Code (AMP) is an opinionated frontier coding agent that can be invoked from the terminal or integrated into editors (VS Code, Cursor, Windsurf, Anti-gravity, Emacs, Neovim, JetBrains). It features a custom TUI framework, specialized sub-agents, and a dual-agent architecture.

## Key Information
- Built a complete terminal UI framework from scratch to leverage modern terminal capabilities (including graceful degradation for basic terminals)
- Editor integration collects diagnostics from Emacs, Neovim, and JetBrains
- Two top-level agents: Smart Agent (complex tasks, sub-agent access) and Rush Agent (fast, tight-loop edits)
- Four core sub-agents: Finder (codebase search), Oracle (deep reasoning), Librarian (external library context), Kraken (large-scale refactors via codemods)
- Custom diff viewer in the editor optimized for reviewing agentic output, with a guided tour feature
- Thread sharing feature allows teammates to see each other's agent sessions and prompting techniques
- Experimental ad network sponsors inference costs for the Rush Agent
- Recently adopted Gemini 3 as the Smart Agent model
- Positions itself as an "agentic research lab" targeting early adopters who "want to live a little bit in the future"
- Notable users include Mitchell Hashimoto (Ghosty) and Hamill Hussein (AI evals authority)
- Community of builders run by Ryan Carson (former Treehouse founder)

## Related
- [[summary-20251222 - Amp Code： Next Generation AI Coding – Beyang Liu, Amp Code]] — source
- [[BeyangLiu]] — team member and presenter
- [[SubAgents]] — core architectural pattern
- [[AgentOrientedArchitecture]] — Amp's architectural philosophy
- [[Ghosty]] — terminal emulator; core contributor built Amp's TUI
- [[MitchellHashimoto]] — notable user
- [[HamillHussein]] — notable user
- [[RyanCarson]] — community leader
- [[Gemini3]] — model powering the Smart Agent
