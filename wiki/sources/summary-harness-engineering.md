---
title: "summary-harness-engineering"
type: source
tags: [source, transcript, harness-engineering, ai-layer, ralph-loop, system-evolution]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260528 - Harness Engineering： What Separates Top Agentic Engineers Right Now.md"]
last_updated: 2026-06-20
---

## Core Summary

[[ColeMedin]] defines **[[HarnessEngineering]]** — "the next big thing for this year just like context engineering was last year." Building the wrapper around the model. Two layers: (1) the single-session **[[AILayer]]** you build on top of your coding agent (rules, skills, MCP, code-search, hooks, sub-agents), and (2) orchestrating *multiple* coding agent sessions into a workflow (the real evolution — e.g. the **[[RalphLoop]]**). Reframes harness engineering as both a skill *and* a mindset: every agent mistake is an opportunity to improve your harness (= [[SystemEvolution]]).

## Key Points

### Definition: building the wrapper around the model

Any agent = underlying LLM + wrapper. Harness engineering is engineering that wrapper. Two parts:
1. **Within a single session** — closely related to [[ContextEngineering]], with key differences.
2. **Across multiple sessions** — orchestrating coding agent sessions for larger tasks (the real evolution).

### Two layers of "harness"

1. **The tool's built-in harness** — [[ClaudeCode]], [[Codex]], Pi, etc. are themselves harnesses a company engineered around their model. *You pick this harness when you choose the tool.* An LLM by itself can't touch the filesystem, run git, or execute commands — the tool's harness layer provides all that (capabilities + system prompt).
2. **The [[AILayer]]** — the wrapper *you* build. Six components built into every modern AI coding assistant:
   - Global rules
   - Skills
   - MCP servers
   - Codebase search (LSP / knowledge graphs)
   - Hooks
   - Sub-agents

### Is this just context engineering? (the honest answer: mostly, with two distinctions)

Cole acknowledges most of the AI layer *is* context engineering (context injection, tool actions, persistence, observability). Two genuine evolutions:

1. **Control** — Ralph loops, orchestrating sessions and sub-agents. This is the true new capability.
2. **The skill-issue reframe (mindset)** — quoting the article: engineers fall into "the agent did something dumb → blame the model → wait for the next version." Harness engineering rejects this. *Every mistake is legible:* the agent didn't know a convention → add it to `agents.md`; ran a destructive command → add a blocking hook. **"Every mistake becomes a rule."** Cole: this is exactly [[SystemEvolution]] — claiming agency, taking ownership, not being at the mercy of the next model version.

### The AI layer in practice

- **Rules** — constraints/conventions/patterns as global rules + on-demand markdown.
- **Skills** — workflows (plan, implement, validate). Cole strongly recommends **separate skills/sessions for plan, implement, validate** — each token-efficient and focused, each outputs a handoff artifact.
- **Hooks** (underused, Cole loves them):
  - **pre-tool-use hook** — security: block reading `.env`, block destructive `rm -rf`, etc.
  - **stop/validation hook** — when the agent says "done," deterministically run tests/lint/type-check; force iteration until passing.
  - **post-edit lint hook** — quick lint after every file edit to keep the codebase clean (which makes future agents more reliable).

### The peak evolution: orchestrating sessions ([[RalphLoop]])

Don't hand a massive PRD to one session — it overwhelms the LLM regardless of how good your AI layer is. Instead, give each coding agent a focused task and chain them:

```
user requirement → explore → plan agent → implement agent
                  → parallel review agents (security / correctness / simplicity)
                  → if pass: create PR; else: iterate
```

The **[[RalphLoop]]** (Jeffrey Huntley, pioneer) automates this: a script (Python/bash) takes a large scope, splits it into tasks, runs coding-agent sessions one at a time building a log, exits when a `done.txt` indicator appears and validation passes. You can do it manually (plan in one Claude Code, implement in another) but the power is automation — no babysitting.

### Cole's framing

"This really is the future of agentic engineering — building these harnesses to handle larger scopes of work as the models and tools get more powerful." Plugs **[[Archon]]** as his open-source harness builder for creating custom harnesses like the Ralph loop.

## Related

- [[HarnessEngineering]] — central concept
- [[AILayer]] — the wrapper you build (six components)
- [[RalphLoop]] — the canonical multi-session automation pattern
- [[AgentHarness]] — the broader concept harness engineering produces
- [[SystemEvolution]] — the mindset half of harness engineering
- [[ContextEngineering]] — the predecessor discipline
- [[ClaudeCode]], [[Codex]] — the tools' built-in harnesses
- [[Archon]] — Cole's harness builder
- [[ColeMedin]] — author
