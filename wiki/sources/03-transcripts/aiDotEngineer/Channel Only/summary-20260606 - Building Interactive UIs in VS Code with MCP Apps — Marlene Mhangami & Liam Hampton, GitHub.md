---
title: "summary-20260606 - Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub"
type: source
tags: [source, transcript, ai, mcp, mcp-apps, vs-code, github-copilot, ui, sandbox, iframe, flame-graph, excalidraw]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Building Interactive UIs in VS Code with MCP Apps — Marlene Mhangami & Liam Hampton, GitHub.md"]
last_updated: 2026-06-30
---

## Core Summary
Marlene Mhangami and Liam Hampton, Senior Developer Advocates at Microsoft and GitHub, present MCP Apps as a way to build rich, interactive UI experiences directly inside VS Code's chat interface. The core thesis: early MCP was limited to returning text, forcing developers to overcompensate with ASCII art and emojis for visual communication. MCP Apps solve this by letting MCP server tools return interactive HTML components that render in sandboxed iframes within the chat host. Marlene covers the architecture (host = VS Code, client = GitHub Copilot, server returns UI resources), while Liam demos a flame graph profiling MCP App built with React that profiles Go application performance over MCP.

## Key Points
- **MCP overview**: Open protocol by Anthropic that standardizes how applications provide context (tools, prompts, resources) to LLMs. Three components: hosts (programs like VS Code), clients (maintain 1:1 connection with servers, e.g. GitHub Copilot), and servers (lightweight programs exposing capabilities).
- **Text-only limitation**: Early MCP could only return text. Developers used ASCII art and emojis to compensate for the inability to generate diagrams or rich interactive content.
- **MCP Apps solution**: Servers return tool results with a UI resource reference pointing to HTML. The host (VS Code) fetches and renders the HTML inside a sandboxed iframe. The app can call back to the server for live interaction and fresh data.
- **Host vs Client distinction**: In VS Code, the host is VS Code itself and the client is GitHub Copilot. The host fetches and renders the UI; the client handles LLM communication and tool calling.
- **Sandboxed iframe rationale**: Liam uses the hamster-in-a-cage analogy — the iframe prevents the app from interacting with VS Code settings, APIs, or anything external, keeping it contained in the chat window.
- **Use cases**: Data exploration (interactive charts instead of typing follow-up questions), e-commerce (full checkout experience inside chat, keeping brand identity), architecture diagrams (Excalidraw), design components (Figma).
- **Shopify**: Building MCP Apps to preserve brand experience within chat, enabling full checkout flows.
- **Excalidraw MCP App**: Generates interactive diagrams in chat. Users can move elements, update text, and interact live.
- **Figma**: Using MCP Apps to generate design components on the fly.
- **Live demo — Flame Graph Profiler**: Liam built an MCP App using a Go profiling skill from Anthropic's MCP repository. The server profiles Go application code (bubble sort, Fibonacci) using Go pprof, returns JSON data with a UI resource reference, and the React-based flame graph UI renders in VS Code's chat. Users can view top functions, summary, and interact with the flame graph.
- **MCP App structure**: Three parts — the tool (LLM + host), the resource (bundled HTML UI, can be React/Vue/Svelte/vanilla JS), and the link between them (host recognizes the UI resource reference in the server response).
- **Tool visibility**: Tools can be configured for model-only invocation, model-and-app invocation, or app-only invocation.

## Related
- [[Marlene Mhangami]] — co-presenter, Senior Developer Advocate at Microsoft & GitHub
- [[Liam Hampton]] — co-presenter, Senior Developer Advocate at Microsoft & GitHub
- [[Microsoft]] — employer, booth at the conference
- [[GitHub]] — employer, booth at the conference
- [[GitHubCopilot]] — MCP client in VS Code
- [[VisualStudioCode]] — MCP host that renders the apps
- [[MCP Apps]] — the protocol extension enabling interactive UI
- [[MCP]] — the underlying Model Context Protocol
- [[Anthropic]] — creator of MCP
- [[MCPApplications]] — concept page for MCP Applications
- [[Sandboxed Iframe]] — security mechanism for MCP App rendering
- [[Excalidraw MCP App]] — interactive diagram generation via MCP Apps
- [[Excalidraw]] — underlying drawing tool
- [[Shopify]] — early adopter building e-commerce MCP Apps
- [[Figma]] — using MCP Apps for design components
- [[Flame Graph Profiling]] — demo use case
- [[Go pprof]] — Go profiling tool used in the demo
- [[summary-20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps]] — prior talk on MCP Apps origins
