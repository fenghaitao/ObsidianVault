---
title: "Claude4"
type: entity
tags: [claude, model-family, anthropic, frontier]
sources: [raw/01-articles/claude/2025-05-22 - New capabilities for building agents on the Anthropic API.md]
last_updated: 2026-06-28
---

## Definition

Claude 4 is a model family from [[Anthropic]] announced in May 2025, representing a new generation of frontier models with advanced capabilities for agentic workflows and complex reasoning.

## Key Information

- Announced May 2025
- Available on [[Anthropic]] API with beta agentic features
- Family includes: [[Claude4Opus]] (flagship) and [[Claude4Sonnet]] (capable variant)
- Supports new agentic capabilities: [[CodeExecutionTool|code execution]], [[MCPConnector|MCP connector]], [[FilesAPI|Files API]], [[PromptCaching|extended prompt caching]]

## Family Members

- **[[Claude4Opus]]** — Flagship model with advanced reasoning
- **[[Claude4Sonnet]]** — Capable variant balancing intelligence and performance

## New Capabilities

The Claude 4 family is the first to support these beta features on the [[Anthropic]] API:

1. **[[CodeExecutionTool|Code Execution Tool]]** — Python code execution in sandboxed environment for data analysis and computational tasks
2. **[[MCPConnector|MCP Connector]]** — Automatic Model Context Protocol server management for tool integration
3. **[[FilesAPI|Files API]]** — Upload-once, reuse-across-sessions document storage
4. **[[PromptCaching|Extended Prompt Caching]]** — 1-hour TTL caching (12x improvement over standard 5-minute) for cost/latency reduction

## Use Cases

- Complex agentic workflows with multiple tool integration
- Data analysis and scientific computing
- Multi-session document processing
- Long-running applications with cost optimization

## Availability

- [[Anthropic]] API (May 2025+)

## Related

- [[Claude4Opus]] — flagship Claude 4 model
- [[Claude4Sonnet]] — Claude 4 capable variant
- [[Anthropic]] — creator
- [[CodeExecutionTool]] — Python execution capability
- [[MCPConnector]] — MCP integration capability
- [[FilesAPI]] — document storage capability
- [[PromptCaching]] — extended caching capability
- [[AIAgent]] — agent architecture utilizing Claude 4 capabilities
- [[summary-2025-05-22 - New capabilities for building agents on the Anthropic API]] — announcement article
