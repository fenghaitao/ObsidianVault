---
title: "AgentHarness"
type: concept
tags: [concept, agents, harness, multi-session, long-running, anthropic, claude-code]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20251218 - Are Agent Harnesses Bringing Back Vibe Coding.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260115 - Ralph Wiggum is the Final Evolution of Vibe Coding (Here's What Comes Next).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260202 - Turn Claude Code into Your Full Engineering Team with Subagents.md"
last_updated: 2026-06-20
---

## Definition

An agent harness is the infrastructure layer that connects multiple LLM sessions together to handle long-running tasks reliably. Where [[ContextEngineering]] optimizes a single session's context window, an agent harness orchestrates **many** context windows in sequence — checkpoints, handoffs, memory artifacts, sub-agents for isolation, validation gates, human-in-the-loop. [[ColeMedin]] frames it as the next evolution after context engineering: *prompt engineering → context engineering → agent harnesses.*

## Key Information

### The evolution

| Era | Year | Optimizes | Limit |
|---|---|---|---|
| **Prompt engineering** | 2020+ | Single LLM calls | Single-turn tasks |
| **[[ContextEngineering]]** | mid-2025 | Single sessions / context windows | One context window's worth of work |
| **Agent harnesses** | late 2025+ | Many sessions stitched together | "How long can the harness keep going?" — currently bounded by handoff fidelity and compounding error rate |

The harness is **not a replacement** for context engineering. It uses context engineering inside each session and adds an outer layer of orchestration.

### Why now

[[ColeMedin]]'s framing: raw LLM power isn't exploding anymore. The benchmarks creep, but the architectural unlocks are now in *the layer around* the LLM. 2020-2025 was the year of scaling parameters; 2026 is the year of harnesses.

### From coder to full "AI engineer" — the tool belt

Per `summary-full-engineering-team-subagents`, a coding-only harness is an incomplete engineer. A real engineer also communicates (Slack), manages tasks (Linear/Jira), and maintains the repo (GitHub/PRs). Cole extends Anthropic's open-source harness with a **tool belt** of service [[SubAgent]]s so the agent works *where humans work*:

- Built on the [[ClaudeAgentSDK]] (agents/MCP/sub-agents defined in code, runs on the Claude Code subscription) and Anthropic's JSON task-list format.
- **[[Arcade]]** MCP gateway connects Linear + GitHub + Slack (91 tools) with agent authorization, so teams share the harness without sharing credentials.
- **Linear becomes the source of truth** — the initializer creates a Linear project + issues plus a meta "progress tracker" issue, *replacing* the local `claude_progress.md` handoff file. Each session reads Linear to know what to validate and build next.
- Dedicated Linear/GitHub/Slack sub-agents isolate context from the orchestrator and can each run a cheaper/faster model (Haiku/Sonnet/Opus).
- Flow: **AppSpec (PRD)** → initializer scaffolds project + Linear + GitHub → coding loop (fresh context each session: get bearings → regression test → implement → Playwright-validate → commit → update Linear + Slack) until all tasks done.

The takeaway Cole stresses: off-the-shelf harnesses are a *starting point*; the real win is a **custom** harness fit to your own workflow (see [[Archon]]'s pivot to "the N8N for AI coding").

### The spectrum: from Ralph (Model T) to a real harness

[[ColeMedin]] frames the [[RalphLoop]] ("Ralph Wiggum") as the **most basic harness possible** — a single Stop hook plus prompting — the "**Model T of AI coding**," not the Tesla. It proves the concept but isn't production-ready. Moving from Ralph to an effective harness means adding exactly the components below: an **initializer agent**, **structured progress tracking**, **human-in-the-loop**, **error recovery**, **memory compression**, **session handoff**, and a **deterministic validation strategy** built into the process (not just bolted on via PRP). Cole's 2026 thesis: the competitive advantage shifts from the model to the harness/tooling around it.

### Anatomy of a harness

Common pattern from [[Anthropic]]'s open-source initializer-coder architecture (Cole's reference example):

```
AppSpec (PRD)
  ↓
Initializer Agent          ← runs once
  • Generates feature list
  • Scaffolds project, git repo
  • Validates env health
  ↓
Task Agent                 ← runs in a loop, fresh context each time
  ┌─→ Prime (read git log, progress file, codebase)
  │   Checkpoint (run tests; fail fast)
  │   Pick highest-priority feature
  │   Implement + self-validate
  │   Update progress.md, commit
  └── Loop until tests + features all pass
```

### Components every harness needs

| Component | Role |
|---|---|
| **Initializer** | Sets the stage; one-time work |
| **Task agent (looped)** | Does the incremental work across many sessions |
| **Memory artifacts** | What survives session boundaries: progress files, git log, codebase, structured task lists |
| **Priming** | Each new session reads the artifacts to catch up |
| **[[ValidationGates]]** | Self-checks at session boundaries; fail-fast |
| **Handoffs** | What each session writes for the next |
| **[[Guardrails]]** | Pre/post checks at agent boundaries |
| **Human-in-the-loop checkpoints** | Strategic injection points; preserves human authority on important decisions |

### Memory strategy: the file system *is* the memory

Common pattern across harnesses (Anthropic's, [[LangChain]]'s Deep Agents, **Manus**):
- **Progress file** — high-level "what's been done" for handoff (e.g. `claude_progress.md`).
- **Feature list / task tracker** — source of truth for what's left. Cole's variant routes this through Linear/Slack/Asana for human visibility.
- **Git log** — implicit memory of completed work.
- **Codebase itself** — the agent reads it to understand state.

Manus's article (Cole cites): *"file system as context."* Cleaner than per-session memory because it's persistent and human-inspectable.

### Named harness implementations

- **Anthropic's initializer-coder architecture** — open-sourced; Cole's primary reference. Variants exist for non-coding domains.
- **LangChain Deep Agents** — multi-domain harness with tool-based file-system context management.
- **Manus** — early-2025 platform that already implemented harness patterns; Cole's source for the "file system as context" framing.
- **Cole's own remote agentic coding system** — under development in the Dynamis community.

### The two unsolved problems

#### 1. Bounded attention / [[ContextRot]]

Even with offloading, summarization is *lossy*. Cole observes Anthropic's harness frequently misses key details (e.g. "validation failed and how it was resolved") in `claude_progress.md`, causing the same mistakes to repeat session after session.

Manus's framing Cole quotes: *"You can't predict which observation becomes critical 10 steps later."* True predictive context — knowing what session 50 will need from session 5 — is essentially unsolvable.

#### 2. Compounding error rate

A 95%-reliable agent over 20 steps yields **36% system reliability** (`0.95^20`). For end-to-end vibe coding to be viable, individual steps need ~99.9% reliability — not happening.

Mitigation:
- **Strategic human-in-the-loop checkpoints** at key boundaries (between agents, between major features).
- **Aggressive [[ValidationGates]]** to catch failures before they propagate.
- **Git-based rollback** to recover when things go wrong.
- **Self-validation patterns** to catch the agent's own mistakes inside a session.

### Relationship to [[VibeCoding]]

The provocative claim from Cole's source video: agent harnesses bring vibe coding back — qualified. With a heavily-engineered harness + HITL checkpoints, you *can* delegate full feature implementation to the AI without writing the code yourself. But the system surrounding it is heavily engineered. So:

- **Pre-2025 vibe coding** = trust the LLM blindly.
- **Harness-era vibe coding** = trust a heavily-engineered harness that uses the LLM.

Same outcome (you don't write most of the code), opposite philosophy (zero structure vs. a lot of structure).

### Why Cole calls 2026 "the year of agent harnesses"

The unlock that's emerging:
- Better context management (compaction, smart summarization)
- File-system-as-memory pattern is proven
- [[ClaudeCode]] + [[ClaudeSkills]] make harness primitives accessible
- Anthropic publishing reference harness code legitimizes the pattern
- The compounding-error problem motivates serious engineering investment

## Related

- [[ContextEngineering]] — predecessor
- [[ClaudeAgentSDK]] — SDK for building harnesses in code
- [[Arcade]] — MCP gateway for service tool belts (Linear/GitHub/Slack)
- [[HarnessEngineering]] — the discipline of building harnesses (and the AI layer); the mature framing of this concept
- [[AILayer]] — the single-session wrapper inside a harness
- [[RalphLoop]] — canonical multi-session automation
- [[AdversarialDev]] — GAN-inspired generator/evaluator harness
- [[ContextRot]] — central problem harnesses are solving
- [[VibeCoding]] — paradigm being qualified-revived
- [[ClaudeCode]], [[Codex]] — primary execution surfaces
- [[Anthropic]] — reference harness publisher
- [[Archon]] — Cole's open-source harness builder
- [[ValidationGates]], [[HumanInTheLoop]], [[Guardrails]] — sub-patterns
- [[SystemEvolution]] — how the harness improves over time
- [[ColeMedin]] — articulator
- [[summary-agent-harnesses-and-vibe-coding]] — primary source
- [[summary-harness-engineering]] — the discipline; multi-session orchestration
- [[summary-adversarial-dev-technique]] — a concrete harness
- [[summary-ralph-wiggum-vibe-coding]] — Ralph as the most basic harness (Model T)
- [[summary-full-engineering-team-subagents]] — extending a harness into a full AI engineer with a tool belt
