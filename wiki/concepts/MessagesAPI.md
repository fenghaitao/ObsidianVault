---
title: "MessagesAPI"
type: concept
tags: [api, messages, anthropic-api, tool-use]
sources: [raw/01-articles/claude/2025-05-07 - Introducing web search on the Anthropic API.md]
last_updated: 2026-06-28
---

# MessagesAPI

Anthropic's primary API endpoint for sending messages to Claude models and receiving responses, with support for tool use and real-time capabilities.

## Overview

The Messages API is the core endpoint through which developers interact with Claude models. It supports various features including [[ToolUse|tool use]], [[WebSearch]], and other capabilities that enable developers to build sophisticated AI applications.

## Capabilities

The Messages API supports:

- **Basic Chat**: Standard message-based conversations with Claude
- **Tool Use**: Ability to call external APIs and tools (see [[ToolUse]])
- **Web Search**: Real-time internet search with citations (see [[WebSearch]])
- **Vision**: Image analysis and understanding
- **Extended Thinking**: Step-by-step reasoning with visible token budgets
- **Streaming**: Real-time streaming of responses
- **Batch Processing**: Asynchronous processing of multiple requests (see [[MessageBatchesAPI]])

## Web Search Integration

[[WebSearch]] is available on the Messages API for supported models. Developers can:

1. Enable the web search tool in their API requests
2. Control search behavior via the `max_uses` parameter
3. Receive responses with citations to source materials

## Supported Models

The Messages API is available for all Claude models including:
- [[Claude3.7Sonnet]]
- [[Claude3.5Sonnet]]
- [[Claude3.5Haiku]]
- [[Claude3Opus]]
- And other Claude variants

## Developer Documentation

Developers can explore the Messages API documentation and pricing to learn more about available features and how to integrate them into their applications.

## Related

- [[WebSearch]] — Web search capability available through Messages API
- [[ToolUse]] — Tool use capability for API integration
- [[MessageBatchesAPI]] — Batch processing variant
- [[Anthropic]] — Organization providing the Messages API
- [[summary-2025-05-07 - Introducing web search on the Anthropic API]] — Source announcement
- [[Citations]] — Citation capability for web-sourced responses
