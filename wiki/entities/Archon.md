---
title: "Archon"
type: entity
tags: [tool, ai-agent, open-source, agent-builder, meta-agent]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/01 - Build an ARMY of AI Agents on Autopilot with Archon, Here's How.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/02 - 10x Your AI Agents with this ONE Agent Architecture.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/03 - Coding Subagents - The Next Evolution of AI IDEs.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
last_updated: 2026-06-19
---

## Definition

Archon is an open-source AI agent that builds other AI agents — a "[[MetaAgent]]" or "agenteer" — created by [[ColeMedin]]. It specializes in generating [[PydanticAI]] and [[LangGraph]] agents using internal [[RetrievalAugmentedGeneration]] over those frameworks' documentation, plus a multi-step agentic flow (Reasoner → Coder → human review) for more consistent output than generalist AI coders.

## Key Information

### What it is

- Open-source, free, runs locally. No vendor lock-in — output is plain Python code using PydanticAI / LangGraph.
- Both a working tool *and* an educational vehicle: Cole builds it in public, with each numbered version (v1, v2, …) demonstrating a different agentic technique.
- Two operating modes:
  1. Standalone Streamlit app with a chat interface and admin tabs.
  2. [[ModelContextProtocol]] server invoked by AI IDEs ([[Windsurf]], [[Cursor]], Cline) as a specialized [[SubAgent]] for agent-building.

### Core architecture

- **LangGraph workflow** for the agent-building process. Nodes include:
  - **Reasoner agent** — defines scope and selects relevant doc pages.
  - **Advisor agent** (v6+) — picks examples and pre-built tools from the resource library.
  - **Coder agent** — actually emits the code, performs RAG over the docs.
  - **Human-in-the-loop** node — pauses for user feedback, then iterates.
- Uses [[Supabase]] as the vector DB for the RAG knowledge base.
- Cole has stated future versions will integrate his [[Crawl4AIRAG]] MCP server as the underlying knowledge layer — replacing Archon's existing custom RAG pipeline with Crawl4AIRAG's [[ContextualRetrieval]]-enhanced ingest. This brings consistency with Cole's broader "build your own knowledge base" toolchain.
- The MCP-server wrapper is a FastAPI endpoint exposing the graph plus two MCP tools: `create_thread_id` and `run_archon`. The thread ID is how Archon maintains conversation state across MCP's otherwise-stateless calls — the calling LLM is trusted to pass it back.

### Roadmap (versioned curriculum)

| Version | Feature |
|---|---|
| 1 | Simple agent (PydanticAI only) |
| 2 | LangGraph agentic workflow |
| 3 | MCP support |
| 4 | Streamlit interface |
| 5 | Multi-agent coding workflow ([[ParallelAgentArchitecture]] for code refinement) |
| 6 | Tool library + MCP examples (advisor agent picks them) |
| 7 | LangGraph docs in the knowledge base |
| 8 | Self-feedback loops (autonomous iteration) |
| 9 | Self-agent execution (spin up containers, test the agent it just built) |
| 10 | Multi-framework support (LangChain, Agno, CrewAI, LlamaIndex) |
| 11 | Autonomous framework learning — saves successful agents back to its examples |
| 12 | Advanced RAG (hybrid search, reranking, hierarchical chunking) |
| 13 | MCP agent marketplace — publish Archon-built agents as MCP servers |

### "Specialized > generalist" thesis

Cole's argument for Archon's existence: AI IDEs like Windsurf and Cursor hallucinate when given too many tools or unfamiliar frameworks. A framework-specialized sub-agent with curated docs + a multi-step generation flow produces more reliable, structurally consistent code. Archon is the prototype for this pattern; the long-term vision is a marketplace of specialized agents reachable via MCP.

### Repositioned as a harness builder (2026)

By the [[HarnessEngineering]] era (mid-2026), Cole reframes Archon as **"my open-source harness builder"** — the easiest way to build your own custom [[AgentHarness]] (like a [[RalphLoop]]) tailored to your exact software-development lifecycle. This is consistent with Archon's original "meta-agent that builds agents" identity, now extended: it doesn't just generate agent *code*, it helps you assemble the multi-session orchestration harnesses that are the frontier of [[AgenticEngineering]]. See `summary-harness-engineering`.

### Demo capabilities seen across the playlist

- Built an "MCP Agent Army" — primary agent + 6 specialized sub-agents (Brave search, GitHub, Slack, Airtable, Filesystem, Firecrawl) — that handles compound tasks like "search → save to Airtable → notify in Slack."
- Generated a Travel Planner with parallel flight/hotel/activity sub-agents and a synthesizer.
- Generated a Brave-search agent end-to-end via Windsurf+Archon, with iterative human-in-the-loop refinement.

## Related

- [[ColeMedin]] — creator
- [[PydanticAI]] — primary target framework Archon generates code for
- [[LangGraph]] — workflow framework Archon uses internally and generates code for
- [[ModelContextProtocol]] — how Archon plugs into AI IDEs
- [[MetaAgent]] — Archon's architectural category
- [[ParallelAgentArchitecture]] — used internally for v5+ self-refinement
- [[SubAgent]] — Archon-as-MCP-tool plays this role for IDEs
- [[Supabase]] — Archon's RAG backend
- [[RetrievalAugmentedGeneration]] — used for doc-grounded code generation
- [[Windsurf]], [[Cursor]] — primary integration targets
- [[summary-introducing-archon-ai-agent-builder]] — official intro
- [[summary-build-an-army-of-ai-agents-archon]] — agent army demo
- [[summary-10x-your-ai-agents-parallel-architecture]] — parallel architecture deep dive
- [[summary-coding-subagents-mcp-evolution]] — MCP integration deep dive
