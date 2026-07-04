---
title: "ExplorePlanCodeCommit"
type: concept
tags: [claude-code, workflow, methodology]
sources: [raw/03-transcripts/Claude/Claude Code 101/06 - The Explore → Plan → Code → Commit workflow in Claude Code.md, raw/03-transcripts/Claude/Code with Claude 2026 - San Francisco/13 - Running an AI-native engineering org.md]
last_updated: 2026-07-04
---

## Definition

Explore, Plan, Code, Commit (EPCC) is the recommended workflow for using Claude Code effectively. It structures development into four phases: exploration (gathering context), planning (producing a detailed plan before writing code), coding (iterative implementation), and committing (review and push).

## Key Information

- **Explore:** gather relevant context about the codebase; can be done with or without plan mode.
- **Plan:** use plan mode (Shift+Tab) to produce a detailed plan of action. This is the best place to course-correct because no code has been written yet.
- **Code:** iterative back-and-forth between user and Claude to implement the plan. Claude troubleshoots but may need steering.
- **Commit:** review the code, run a sub-agent code reviewer, have Claude generate a commit message, then push.
- Success criteria should be explicit in the plan so Claude can confidently determine completion.
- Include self-validation tools: browser extension for UI testing, test suites for continuous validation.
- If Claude repeatedly hits the same issues, save the solution to CLAUDE.md.

### Settling technical debates with generated PRs instead of planning meetings

As coding throughput stopped being the bottleneck, the Claude Code team shifted technical debates away from whiteboard planning sessions: instead of arguing which implementation approach to take, an engineer can have Claude generate multiple competing PR versions and compare them directly — including downstream impact on callers, not just the implementation itself ("building is cheap, arguing is expensive"). This pushed planning toward "JIT planning" (sized to match how fast prototyping now moves, replacing stale six-month roadmaps) and reduced reliance on pre-code design docs in favor of discussion via PRs and prototypes. See [[summary-13 - Running an AI-native engineering org]] and [[summary-03 - Running an AI-native engineering org]].

## Related

- [[summary-06 - The Explore → Plan → Code → Commit workflow in Claude Code]] — source summary
- [[ClaudeCode]] — the tool this workflow is designed for
- [[CLAUDE-md]] — where repeated solutions are saved
- [[AgenticLoop]] — the underlying execution pattern
- [[summary-13 - Running an AI-native engineering org]] — PR-based technical debates and JIT planning
- [[summary-03 - Running an AI-native engineering org]] — the London-venue delivery of the same talk
