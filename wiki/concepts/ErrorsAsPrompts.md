---
title: "Errors as Prompts"
type: concept
tags: [mcp, error-handling, tool-design, progressive-disclosure]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect.md"]
last_updated: 2026-06-26
---

## Definition
Errors as Prompts is the principle that error messages from MCP tools become part of the agent's next prompt, making them an opportunity to document the API and guide recovery rather than just signaling failure.

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

## Related
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — source
- [[AgenticProductDesign]] — parent design philosophy
- [[TokenBudget]] — constraint this technique helps address
- [[ProgressiveDisclosure]] — related pattern
