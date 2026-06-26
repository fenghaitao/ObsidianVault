---
title: "ToolCalling"
type: concept
tags: [llm, agent-architecture, function-calling, coding-agents, mcp]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240805 - What's new from Anthropic and what's next： Alex Albert.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20240724 - From Software Developer to AI Engineer： Antje Barth.md"]
last_updated: 2026-06-26
---

## Definition
Tool calling is the LLM capability that enables models to output structured function calls (JSON) as part of their response, allowing agents to interact with external systems. It is the fundamental abstraction that makes the master while-loop architecture possible, replacing earlier approaches like JSON formatters and regex-based parsing. Tools are essentially callable functions wrapped with descriptions that guide agents on when and how to use them.

## Key Information
- **Anthropic Tool Use API**: Gives Claude custom client-side functions it can intelligently leverage. Combined with Claude 3.5 Sonnet, enables consistent structured JSON output. Developers give Claude hundreds of tools at a time
- Tool calls have not always existed — they are a relatively new abstraction for structured JSON output from LLMs
- Replaced earlier approaches like GitHub's JSON former library and regex-based parsing
- Models are increasingly being trained specifically to get better at tool calling
- Anthropic's models are described as "very optimized tool calling models"
- The tool call structure for sub-agents (Tasks) includes a description (user-visible) and a prompt (long string the agent fills with instructions)
- Jared Zoneraich recommends making tool calls rigorous and testable, treating them like functions with inputs and outputs
- Two schools of thought: one master loop with hundreds of tool calls vs. minimal tool calls (mostly just bash)
- Zoneraich leans toward fewer tool calls, with bash as the universal adapter
- Tool descriptions are injected into the system prompt to guide model behavior
- **Third-party tool optimization**: Generic third-party tools often need curation (filtering irrelevant tools), wrapping (enhanced descriptions), deterministic guardrails, composition (new tools from existing ones), and deterministic usage outside the agent loop to work effectively for specific use cases.
- **Description importance**: Tool descriptions are critical because they let agents know when to use the code and how to use it. Generic descriptions from third-party MCP servers are often too shallow for specific applications.

## Related
- [[summary-20240805 - What's new from Anthropic and what's next： Alex Albert]] — source for Anthropic Tool Use API
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — source
- [[summary-20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz]] — source (tool optimization)
- [[MasterWhileLoop]] — the architecture enabled by tool calling
- [[BashAsUniversalAdapter]] — the argument for minimizing tool calls
- [[DAGvsLoopArchitecture]] — related design trade-off
- [[ThirdPartyToolOptimization]] — framework for optimizing tool descriptions and behavior
- [[MCP]] — protocol for tool integration
- [[summary-20240724 - From Software Developer to AI Engineer： Antje Barth]] — source (Bedrock Converse API function/tool calling)
- [[Converse API]] — Bedrock API with built-in function calling support
