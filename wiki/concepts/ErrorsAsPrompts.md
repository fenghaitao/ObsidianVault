---
title: "Errors as Prompts"
type: concept
tags: [mcp, error-handling, tool-design, progressive-disclosure, agent-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition
Errors as Prompts is the principle that error messages from MCP tools become part of the agent's next prompt, making them an opportunity to document the API and guide recovery rather than just signaling failure. In the broader agent engineering context, this extends to treating all errors as normal inputs to the model — similar to Go's pattern of treating errors as values alongside success values.

## Key Information
- Part of Jeremiah Lowin's "instructions are context" best practice
- LLMs don't distinguish between successful responses and errors -- both are just information about what happened
- Cryptic error messages (empty value errors, integer error codes) give the agent no useful guidance
- Error messages are an opportunity to document the API through failure recovery
- A strategy for complex APIs: instead of documenting every possibility in the docstring, document how to recover from the most common failures in error messages
- This creates a form of progressive disclosure where more information is sent only when needed
- If error messages are too aggressive or scary, the agent may permanently avoid the tool
- "Be as helpful as possible in your error messages. Do go overboard."
- This is a token-budget-saving technique: instructions in error messages don't consume handshake tokens
- **Philipp Schmid's framing**: Errors are just inputs — treat them like Go treats errors (as values alongside success). In long-running agents (5-15 min), restarting from scratch wastes compute and loses context. Feed errors back to the model for recovery

## Related
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — source
- [[summary-20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind]] — source
- [[PhilippSchmid]] — speaker who framed errors as inputs
- [[AgenticProductDesign]] — parent design philosophy
- [[TokenBudget]] — constraint this technique helps address
- [[ProgressiveDisclosure]] — related pattern
- [[Design for Recovery]] — related concept: building agents that recover from failures
- [[DurableAgents]] — related concept: agents that survive failures
