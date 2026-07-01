---
title: "Elicitation"
type: concept
tags: [mcp, protocol, interaction, approvals]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - The Future of MCP — David Soria Parra, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora.md"]
last_updated: 2026-06-26
---

## Definition
Elicitation is an MCP protocol feature that allows a tool to request additional structured input from the client mid-execution, enabling approvals, confirmations, and progressive disclosure of complex arguments.

## Key Information
- Formal MCP request where a tool says "I need more information" during execution
- Structured: the tool specifies what input it needs (e.g., yes/no approval, form fields)
- Most common use case: approvals for irreversible side effects
- Can be used for confirmations on destructive tools (with default=false, forcing the LLM to acknowledge)
- Could be used to handle tightly coupled arguments by eliciting them progressively
- Limited client support is the main barrier to adoption
- Reason for limited support: handling elicitation is complex -- user-facing clients can show forms, but automated/backgrounded clients have no clear way to respond
- Lowin: "I wish it were used more so I could say yes and you should depend on it"

## Related
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — source
- [[MCP]] — protocol that defines elicitation
- [[FlattenArguments]] — alternative approach when elicitation isn't available
- [[AgenticProductDesign]] — design philosophy
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — source (elicitation as underused MCP primitive)
- [[DavidSoriaParra]] — called out elicitation as an underused MCP capability
- [[summary-20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora]] — source (elicitation as control mechanism in agent-human collaboration)
- [[Decision Log]] — non-blocking elicitation pattern: agents make decisions and log them for later human review
- [[AgentHuman Collaboration]] — framework where elicitation increases control
- [[JacobLauritzen]] — presented elicitation as a way to increase control in agent-human collaboration
