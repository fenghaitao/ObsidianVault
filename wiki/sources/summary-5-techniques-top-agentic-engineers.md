---
title: "summary-5-techniques-top-agentic-engineers"
type: source
tags: [source, transcript, agentic-engineering, techniques, claude-code, prd]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260108 - The 5 Techniques Separating Top Agentic Engineers Right Now.md"]
last_updated: 2026-06-19
---

## Core Summary

[[ColeMedin]] presents five concrete techniques distinguishing top agentic engineers. **None require new tools** — they're disciplines around how you *use* [[ClaudeCode]] (or any AI coding assistant). The techniques: **PRD-first development**, **modular rules architecture**, **commandifying everything**, **context reset between plan and execute**, and most importantly **system evolution** — fix the system that allowed the bug, not just the bug. This source consolidates a lot of fragmented technique-content into a clean checklist.

## Key Points

### 1. PRD-First Development

A single markdown document defining the entire scope of work — the **north star** for the coding agent.
- **Greenfield**: spec everything to be built for MVP/POC.
- **Brownfield**: document what exists + what comes next.
- Run `/create-prd` after a planning conversation; the agent outputs a structured doc. Then `/prime` at the start of every new session loads the PRD as context. *"Based on the PRD, what should we build next?"* becomes Cole's daily prompt.

> Note: Cole's "PRD" here is a project-level scope doc (more PM-flavored). Distinguish from Rasmus's [[PRPFramework]] PRP, which is a per-feature implementation prompt. PRDs spawn PRPs.

### 2. Modular Rules Architecture

`CLAUDE.md` (or `AGENTS.md`) at project root should be *short* — only constraints that apply to every task. Anything task-specific (frontend rules, API rules, deployment rules, auth flow rules) lives in separate markdown files under `.claude/reference/`. The global rules file *references* them so they're loaded only when relevant.
- Cole's habit-tracker demo: `claude.md` < 200 lines, with a "Reference" section pointing at deeper rules per task type.
- Reason: protect the context window. Loading 1000-line global rules into every session burns tokens you'd rather have for actual work.

### 3. Commandify Everything

If you've prompted the same workflow more than twice, it should be a slash command. Cole's habit-tracker repo ships markdown commands for: PRD creation, feature priming, structured planning, plan execution, validation, system evolution.
- Commands are just markdown — portable across IDEs (Claude Code, [[Cursor]], [[Windsurf]], Kiro). For non-`/`-aware IDEs, paste the file contents into the prompt.
- Saves keystrokes; standardizes process across team and projects.

### 4. Context Reset Between Plan and Execute

Always `/clear` (or restart the agent) between planning and execution. The plan is captured in a structured-plan markdown doc with all needed context for execution. Then `/execute-plan <doc>` runs with a clean slate.
- **Why**: leave maximum room for the agent's reasoning during execution. A planning conversation can balloon to tens of thousands of tokens; you don't need any of that during the build.
- This is the same idea as [[Rasmus]]'s `/clear` between `/generate-prp` and `/execute-prp` in [[PRPFramework]].

### 5. System Evolution — "Fix the system that allowed the bug"

The mindset Cole calls "the most powerful way to use coding agents." When you encounter a bug or AI mistake:
- Don't just fix the bug.
- Ask: *which rule was missing? which part of the workflow let this through?*
- Update the global rules, reference docs, command templates — whichever layer prevents this class of issue.
- Concrete examples Cole gives:
  - **AI uses wrong import style** → add a one-line global rule.
  - **AI forgets to run tests** → update the structured-plan template to include a testing section.
  - **AI doesn't understand the auth flow** → create a reference doc + add a conditional reference in global rules.
- After every feature: ask the agent to self-reflect — "compare execution to the plan and the rules; what discrepancies are there? what should we fix in the system?"

This is where the system compounds: each fix makes the next feature more reliable.

## Related

- [[PRDFirstDevelopment]] — technique 1 (concept page)
- [[ModularRulesArchitecture]] — technique 2 (concept page)
- [[Commandification]] — technique 3 (concept page)
- [[ContextReset]] — technique 4 (concept page)
- [[SystemEvolution]] — technique 5 (concept page)
- [[ClaudeCode]] — primary surface
- [[ContextEngineering]] — umbrella discipline
- [[PRPFramework]] — Rasmus's per-feature variant; PRDs spawn PRPs
- [[ColeMedin]] — author
