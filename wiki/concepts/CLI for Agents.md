---
title: "CLI For Agents"
type: concept
tags: [agents, cli, mcp, token-efficiency, tool-design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google.md"]
last_updated: 2026-06-30
---

## Definition
CLI For Agents is the technique of offering a command-line interface alongside an MCP server, enabling agents to chain commands together for post-processing. This saves tokens because the model doesn't need to process intermediate results — token post-processing happens on the local machine.

## Key Information
- Third of three token burn reduction angles in Chrome DevTools MCP
- Chrome DevTools MCP offers both an MCP server and a CLI interface with nearly the same functionality
- Enables command chaining: e.g., extract accessibility tree with grep, pipe the ID into a click command
- Key benefit: token savings — the model doesn't need to process intermediate data between commands
- Token post-processing happens on the user's computer, not in the model's context
- Contrasts with pure MCP approach where every tool call round-trips through the model
- Complements [[Slim Mode]] and [[Tool Categorization]]

## Related
- [[summary-20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google]] — source
- [[Slim Mode]] — complementary technique
- [[Tool Categorization]] — complementary technique
- [[Tokens Per Successful Outcome]] — metric this optimizes for
- [[Chrome DevTools MCP]] — implementation
- [[BashTool]] — related pattern of using shell commands as agent tools
