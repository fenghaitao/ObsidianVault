---
title: "Codex"
type: entity
tags: [tool, openai, ai-coding-assistant, agent-cli, harness]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260330 - Coding Agent Reliability EXPLODES When They Argue (New Adversarial Dev Technique).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260528 - Harness Engineering： What Separates Top Agentic Engineers Right Now.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260319 - The Subagent Era Is Officially Here - Learn this Now.md"
last_updated: 2026-06-20
---

## Definition

Codex is [[OpenAI]]'s agentic coding assistant — the primary competitor to [[ClaudeCode]] as a terminal/CLI-based coding agent. In [[ColeMedin]]'s 2026 content it appears consistently as the "or Codex" alternative whenever he discusses Claude Code, and he builds Codex-parallel versions of his harnesses to demonstrate tool-agnosticism.

## Key Information

### Role in this corpus

- **The standard alternative to Claude Code.** Cole's recurring phrasing: "Claude Code, Codex, Pi, you name the millions of coding agents." Codex is the most-named alternative.
- **Adversarial dev parity** — in `summary-adversarial-dev-technique`, Cole built both a Claude Code and a Codex version of the generator/evaluator harness, with identical structure, to prove the [[AdversarialDev]] pattern isn't Anthropic-specific. You can even mix: Claude as generator, Codex as evaluator (cross-model evaluation reduces shared blind spots).
- **A "harness" in [[HarnessEngineering]] terms** — Codex, like Claude Code, *is itself a harness* OpenAI engineered around its model (GPT family). When you choose Codex, you're picking that vendor's wrapper. The [[AILayer]] you build on top is what differentiates your usage.

### Codex vs Claude Code

Cole notes there's "a lot of debate right now" over which is the best harness for coding — some say Claude Code, some say Codex. He uses Claude Code as his primary driver but treats Codex as a fully legitimate alternative and builds his patterns to work with both.

The two are architecturally similar from the user's perspective:
- Terminal/CLI-based agentic coding.
- Filesystem + git + command execution.
- Subscription or API-key auth (Cole notes you can use a subscription for local dev/experimentation with the Agent SDK; API key required if others use your script — same ToS pattern for both).

### Cross-model harnesses

A recurring Cole theme: harnesses let you mix models/tools. Because different models have different blind spots, a cross-model [[AdversarialDev]] setup (Claude implements, Codex critiques, or vice versa) can be *more* robust than single-model. Codex is the natural counterpart to Claude in these setups.

### Strong sub-agent host (the "sub-agent era")

Per `summary-subagent-era`, Codex is a first-class place to run sub-agents with **GPT-5.4 Mini/Nano** — small models OpenAI explicitly markets for sub-agents and coding (cheaper and faster than Claude Haiku 4.5, and more capable). You can tell Codex which model to use for its sub-agents (e.g. GPT-5.4 Mini at medium reasoning), and it'll fan out parallel research agents burning huge token counts cheaply. Cole notes he's *considering switching from Claude Code to Codex* largely because of this sub-agent model economics. See [[SubAgent]].

## Related

- [[OpenAI]] — vendor
- [[ClaudeCode]] — primary competitor / counterpart
- [[SubAgent]] — Codex as a strong sub-agent host (GPT-5.4 Mini)
- [[AICodingAssistant]] — category
- [[HarnessEngineering]] — Codex is itself a vendor-built harness
- [[AdversarialDev]] — Cole built Codex and Claude versions; cross-model mixing
- [[AILayer]] — what you build on top of Codex
- [[ColeMedin]] — uses Codex as the standard Claude Code alternative
- [[summary-20260330 - Coding Agent Reliability EXPLODES When They Argue (New Adversarial Dev Technique)]], [[summary-20260528 - Harness Engineering： What Separates Top Agentic Engineers Right Now]] — primary sources
- [[summary-20260319 - The Subagent Era Is Officially Here - Learn this Now]] — Codex + GPT-5.4 Mini sub-agents
