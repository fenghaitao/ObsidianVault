---
title: "summary-2026-03-24 - Auto mode for Claude Code"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-03-24 - Auto mode for Claude Code.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic introduces **auto mode**, a new permissions mode for Claude Code that lets Claude make permission decisions on its own behalf, with a classifier monitoring each tool call before it runs. It is positioned as a middle path between Claude Code's conservative default (ask before every file write and bash command) and `--dangerously-skip-permissions` (which removes all checks and carries real risk of dangerous or destructive outcomes). Before each tool call, a classifier screens for potentially destructive actions — mass file deletion, sensitive data exfiltration, malicious code execution — allowing safe actions to proceed automatically, blocking risky ones (redirecting Claude to another approach), and escalating to a user permission prompt if Claude keeps hitting blocks. Auto mode reduces but does not eliminate risk versus skipping permissions entirely, since the classifier can still misjudge ambiguous intent or lack environmental context, and Anthropic continues to recommend isolated environments regardless. Launched March 24, 2026 as a research preview for Claude Team plan users, with Enterprise and API rollout "in the coming days," supporting both Claude Sonnet 4.6 and Opus 4.6, with a small expected impact on token consumption, cost, and latency.

## Key Points

- Auto mode is a new Claude Code permissions mode where a classifier reviews each tool call before execution, rather than the user approving every action.
- Safe actions proceed automatically; risky/destructive actions (mass deletion, data exfiltration, malicious code execution) are blocked and Claude is redirected to a different approach.
- Repeated blocking on an action Claude insists on eventually escalates to a human permission prompt.
- Framed as safer than `--dangerously-skip-permissions` but not risk-free: the classifier can still allow risky actions under ambiguous intent or insufficient environmental context, or occasionally block benign actions.
- Still recommended for use in isolated environments, same guidance as other permission-relaxing features.
- May slightly increase token consumption, cost, and latency per tool call.
- Released March 24, 2026 as a research preview on the Claude Team plan; Enterprise plan and API access to follow "in the coming days."
- Compatible with both Claude Sonnet 4.6 and Claude Opus 4.6.

## Related

- [[ClaudeCode]] — the tool auto mode is a permissions mode within
- [[PermissionModes]] — the broader concept of Claude Code's permission system (default, auto-accept-edits, plan mode, sandboxing, auto mode, skip-permissions)
- [[Sandboxing]] — sibling risk-reduction approach (OS-level isolation vs. classifier-based auto mode)
- [[ClaudeTeamPlan]] — plan where auto mode first ships as a research preview
- [[ClaudeEnterprise]] — plan auto mode is rolling out to next
- [[Claude4.6Sonnet]] — model auto mode supports
- [[Claude4.6Opus]] — model auto mode supports
