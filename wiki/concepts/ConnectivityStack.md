---
title: "Connectivity Stack"
type: concept
tags: [agents, architecture, mcp, skills, computer-use]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - The Future of MCP — David Soria Parra, Anthropic.md"]
last_updated: 2026-06-26
---

## Definition
The Connectivity Stack is a framework for agent connectivity that combines three distinct tools — Skills, MCP, and CLI/Computer Use — each suited to different scenarios. There is no single solution to all connectivity problems; the right tool depends on the use case.

## Key Information
- **Skills**: Domain knowledge captured in simple files, mostly reusable. Minor differences between platforms. Best for capturing specific capabilities.
- **MCP**: Rich semantics, UI for long-running tasks, resources, full decoupling, platform independence, authorization, governance, policies, enterprise features. Best when you need rich semantics, don't have a sandbox, or need enterprise-grade infrastructure. Also enables experiments like MCP applications and skills over MCP.
- **CLI/Computer Use**: Great for local coding agents with sandboxes. Models can automatically discover CLI capabilities. Particularly good when the tool is already in pre-training data (git, GitHub). Best when you have a local agent with a sandbox and code execution environment.
- David Soria Parra: "If someone tells you there's one solution to all your connectivity problem, be it computer use, be it CLIs, be it MCP, they are probably pretty wrong"
- 2026 vision: agents will use all three seamlessly together, not just one
- The stack reflects that different connectivity needs require different approaches — a REST API wrapper is not always the right answer

## Related
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — source
- [[MCP]] — one pillar of the stack
- [[Skills]] — one pillar of the stack
- [[Computer Use]] — one pillar of the stack (CLI/Computer Use)
- [[BashAsUniversalAdapter]] — CLI as universal connectivity
- [[DavidSoriaParra]] — presenter
