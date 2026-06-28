---
title: "New capabilities for building agents on the Anthropic API"
type: source
tags: [anthropic, api, agents, code-execution, mcp, files, caching]
sources: [raw/01-articles/claude/2025-05-22 - New capabilities for building agents on the Anthropic API.md]
last_updated: 2026-06-28
---

# New capabilities for building agents on the Anthropic API

**Source:** Anthropic Blog (May 22, 2025)

## Summary

Anthropic announced four new beta capabilities for the [[Anthropic]] API that enable developers to build more powerful AI agents:

1. **[[CodeExecutionTool|Code execution tool]]** — Claude can now execute Python code in a sandboxed environment for data analysis, visualization, and computational tasks.

2. **[[MCPConnector|MCP connector]]** — The API now handles all Model Context Protocol server connections automatically without requiring custom client code. Developers can connect to remote MCP servers from [[Zapier]] and [[Asana]].

3. **[[FilesAPI|Files API]]** — Developers can upload documents once and reference them repeatedly across conversations, streamlining document storage and access workflows.

4. **[[PromptCaching|Extended prompt caching]]** — A new 1-hour time-to-live (TTL) option (vs. standard 5-minute) for caching, enabling cost reductions up to 90% and latency reductions up to 85% for long-running agent workflows.

## Key Use Case Example

A project management AI agent powered by [[Claude4Sonnet|Claude Sonnet 4]] and [[Claude4Opus|Claude Opus 4]] can:
- Use the MCP connector with Asana to reference tasks and assign work
- Upload relevant reports via the Files API
- Analyze progress and risks with the code execution tool
- Maintain full context throughout with extended prompt caching

## Code Execution Tool

- **Language:** Python (sandboxed environment)
- **Capabilities:** Load datasets, generate exploratory charts, identify patterns, iteratively refine outputs
- **Use cases:** Financial modeling, scientific computing, business intelligence, document processing, statistical analysis
- **Pricing:** 50 free hours per day, then $0.05/hour per container

## Files API

- Simplifies multi-session document workflows
- Integrates with code execution tool for direct file access and output generation
- Enables upload-once, reuse-across-sessions workflows

## Extended Prompt Caching

- Developers can opt for 1-hour TTL at additional cost (12x improvement over 5-minute standard)
- Up to 90% cost reduction for long prompts
- Up to 85% latency reduction for long-running applications
- Makes long-running agents practical at scale

## Related

- [[Anthropic]] — API provider
- [[AIAgent]] — broader agent architecture
- [[CodeExecutionTool]] — Python code execution capability
- [[MCPConnector]] — automatic MCP server management
- [[FilesAPI]] — document storage and reuse
- [[PromptCaching]] — extended TTL caching for context
- [[ToolUse]] — related capability for agent interactions
- [[Claude4Sonnet]] — featured model
- [[Claude4Opus]] — featured model
- [[Asana]] — remote MCP server example
- [[Zapier]] — remote MCP server example
