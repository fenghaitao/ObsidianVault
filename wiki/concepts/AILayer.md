---
title: "AILayer"
type: concept
tags: [concept, harness-engineering, claude-code, rules, skills, hooks]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260528 - Harness Engineering： What Separates Top Agentic Engineers Right Now.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260223 - My COMPLETE Agentic Coding Workflow to Build Anything (No Fluff or Overengineering).md"
last_updated: 2026-06-20
---

## Definition

The AI Layer is [[ColeMedin]]'s term for the wrapper you build on top of an AI coding assistant — the customization layer above the tool's own built-in harness. It's the part of [[HarnessEngineering]] you control. Cole identifies six components, built into essentially every modern AI coding assistant, through which you inject all your context and processes.

## Key Information

### The stack

```
┌─────────────────────────────────────┐
│  AI Layer (YOU build this)           │  ← global rules, skills, MCP,
│                                      │     code-search, hooks, sub-agents
├─────────────────────────────────────┤
│  Tool's built-in harness             │  ← Claude Code / Codex / Pi:
│  (vendor builds this)                │     filesystem, git, command exec,
│                                      │     system prompt — you pick it by
│                                      │     choosing the tool
├─────────────────────────────────────┤
│  LLM (the reasoning)                 │  ← Claude / GPT
└─────────────────────────────────────┘
```

An LLM alone can't touch files or run commands. The tool's harness adds those. The AI layer adds *your* context and process on top.

### The six components

| Component | Role |
|---|---|
| **Global rules** | Constraints, conventions, patterns (`CLAUDE.md` / `AGENTS.md`). See [[ModularRulesArchitecture]]. |
| **Skills** | Reusable workflows / capabilities. See [[ClaudeSkills]]. Cole recommends separate skills for plan / implement / validate. |
| **MCP servers** | External tool access via [[ModelContextProtocol]]. |
| **Codebase search** | LSP (language server) or [[RetrievalAugmentedGeneration|knowledge graphs]] for the agent to navigate code. |
| **Hooks** | Code that runs at lifecycle events (pre-tool-use, session-start, stop, post-edit). |
| **Sub-agents** | Isolated agents for focused tasks ([[SubAgent]]). |

No matter how you want to inject process or rules, it goes through one of these six.

### The AI layer as your reusable starting point (greenfield)

Per `summary-complete-agentic-coding-workflow`, in practice the AI layer is the set of **context assets** you set up *before writing any code*: the PRD (what to build), global rules (how to build), commands (reusable workflows like `/prime`, `/create-prd`, `/plan-feature`, `/execute`, `/commit`), research sub-agents, and a **reference folder** of on-demand context. Cole keeps a **generic starter** AI layer he drops into every new project, then **evolves it to be project-specific** as the codebase grows — the reason he prefers a simple own-it framework over heavyweight ones (BMAD, GitHub Spec Kit).

**Reference folder = [[ProgressiveDisclosure]]**: keep `AGENTS.md` concise (~230 lines, always loaded) and push bigger guides (`components.md`, `api.md`, `styles.md`) into a reference folder that the agent loads *only* when working on that area — pointed to from the global rules. (These can equally be [[ClaudeSkills]].)

### Hooks deep-dive (the underused component)

Cole singles out hooks as underused and powerful:

- **pre-tool-use hook** — runs before any tool call (file write, command). Use for **security**: block reading `.env` files (keep secrets out of context), block destructive commands (`rm -rf`), etc.
- **stop / validation hook** — runs when the agent claims it's done. Deterministically run tests, lint, type-checking; if failing, *force* the agent to keep iterating. Hard enforcement of [[ValidationGates]].
- **post-edit lint hook** — quick lint after every file edit. Keeps the codebase clean, which (importantly) makes *future* agent sessions more reliable.

Hooks are where [[SystemEvolution]] often lands — "agent ran a destructive command → add a hook that blocks it."

### Skills: plan / implement / validate separation

Cole strongly recommends a skill per phase, each in its own session:
- **plan skill** → outputs a plan markdown artifact.
- **implement skill** → reads the plan, builds, outputs.
- **validate skill** → checks the work.

Each stays token-efficient and focused; the artifacts are handoffs between sessions. This is the building block for stringing sessions together ([[RalphLoop]]).

### Why "you pick the first harness by choosing the tool"

A subtle point: the tool itself ([[ClaudeCode]] vs [[Codex]] vs Pi) *is* a harness the vendor engineered. Debate over "which is the best harness for coding" is really debate over which vendor's wrapper you prefer. But the higher-leverage layer — the one that differentiates *you* — is the AI layer you build on top, because that's where your specific context and process live.

### Portability

Like all of [[ColeMedin]]'s patterns, the AI layer is mostly **markdown** (rules, skills, sub-agent definitions) plus small hook scripts. This makes it portable across tools — the markdown comes with you when you switch from Claude Code to Codex or vice versa.

## Related

- [[HarnessEngineering]] — the discipline the AI layer is the core of
- [[AgentHarness]] — multi-session artifact
- [[RalphLoop]] — what you build by orchestrating AI-layer sessions
- [[ClaudeSkills]] — the skills component
- [[ModularRulesArchitecture]] — the rules component
- [[ModelContextProtocol]] — the MCP component
- [[SubAgent]] — the sub-agents component
- [[ValidationGates]] — enforced by stop/validation hooks
- [[SystemEvolution]] — where hooks/rules come from over time
- [[ClaudeCode]], [[Codex]] — the tools' built-in harnesses
- [[ColeMedin]] — articulator
- [[PIVLoop]] — the per-phase loop the AI layer is set up to run
- [[ProgressiveDisclosure]] — the reference-folder / on-demand-context pattern
- [[summary-harness-engineering]] — primary source
- [[summary-complete-agentic-coding-workflow]] — the AI layer as a greenfield starter
