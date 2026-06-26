---
title: "Progressive Discovery"
type: concept
tags: [mcp, context, tool-calling, optimization, client]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260419 - The Future of MCP — David Soria Parra, Anthropic.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora.md"]
last_updated: 2026-06-26
---

## Definition
Progressive Discovery is a client-side pattern for MCP where tools are loaded on demand rather than all at once into the context window. The model uses a tool search or tool loading mechanism to discover and load tools only when needed, dramatically reducing context usage.

## Key Information
- Contrasts with the common early approach of dumping all tools into the context window and being surprised by context bloat
- The protocol puts information across the wire, but the client is responsible for dealing with that information
- Implementation approaches: (1) Use tool search (available in the Anthropic API and competitors' APIs) to defer loading; (2) Build a tool loading tool yourself — give the model a tool that loads other tools, and the model decides when to look up what it needs
- Demonstrated in Claude Code: before adding progressive discovery, tool context usage was high; after, there was a "massive reduction in tool context usage"
- Related to but distinct from Progressive Disclosure (which is a server-side pattern for revealing tool details incrementally)
- David Soria Parra called this "the number one thing we need to go and start building" on the client/agent harness side

## Related
- [[summary-20260419 - The Future of MCP — David Soria Parra, Anthropic]] — source
- [[MCP]] — protocol
- [[ProgressiveDisclosure]] — related server-side pattern
- [[ToolSearch]] — implementation mechanism
- [[ProgrammaticToolCalling]] — companion client-side pattern
- [[ContextExhaustion]] — problem this pattern solves
- [[ClaudeCode]] — demonstrated the benefits
- [[summary-20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora]] — source (skills as a form of progressive discovery: skills encode human judgment into work nodes and handle contingencies discovered during execution)
- [[Skills]] — skills enable progressive discovery by encoding knowledge that activates when specific conditions are encountered during work
- [[Agent-Human Collaboration]] — progressive discovery through skills increases control by handling contingencies without requiring upfront planning
