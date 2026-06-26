---
title: "Outcomes Over Operations"
type: concept
tags: [mcp, design-pattern, tool-design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect.md"]
last_updated: 2026-06-26
---

## Definition
Outcomes Over Operations is an MCP server design principle advocating that tools should represent complete agent workflows (outcomes) rather than individual API calls (operations), avoiding the anti-pattern of using LLMs as orchestrators.

## Key Information
- First of Jeremiah Lowin's five MCP best practices
- The trap: exposing atomic REST API operations as individual tools (e.g., getUser, getOrders, checkStatus as separate tools)
- The fix: compose multiple API calls into a single outcome-oriented tool (e.g., "track latest order by email")
- "Agent as glue" or "agent as orchestrator" is an anti-pattern -- agents can orchestrate but it's expensive, slow, hard to debug, and stochastic
- LLMs should only be used as orchestrators when the algorithm is genuinely unknown and non-programmatic
- Finding an order status is a "really bad time" to use an LLM as an orchestration service
- One tool should equal one agent story -- a complete task a programmatic autonomous agent is trying to achieve
- Name tools for the agent, not for developers: use descriptive, outcome-oriented names even if they feel "silly"
- Block's playbook reinforces this: "designed top down from the workflow, not bottom up from the API endpoints"

## Related
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — source
- [[AgenticProductDesign]] — parent design philosophy
- [[AgentStory]] — related concept for framing tool scope
- [[CurateRuthlessly]] — complementary principle
