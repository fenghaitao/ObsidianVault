---
title: "summary-20260523 - Introducing WebMCP： Agents in the Browser — RL Nabors"
type: source
tags: [source, transcript, ai, webmcp, mcp, mcp-apps, mcp-transports, browser, agents, agentic-web, web-standards]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260523 - Introducing WebMCP： Agents in the Browser — RL Nabors.md"]
last_updated: 2026-06-30
---

## Core Summary
RL Nabors presents WebMCP, a protocol that turns every HTML page into a mini MCP tools server, allowing browser-based agents to call JavaScript functions and navigate pages directly rather than relying on screenshots or DOM traversal. The talk covers three layers: MCP transports (STDIO vs HTTP), MCP Apps (single-file HTML bundles rendered as rich media in agent chat), and WebMCP itself (declarative and imperative models for exposing page functions to agents). The core thesis: CSS and JavaScript are not just the language of the web — they are the language of interactive experiences on agents. The browser is an infinite canvas with existing APIs (Web Speech, Animation, Audio, Canvas, WASM) waiting to be used for agentic experiences.

## Key Points
- **MCP Transports**: Two modes — STDIO ("studio," local process spawned by client) and HTTP (web service at an endpoint, works with serverless). HTTP transport offers simpler user experience (paste a URL) but has security/privacy considerations.
- **MCP Tools on the Web**: Nabors built MCP tools for her web comics site (rachelagreat.com) — list comics, list storylines, list characters, search comics, search by character, get transcript. Tools return structured JSON except get transcript which returns markdown.
- **MCP Resources gap**: Resources are the right vehicle for pre-priming agent context with documentation and bulk content, but the spec is loosely defined and no major client UI exposes them. Nabors calls for harness builders to implement resources.
- **MCP Apps as rich media**: Instead of returning text from tool calls, MCP tools can return interactive MCP Apps — single HTML files bundled with CSS, JS, fonts (base64), rendered in a sandboxed iframe. Nabors demoed a comic reader inside Claude.
- **MCP App constraints**: Sandboxed iframe, no localStorage, no network access (must call server via `call server` tool), external resources need CSP configuration, links require host permission. Design systems are valuable here since you can share fonts/CSS from the same server.
- **Tool visibility**: Set `visibility: app` on tools meant only for MCP App interaction (like forward/back navigation) to prevent the model from calling them and returning JSON.
- **Chat as lowest common denominator**: Nabors critiques the "starfish design" (blank chatbox that puts all discovery burden on the user). MCP Apps are a path toward richer agent experiences, analogous to how GUIs replaced CLIs.
- **WebMCP**: Makes every HTML page a mini MCP tools server. Two flavors — declarative (add `tool-name` and `tool-description` attributes to HTML forms) and imperative (`navigator.modelContext.registerTools` with callbacks). Not one-to-one compliant with MCP spec; "WebMCP is to MCP as JavaScript is to Java."
- **WebMCP imperative model**: Register tools with name, description, input schema, and execution callback. Nabors used it for page navigation — the agent calls "next page" and the callback grabs the link rail from the DOM.
- **WebMCP origin**: Started at Amazon by a developer working around auth issues. Not yet fully supported; standards bodies still debating. Can be previewed via the MCP B extension (debugging extension with chat window).
- **Browser APIs for agents**: Web Speech API (zero-dependency TTS), Web Animations, Audio, Canvas, WASM, CSS — all existing browser primitives ready for agentic experiences. Nabors demoed a talking comic reader using Web Speech API, noting 11 Labs could provide higher quality.
- **The web isn't dead, it's evolving**: Nabors's previous talk predicted browser death; the real takeaway is that CSS and JavaScript are becoming the language of interactive agent experiences, not just websites.

## Related
- [[RL Nabors]] — speaker, principal DX engineer at Arise, former Mozilla/Microsoft/React
- [[WebMCP]] — the protocol for exposing page functions to browser agents
- [[MCP Transports]] — STDIO vs HTTP transport modes
- [[MCP Resources]] — under-implemented MCP feature for pre-priming context
- [[MCP Apps]] — single-file HTML bundles as interactive agent UI
- [[MCP]] — the underlying Model Context Protocol
- [[Arise]] — Nabors's current company (evals)
- [[ASA (AntiSocial Social Agent)]] — Nabors's MCP app for Twitter/BlueSky
- [[Browser as Infinite Canvas]] — core thesis about the browser's capabilities
- [[Agentic Web]] — Nabors's newsletter and the broader concept
- [[Chat as Lowest Common Denominator]] — UX critique of blank chatboxes
- [[aiDotEngineer]] — conference where this talk was given
- [[Mozilla]] — former employer (Firefox DevTools)
- [[W3C]] — former standards work (Web Animations API)
- [[React]] — former employer (react.dev, reactnative.dev)
- [[ElevenLabs]] — suggested for higher-quality TTS
- [[Anthropic]] — Claude used for MCP App demo
- [[Web Speech API]] — browser's built-in TTS capability
- [[Web Animations API]] — W3C standard Nabors worked on
- [[Microsoft Edge]] — former employer (PM on Edge browser)
- [[Firefox DevTools]] — former employer at Mozilla
