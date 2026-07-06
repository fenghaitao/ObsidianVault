---
title: "ModelContextProtocol"
type: entity
tags: [protocol, standard, anthropic, tool-use, mcp]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/01 - Build an ARMY of AI Agents on Autopilot with Archon, Here's How.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/03 - Coding Subagents - The Next Evolution of AI IDEs.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250414 - The ULTIMATE Guide to Building Your Own MCP Servers (Free Template).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250515 - The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260702 - Finally, an Open Standard for the Karpathy LLM Wiki is HERE.md"
last_updated: 2026-07-06
---

## Definition

The Model Context Protocol (MCP) is a protocol developed by [[Anthropic]] for standardizing how large language models discover and call external tools. An "MCP server" exposes a set of tools (functions) over the protocol; any MCP-aware client (Claude Desktop, [[Cursor]], [[Windsurf]], custom Python agents using [[PydanticAI]]'s `mcp_servers` parameter) can spin one up and gain instant access to its tools.

## Key Information

### Why it matters in this playlist

MCP is the mechanism that makes [[Archon]]'s "specialized sub-agent for AI IDEs" pattern work. Archon wraps its [[LangGraph]] workflow as an MCP server with two tools (`create_thread_id`, `run_archon`); [[Windsurf]] / [[Cursor]] then invoke Archon as a tool when generating PydanticAI/LangGraph code.

### MCP server ecosystem (mentioned in the playlist)

Cole's "MCP Agent Army" demo connects to:
- **Brave Search** — web search
- **GitHub** — repo operations
- **Slack** — messaging
- **Airtable** — database/spreadsheet
- **Filesystem** — local file ops
- **Firecrawl** — webpage scraping

Other MCP servers Cole mentions are available: Google Drive, Discord, JetBrains, Stripe, AWS S3, DeepSeek, Qdrant.

### Architectural patterns enabled

1. **MCP-as-tool-vendor**: a generalist LLM gets specialized capabilities just by mounting MCP servers. No code changes to the LLM client.
2. **MCP-as-sub-agent**: wrap a complex agentic workflow (like Archon) as an MCP server. Calling LLMs treat it as a single tool but get a multi-step agent under the hood. Pattern Cole calls "the next evolution of AI IDEs."
3. **MCP Agent Army**: many sub-agents, each owning one MCP server's tools, with a primary agent dispatching among them. Solves LLM tool-overload at scale.

### Key technical details

- **Stateless by design** — each tool call is independent. Cole's "thread_id workaround" (the calling LLM passes back an ID to maintain server-side state) is necessary for stateful agents like Archon.
- **Tool docstrings drive selection** — the calling LLM reads each MCP tool's description (its docstring) to decide when to invoke it. Good docstrings are the equivalent of good prompt engineering for the MCP boundary.
- **Cross-language SDKs** — Python and TypeScript both first-class.
- **Configuration is uniform across clients** — the same JSON config works in Claude Desktop, Windsurf, Cursor.

### PydanticAI integration

PydanticAI's `mcp_servers=[...]` parameter on an agent connects it directly to one or more MCP servers. The agent's tool list automatically includes all the server's exposed tools.

### Building your own MCP server

Cole's published template (covered in [[summary-20250414 - The ULTIMATE Guide to Building Your Own MCP Servers (Free Template)]]) using `FastMCP` from Anthropic's Python SDK. Three structural pieces every well-built server has:

1. **Lifespan management** — initialize shared resources (DB clients, vector store connections, [[Mem0]] clients) **once** at startup, expose them via context to every tool call. Many existing MCP servers in the wild miss this and re-initialize per call.
2. **`FastMCP` instance + `@mcp.tool` decorators** — minimal boilerplate, the function docstring becomes the tool description sent to the LLM.
3. **Dual-transport support** (`stdio` + `SSE`) — most published servers only ship one. Some clients (like [[N8N]]) only support SSE; some local-only setups prefer stdio. Supporting both is a best practice.

> See `Cole's mem0 MCP server` referenced in [[Mem0]] for a complete implementation.

### The OKF analogy

Per [[ColeMedin]] in `summary-20260702 - Finally, an Open Standard for the Karpathy LLM Wiki is HERE`: "what MCP did for agent-to-tool communication, [[OpenKnowledgeFormat|OKF]] is doing for agent-to-knowledge-base communication" — both are thin, adoption-friendly standards that let any agent interoperate with any tool/knowledge-base built by someone else, without bespoke integration work per pair.

### Cole's "3 must-have MCP servers" for AI coding

From [[summary-20250515 - The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them)]] — Cole's recommended slot fillers:

| Slot | Recommended | Purpose |
|---|---|---|
| Documentation RAG | [[Crawl4AIRAG]] (or Context7) | Curated framework docs the IDE can query while coding |
| Database management | [[Supabase]] MCP (or [[Neon]] MCP) | Create tables, migrations, run SQL via natural language |
| Web search | Brave MCP | Supplemental retrieval for examples and forum posts |

Pairs commonly used together: **Crawl4AIRAG + Brave** — query private docs first, fall back to web for examples not in the curated set.

## Related

- [[Anthropic]] — protocol author
- [[Archon]] — wrapped as an MCP server in v3+
- [[PydanticAI]] — first-class MCP integration for sub-agents
- [[N8N]] — MCP-aware no-code platform; SSE-only
- [[Windsurf]], [[Cursor]] — MCP-aware AI IDEs
- [[Crawl4AIRAG]] — Cole's documentation-RAG MCP server
- [[Mem0]] — long-term-memory library Cole's MCP template uses as its example
- [[SubAgent]] — pattern often realized via MCP
- [[ToolUse]] — what MCP standardizes
- [[OpenKnowledgeFormat]] — the analogous standard for agent-to-knowledge-base communication
- [[summary-03 - Coding Subagents - The Next Evolution of AI IDEs]] — MCP-as-sub-agent thesis
- [[summary-01 - Build an ARMY of AI Agents on Autopilot with Archon, Here's How]] — MCP Agent Army demo
- [[summary-20250414 - The ULTIMATE Guide to Building Your Own MCP Servers (Free Template)]] — building your own MCP server with best practices
- [[summary-20250515 - The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them)]] — recommended MCP server triad for AI coding
- [[summary-20250627 - MCP Sampling in Pydantic AI： How to Proxy LLM Calls]] — MCP sampling feature
- [[summary-20260702 - Finally, an Open Standard for the Karpathy LLM Wiki is HERE]] — the OKF analogy
