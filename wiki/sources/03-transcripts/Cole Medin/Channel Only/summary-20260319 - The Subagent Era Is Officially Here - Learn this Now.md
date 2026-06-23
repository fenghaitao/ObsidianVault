---
title: "summary-20260319 - The Subagent Era Is Officially Here - Learn this Now"
type: source
tags: [source, original-material, subagents, models, context-rot, codex]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260319 - The Subagent Era Is Officially Here - Learn this Now.md"]
last_updated: 2026-06-20
---

## Core Summary

[[ColeMedin]] argues we've entered the **"sub-agent era"**: model providers are now explicitly building small, fast, cheap LLMs *for sub-agents* (GPT-5.4 Mini/Nano marketed for sub-agents and coding; Gemini 3.1 Flash Lite for "intelligence at scale"), and every coding agent is building sub-agents in. Because sub-agent work (codebase analysis, web research) is token-heavy but low-reasoning, cheap models make massive [[SubAgent]] use viable — the key lever against [[ContextRot]] (the "Isolate" pillar of the [[WISKFramework]]).

## Key Points

- **The trajectory matters more than any one model**: the industry is shifting effort from the biggest models to smaller/cheaper/faster ones, heading toward effectively "unlimited budget" for sub-agent usage.
- **Model economics** (why cheap+fast matters for sub-agents):
  - Cole's prior go-to was **Claude Haiku 4.5** (~$1/M input, $5/M output, ~53 tok/s) — cheap but not *that* cheap or fast.
  - **GPT-5.4 Nano** is ~**1/5 the price**, ~**188 tok/s**, and more powerful than Haiku 4.5; **GPT-5.4 Mini** is also cheaper than Haiku and faster. LiveBench: GPT-5 Mini (predecessor) ~66 vs Haiku 4.5 ~61.
  - Using a *large* model (Opus 4.6, GPT-5.4-High) for sub-agents would blow your weekly rate limit fast; cheap models keep sub-agent usage to a few percent. Cole is even considering switching from Claude Code to **[[Codex]]** for the sub-agent model economics.
- **Sub-agents are now built into most coding agents**: [[ClaudeCode]] (first; growing hooks/custom-subagent support), [[Codex]] (where you pick GPT-5.4 Mini), Gemini CLI (experimental), GitHub Copilot, [[Cursor]], OpenCode — so you often don't build custom ones. Built-ins auto-pick cheaper models (Claude Code uses Haiku/Sonnet under the hood vs Opus in the main window; Codex GPT-5.4 Mini at medium reasoning).
- **Research only — never implementation** (warning repeated): sub-agents spend 10s–100s of thousands (even *millions*) of tokens and return a small summary, which is perfect for synthesis but bad for implementation — the main agent must see all the files it changes to validate. Cole's failed experiment: parallel front-end/back-end/database sub-agents that don't talk to each other → hallucinations.
- **Concrete token scale** (a worktree-bug planning example, 3 parallel sub-agents): Claude Code used 80k/96k/40k tokens; Codex used 70k (frontend) + ~2M (web research) + ~1.5M (backend) — only sane with dirt-cheap models. Per-model control: Claude Code can be told to use Haiku/Sonnet for a sub-agent; Codex GPT-5.4 Mini.
- **Use them for everything** (not just planning): codebase analysis, web research, **code review**, validation. The **"sidecar" pattern** — when you hit an unrelated bug mid-feature, spin up a sub-agent to research it and file a GitHub issue without polluting your primary context.

## Related

- [[SubAgent]] — the pattern this video is entirely about
- [[WISKFramework]] — sub-agent isolation is its "Isolate" pillar
- [[ContextRot]] — the problem cheap-model sub-agents help solve
- [[Codex]] — strong sub-agent host (GPT-5.4 Mini); Cole eyeing a switch
- [[ClaudeCode]] — first to ship sub-agents; per-model selection
- [[Cursor]] — among the tools with built-in sub-agents
- [[ColeMedin]] — articulator
