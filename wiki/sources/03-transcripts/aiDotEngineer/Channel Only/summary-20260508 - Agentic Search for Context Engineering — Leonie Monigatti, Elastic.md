---
title: "summary-20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic"
type: source
tags: [source, transcript, agentic-search, context-engineering, search-tools, rag, elasticsearch, shell-tool, agent-skills, tool-description, esql, gina-grap]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260508 - Agentic Search for Context Engineering — Leonie Monigatti, Elastic.md"]
last_updated: 2026-06-29
---

## Core Summary
Leonie Monigatti from Elastic presents a workshop on agentic search as the core of context engineering. She argues that context engineering is about 80% agentic search — the search tools that decide what goes from context sources into the context window. The talk covers the evolution from fixed RAG pipelines to agentic RAG, the landscape of search tools (semantic search, general-purpose query execution, shell/bash tools, custom CLIs), common failure modes, and practical recommendations for curating a balanced set of specialized (low floor) and general-purpose (high ceiling) search tools.

## Key Points

### Context Engineering = 80% Agentic Search
- Context engineering is the art of deciding what goes into the context window from all possible context sources
- The search tool (the arrow from context sources to context window) is the underappreciated component
- Context sources include: local files, working memory (scratch pads), agent skills, databases, web, long-term memory

### Evolution: Fixed RAG → Agentic RAG → Multi-Source Search
- **Fixed RAG**: User message verbatim as search query → vector search → retrieved chunks + user message → LLM. Limitations: always retrieves even when not needed, single retrieval can't handle multi-hop queries
- **Agentic RAG**: Agent decides whether/when to call the search tool, can rewrite queries, retrieve multiple times
- **Multi-Source**: Different context sources need different native search tools (file search, skill loading, database search, web search, memory tools)

### The Shell Tool as Universal Adapter
- Called "shell tool" (LangChain), "bash tool" (Anthropic), "exec tool" (OpenClaw)
- Lets agents run terminal commands: ls, grep, CLIs, curl, write scripts
- Agents can "cheat" at semantic search by chaining grep with synonyms (e.g., searching for "regulate", "compliance", "GDPR", "governance")
- Works but is inefficient — you don't want agents searching for all possible animal names to find "movies with animal superheroes"
- Can be extended with custom CLIs like Gina Grap for proper semantic search over local files

### Three Common Failure Modes
1. **Agent doesn't call any tool**: Thinks it can answer from parametric knowledge
2. **Agent calls the wrong tool**: e.g., calling web search instead of database search
3. **Agent generates wrong parameters**: Especially for complex tools like ESQL query generation (e.g., using `%` instead of `*` as wildcard)

### Tool Description Best Practices
- Start with core purpose; if that works, great
- If agent struggles, add: trigger conditions (when to use/not use), relationships (call skill X before tool Y), reinforcement in system prompt
- Error handling in tools is critical — return errors to the agent so it can self-correct rather than crashing

### Agent Skills for Complex Tool Parameters
- Agent skills use progressive disclosure: name + description in system prompt, full body loaded on demand
- Skills provide documentation for complex parameters (e.g., ESQL syntax, wildcard rules)
- Tool description should reference the skill: "always use the ESQL skill to generate the query before using this tool"
- Allows agents to do aggregations and calculations in the search tool rather than in the LLM (LLMs are bad at counting)

### Practical Recommendations: Low Floor + High Ceiling
- **Low Floor**: Specialized tools with simple parameters that agents can use out of the box with few mistakes (e.g., semantic search, get-customer-by-ID)
- **High Ceiling**: General-purpose tools (shell tool, query execution tool) for unexpected/complex queries
- **Start with general-purpose** if you don't know agent query behavior yet
- **Log agent behavior**: If agent takes 4-5 tool calls per question, the tool is too difficult — scope out something more specialized
- **Stronger models reduce error rates** for general-purpose tools but don't eliminate errors entirely

### Demo Highlights
- Semantic search tool (Elasticsearch vector store) — works for simple queries, fails on keyword searches (GPA → returns unrelated Gemma results)
- ESQL query execution tool — more powerful but agent initially used wrong wildcard (`%` vs `*`)
- Agent skill fixed the ESQL issue by loading syntax documentation on demand
- Shell tool with grep — works for exact matches, agents chain synonyms for fuzzy search
- Gina Grap CLI — proper semantic search over local files, agent correctly used it on first try

### Q&A Highlights
- **Model strength matters**: Stronger models reduce parameter error rates significantly for general-purpose tools
- **RAG vs Agentic RAG**: RAG is still effective for many use cases; switching between them needs agentic logic
- **Combining tools**: Vercel experiment showed hybrid agent (bash + database tools) achieved highest accuracy by using database tool first, then verifying with shell tool
- **Sub-agents for search**: Claude Code uses sub-agents for specific niche search tasks
- **Context clearing**: Progressive disclosure — load skill body when needed, offload when context window progresses past it

## Related
- [[Leonie Monigatti]] — speaker, Elastic
- [[Elastic]] — company behind Elasticsearch
- [[Agentic Search]] — the core concept
- [[Agentic RAG]] — evolution from fixed RAG
- [[ContextEngineering]] — the parent paradigm
- [[Shell Tool]] — universal adapter concept
- [[Tool Description]] — best practices for tool descriptions
- [[Agent Skills]] — progressive disclosure for complex parameters
- [[Low Floor High Ceiling]] — tool curation strategy
- [[ESQL]] — Elasticsearch Query Language
- [[Gina Grap]] — semantic search CLI for local files
- [[LangChain]] — framework used for demos
- [[BashTool]] — Anthropic's bash tool
- [[RAG]] — the earlier paradigm
- [[ProgressiveDisclosure]] — design pattern for skills
- [[aiDotEngineer]] — event host
