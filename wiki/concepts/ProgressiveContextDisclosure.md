---
title: "ProgressiveContextDisclosure"
type: concept
tags: [agents, context-management, skills, bash]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro.md"]
last_updated: 2026-06-26
---

## Definition
Progressive context disclosure is a pattern where an agent discovers capabilities incrementally rather than having all tool definitions loaded into context at once. Skills (folders of files the agent CDs into and reads) and CLI tools with `--help` flags are examples of this pattern.

## Key Information
- Skills are a form of progressive context disclosure: when the agent needs to perform a task (e.g., create a docx file), it CDs into the skill directory, reads the instructions, and proceeds
- CLI scripts designed with `--help` flags let the agent discover sub-commands progressively, reducing context usage compared to loading all tool definitions
- This pattern trades some latency (discovery time) for lower context usage and greater flexibility
- Skills are "just really folders that your agent can CD into and read" — they are file-system-native
- Contrasts with traditional tool calling where all tool definitions are loaded into the system prompt, consuming context even for unused tools
- Related to the broader principle that the file system is a context engineering tool
- **Kiro context**: Al Harris describes this as "incremental disclosure" — a pattern heard frequently at the AI Engineer conference. Kiro applies this by giving agents tools to find context rather than loading everything upfront. Based on benchmarks showing agents perform better with less initial context but with discovery tools.

## Related
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — source
- [[BashTool]] — the mechanism for CD and --help discovery
- [[FileSystemAsContextEngineering]] — the broader pattern
- [[ToolsVsBashVsCodeGen]] — context usage trade-offs
- [[summary-20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro]] — source
- [[IncrementalDisclosure]] — closely related concept from Kiro
- [[AmazonKiro]] — IDE applying this pattern
