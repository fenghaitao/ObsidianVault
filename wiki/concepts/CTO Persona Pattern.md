---
title: "CTO Persona Pattern"
type: concept
tags: [vibe-coding, prompting, ai]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz.md"]
last_updated: 2026-07-11
---

## Definition

[[Zevi Arnovitz]]'s technique of prompting an AI project/agent to behave as a specific, opinionated human role — originally a "CTO" — rather than a generic assistant, explicitly countering default chatbot sycophancy so it can push back on bad decisions instead of agreeing with them.

## Key Information

- Originated as a [[ChatGPT]] project prompted with: you are the complete technical owner of this project, you own how users should feel, challenge me, don't be a people-pleaser — explicitly designed to mitigate what Zevi calls "regular chatbotisms."
- Motivating anecdote: outside this dedicated project, [[ChatGPT]] falsely agreed his question about Bun JavaScript was "the same" as an unrelated framework (Zustand), then admitted "I thought you were just making this up and I was riffing with you" when corrected — illustrating the sycophancy risk a generic chatbot poses for someone without the technical background to catch the error themselves.
- Zevi's broader mental model: he finds it easiest to reason about different AI tools/models by imagining them as specific people with distinct personalities, rather than as interchangeable assistants — a framing he extends into [[Multi-Model Peer Review]] (Claude as a communicative "dev lead," Codex as a heads-down solo problem-solver, Gemini as a talented but erratic "crazy scientist").
- As agentic coding tools improved, the standalone [[ChatGPT]] "CTO" project became unnecessary as a separate step — the same persona and instructions were folded directly into a project's `claude.md` file inside [[Claude Code]]/[[Cursor]], since one agent could now handle both exploration and execution that previously required a conversational planning layer plus a separate execution tool.
- Forms the persona layer underneath Zevi's [[Slash Command Development Workflow]]: the CTO persona is who is "talking" through each of the create-issue, exploration, planning, and execution stages.

## Related

- [[summary-31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz]] — source summary
- [[Zevi Arnovitz]] — originates this pattern
- [[Slash Command Development Workflow]] — the workflow this persona underlies
- [[Multi-Model Peer Review]] — extends the same personification approach to multiple models
- [[Claude Code]] / [[Cursor]] — where the persona is currently implemented
- [[ChatGPT]] — where the persona originated as a project
