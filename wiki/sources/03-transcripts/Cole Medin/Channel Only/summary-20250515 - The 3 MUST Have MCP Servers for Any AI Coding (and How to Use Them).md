---
title: "summary-20250515 - The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them)"
type: source
tags: [source, transcript, mcp, ai-coding, workflow]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20250515 - The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them).md"]
last_updated: 2026-06-19
---

## Core Summary

[[ColeMedin]] names three [[ModelContextProtocol]] server categories he considers non-negotiable for any AI-coding workflow: **documentation RAG**, **database management**, and **web search**. Demonstrated together in a live build of a [[PydanticAI]] + [[Supabase]] RAG agent inside [[Windsurf]]. Reinforces his earlier "specialized MCP servers > fat agents" thesis at the developer-tooling layer.

## Key Points

The three categories with Cole's recommended servers:

| Category | Recommended | Purpose |
|---|---|---|
| **Documentation RAG** | [[Crawl4AIRAG]] (Cole's open-source) — alt: Context7 | Bring framework docs (PydanticAI, Supabase, etc.) into the AI IDE so it stops hallucinating APIs |
| **Database management** | [[Supabase]] MCP — alt: [[Neon]] MCP | Let the IDE create tables, run migrations, write SQL via natural language |
| **Web search** | Brave MCP | Supplemental reference (forum posts, examples) when local docs aren't enough |

- **The "Brave + Crawl4AIRAG" pairing** is the typical pattern: query your curated knowledge base first, fall back to web search for examples and adjacent context.
- **Workspace rules** (Windsurf's `manage_memories` → workspace rules) carry persistent instructions like "always check planning.md and tasks.md before coding" — context that shouldn't have to be in every prompt.
- **Planning files + task files** structure: Cole drafts a `planning.md` (project overview, components) with Claude Desktop, and a `tasks.md` (granular checklist). The IDE reads both before any code generation. Keeps prompts short and the AI focused.
- **Live demo**: built a full Pydantic AI RAG agent with [[Streamlit]] frontend, document ingestion, and Supabase storage in <1 hour, with ~20 minutes of manual cleanup. Caveat: the IDE didn't reliably use the Supabase MCP to create tables on first prompt — Cole had to re-prompt.
- **Examples are the highest-leverage prompting trick.** Cole gives a previous Pydantic AI streaming-Streamlit script as a reference file in the prompt; the IDE matches that style in the new agent.

## Related

- [[ModelContextProtocol]] — common substrate
- [[Crawl4AIRAG]] — Cole's recommended docs-RAG server
- [[Supabase]] — recommended database (with its own MCP)
- [[Neon]] — alternative Postgres MCP
- [[Windsurf]] — primary AI IDE in the demo
- [[Cursor]] — equivalent target
- [[PydanticAI]] — agent framework used in demo
- [[Streamlit]] — frontend in demo
- [[ColeMedin]] — author
- [[AICodingAssistant]] — what's being augmented
