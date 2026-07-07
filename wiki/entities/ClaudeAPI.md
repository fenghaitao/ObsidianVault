---
title: "ClaudeAPI"
type: entity
tags: [api, claude, anthropic, developer-platform, infrastructure]
sources: []
last_updated: 2026-07-07
---

## Definition

The Claude API is Anthropic's developer-facing API that provides programmatic access to Claude models, enabling developers to build applications powered by Claude's language and reasoning capabilities. It is the foundational interface through which all Claude-powered products and custom applications interact with the model.

## Key Information

- Powers custom applications such as CLAFTS (Jared Sires' Gmail-integrated email drafting tool), which uses the Claude API to generate customer email replies in a specific voice, saving 10-15 hours per week.
- Supports a rich set of features including [[PromptCaching|prompt caching]] (up to 90% cost reduction), [[ToolUse|tool use]], [[CodeExecutionTool|code execution]], [[MCPConnector|MCP connectors]], [[FilesAPI|Files API]], [[Citations|citations]], and [[StructuredOutputs|structured outputs]].
- Year-over-year API volume on the [[Anthropic]] platform is up nearly 17x.
- Available directly through the Anthropic API, as well as via [[AmazonBedrock|Amazon Bedrock]] (AWS), [[VertexAI|Vertex AI]] (Google Cloud), and [[MicrosoftFoundry|Microsoft Foundry]].
- The API's native context compaction feature incorporates cache-safe forking patterns pioneered by [[ClaudeCode]]'s harness, preserving cached prefixes during summarization.
- Underpins [[ClaudeCode]], [[ClaudeCowork]], and [[ClaudeManagedAgents]] as the model interface layer.
- The `claude-api` skill encodes expertise for writing production-ready Claude API code and has been bundled into partner developer tools including [[CodeRabbit]], [[JetBrains]], [[ResolveAI|Resolve AI]], and [[Warp]].

## Related

- [[Anthropic]] — the company that provides and operates the Claude API
- [[ClaudeCode]] — built on the Claude API; its prompt caching engineering lessons were incorporated into the API
- [[PromptCaching]] — key API feature for cost and latency reduction
- [[TokenOptimization]] — strategies for efficient API usage
- [[ToolUse]] — API capability for calling external tools and APIs
- [[AnthropicConsole]] — developer console for building with the API
- [[MessagesAPI]] — core API endpoint for message-based interactions
- [[AIAcceleratedSalesWorkflows]] — CLAFTS application powered by the Claude API
- [[summary-2025-06-23 - Introducing Citations on the Anthropic API]] — source summary
