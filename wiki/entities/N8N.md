---
title: "n8n"
type: entity
category: platform
tags: [platform, automation, low-code, workflow, agent-orchestration, open-source]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle.md"]
last_updated: 2026-06-29
---

## Definition
n8n is a visual, low-code workflow automation platform founded in 2019. Originally an integration/workflow tool (pre-ChatGPT), it has evolved into an AI agent builder and orchestrator with built-in human-in-the-loop review, tool-based agent capabilities, and a native MCP server.

## Key Information

- **Founded**: 2019, before ChatGPT and the AI agent boom
- **Core Paradigm**: Visual, node-based workflow builder. Every workflow starts with a trigger (schedule, webhook, form, chat, Slack message) and chains actions (API calls, Google services, Salesforce, etc.) with control flow (if/else, conditions)
- **AI Agent Node**: A special node type that connects a chat model (LLM) to tools. The agent can call any n8n node converted into a tool at its discretion
- **Tool System**: Any regular n8n node can be converted into a tool (circle shape) that the AI agent uses. Tools expose individual fields — the agent can only set fields you explicitly configure, providing fine-grained permission control
- **Human-in-the-Loop Review**: A node placed on a tool's output branch that intercepts tool calls before execution. The workflow cannot proceed past this node without human approval via chat (n8n chat, Slack). Supports custom approve/deny buttons, custom messages, and deny-by-response
- **Agent Memory**: Built-in "Simple Memory" (stores messages in n8n with configurable context window) or external options (Postgres, Redis) for integration with existing systems
- **Expressions**: JavaScript inside curly braces (`{{ }}`) for dynamic values. Uses Luxon date library. Supports convenience functions like `now` for current date/time
- **LLM Flexibility**: Can connect any LLM provider. If not in the list, use the OpenAI model node with a custom base URL. OpenRouter is commonly used for multi-model access
- **Native MCP Server**: Built-in MCP server (Settings → Instance Level MCP) that exposes published workflows as MCP tools. Supports OAuth and access token authentication. Can execute workflows (not just read/create). Per-workflow access control
- **AI Builder**: On cloud/enterprise plans, an AI assistant can add and configure nodes automatically
- **Enterprise Features**: Projects for credential isolation and access control. Git integration and environments (dev/staging/prod). Collaborative editing with auto-save and live updates
- **REST API Creation**: Workflows can be exposed as REST APIs via webhook triggers with RESTful path naming. Liam built n8n's coupon generation system as a REST API in ~6 hours
- **Sub-Agent Pattern**: Main agent delegates to specialized sub-agents (calendar/email, GitHub issues, Jira), each with different LLMs optimized for their domain
- **Plans**: Cloud (free trial, Pro), Enterprise, Self-hosted

## Related

- [[Liam McGarrigle]] — Developer Advocate at n8n
- [[summary-20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle]] — workshop source
- [[HumanInTheLoopWorkflows]] — n8n's human review node implementation
- [[FineGrained Tool Permissions]] — n8n's field-level tool access control
- [[MCP]] — n8n's native MCP server
- [[OpenRouter]] — LLM gateway used in n8n workshops
- [[Gmail]] — integration target
- [[Google Calendar]] — integration target
- [[Slack]] — chat integration target
- [[WorkflowPattern]] — n8n's trigger → action → control flow architecture
- [[SubAgent Orchestration]] — pattern for scaling agents with specialized sub-agents
