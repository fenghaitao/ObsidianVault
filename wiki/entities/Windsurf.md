---
title: "Windsurf"
type: entity
tags: [tool, ai-coding-assistant, ai-ide, mcp-client]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/01 - Build an ARMY of AI Agents on Autopilot with Archon, Here's How.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/03 - Coding Subagents - The Next Evolution of AI IDEs.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
last_updated: 2026-06-19
---

## Definition

Windsurf is an AI-powered IDE (a fork-of-VS-Code class [[AICodingAssistant]]) made by Codeium. It's [[ColeMedin]]'s primary demo target throughout the Archon playlist for showing [[ModelContextProtocol]] integration with specialized [[SubAgent]]s.

> **Note on the source transcripts**: YouTube auto-captions consistently transcribe "Windsurf" as "Windswept" or "Wind Surf" or "Win Sur" — these are transcription errors. The actual product name is **Windsurf**.

## Key Information

### Role in the playlist

Cole uses Windsurf as the "primary agent" / orchestrator that calls [[Archon]] as an MCP-wrapped specialized [[SubAgent]] for [[PydanticAI]] / [[LangGraph]] code generation. The pattern:

1. User asks Windsurf to build an AI agent.
2. Windsurf realizes this is framework-specialized work and invokes Archon via the configured MCP server.
3. Archon's internal LangGraph workflow (Reasoner → Coder) returns generated code.
4. Windsurf takes the code and writes the actual files into the workspace.
5. User says "ask Archon to fix X" — Windsurf re-invokes Archon, passing back the same `thread_id` for stateful iteration.

### Notable behaviors observed

- Reads MCP tool docstrings to decide *when* to invoke each tool — Cole demonstrates customizing the Archon tool docstring to nudge Windsurf into using it for PydanticAI/LangGraph requests specifically.
- Default LLM in the demos is **Claude 3.5 Sonnet** (also tested with 3.7).
- Built-in `@DocumentationName` references (e.g. `@PydanticAI`, `@LangGraph`) for inline doc retrieval — Cole argues this is *insufficient* compared to Archon's full agentic flow.
- Hallucination rate on framework-specific code is what motivates the entire Archon project.

### Configuration

Windsurf's MCP server config uses the same JSON shape as Claude Desktop and Cursor — paste in server name, command, args, and env. Archon ships a `setup_mcp.py` script that emits ready-to-paste config.

### Cole's positioning

- **Generalist AI coder.** Strong on broad tasks, weak on framework specifics.
- **MCP client first.** The reason it can be paired with Archon at all.
- **Not a replacement for specialization.** Hence the entire "Coding Subagents" thesis.

## Related

- [[Cursor]] — direct competitor, equivalent role in the playlist
- [[Archon]] — used as Windsurf's specialized PydanticAI sub-agent
- [[ModelContextProtocol]] — integration mechanism
- [[Anthropic]] — provides Claude, Windsurf's default LLM
- [[AICodingAssistant]] — Windsurf's category
- [[SubAgent]] — pattern enabled when Windsurf calls Archon
- [[summary-coding-subagents-mcp-evolution]] — primary demo source
