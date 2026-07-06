---
title: "summary-2025-11-17 - How three YC startups built their companies with Claude Code"
type: source
tags: [source, claude-code, y-combinator, case-studies, agentic-coding]
sources: ["raw/01-articles/claude/2025-11-17 - How three YC startups built their companies with Claude Code.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic profiles three [[YCombinator]] startups built substantially with [[ClaudeCode]]: [[HumanLayer]] (human-approval infrastructure for risky agent actions, later pivoting to parallel Claude Code session tooling via CodeLayer), [[Ambral]] (an account-management AI built solo by a CTO using the Claude Agent SDK and dedicated data-type subagents), and [[Vulcan]] (non-engineer founders who won a Virginia state government contract for AI-powered regulatory analysis).

## Key Points

- **HumanLayer**: founded on the insight that the most useful agent functions are also the riskiest (e.g., dropping database tables); built an API/SDK letting agents request human approval via Slack, email, SMS. Published "12-Factor Agents" (April 2025), a widely-circulated guide to production agent architecture and context engineering. Pivoted around Claude Code and the Claude Agent SDK's headless execution to build CodeLayer, which runs multiple Claude Code sessions in parallel via worktrees and remote cloud workers — surfacing organizational (not just technical) challenges once whole teams ship AI-written code.
- **Ambral**: solves account-manager context overload (50-100 accounts each) by synthesizing customer signals into per-account AI models. Sole engineer/CTO Jack Stettner uses a three-phase workflow — Opus 4.1 for research/planning, Sonnet 4.5 for implementation from markdown plans, discrete sessions per phase to avoid context contamination — and built the product's core research engine on the [[ClaudeAgentSDK]] with dedicated [[ClaudeCodeSubagents|subagents]] per data type (Slack, meeting transcripts, product usage).
- **Vulcan**: founders Aleksander Mekhanik and Tanner Jones (no engineering background) built a regulatory-analysis prototype for Virginia's governor's office by copy-pasting Claude outputs (pre-Claude Code), winning the contract over established consulting firms; velocity multiplied again once Claude Code launched. Reduced Virginia's average new-home price by $24,000, prompting the governor to sign Executive Order 51 mandating agentic AI regulatory review across state agencies. Raised an $11M seed round.
- **Shared practices**: use discrete prompts/sessions per phase (research vs. planning vs. implementation) rather than mixing them in one context; watch Claude's reasoning and interrupt early on a wrong direction rather than letting a misguided approach run to completion; be deliberate about what enters a system prompt to avoid internal contradictions degrading output quality.

## Related

- [[ClaudeCode]] — the tool underlying all three startups' velocity
- [[ClaudeAgentSDK]] — powers Ambral's product and HumanLayer's CodeLayer
- [[ClaudeCodeSubagents]] — Ambral's per-data-type subagent architecture
- [[YCombinator]] — the accelerator all three startups are part of
- [[HumanLayer]] — profiled startup
- [[Ambral]] — profiled startup
- [[Vulcan]] — profiled startup
