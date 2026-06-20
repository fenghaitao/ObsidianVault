---
title: "ContextEngineering"
type: concept
tags: [concept, ai-coding, prompt-engineering, context, claude-code, paradigm]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20250703 - Context Engineering is the New Vibe Coding (Learn this Now).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250717 - Context Engineering 101 - The Simple Strategy to 100x AI Coding.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250724 - Build ANY AI Agent with this Context Engineering Blueprint.md"
last_updated: 2026-06-19
---

## Definition

Context engineering is the discipline of supplying an [[AICodingAssistant]] with all the information it needs — instructions, examples, documentation, plans, tools, structured outputs, memory, and retrieval — to plausibly solve the task on the first attempt. **It is to prompt engineering what software architecture is to writing one good function.** [[AndrejKarpathy]] articulated it as "the art of providing all the context for the task to be plausibly solvable by the LLM." Mid-2025 onwards it became the dominant paradigm for production AI coding work, replacing [[VibeCoding]].

## Key Information

### How it differs from prompt engineering

**Prompt engineering** = tweaking the wording of a single prompt to coax a single good output. Word choice, tone, role-play, chain-of-thought triggers.

**Context engineering** ⊃ prompt engineering. The prompt is one slice of a much larger surface:

| Layer | What lives here | Stability |
|---|---|---|
| **Global rules** (e.g. `CLAUDE.md`) | Project-wide conventions: naming, test patterns, file structure, "never edit the secrets file" | Forever / very rare changes |
| **Slash commands** / workflows | Domain-agnostic planning + execution flows | Per-project type |
| **Base PRP** / use-case template | Domain-specific patterns, gotchas, doc references | Per project type |
| **Generated PRP** | Feature-specific plan with all relevant context curated | Per feature |
| **Initial prompt** | The task description that seeds the rest | Per task |
| **Examples** | Real code patterns the AI matches against | As they accumulate |
| **Documentation** | External docs referenced by URL or pre-fetched via [[RetrievalAugmentedGeneration]] | Stable |
| **State / memory** | What's been built before; conversation history | Per session |

The act of context engineering is *deciding what goes in each layer and how it's structured.*

### Why it matters

- **AI coding assistants don't fail because the LLM is dumb.** They fail because they don't have the information. The Codto survey [[ColeMedin]] cites: 76.4% of developers have low confidence shipping unreviewed AI code, with hallucination as the dominant problem. Context engineering directly attacks the cause.
- **Intuition doesn't scale; structure does.** [[VibeCoding]] is intuition-driven. It works for prototypes, breaks at production. Context engineering is the structured alternative — slower per task but linearly composable as project complexity grows.
- **Sharpening the axe.** Cole's Lincoln quote: *"Give me six hours to chop down a tree, I'll spend the first four sharpening my axe."* Time invested up-front in good context dramatically reduces total time spent on the build.

### What's in a typical context-engineered project

Pattern that emerged through the trilogy of videos:

```
project/
├── CLAUDE.md                   # global rules, never-changes
├── .claude/commands/           # slash commands: /generate-prp, /execute-prp
│   ├── generate-prp.md
│   └── execute-prp.md
├── PRPs/
│   ├── templates/base-prp.md   # use-case-specific template
│   └── <feature>.md            # the generated PRP for this build
├── examples/                   # real code patterns to match
└── initial.md                  # feature description input
```

### Concrete implementations

- **[[PRPFramework]]** — [[Rasmus]]'s specific implementation; the canonical context-engineering toolkit Cole uses across his content. PRP = Product Requirements Prompt.
- **Use-case templates** — specialized PRP templates per (language × project type). Examples Cole has shipped: generic, MCP servers (Cloudflare/TypeScript), [[PydanticAI]] agents.
- **[[ValidationGates]]** — the testing/linting/iteration loop baked into PRP execution.

### Components frequently cited

[[ContextEngineering]] umbrella includes (per the Lang Chain article + the X discourse):
- Prompt engineering
- [[StructuredOutputs]]
- State / history / memory
- Examples
- [[RetrievalAugmentedGeneration]]
- Tools (and their docstrings — see [[ToolUse]])

## Related

- [[VibeCoding]] — the foil paradigm being replaced
- [[PRPFramework]] — the concrete implementation Cole uses
- [[Rasmus]] — PRP framework creator
- [[AndrejKarpathy]] — articulated the canonical definition
- [[ClaudeCode]] — primary execution surface
- [[ColeMedin]] — primary teacher in this corpus
- [[CapabilitiesOverTools]] — Cole frames Context Engineering as the "capability" version of various tool-specific skills
- [[ValidationGates]] — sub-pattern
- [[AICodingAssistant]] — what context engineering is *for*
- [[summary-context-engineering-is-new-vibe-coding]] — intro
- [[summary-context-engineering-101]] — deeper dive with Rasmus
- [[summary-context-engineering-blueprint-for-ai-agents]] — PydanticAI use-case template
- [[evolution-vibe-coding-to-harness-engineering]] — synthesis: where Context Engineering sits in the paradigm timeline
