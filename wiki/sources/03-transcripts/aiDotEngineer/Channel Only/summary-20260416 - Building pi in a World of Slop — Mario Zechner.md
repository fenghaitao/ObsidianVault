---
title: "summary-20260416 - Building pi in a World of Slop — Mario Zechner"
type: source
tags: [source, transcript, ai, coding-agents, agent-harness, open-source, pi, context, extensibility, slop]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - Building pi in a World of Slop — Mario Zechner.md"]
last_updated: 2026-06-26
---

## Core Summary
Mario Zechner presents a three-act tragedy about building Pi, his own coding agent harness, after becoming frustrated with Claude Code's context control, instability, and lack of extensibility. Act 1 details why he abandoned Claude Code (system prompt changes, hidden context manipulation, zero observability, no model choice, shallow hooks) and built Pi — a minimal, self-modifying, extensible agent harness. Act 2 covers the collateral damage of "clankers" (AI agents) destroying open source projects with garbage issues and PRs. Act 3 is a call to slow down: agents compound errors without learning, generate enterprise-grade complexity from internet garbage, and cannot replace human judgment and discipline.

## Key Points

### Act 1: Building Pi
- Mario loved Claude Code initially (April 2025) when it was simple and predictable, but velocity brought bugs and feature bloat
- Core complaint: Claude Code controls the user's context behind their back — system prompts change every release, tools are removed/modified, system reminders inject "information that may or may not be relevant," confusing the model and breaking workflows
- Zero observability, zero model choice (Anthropic-only), and shallow extensibility (hooks spawn new processes, inefficient)
- Amp and FactoryDroid are the "Porsche and Lamborghini" of agent harnesses — excellent but not free
- Open Code (OSS alternative) had its own problems: tool output pruning that "lobotomizes" the model, LSP error injection mid-edit confusing the model, per-message JSON files on disk, CORS misconfiguration exposing the server
- Terminal Bench finding: the most minimal harness (Terminus, only keystroke send + tmux read tools) scores highest regardless of model family — suggesting current agent form is not final
- Pi's design: minimal core (AI abstraction, agent core as while loop + tool calling, bespoke TUI framework), only 4 tools (read, write, edit, bash), tiny system prompt, skills as markdown files
- Pi ships its own documentation and code examples so the agent can modify itself by writing TypeScript extensions
- Security: "yellow by default" — gives users enough rope to build their own security model rather than nag dialogs
- Extensions are TypeScript modules with hot reloading; can hook into everything (tools, slash commands, events, session state, compaction, providers)
- Extensions are distributed via NPM/GitHub, not a new marketplace silo
- Pi scored 6th on Terminal Bench before it even had compaction

### Act 2: OSS in the Age of Clankers
- "Clankers" (AI agents) are destroying OSS — flooding issue trackers and PR queues with garbage
- Till Draw closed their issue/PR tracker; Open Claw's tracker similarly overwhelmed; half of Pi's tracker is Open Claw instances posting garbage
- Mario's defense: auto-close PRs with a comment asking for a human-written issue; if the human responds, their account gets whitelisted ("vouch" system, later turned into a tool by Mitchell)
- Also: label Open Claw interactions to deprioritize issues, embed issue texts in 3D space to spot clusters, "OS certification" (close the tracker whenever you want)

### Act 3: Slow the F*** Down
- Agents compound "booboos" (errors) with zero learning, no bottlenecks, and delayed pain for humans
- Agent-written code is hard to review at scale; review agents create an "ouroboros" that doesn't work
- Models learn complexity from internet garbage (90% of code is old garbage); every agent decision is local, leading to enterprise-grade complexity in 2 weeks
- A sufficiently detailed spec is a program — blanks get filled with internet garbage
- Humans feel pain and act on it (quit, blame, refactor); agents happily keep dumping garbage
- Long context windows are a hack; agentic search is failing; agents patch locally and break globally
- Good agent tasks: well-scoped (agent can find everything needed), have an evaluation function, non-mission-critical, boring/repetitive, reproduction cases, rubber ducking
- Critical code must be read line by line; friction builds understanding; write important things by hand
- "Slow the f*** down. Learn to say no. Fewer features, but the ones that matter."

## Related
- [[MarioZechner]] — speaker, creator of Pi
- [[Pi (coding agent)]] — the agent harness
- [[ClaudeCode]] — what Mario abandoned
- [[Anthropic]] — company behind Claude Code
- [[OpenCode]] — OSS alternative Mario evaluated
- [[TerminalBench]] — benchmark that informed Pi's design
- [[Terminus]] — minimal harness topping Terminal Bench
- [[AmpCode]] — "Porsche" of agent harnesses
- [[FactoryAI]] — "Lamborghini" of agent harnesses (FactoryDroid)
- [[MitchellHashimoto]] — from Ghosty, created vouch tool
- [[OpenClaw]] — Peter put Pi inside it as agent core
- [[SelfModifyingAgents]] — core thesis: agents that can modify themselves
- [[ContextOwnership]] — the problem of harness controlling context
- [[MinimalAgentDesign]] — minimal system prompts and tool definitions
- [[AgentExtensibility]] — TypeScript extensions with hot reloading
- [[CompoundingBooboos]] — errors compounding without learning
- [[AgentCodeReviewLimitations]] — ouroboros problem
- [[GoodAgentTasks]] — properties of tasks suitable for agents
- [[SlowingDownWithAgents]] — discipline, friction, critical vs non-critical code
- [[OSSInAgeOfClankers]] — AI agents destroying open source
- [[Slop]] — the world of slop Pi was built in
- [[AgentObservability]] — what Claude Code lacked
- [[Skills]] — markdown-based agent instructions Pi adopted
- [[Context Management]] — what Claude Code does behind the user's back
