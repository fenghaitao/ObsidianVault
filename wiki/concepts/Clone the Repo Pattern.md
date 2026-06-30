---
title: "Clone the Repo Pattern"
type: concept
tags: [ai, agents, coding, context, libraries, prompt-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful.md"]
last_updated: 2026-06-29
---

## Definition

The "Clone the Repo" pattern is a technique for teaching AI coding agents to use unfamiliar libraries: clone the library's source code into your project as a git subtree so the model treats it as part of your codebase and learns patterns from it. Coined by Michael Arnaldi, the core insight is "just clone the [expletive] repo."

## Key Information

- Coding agents are trained to focus on your own code, not node_modules or gitignored directories — so having a library in node_modules doesn't help the model learn it
- Models have a knowledge cutoff and cannot learn new information after training — they need access to current library source code
- MCP servers, skills, and markdown documentation are less effective because models are primarily trained to consume and produce code, not read human documentation
- The technique: clone the library repo into a `repos/` folder as a git subtree (squashed, no history), reference it in `agents.md`, and have the model explore it to generate pattern files
- Works across languages (TypeScript, Rust) and even for libraries with zero documentation
- Michael Arnaldi has used this successfully for Effect library development since late summer 2025
- The effect.solutions website initially tried a CLI-based approach but eventually admitted the repo should just be cloned
- For brownfield projects: clone the main libraries used (e.g., TanStack Router, Svelte), ask the model to generate best practice files
- The model is good when it can operate at large scale using patterns — the zero-to-one problem is only a problem for the first 10 hours

## Related

- [[summary-20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful]] — source
- [[Michael Arnaldi]] — coined the pattern
- [[Effect]] — library used in the original demonstration
- [[Pattern Files (AI)]] — the next step after cloning
- [[AgentsDotMd]] — where repo references are configured
- [[KnowledgeCutoff]] — the LLM limitation this pattern addresses
- [[ContextEngineering]] — the broader practice of curating model context
