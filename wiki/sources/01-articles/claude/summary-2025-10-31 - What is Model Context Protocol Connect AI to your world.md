---
title: "summary-2025-10-31 - What is Model Context Protocol Connect AI to your world"
type: source
tags: [source, mcp, model-context-protocol, connectors]
sources: ["raw/01-articles/claude/2025-10-31 - What is Model Context Protocol Connect AI to your world.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic's explainer on the Model Context Protocol (MCP): an open standard, likened to "USB-C for LLMs," that replaces bespoke per-application integrations with one universal connector format. MCP was created at Anthropic by David Soria Parra and Justin Spahr-Summers, modeled on the Language Server Protocol, and open-sourced in November 2024. It works through a two-sided client/server model — AI apps build MCP Clients, tool providers build MCP Servers — solving the M×N integration problem.

## Key Points

- **Origin**: David Soria Parra's frustration with constantly copying code between Claude Desktop and his IDE led him to pitch Justin Spahr-Summers on a protocol solving the classic M×N (M applications × N tools) integration problem.
- **Client/Server model**: AI agents/chatbots implement MCP Clients to connect to any MCP Server; companies implement a single MCP Server to become instantly compatible with every MCP-supporting AI assistant, rather than building N custom integrations.
- **Claude Connectors**: Claude's user-facing name for pre-built MCP Servers (Canva, Notion, Linear, Figma, and others), each taking seconds to configure. An open-source MCP Registry hosts community-built servers beyond Claude's own directory.
- Positions MCP as foundational infrastructure for end-to-end agentic task automation — letting agents read an email thread and reply, access a codebase and deploy an update, or review a design brief and generate a first draft, without custom per-tool integration code.

## Related

- [[ModelContextProtocol]] — the protocol this article explains in depth, including its origin story
- [[Claude.ai]] — surfaces MCP servers to end users as Connectors
- [[Notion]] — example Connector cited
- [[Figma]] — example Connector cited
- [[Linear]] — example Connector cited
