---
title: "PermissionModes"
type: concept
tags: [claude-code, permissions, security, autonomy]
sources: [raw/01-articles/claude/2026-03-24 - Auto mode for Claude Code.md]
last_updated: 2026-07-04
---

## Definition

Permission modes are the set of configurable policies governing when Claude Code asks a human for approval before writing files or running commands, spanning a spectrum from fully manual approval to fully autonomous execution.

## Key Information

- **Default mode**: every file write and bash command asks for approval — conservative and safe, but interrupts long-running tasks frequently.
- **Auto-accept edits mode**: file edits proceed without asking, but commands still require approval.
- **Plan mode**: read-only; Claude compiles a plan before taking any action.
- **Auto mode** (March 2026, research preview): a classifier screens each tool call before execution, auto-approving safe actions, blocking destructive ones (mass deletion, data exfiltration, malicious code execution) and redirecting Claude, and escalating to a human prompt if blocks persist. Positioned as safer than `--dangerously-skip-permissions` but not risk-free — the classifier can misjudge ambiguous intent or lack environmental context. Works with Claude Sonnet 4.6 and Opus 4.6; small token/cost/latency overhead. Shipped first on the Team plan, with Enterprise and API access following.
- **`--dangerously-skip-permissions`**: removes all permission checks; fastest but genuinely dangerous outside isolated environments — explicitly discouraged by Anthropic except in sandboxed/isolated contexts.
- **Sandboxing** is a complementary, distinct risk-reduction axis: OS-level filesystem/network isolation rather than per-action classification — see [[Sandboxing]].

## Related

- [[summary-2026-03-24 - Auto mode for Claude Code]] — source summary introducing auto mode
- [[ClaudeCode]] — the tool these permission modes govern
- [[Sandboxing]] — complementary OS-level isolation approach
- [[PromptInjection]] — threat model these modes partly mitigate
