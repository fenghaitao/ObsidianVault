---
title: "WebMCP"
type: entity
tags: [protocol, web, mcp, agents, browser-automation, browser, declarative, imperative]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260523 - Introducing WebMCP： Agents in the Browser — RL Nabors.md"]
last_updated: 2026-06-30
---

## Definition
WebMCP is a protocol that turns every HTML page into a mini MCP tools server, allowing browser-based AI agents to call JavaScript functions and navigate pages directly rather than relying on screenshots or DOM traversal. It comes in two flavors: declarative (adding attributes to HTML forms) and imperative (registering tools via `navigator.modelContext.registerTools`). WebMCP is to MCP as JavaScript is to Java — inspired by, but not one-to-one compliant with the MCP spec.

## Key Information
- **Core purpose**: Expose web page functions and navigation to browser-based agents so they can interact with pages programmatically rather than through visual models or DOM parsing
- **Problem it solves**: Browser agents currently rely on taking screenshots and guessing navigation, or traversing the DOM burning tokens on XML — both compute-intensive approaches
- **Two flavors**:
  - **Declarative**: Add `tool-name` and `tool-description` attributes to HTML forms. Great for sites with lots of existing forms. The form is automatically exposed as a tool to the agent.
  - **Imperative**: Use `navigator.modelContext.registerTools` with name, description, input schema, and execution callback. Great for API calls, workflows, and data transformation.
- **Not MCP-compliant**: WebMCP takes inspiration from MCP but is not one-to-one compliant. "WebMCP is to MCP as JavaScript is to Java." The specs may diverge.
- **Origin**: Started at Amazon by a developer working around authentication issues
- **Current status**: Not fully supported yet; standards bodies are still debating. Can be previewed via the MCP B extension (a debugging extension with chat window that imitates what users might see in Gemini or future in-browser agents)
- **Standards**: There is a W3C community group working on the standard
- **MCP Apps interoperability**: MCP Apps is working on interoperability with WebMCP as part of building a unified standard for UI in chat apps
- **Usage example**: RL Nabors used the imperative model for page navigation on her comics site — the agent calls "next page" and the callback grabs the link rail from the DOM and navigates
- **Detection**: Check for `modelContext` in `navigator` to determine if WebMCP is available

## Related
- [[summary-20260523 - Introducing WebMCP： Agents in the Browser — RL Nabors]] — primary source with detailed explanation
- [[summary-20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps]] — source (interoperability mention)
- [[RL Nabors]] — speaker who presented WebMCP in depth
- [[MCP Apps]] — protocol working toward interoperability and standardization
- [[AgentToUI Interaction]] — upcoming MCP Apps feature addressing the same space
- [[A2UI]] — another interoperability target (Google)
- [[Browser as Infinite Canvas]] — the broader vision WebMCP enables
- [[Agentic Web]] — the paradigm WebMCP supports
- [[MCP]] — the protocol that inspired WebMCP
- [[W3C]] — standards body with a WebMCP community group
