---
title: "Visual Automation"
type: concept
tags: [automation, low-code, workflow, n8n, agent-building]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle.md"]
last_updated: 2026-06-29
---

## Definition
Visual automation is a low-code approach to building workflows and AI agents using a visual, node-based canvas instead of writing code. Platforms like n8n provide drag-and-drop nodes for triggers, actions, control flow, and AI agent orchestration, with the ability to break out into code (JavaScript expressions) wherever needed.

## Key Information

- **Node-Based Architecture**: Workflows are built by connecting nodes on a canvas. Every workflow starts with a trigger node (schedule, webhook, form, chat, Slack message) and chains action nodes with optional control flow (if/else, conditions)
- **AI Agent Nodes**: Special node types with tool "legs" that connect LLMs to tool nodes the agent can call at its discretion
- **Tool Conversion**: Regular integration nodes (Gmail, Google Calendar, Salesforce) can be converted into tool nodes (circle shape) for AI agent use
- **Human-in-the-Loop**: Visual review nodes can be placed on tool output branches to intercept execution before it happens
- **Expressions**: JavaScript inside curly braces (`{{ }}`) enables dynamic values, date formatting (Luxon), and field references without writing full code nodes
- **Code Escape Hatch**: Full JavaScript code nodes are available when visual configuration isn't enough. Even individual fields support inline JavaScript expressions
- **Copy-Paste**: Workflows can be exported as JSON and shared, enabling rapid iteration and workshop distribution
- **Observability**: The Executions tab shows every workflow run with per-node input/output inspection. Test executions are marked separately

## Related

- [[n8n]] — primary platform exemplifying visual automation
- [[WorkflowPattern]] — the architectural pattern underlying visual automation
- [[summary-20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle]] — source
- [[DAGvsLoopArchitecture]] — visual DAG-based workflows vs agentic loops
- [[AgenticWorkflows]] — combining visual workflows with AI agents
- [[HumanInTheLoopWorkflows]] — human review in visual workflows
