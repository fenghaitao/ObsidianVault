---
title: "HarnessEngineering"
type: concept
tags: [concept, harness, ai-layer, agentic-engineering, 2026, claude-code]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260528 - Harness Engineering： What Separates Top Agentic Engineers Right Now.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260618 - The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore!.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260625 - Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good).md"
last_updated: 2026-07-06
---

## Definition

Harness Engineering is the discipline of building the wrapper around an LLM that turns it into a reliable agent. [[ColeMedin]] frames it as "the next big thing for 2026, just like [[ContextEngineering]] was for 2025" — and as both a **skill** (building the [[AILayer]]) and a **mindset** ([[SystemEvolution]] — every mistake improves the harness). It has two layers: the single-session AI layer you build, and the multi-session orchestration ([[RalphLoop]]-style) that's the genuine evolution beyond context engineering.

## Key Information

### The core framing: wrapper around the model

Any agent = underlying LLM (reasoning) + wrapper (context + processes). Harness engineering = engineering that wrapper. An LLM alone can't touch a filesystem, run git, or execute commands. Everything that makes it an agent is harness.

### Two layers of harness

| Layer | Who builds it | What it is |
|---|---|---|
| **Tool's built-in harness** | The vendor (Anthropic, OpenAI...) | [[ClaudeCode]], [[Codex]], Pi — the capabilities + system prompt wrapped around the model out of the box. **You pick this harness when you choose the tool.** |
| **The [[AILayer]]** | **You** | Global rules, skills, MCP servers, code-search (LSP/knowledge graphs), hooks, sub-agents. This is what harness engineering proper is about. |

### Is it just context engineering rebranded?

Cole's honest answer: **mostly, with two genuine distinctions.** Much of the AI layer (context injection, tool actions, persistence, observability) *is* [[ContextEngineering]]. The two real evolutions:

1. **Control** — orchestrating multiple sessions and sub-agents ([[RalphLoop]]). This is the actually-new capability that context engineering didn't cover.
2. **The skill-issue reframe (mindset)** — see below.

### The mindset: the skill-issue reframe

The anti-pattern Cole (quoting the harness-engineering article) calls out:

> Agent does something dumb → engineer blames the model → blame filed under "wait for the next version" (wait for Opus 5, GPT-6...).

Harness engineering rejects this. Failures are *legible*:
- Agent didn't know a convention → add it to `agents.md`.
- Agent ran a destructive command → add a hook that blocks it.

**"Every mistake becomes a rule."** This is exactly [[SystemEvolution]] — claiming agency, taking ownership, improving your harness over time rather than being at the mercy of the next model release. The human is "the one steering the system, feeding forward."

### The feedback-loop view

- **Initial generation**: principles + context fed in (rules, skills).
- **Sensors for feedback**: hooks, review agents, self-correction skills.
- **Evolution**: the AI layer improves over time as mistakes surface fixes.

### Single-session AI layer best practices

- **Separate skills/sessions for plan, implement, validate** — each token-efficient and focused, each outputs a handoff artifact. (Connects to [[ContextReset]].)
- **Hooks** (Cole says underused):
  - *pre-tool-use* — security (block `.env` reads, destructive `rm -rf`).
  - *stop/validation* — when agent claims done, deterministically run tests/lint/types; force iteration if failing. (A hard [[ValidationGates]] enforcement.)
  - *post-edit lint* — keep the codebase clean, which makes future agents more reliable.

### Multi-session orchestration — the peak

The real power. Don't hand a massive PRD to one session (overwhelms the LLM no matter how good your AI layer). Instead chain focused sessions:

```
requirement → explore → plan agent → implement agent
            → parallel review agents (security / correctness / simplicity)
            → pass? create PR : iterate
```

Automated via the **[[RalphLoop]]** or built custom via [[Archon]] (Cole's open-source harness builder).

### Relationship to other concepts

```
PromptEngineering → ContextEngineering → HarnessEngineering
                                              │
                            ┌─────────────────┴─────────────────┐
                       AILayer (single-session)        AgentHarness (multi-session)
                            │                                    │
                       6 components                        RalphLoop, AdversarialDev
```

- [[AgenticEngineering]] (Cole's 5 techniques) is the practitioner-discipline view; Harness Engineering is the architecture-and-mindset view. Heavy overlap — [[SystemEvolution]] is shared between them.
- [[AgentHarness]] is *what harness engineering produces*. This page is the discipline; that page is the artifact.
- [[LoopEngineering]] (the 2026 buzzword from Boris Cherny / Peter Steinberger) is, per `summary-loop-engineering`, just the multi-session-orchestration layer of harness engineering with a 24/7-autonomy framing — Cole explicitly folds it in ("it doesn't deserve its own buzzword").
- [[Google]]'s agentic-engineering masterclass (June 2026) independently arrives at the same core claim under its own vocabulary — the "**factory model**": instead of the engineer writing code by hand, the engineer designs the system/harness/guardrails and the agent produces the code and docs inside a repeatable plan → build → test/eval loop. Same idea as harness engineering, different label; see [[AIDrivenSDLC]].

## Related

- [[AILayer]] — the single-session wrapper you build
- [[AgentHarness]] — the multi-session artifact harness engineering produces
- [[RalphLoop]] — canonical multi-session automation
- [[AdversarialDev]] — a specific harness pattern
- [[SystemEvolution]] — the mindset half
- [[ContextEngineering]] — predecessor discipline
- [[AgenticEngineering]] — overlapping practitioner discipline
- [[ClaudeCode]], [[Codex]] — tools' built-in harnesses
- [[Archon]] — Cole's harness builder
- [[ColeMedin]] — articulator
- [[LoopEngineering]] — the 2026 "loops do the work" framing, folded into this discipline
- [[cole-vs-brian-agent-autonomy]] — synthesis comparing Cole's and Brian's autonomy patterns
- [[cole-brian-pydantic-agent-infrastructure]] — cross-cutting synthesis with Pydantic and Brian Casel
- [[AIDrivenSDLC]] — Google's parallel "factory model" framing
- [[Google]] — independent convergence on this discipline
- [[summary-20260528 - Harness Engineering： What Separates Top Agentic Engineers Right Now]] — primary source
- [[summary-20260618 - The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore!]] — loop engineering as harness engineering
- [[summary-20260625 - Google Just Dropped a Masterclass on Agentic Engineering (It's SO Good)]] — Google's factory-model framing
