---
title: "VibeCoding"
type: concept
tags: [concept, ai-coding, paradigm, karpathy, prototyping]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20250703 - Context Engineering is the New Vibe Coding (Learn this Now).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20251218 - Are Agent Harnesses Bringing Back Vibe Coding.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260115 - Ralph Wiggum is the Final Evolution of Vibe Coding (Here's What Comes Next).md"
last_updated: 2026-06-20
---

## Definition

Vibe coding is the practice of letting an [[AICodingAssistant]] write code with minimal upfront planning, minimal context, and minimal review — relying on intuition and rapid iteration to get to "it works" without engineering structure. The term was **coined by [[AndrejKarpathy]] in early 2025** and went viral. By mid-2025, [[ContextEngineering]] emerged as the explicit counter-paradigm.

## Key Information

### Why it caught on

- **Dopamine of instant code generation.** Tell the AI what you want, watch it appear. Skipping the slow planning phase felt like a productivity superpower.
- **Genuinely good for prototypes and weekend hacks.** When you don't know what you want yet, vibe coding lets you find out by trying things at LLM speed.
- **Lower barrier to entry.** No need to plan architecture before you start building.

### Why it breaks at scale

- **Hallucination.** Without curated context, AI coding assistants invent APIs that don't exist, miss project conventions, and reuse patterns from their training data that don't fit your codebase.
- **No human review = no quality floor.** [[ColeMedin]] cites a Codto survey: 76.4% of developers have low confidence shipping unreviewed AI code.
- **Intuition doesn't scale.** A small project can be held in your head; a 50-file production codebase can't. Vibe coding works against the grain of large systems.
- **Compounding wrong decisions.** Without an explicit plan, the AI fills in architectural decisions implicitly, inconsistently. Future iterations build on top of those, multiplying the inconsistency.

### The ceiling — [[RalphLoop|Ralph Wiggum]] as the "final evolution"

Per `summary-ralph-wiggum-vibe-coding`, Cole names the [[RalphLoop]] (the "Ralph Wiggum" technique) the **ceiling of vibe coding**: forcing a coding agent to run in a loop until it declares done is Karpathy's original tenets (no research, no plan, trust the agent, forget the code) taken to their infinite-loop extreme. You literally cannot get "more vibey." The point is double-edged — once Ralph's output is unacceptable, vibe coding has nowhere left to go, and you're forced to apply human judgment and **build a system** (an [[AgentHarness]]). So Ralph marks both the peak *and* the dead-end of the paradigm.

### Cole's framing — when vibe coding is fine vs. when it isn't

> *"Vibe coding builds prototypes that break when you try to scale."* — Cole's recurring soundbite.

It's not vibe coding that's bad — it's vibe coding for production. The right uses:
- **One-off scripts** you'll throw away.
- **Initial exploration** before you know the problem shape.
- **Personal projects** with no users.
- **Demos** for talking through an idea.

When the work is meant to ship to real users on real data, [[ContextEngineering]] is the discipline that picks up where vibe coding leaves off.

### The Karpathy connection

Karpathy coined the term in a tweet, watched it go viral, and later watched [[ContextEngineering]] emerge as its successor. His response (also on X): vibe coding is fine for prototypes; for real work, you want the engineered context. Cole's video on Context Engineering opens with Karpathy's reply quoted in full — same thinker, evolved framing.

### Vibe coding's afterlife — the "harness era" reframe

Per `summary-agent-harnesses-and-vibe-coding`, [[ColeMedin]] later argues that **[[AgentHarness|agent harnesses]] make a more sophisticated kind of vibe coding viable again** — because the harness itself supplies much of the context engineering. The cycle:

```
Vibe coding (no structure)
    ↓ "this breaks at production"
Context engineering (per-session structure)
    ↓ "we need to chain sessions reliably"
Agent harnesses (multi-session structure)
    ↓ "wait — we can trust full feature delegation again now!"
Harness-mediated vibe coding (qualified)
```

The harness-era version isn't trust-the-LLM-blindly. It's trust-a-heavily-engineered-system-that-uses-the-LLM. Same outcome (you don't write most of the code), opposite philosophy (no structure → lots of structure).

## Related

- [[ContextEngineering]] — the counter-paradigm
- [[RalphLoop]] — the "Ralph Wiggum" ceiling/final evolution of vibe coding
- [[AgentHarness]] — the layer that makes "vibe coding viable again" (qualified)
- [[AndrejKarpathy]] — coiner of the term
- [[ColeMedin]] — author of the Cole-side framing in this corpus
- [[AICodingAssistant]] — what vibe coding is done with
- [[summary-context-engineering-is-new-vibe-coding]] — primary source for this framing
- [[summary-agent-harnesses-and-vibe-coding]] — the harness-era reframe
- [[summary-ralph-wiggum-vibe-coding]] — Ralph as the ceiling of vibe coding
