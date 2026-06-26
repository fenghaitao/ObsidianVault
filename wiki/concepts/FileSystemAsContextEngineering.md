---
title: "FileSystemAsContextEngineering"
type: concept
tags: [agents, context-management, file-system, claude-code]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md"]
last_updated: 2026-06-25
---

## Definition
File system as context engineering is the pattern of using the agent's file system to store memory, tool call results, scripts, and state, rather than keeping everything in the conversation context window. It is a core design principle of the Claude Agent SDK.

## Key Information
- The file system is a way of context engineering beyond just the prompt — it includes tools, files, and scripts the agent can use
- Best practice: save tool call results to the file system and have the tool return the file path, enabling the agent to search across results and recheck its work
- Skills are an example: they are just folders of files the agent can CD into and read
- Memory can be implemented as a "memories" folder where the agent writes and retrieves information
- Claude.md files and helper scripts in the working directory are part of the file system context
- The file system stores state between context resets: after clearing context, the agent can look at git diff or file contents to understand what was done
- For non-coding agents: the spreadsheet or data files themselves store state, reducing the need to keep everything in conversation history
- Contrasts with traditional chatbot architecture where all state must be in the conversation

## Related
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[BashTool]] — the mechanism for file system operations
- [[ProgressiveContextDisclosure]] — skills as a file system pattern
- [[ContextManagement]] — broader context management strategies
