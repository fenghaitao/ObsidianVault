---
title: "Agent-Ready Eval Tooling"
type: concept
tags: [evals, agents, tooling, cli, coding-agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260517 - Fighting AI with AI — Lawrence Jones, Incident.md"]
last_updated: 2026-06-30
---

## Definition

Agent-ready eval tooling is the practice of building CLI tools or APIs that enable coding agents to programmatically interact with evaluation suites — listing, editing, replacing, and adding test cases — rather than requiring agents to read and modify large YAML or JSON eval files directly. This solves the context-window problem that arises when production evals contain multi-megabyte datasets.

## Key Information

- **Problem solved**: Production evals often contain entire incident reports or interaction traces (2MB+ of YAML), which exceed coding agent context windows when loaded directly. Agents cannot effectively "read and modify" the eval suite.
- **Solution pattern**: Build a small CLI tool that exposes operations like: list test cases, get a specific test case, edit a test case, replace a test case, add a new test case, run the eval suite
- **Implementation at [[IncidentIo]]**: Created `eval tool`, a CLI that wraps their YAML-based eval suite, enabling Claude Code and Codex to work with evals without loading the full file content
- **Runbook integration**: The CLI is packaged with a runbook (or skill) that guides the coding agent through the [[Eval Red Green Cycle]]: find the problem, create an eval, fix the prompt, verify no regressions, consolidate
- **Key design insight**: Tools designed for humans (UIs, direct file editing) often do not work for coding agents. Agent-ready tooling must consider context limits, grep-ability, and structured programmatic interfaces
- **Broader principle**: Any internal tool used for debugging or improving AI systems should be made accessible to coding agents, not just humans

## Related

- [[summary-20260517 - Fighting AI with AI — Lawrence Jones, Incident]] — primary source
- [[Eval Red Green Cycle]] — the workflow this tooling enables
- [[EvalEngineering]] — the practice of crafting evaluation prompts
- [[EvalFlywheel]] — broader continuous improvement loop
- [[IncidentIo]] — company that built the reference implementation
- [[ClaudeCode]] — coding agent using the tooling
- [[Codex]] — coding agent using the tooling
- [[Skills]] — runbooks/skills as packaging mechanism for agent workflows
