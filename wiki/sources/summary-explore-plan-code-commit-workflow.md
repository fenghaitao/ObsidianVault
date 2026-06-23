---
title: "summary-explore-plan-code-commit-workflow"
type: source
tags: [source, claude-code, workflow, plan-mode, transcript]
sources: [raw/03-transcripts/Claude/Claude Code 101/06 - The Explore → Plan → Code → Commit workflow in Claude Code.md]
last_updated: 2026-06-23
---

## Core Summary

The recommended Claude Code workflow is Explore, Plan, Code, Commit. Most users jump straight to coding, which causes more course correction later. Plan mode (Shift+Tab) is the fastest way through steps 1-2: it reads files, does web research, and produces a plan of action before any code is written. After approving the plan, Claude executes it. Include tools (browser extension for UI testing, test suites) to reduce back-and-forth. Before committing, run a sub-agent code reviewer and have Claude generate a commit message.

## Key Points

- **Explore:** gather relevant context about the codebase; can be done in or out of plan mode.
- **Plan:** use plan mode to produce a detailed plan of action; review and course-correct here before any code is written.
- **Code:** the back-and-forth between user and Claude to implement the plan; Claude troubleshoots but may need steering.
- **Commit:** review the code, run a sub-agent code reviewer, have Claude generate a commit message, then push.
- Include tools that help Claude self-validate: browser extension for UI testing, test suites for continuous validation.
- If Claude repeatedly hits the same issues, ask it to save the solution to CLAUDE.md.
- Make success criteria explicit in the plan so Claude can confidently determine when it's done.

## Related

- [[ClaudeCode]] — the tool this workflow is for
- [[summary-your-first-claude-code-prompt]] — plan mode walkthrough
- [[summary-the-claude-md-file]] — saving solutions to CLAUDE.md
- [[AgenticLoop]] — the loop that executes the plan
