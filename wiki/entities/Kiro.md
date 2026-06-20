---
title: "Kiro"
type: entity
tags: [tool, ai-coding-assistant, agent-cli, ide, aws]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260101 - AI Exploded in 2025 - Here’s Everything That Happened.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260105 - The Kiro AI Coding Hackathon has Officially Started! Build ANYTHING, Win Big Prizes.md"
last_updated: 2026-06-20
---

## Definition

Kiro is a feature-rich agentic AI coding assistant in the [[AICodingAssistant]] agentic ("loop-first") camp, available as both a CLI (Cole's preferred surface) and an IDE. It is associated with Amazon/AWS's 2025 push into coding agents (referenced as "Amazon's Kiro/Hero" in Cole's 2025 recap). [[ColeMedin]] treats it as a credible [[ClaudeCode]] counterpart and partnered with the Kiro team for a January 2026 hackathon.

> **Transcription note:** the auto-transcript renders the name inconsistently as "Kuro", "Curo", "Kira", "Kirao", and "Hero". These all refer to **Kiro**.

## Key Information

### Workflow primitives

Kiro's project model mirrors patterns this wiki already documents for [[ClaudeCode]]:

- **Steering documents** — Kiro's term for **global rules** that guide the agent across a project (the [[ModularRulesArchitecture]] / `CLAUDE.md` equivalent). Set up via an interactive quick-start command that interviews the developer.
- **Prompts / commands** — reusable workflows defined in markdown (the [[Commandification]] equivalent of `.claude/commands/`).
- **Devlog** — a running record of timeline, decisions, and challenges; Kiro encourages documenting the *development journey*, not just the finished code.
- **`.kiro` folder** — project-root config directory holding steering docs and prompts (analogous to `.claude/`); concepts translate between CLI and IDE.

### Advanced features

- **Tangent mode** — a Kiro-specific mode for side explorations.
- **Cross-session knowledge management** — persistence of context/knowledge between sessions.
- **Sub-agents** — built-in [[SubAgent]] delegation.
- **MCP servers** — first-class [[ModelContextProtocol]] client support.

### Positioning

Cole groups Kiro with [[ClaudeCode]] as agentic-first (long autonomous loops) rather than interactive-first like [[Cursor]] / [[Windsurf]]. He notes the CLI is preferred over the IDE for serious work, and provides a clonable GitHub quick-start template with a "Kiro guide" aimed at users migrating from other AI coding assistants.

## Related

- [[AICodingAssistant]] — Kiro's category (agentic/loop-first camp)
- [[ClaudeCode]] — closest counterpart; same workflow-primitive model
- [[Commandification]] — Kiro "prompts/commands" pattern
- [[ModularRulesArchitecture]] — Kiro "steering documents" pattern
- [[SubAgent]] — built-in delegation
- [[ModelContextProtocol]] — MCP client support
- [[ColeMedin]] — partnered for the hackathon
- [[summary-kiro-hackathon]] — primary source
- [[summary-ai-exploded-in-2025]] — Amazon's coding-agent push (2025 recap)
