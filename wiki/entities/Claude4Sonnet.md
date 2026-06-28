---
title: "Claude4Sonnet"
type: entity
tags: [claude, model, anthropic, capable, intelligence]
sources: [raw/01-articles/claude/2025-05-22 - New capabilities for building agents on the Anthropic API.md, raw/01-articles/claude/2025-08-12 - Claude Sonnet 4 now supports 1M tokens of context.md, raw/01-articles/claude/2025-09-24 - Claude is now available in Microsoft 365 Copilot.md]
last_updated: 2026-06-28
---

## Definition

Claude 4 Sonnet (Claude Sonnet 4) is a capable model in the Claude 4 family, balancing intelligence with performance for a wide range of tasks and applications.

## Key Information

- Part of the [[Claude4]] model family announced in May 2025
- Capable model across reasoning, analysis, and agentic tasks
- Supports beta features: [[CodeExecutionTool|code execution]], [[MCPConnector|MCP connector]], [[FilesAPI|Files API]], [[PromptCaching|extended prompt caching]]
- Available on [[Anthropic]] API, [[AmazonBedrock]], and [[VertexAI]]
- Supports **1 million token [[ContextWindow]]** (as of August 2025, public beta) — a 5x increase enabling entire-codebase analysis and large-scale document synthesis

## Capabilities

- Strong reasoning capabilities
- Code execution in sandboxed Python environment
- Automatic MCP server connections for tool integration
- File storage and multi-session document access
- Extended prompt caching (1-hour TTL option)
- Efficient performance for high-throughput applications

## Use Cases

- Data analysis with code execution
- Agent workflows with tool integration
- Long-running applications with extended caching
- Production agent applications balancing capability and cost

## Availability

- [[Anthropic]] API — including Tier 4 and custom rate limits for 1M context (public beta, August 2025)
- [[AmazonBedrock]] — including 1M context support
- [[VertexAI]] — 1M context added August 26, 2025
- [[CopilotStudio]] (via [[Microsoft365Copilot]]) — available as selectable model in Copilot Studio (September 2025)

## Related

- [[Claude4]] — model family
- [[Claude4Opus]] — flagship variant in Claude 4 family
- [[Anthropic]] — creator
- [[CodeExecutionTool]] — capability available on Sonnet 4
- [[MCPConnector]] — capability available on Sonnet 4
- [[FilesAPI]] — capability available on Sonnet 4
- [[PromptCaching]] — capability available on Sonnet 4
- [[AmazonBedrock]] — cloud platform availability
- [[VertexAI]] — cloud platform availability
- [[BoltNew]] — customer using Sonnet 4 for code generation at scale
- [[iGentAI]] — customer using Sonnet 4 for autonomous software engineering (Maestro)
- [[BatchProcessing]] — 50% cost savings when combined with long context
- [[summary-2025-05-22 - New capabilities for building agents on the Anthropic API]] — source article
- [[summary-2025-08-12 - Claude Sonnet 4 now supports 1M tokens of context]] — 1M context window announcement
- [[Microsoft365Copilot]] — enterprise platform where Sonnet 4 is available
- [[CopilotStudio]] — agent-building platform within M365 Copilot
- [[Microsoft]] — enterprise partner
- [[summary-2025-09-24 - Claude is now available in Microsoft 365 Copilot]] — Microsoft 365 Copilot availability announcement
