---
title: "Flatten Arguments"
type: concept
tags: [mcp, tool-design, arguments]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect.md"]
last_updated: 2026-06-26
---

## Definition
Flatten Arguments is an MCP server design principle that recommends using top-level primitive arguments (strings, booleans, enums) instead of complex nested structures (dicts, Pydantic models) to reduce agent confusion and errors.

## Key Information
- Second of Jeremiah Lowin's five MCP best practices
- Complex arguments (configuration dictionaries, nested objects) cause agents to struggle with correct formatting
- Even well-annotated Pydantic models are harder for agents than flat primitives
- Claude Desktop sends all structured object arguments as strings, creating a real compatibility problem
- FastMCP had to implement automatic string-to-object deserialization as a workaround, which Lowin "really hates"
- Best practice: use top-level primitives with clear names (email: str, include_cancelled: bool)
- Strongly recommend Literals or Enums whenever options are constrained -- much better than free-form strings
- Avoid tightly coupled arguments where one argument's value determines valid inputs for another
- Name arguments for the agent, not for developers

## Related
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — source
- [[AgenticProductDesign]] — parent design philosophy
- [[ClaudeDesktop]] — client with structured argument issues
- [[Elicitation]] — alternative approach for complex arguments
