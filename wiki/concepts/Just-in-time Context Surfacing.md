---
title: "Just-in-time Context Surfacing"
type: concept
tags: [ai, context-engineering, agentic-engineering, methodology]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI.md"]
last_updated: 2026-06-26
---

## Definition
Just-in-time context surfacing is the practice of deferring instructions and requirements to later stages of the development workflow (lint time, test time, review time) rather than front-loading all context at the start of a task. This prevents overwhelming the agent's context window and allows it to prototype before receiving refinement instructions.

## Key Information
- Practice from Ryan Lopopolo's team at OpenAI
- Core principle: don't front-load all instructions — surface them when the agent needs them
- Example: for React component decomposition rules, let the agent prototype the UI first, then at lint/test time say "break this apart so components are small and stateless"
- The agent receives the new instruction as a fresh prompt and modifies the patch accordingly
- Works with auto-compaction: since context gets paged out over time, requirements must be re-surfaced at the right moments
- Implementation mechanisms: lint failures with remediation messages, test assertions about code structure, reviewer agent comments on PRs
- This pattern is not obsoleted by model capability improvements — it's about getting the right text to the agent at the right time

## Related
- [[summary-20260417 - Harness Engineering： How to Build Software When Humans Steer, Agents Execute — Ryan Lopopolo, OpenAI]] — source
- [[Harness Engineering]] — the broader discipline
- [[Auto-compaction]] — why JIT surfacing is necessary
- [[ProgressiveContextDisclosure]] — related concept
- [[Context Management]] — broader topic
- [[Reviewer Agents]] — one mechanism for JIT surfacing
