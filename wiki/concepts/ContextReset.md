---
title: "ContextReset"
type: concept
tags: [concept, agentic-engineering, context-management, planning, technique]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260108 - The 5 Techniques Separating Top Agentic Engineers Right Now.md"
last_updated: 2026-06-19
---

## Definition

Context Reset is the practice of clearing the agent's context window between distinct phases of work — typically between **planning** and **execution**. The plan is captured in a structured-plan markdown document with all context the executor will need; then the conversation is cleared (`/clear` in [[ClaudeCode]]) before execution begins. Defends against [[ContextRot]] by ensuring execution starts with a maximally clean working memory.

## Key Information

### The pattern

```
1. Planning conversation
   ├─ /prime (load codebase + PRD)
   ├─ Discussion: what should we build, how?
   ├─ /plan-feature → outputs structured-plan markdown
2. /clear                                         ← context reset
3. Execution
   └─ /execute-plan plans/feature-XYZ.md          ← starts from clean slate
```

The structured-plan document is the bridge: the planning context is *captured* in it (so nothing is lost) but is *no longer in the active context* during execution (so the agent has full reasoning room for the build).

### What goes in the structured-plan document

Cole's typical sections:

- Feature description + user story
- High-level architecture for the change
- File-by-file implementation breakdown
- Task list (the agent will work through these)
- Validation gates (tests, lint, manual checks)
- References to relevant rules / docs

If you can't generate this without referring back to the planning conversation, your plan isn't comprehensive enough yet.

### Why it works

- **Maximum reasoning room** during execution. A planning conversation can balloon to tens of thousands of tokens; the executor doesn't need any of that.
- **Forces a sharp planning artifact**. If you can't fully capture the plan in a markdown doc, the plan isn't ready.
- **Cleaner [[ValidationGates]]**. The executor can focus on running and iterating on tests without conversation-history noise.
- **Reduces [[ContextRot]]**. Long-running execution sessions accumulate enough context just from doing the work; starting clean buys headroom.

### Same pattern in [[PRPFramework]]

[[Rasmus]]'s PRP framework explicitly recommends `/clear` between `/generate-prp` and `/execute-prp` — same idea. PRPs are the structured-plan document under a different name.

### When to skip context reset

If the plan is trivial enough that the conversation context is small (a few hundred lines of dialogue), the cost of resetting (re-priming, etc.) can outweigh the benefit. Cole's heuristic: if the planning took longer than ~5 minutes of conversation, reset.

### Pre-execution priming after reset

Cole doesn't re-prime after a reset for execution — the plan document *is* the prime. The agent reads the plan, sees it has all the context it needs (file references, examples, validation gates), and proceeds. Re-priming would defeat the point.

## Related

- [[AgenticEngineering]] — technique 4 of 5
- [[ContextRot]] — failure mode this avoids
- [[ContextEngineering]] — broader discipline
- [[ClaudeCode]] — primary surface (`/clear` is its native command)
- [[PRPFramework]] — same pattern under different naming
- [[PRDFirstDevelopment]], [[ModularRulesArchitecture]], [[Commandification]], [[SystemEvolution]] — companion techniques
- [[ColeMedin]] — author
- [[summary-5-techniques-top-agentic-engineers]] — primary source
