---
title: "Human-in-the-Loop Automation with n8n — Liam McGarrigle"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle.md"
date: 2026-05-02
ingested: 2026-06-29
tags: [workshop, n8n, human-in-the-loop, automation, agent, gmail, google-calendar, openrouter, mcp]
---

## Core Thesis
Liam McGarrigle (Developer Advocate at n8n) leads a hands-on workshop building a Gmail and calendar management agent in n8n with human-in-the-loop review steps. The session demonstrates how n8n's visual workflow builder, AI agent node, tool system, and human review nodes combine to create controllable, observable AI agents where destructive actions (send email, create calendar event, reply) are intercepted for human approval before execution.

## Key Topics
- **n8n Platform Overview**: n8n started in 2019 as a low-code workflow integration tool (pre-ChatGPT). It is a visual, node-based builder where every workflow starts with a trigger (schedule, webhook, form, chat) and chains actions. Control flow (if/else, conditions) enables complex routing. Expressions use JavaScript inside curly braces for dynamic values.
- **AI Agent Node**: A special node type with "legs" on the bottom instead of sides. Requires a chat model (LLM) connected to it. Supports any LLM provider — if not in the list, use the OpenAI model node with a custom base URL. The workshop uses OpenRouter for multi-model access with a shared API key.
- **Agent Memory**: The agent has no memory by default. n8n provides a "Simple Memory" option (stores messages in n8n, configurable context window length) or external options like Postgres/Redis for integration with existing systems. Memory works via a session ID passed from the chat trigger.
- **Tools as Agent Capabilities**: Every regular n8n node (Gmail, Google Calendar, etc.) can be converted into a tool node (circle shape) that the AI agent can call at its discretion. The AI fills in tool parameters automatically via the "From AI" expression.
- **Fine-Grained Tool Permissions**: Unlike other platforms where the AI gets full API access, n8n tools expose individual fields. The agent can only set fields you explicitly configure. You can mix "From AI" values with hardcoded static text and references to other fields (e.g., chat input).
- **Tool Prompting and Descriptions**: Node names become tool names; node descriptions become tool descriptions passed to the LLM. Liam recommends writing full prompts in tool descriptions instead of the system prompt for modularity. Field-level descriptions can be added to guide the AI on specific parameters (e.g., "summary" in Google Calendar is actually the event title).
- **System Prompt Design**: Keep system prompts simple and add instructions as needed. Include behavioral rules (ask instead of hallucinate), time awareness (use the `now` convenience function since LLMs don't know the current time), and warnings about placeholder values.
- **Human-in-the-Loop Review Node**: Placed on a tool's output branch, this node intercepts tool calls before execution. The workflow cannot proceed past this node without human approval. Works with chat platforms (native n8n chat, Slack). Supports custom approve/deny buttons, custom messages showing tool parameters, and deny-by-response (typing anything denies).
- **Response Mode Configuration**: Chat trigger must be set to "using respond nodes" (not streaming) for human review to work. A "Send Message" chat node must be added after the agent to return responses.
- **Execution Observability**: The Executions tab shows all workflow runs with detailed logs per node. Test executions are marked with a flask icon. "Copy to editor" lets you work with real execution data for debugging and refinement.
- **JavaScript Expressions for Formatting**: n8n uses Luxon date library. Expressions like `{{ $json.date.toDateTime().format('DDDD TT') }}` format timestamps into human-readable dates. Built-in docs show function signatures and examples.
- **n8n AI Builder**: On cloud/enterprise plans, an AI assistant can add nodes (e.g., "add human in the loop just like it is on send an email") and configure them automatically.
- **Native MCP Server**: n8n has a built-in MCP server (Settings → Instance Level MCP). Can expose published workflows as MCP tools. Supports OAuth and access token authentication. Unlike community MCP servers, n8n's can also execute workflows (send chat messages to running workflows). Per-workflow access control.
- **Scaling with Sub-Agents**: For adding many tools, Liam recommends using the sub-agent tool pattern — one main agent that calls specialized sub-agents (calendar/email agent, GitHub issues agent, Jira agent). Each sub-agent can use a different LLM optimized for its domain, reducing context bloat in the main agent.
- **Slack Integration**: The chat trigger can be replaced with Slack triggers. Human review messages route through Slack with approve/deny buttons. A loading indicator can be added via a Slack node with a GIF.
- **Autonomous Background Agents**: By adding a schedule trigger alongside the chat trigger, the agent can run autonomously (e.g., hourly inbox clearing) while still routing destructive actions through human review in Slack.
- **REST API Creation**: n8n workflows can be exposed as REST APIs via webhook triggers with RESTful path naming. Liam built n8n's entire coupon generation system as a REST API in n8n in ~6 hours.
- **Enterprise Features**: Projects for credential isolation and access control. Git integration and environments (dev/staging/prod) for workflow versioning. Collaborative editing with auto-save and live updates.

## Entities
- [[n8n]] — visual workflow automation platform, founded 2019
- [[Liam McGarrigle]] — Developer Advocate at n8n, workshop presenter
- [[OpenRouter]] — API gateway for multi-model LLM access, used in workshop
- [[Gmail]] — Google email service, used as agent tool
- [[Google Calendar]] — Google calendar service, used as agent tool
- [[Slack]] — messaging platform, integration target for agent
- [[Notion]] — documentation platform, workshop materials hosted here
- [[Anthropic]] — provider of Claude/Sonnet models used via OpenRouter
- [[ClaudeCode]] — referenced for MCP integration comparison
- [[Google]] — OAuth provider for Gmail and Calendar connections
- [[Postgres]] — database option for agent memory
- [[Microsoft Teams]] — mentioned as alternative to Slack
- [[Salesforce]] — mentioned as integration example
- [[GitHub]] — mentioned for issues/PR agent use case
- [[Jira]] — mentioned as potential sub-agent domain

## Concepts
- [[HumanInTheLoopWorkflows]] — n8n's human review node implementation
- [[Fine-Grained Tool Permissions]] — exposing individual fields to AI instead of full API access
- [[Visual Automation]] — low-code visual workflow building
- [[AgentMemory]] — simple memory vs Postgres/Redis for conversation persistence
- [[ToolCalling]] — AI agent using nodes as tools with descriptions
- [[Sub-agent Orchestration]] — main agent delegating to specialized sub-agents
- [[AgentObservability]] — execution logs, per-node input/output inspection
- [[MCP]] — n8n's native MCP server for exposing workflows as tools
- [[SystemPromptFeedbackLoop]] — iterative prompt refinement based on tool behavior
- [[AgenticLoop]] — chat trigger → AI agent → tools → human review pattern
- [[WorkflowPattern]] — n8n's trigger → action → control flow architecture
- [[DAGvsLoopArchitecture]] — n8n's DAG-based workflow vs agentic loop
- [[Autonomy Slider]] — human review as a spectrum from full auto to full manual
- [[Agent-Human Collaboration]] — human review as interception layer
- [[AgenticWorkflows]] — combining deterministic workflows with AI agents
- [[Slack Bot Integration]] — connecting agents to Slack for human review
- [[REST API for Agents]] — exposing agent workflows as webhook APIs
- [[DeterministicGuardrails]] — human review as a hard block, not LLM-decided
- [[Context Budget]] — sub-agents reduce context bloat in main agent
- [[AgentSpecialization]] — different LLMs for different sub-agent domains

## Related
- [[summary-20260106 - Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel]] — human-in-the-loop via webhooks
- [[summary-20260415 - Paperclip： Open Source Human Control Plane for AI Labor — Dotta Bippa]] — human review gates
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — MCP ecosystem and roadmap
- [[summary-20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora]] — agent-human collaboration
