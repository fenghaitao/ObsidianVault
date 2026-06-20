# LLM Wiki — AI Agents & Agentic Engineering

A structured, self-evolving knowledge base for **AI agents, agentic engineering, and Claude-based development patterns**. Built on [Karpathy's LLM-Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) using Obsidian + Claude Code.

## What is this vault?

This is a **compiled knowledge base**, not a RAG system. Instead of retrieving fragments on-demand, new information is **ingested, synthesized, and permanently integrated** into a heavily cross-linked network of concepts, entities, and source summaries. Think of it as a **second brain that learns**.

The vault focuses on:
- **AI agents & sub-agents** — Architecture patterns, tool use, orchestration
- **Agentic engineering** — Techniques for production-grade AI coding systems
- **Context engineering** — How to supply agents with the context they need to solve problems on the first try
- **Cole Medin's frameworks** — PRP framework, harness engineering, five golden rules for greenfield coding
- **RAG strategies** — Contextual retrieval, hybrid search, reranking, vs. agentic search
- **Agent harnesses** — Multi-session orchestration, avoiding context rot, system evolution

## Directory Structure

```
vault/
├── raw/                          # Source material (immutable)
│   ├── 01-articles/             # Blog posts, articles, markdown
│   ├── 02-papers/               # PDFs, research papers
│   ├── 03-videos/               # Video transcripts, show notes
│   ├── 04-audio/                # Podcast transcripts
│   ├── 09-archive/              # Processed files (never read)
│
├── wiki/                         # Compiled knowledge base (you own this)
│   ├── index.md                 # Global directory of all pages
│   ├── log.md                   # Append-only operation log
│   ├── concepts/                # Frameworks, theories, patterns (TitleCase)
│   ├── entities/                # People, companies, tools, products (TitleCase)
│   ├── sources/                 # One-to-one summaries of raw/ files (kebab-case)
│   └── syntheses/               # Cross-document analyses, comparisons (kebab-case)
│
├── assets/                       # Images, diagrams, media
├── .claude/                      # Claude Code configuration
│   └── skills/                   # /ingest, /query, /lint workflow skills
│
├── CLAUDE.md                      # (This file) Rules & schema for the vault
└── README.md                      # (This file) Overview & quick start
```

## How to Use: The Workflow

This vault runs on three skills:

### `/ingest <path>` — Process new material

When you have a source file (article, video transcript, PDF):

```
/ingest raw/01-articles/some-article.md
```

The skill will:
1. **Read** the source file
2. **Extract** key concepts and entities
3. **Integrate** into relevant wiki pages (create or update)
4. **Create** a source summary (`summary-{slug}.md`)
5. **Update** `wiki/index.md` and `wiki/log.md`
6. **Archive** the source to `raw/09-archive/`

**Key rule**: The raw file is immutable. Only the wiki pages change.

### `/query <question>` — Ask the wiki

To search your knowledge base:

```
/query What are the 5 techniques Cole recommends for agentic engineering?
```

The skill will:
1. **Scan** `wiki/index.md` for relevant pages
2. **Deep-read** concept & entity pages
3. **Synthesize** an answer with [[wikilink]] citations
4. **Optionally save** as a synthesis page (for high-value answers)

Answers always cite specific pages, not just hallucinations.

### `/lint` — Health check your wiki

To audit the knowledge base:

```
/lint
```

Detects:
- **Orphan pages** — Pages with zero inbound links
- **Dead links** — Wikilinks pointing to non-existent pages
- **Unsynced index** — Pages that exist but aren't registered in `wiki/index.md`
- **Unresolved conflicts** — Contradictions between sources

All issues are reported; fixes are applied only with your approval.

---

## Vault Content Overview

### Current Scope
- **44 source summaries** — Cole Medin's YouTube series (Jan–May 2026), Anthropic guides
- **27 entities** — Tools (Claude Code, PydanticAI, LangGraph), people (Cole, Karpathy), companies
- **30+ concepts** — Agent architecture, RAG patterns, harness engineering, 5 golden rules
- **4 syntheses** — Cross-document analyses: RAG playbooks, context-rot countermeasures, vault self-description

### Key Concepts (Start Here)
- [[AIAgent]] — Fundamentals of what an AI agent is
- [[AgentHarness]] — Multi-session orchestration for long-running tasks
- [[ContextEngineering]] — Supplying context to agents for first-try success
- [[PRPFramework]] — Rasmus's structured context-engineering methodology
- [[ContextRot]] — The "dumb zone" problem and how to fight it

### Key Entities
- [[ColeMedin]] — Creator of Archon, vocal advocate for PydanticAI + MCP
- [[ClaudeCode]] — Anthropic's AI coding agent (primary execution surface)
- [[PydanticAI]] — Type-safe Python agent framework Cole champions
- [[ModelContextProtocol]] — Standardized tool/MCP-server protocol

### Sample Syntheses
- [[evolution-vibe-coding-to-harness-engineering]] — The paradigm shift over 2025–2026
- [[cole-medin-rag-playbook]] — Consolidated RAG strategies and recommendations
- [[fighting-context-rot]] — Every technique to avoid the "dumb zone"

---

## Quick Start

1. **Explore the wiki**: Open [[wiki/index.md]] to see all pages
2. **Ask a question**: Try `/query what is context engineering?`
3. **Add new material**: Drop an article/transcript into `raw/01-articles/`, then `/ingest raw/01-articles/your-file.md`
4. **Check health**: Run `/lint` periodically to catch orphans and dead links

---

## Key Rules

**Never break these:**
- 🚫 **Never modify `raw/`** — Read-only. Only archive after ingest.
- 🚫 **Never create orphan pages** — Every page must have ≥1 inbound link from other content.
- 🚫 **Never silently resolve conflicts** — Surface contradictions, flag them, let humans decide.
- 🚫 **Never invent citations** — If it's not in the source, mark it inferred or omit it.
- ✅ **Always update `wiki/index.md`** after adding a page
- ✅ **Always update `wiki/log.md`** with an entry after every operation
- ✅ **Always add a `## Related` section** linking to 2–5 related pages

---

## Page Structure

Every wiki page starts with YAML frontmatter:

```yaml
---
title: "Page Title"
type: concept | entity | source | synthesis
tags: [tag1, tag2, tag3]
sources: [raw/01-articles/example.md]
last_updated: 2026-06-20
---
```

Then the body:
```markdown
# Concept Title

[1–3 sentence definition]

## Key Points
- Point 1
- Point 2

## Related
- [[RelatedPage1]]
- [[RelatedPage2]]
```

---

## Language & Conventions

- **All content in English** (translate if source is another language)
- **Wiki pages** are `TitleCase` for concepts/entities, `kebab-case` for sources/syntheses
- **Links** use Obsidian wikilinks: `[[PageName]]` (not `[text](url)`)
- **Images** embedded as: `![[image.png]]` from `/assets/`

---

## Contributing

1. Add raw source to `raw/` (organized by type: articles, papers, videos, audio)
2. Run `/ingest raw/path/to/file`
3. Skill will create summary, integrate, and archive
4. Review the changes in `wiki/` and `wiki/log.md`
5. Run `/lint` to ensure no orphans or dead links

---

## Related

- [[KarpathyLLMWiki]] — The foundational pattern
- [[SecondBrain]] — This vault as a personal knowledge engine
- [[CLAUDE.md]] — Detailed schema, permissions, and hard rules
