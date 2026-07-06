---
title: "ContextEngineering"
type: concept
tags: [agent, context, memory, file-system, agentic]
sources: ["raw/01-articles/claude/2025-09-29 - Building agents with the Claude Agent SDK.md"]
last_updated: 2026-06-28
---

## Definition

Context engineering is the practice of deliberately designing an agent's environment — particularly its file and folder structure — so that the right information flows into the model's context window at the right time. Rather than loading everything upfront, the agent selects what to read based on the task at hand.

## Key Information

- The file system represents information that *could* be pulled into the model's context. How that information is organized determines how efficiently the agent can retrieve it.
- In [[ClaudeAgentSDK]], Claude uses bash tools (`grep`, `tail`) to perform agentic search: selectively loading only relevant portions of large files (logs, conversation histories, user uploads) rather than ingesting everything.
- Folder structure becomes a first-class design decision: an email agent storing conversations in a `Conversations/` folder can search that folder for relevant context on demand.
- Context engineering is an alternative framing to (and complement of) [[RetrievalAugmentedGeneration]]: where RAG chunks and embeds data into vectors, context engineering relies on the agent to navigate the raw file system directly.

### Agentic Search vs. Semantic Search

| Dimension | Agentic Search (context engineering) | Semantic Search ([[RetrievalAugmentedGeneration|RAG]]) |
|---|---|---|
| Speed | Slower | Faster |
| Accuracy | Higher | Lower |
| Transparency | High (bash commands visible) | Lower (embedding/vector black box) |
| Maintenance | Simpler | More complex (chunking, embeddings) |
| Recommendation | Start here | Add only when speed is critical |

### Relationship to Compact Feature

When context accumulates during long agent runs, the [[ClaudeAgentSDK]]'s compact feature summarizes prior messages automatically — ensuring the context window remains usable without manual intervention.

### Relationship to Subagents

[[ClaudeCodeSubagents]] complement context engineering: subagents run in isolated [[ContextWindow|context windows]], performing targeted searches and returning only the relevant excerpts. This keeps the orchestrator's context clean even when the search space is large.

### Context Engineering in Clinical Reasoning (Carta Healthcare)

[[CartaHealthcare]]'s Lighthouse platform illustrates a broader sense of context engineering beyond file-system navigation: assembling the right source documents, precise time boundaries (e.g., exact procedure start times), and priority order at runtime so Claude can answer clinical registry questions correctly. The team found that context construction — not prompt tuning — was the harder engineering problem: "A perfectly written prompt with bad context gives bad answers. A straightforward prompt with the right context delivers the results you need" (Matthew Mazzanti, Software Engineering Manager). This reinforces a general principle: agent performance is bottlenecked by what the model is given to work with, not solely by model capability or prompt wording.

### Navigating Large Codebases (May 2026)

At large-organization scale (multi-million-line monorepos, decades-old legacy systems, dozens of microservices), Claude's ability to help is bounded by its ability to find the right context — too much context loaded into every session degrades performance, while too little leaves Claude navigating blind. Recurring patterns for making a large codebase legible:

- **Lean, layered CLAUDE.md**: Claude loads CLAUDE.md files additively as it moves through the tree — root file for the big picture, subdirectory files for local conventions. The root file should hold pointers and critical gotchas only; everything else drifts into noise. See [[CLAUDE-md]].
- **Initializing in subdirectories, not the repo root**: counterintuitive in monorepos where tooling assumes root access, but Claude automatically walks up the directory tree and loads every CLAUDE.md file along the way, so root-level context is never lost.
- **Scoping test/lint commands per subdirectory**: running a full suite when only one service changed wastes context and causes timeouts; works well for service-oriented codebases, harder in compiled-language monorepos with deep cross-directory dependencies.
- **Version-controlled exclusions**: `.ignore` files plus `permissions.deny` rules in `.claude/settings.json` exclude generated files, build artifacts, and third-party code consistently for every developer; individuals working on code generators can override locally.
- **Codebase maps**: for organizations where code isn't consolidated in a conventional directory structure, a lightweight root-level markdown file listing each top-level folder with a one-line description gives Claude a table of contents to scan before opening files — layered (root = highest-level structure, subdirectories = next-level detail) for codebases with hundreds of top-level folders; for simpler cases, `@`-mentioning specific files/directories does the same job.
- **[[LanguageServerProtocol|LSP]] for symbol-level search**: grepping a common function name in a large codebase returns thousands of matches Claude must open files to disambiguate; LSP returns only references to the same symbol, filtering before Claude reads anything.
- Known limits of the hierarchical CLAUDE.md approach: codebases with hundreds of thousands of folders/millions of files, or legacy systems on non-git version control.

See [[summary-2026-05-14 - How Claude Code works in large codebases Best practices and where to start]].

## Related

- [[summary-2025-09-29 - Building agents with the Claude Agent SDK]] — source article introducing this framing
- [[CartaHealthcare]] — clinical-abstraction case study demonstrating context construction as the dominant engineering problem
- [[summary-2026-04-08 - How Carta Healthcare gets AI to reason like a clinical abstractor]] — source case study
- [[ClaudeAgentSDK]] — the SDK where context engineering is a first-class pattern
- [[ClaudeCode]] — the tool that pioneered agentic file-system navigation
- [[RetrievalAugmentedGeneration]] — the vector-search alternative to agentic file-system navigation
- [[ContextWindow]] — the resource context engineering is designed to manage efficiently
- [[ClaudeCodeSubagents]] — isolated context windows for parallel context gathering
- [[AIAgent]] — the broader agent paradigm context engineering serves
- [[LanguageServerProtocol]] — symbol-level search as a large-codebase navigation mechanism
- [[CLAUDE-md]] — layered CLAUDE.md hierarchy for large-codebase legibility
- [[AgenticCoding]] — organizational patterns for scaling codebase legibility
- [[summary-2026-05-14 - How Claude Code works in large codebases Best practices and where to start]] — large-codebase navigation patterns
