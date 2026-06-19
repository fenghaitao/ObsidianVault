---
title: "ModelContextProtocol"
type: entity
tags: [protocol, standard, anthropic, tool-use, mcp]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/01 - Build an ARMY of AI Agents on Autopilot with Archon, Here's How.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/03 - Coding Subagents - The Next Evolution of AI IDEs.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
last_updated: 2026-06-19
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

## Related

- [[Anthropic]] — protocol author
- [[Archon]] — wrapped as an MCP server in v3+
- [[PydanticAI]] — first-class MCP integration for sub-agents
- [[Windsurf]], [[Cursor]] — MCP-aware AI IDEs
- [[SubAgent]] — pattern often realized via MCP
- [[ToolUse]] — what MCP standardizes
- [[summary-coding-subagents-mcp-evolution]] — MCP-as-sub-agent thesis
- [[summary-build-an-army-of-ai-agents-archon]] — MCP Agent Army demo
