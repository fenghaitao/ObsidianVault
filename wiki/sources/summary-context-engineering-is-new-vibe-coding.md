---
title: "summary-context-engineering-is-new-vibe-coding"
type: source
tags: [source, transcript, context-engineering, vibe-coding, claude-code, karpathy]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20250703 - Context Engineering is the New Vibe Coding (Learn this Now).md"]
last_updated: 2026-06-19
---

## Core Summary

[[ColeMedin]] introduces **[[ContextEngineering]]** — the emerging paradigm replacing [[VibeCoding]] for production AI coding work. The thesis: AI coding assistants don't fail because the LLM is bad; they fail because they lack context. Cole demonstrates [[Rasmus]]'s [[PRPFramework]] (Product Requirements Prompts) inside [[ClaudeCode]] to build a Pydantic AI agent end-to-end with minimal hand-holding. Frames Context Engineering as the most important AI engineering skill of mid-2025.

## Key Points

- **The frame**: [[AndrejKarpathy]] coined "vibe coding" earlier in 2025 — letting the AI write code with minimal validation. Cole argues the honeymoon is over: "intuition does not scale, structure does." Cites a Codto survey: 76.4% of developers have low confidence shipping unreviewed AI code.
- **The definition (Karpathy, on X)**: Context engineering is "the art of providing all the context for the task to be plausibly solvable by the LLM." Toby (Shopify CEO) framed it as a paradigm shift from prompt engineering — context deserves to be "treated as an engineered resource requiring careful architecture."
- **Context engineering ⊃ prompt engineering**: prompt engineering tweaks wording for one good output; context engineering supplies the entire ecosystem (instructions, rules, documentation, plans, tools, examples, structured output, state/memory, RAG).
- **The PRP framework (from [[Rasmus]] in the Dynamis community)** — Cole's preferred concrete approach:
  - `CLAUDE.md` — global rules that don't change between features (style guides, test conventions, project structure).
  - `initial.md` — feature description for the *next* implementation: feature, examples, documentation, considerations.
  - `examples/` — real code examples the AI should pattern-match against.
  - **Slash commands** like `/generate-prp` and `/execute-prp` in [[ClaudeCode]] — markdown files in `.claude/commands/` that drive multi-step planning then implementation.
  - **PRP** (Product Requirements Prompt) — a generated prompt-document combining the feature requirements + curated codebase intelligence + agent runbook. The minimum viable packet for the AI to plausibly ship production code on the first pass.
- **Demo**: ran `/generate-prp initial.md` → Claude Code researched APIs, analyzed examples, produced a full implementation plan as a PRP. Then `/execute-prp <path>` → 30 minutes later, a working Pydantic AI agent with passing tests. One iteration needed for a Pydantic AI gotcha.
- **The Lincoln quote** Cole returns to: "If you give me six hours to chop down a tree, I'm going to spend the first four sharpening my axe." Context engineering is the sharpening.
- **The Lang Chain framing** Cole cites: "context engineering is becoming the most important skill an AI engineer can develop."

## Related

- [[ContextEngineering]] — central concept
- [[VibeCoding]] — the foil
- [[PRPFramework]] — concrete implementation
- [[ClaudeCode]] — primary AI IDE
- [[AndrejKarpathy]] — coined Vibe Coding, articulated Context Engineering
- [[Rasmus]] — PRP framework creator
- [[ColeMedin]] — author
- [[CapabilitiesOverTools]] — Cole connects this principle directly: "Gemini CLI is a tool, context engineering is a capability"
- [[PydanticAI]] — agent framework used in the demo
