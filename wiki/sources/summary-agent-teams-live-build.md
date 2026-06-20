---
title: "summary-agent-teams-live-build"
type: source
tags: [source, original-material, agent-teams, claude-code, planning, validation, brownfield]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260216 - How to Properly Use Claude Code Agent Teams (FULL LIVE BUILD).md"]
last_updated: 2026-06-20
---

## Core Summary

A live brownfield build where [[ColeMedin]] adds a ChargeBee token-purchase payment feature to an existing agentic chat app using [[ClaudeCode]]'s new **[[AgentTeams]]** feature (released with Opus 4.6). The video is two lessons in one: (1) a rigorous **planning methodology** centered on making the agent *ask clarifying questions to reduce assumptions*, and (2) parallel multi-agent implementation via Agent Teams using a **contract-first** command, finished by autonomous end-to-end validation with the [[VercelAgentBrowser]] CLI. Cole's verdict: Agent Teams is experimental and unreliable today (non-deterministic, token-heavy, no observability) but clearly points at where agentic engineering is heading within ~6 months.

## Key Points

- **[[AgentTeams]] vs [[SubAgent]]s**: sub-agents run in parallel but *don't communicate* — they just report back to a main agent. Agent Teams spawn teammates that **share a task list and message each other** (teammate→teammate, teammate→lead), coordinating who takes which tasks. Downsides: non-deterministic (lots of control handed to the lead), token-heavy (communication overhead), and missing observability (no dashboard of who claimed what / messages — Cole expects Anthropic to add this; possibly buildable with hooks). Despite reputation, Cole's run used only ~16% of his session limit.
- **Contract-first command**: Claude Code alone is "surprisingly not that good" at Agent Teams because parallel work has blockers (e.g. the DB schema must exist before the backend agent can proceed). Cole's `build with agent team` command implements a **contract-first approach**: the lead agent first maps the contracts between front-end/back-end/database, passes them into each teammate's prompt, and only *then* (step 5) spawns agents in parallel — so they don't step on each other. Takes a plan path + an optional agent count (omit it and Claude Code decides based on the plan).
- **Planning methodology** (the core lesson):
  - **Prime first**: a `/prime` command run at the start of every new build, walking the agent through the codebase so it has context before researching the feature.
  - **Start unstructured**: a brain-dump of what you want, with instructions to search the codebase *and* the web.
  - **Make it ask questions**: *"The number one goal of planning is to reduce the number of assumptions the coding agent is making."* Cole demands **≥10 clarifying questions**. Two kinds of agent mistakes — writing bad code, or deviating from intent — and "technically both are your fault." Asking questions surfaces assumptions you didn't know you were making.
  - **[[ClaudeCode]]'s AskUserQuestion tool** (~1 month old): pops multiple-choice questions with a recommended option (hit enter to accept, or type a free-form answer) — makes the Q&A fast. Claude Code only asks a few at a time and isn't dynamic across answers, so you sometimes restate context.
  - **Formalize with a `/plan` command** into a structured plan (summary, user story, key decisions, patterns-to-follow for brownfield, task list, validation), then **review the plan carefully** — it's high-leverage: "one error in your plan can lead to hundreds of lines of bad code; one line of bad code is just one line."
  - **Context reset**: after planning, the plan *is* all the context the implementation needs — start a fresh session (here, no compaction was even required).
- **Validation defined upfront**: the plan specifies lint, type-checking, unit tests, and especially **end-to-end** scenarios. Cole uses the **[[VercelAgentBrowser]] CLI** — the agent drives a real browser through every user journey (register, buy tokens, chat, see deductions), self-fixing issues before returning control. He calls it "a big upgrade over the Playwright/Puppeteer MCP servers." Note: Opus 4.6 kept *skipping* the e2e step for him (Opus 4.5 did it automatically) — a prompt/command-tuning issue when models change.
- **SaaS platforms ship skills**: the **ChargeBee integration skill** gives Claude Code accurate SDK docs so it doesn't hallucinate (training-cutoff gap). Cole predicts "every platform you integrate will ship a skill" — and notes this fulfills what [[Archon]] originally did with RAG-over-docs, now built into the tools.
- **Setup specifics**: Agent Teams enabled via `.claude/settings.local.json` (`experimental agent team = 1`); run inside **tmux** (and **WSL** on Windows — Agent Teams/sub-agents don't run well on native Windows); YOLO / `--dangerously-skip-permissions` for speed.

## Related

- [[AgentTeams]] — the feature this video teaches
- [[SubAgent]] — the predecessor Agent Teams extends with communication
- [[VercelAgentBrowser]] — end-to-end validation tool used in the build
- [[ClaudeCode]] — host for Agent Teams + the AskUserQuestion tool
- [[PRPFramework]] — the planning/structured-plan methodology refined here
- [[ValidationGates]] — validation defined upfront, run autonomously
- [[ContextReset]] — fresh session for implementation after planning
- [[ClaudeSkills]] — the ChargeBee skill; "every SaaS ships a skill"
