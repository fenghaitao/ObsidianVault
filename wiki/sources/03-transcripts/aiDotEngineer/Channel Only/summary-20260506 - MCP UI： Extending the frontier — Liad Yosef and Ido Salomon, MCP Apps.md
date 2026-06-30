---
title: "summary-20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps"
type: source
tags: [source, transcript, ai, mcp, mcp-apps, mcp-ui, ui, agents, generative-ui, protocol, web]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps.md"]
last_updated: 2026-06-29
---

## Core Summary
Ido Salomon and Liad Yosef present MCP UI and MCP Apps, the first official MCP extension for passing UI over the Model Context Protocol. The core thesis: text is a terrible interface for agent interactions, and companies should be able to send their own branded, interactive UI chunks to chat hosts instead of being reduced to walls of text. MCP Apps standardizes how servers ship UI as resources, how those UIs communicate back to the host via message passing (notifications, tool calls, prompts), and how the host renders them in a sandbox. The spec, co-developed with Anthropic and OpenAI, has been adopted by Claude, ChatGPT, VS Code, Cursor, Copilot, and others. The talk frames MCP Apps as ushering in a "new web" where personal assistants compose experiences from atomic UI chunks rather than users navigating monolithic websites.

## Key Points
- **Text is suboptimal for agent UI**: Companies don't want their data reduced to walls of text without identity. MCP Apps lets every company send its own branded, interactive UI to the chat.
- **MCP UI origins**: Released by Ido Salomon in May 2025 as a way to pass UI over MCP, with community SDKs. Later partnered with Anthropic and OpenAI to become the first official MCP extension called MCP Apps.
- **How it works**: Instead of returning text from a tool call, the server returns a resource pointing to HTML UI. The host renders it in a sandboxed iframe. The UI communicates back to the host via standardized messages, keeping the model in the loop.
- **Bidirectional message passing**: Every UI interaction sends a message back to the host. The host decides what to do (call a tool, run a prompt), keeping control and context with the host rather than letting the UI talk directly to its backend.
- **Message spectrum**: Three levels of UI-to-host communication — notification (UI just informs the host), tool call (UI tells host to call a specific tool), prompt (UI releases all control and tells host to run a prompt).
- **Interactive, not just presentational**: Users can click on UI elements to trigger follow-up actions. Example: clicking a funnel step in a PostHog visualization to ask follow-up questions about that specific step.
- **Early adopters**: Shopify (millions of stores sending MCP UI chunks), Hugging Face (all Spaces as MCP UI widgets) adopted even before standardization.
- **Post-standardization adoption**: VS Code, Cursor, Copilot, GitHub, ChatGPT, Claude, Postman, Goose, LibreChat, Spy all support MCP Apps. ChatGPT recommends MCP Apps as the way to build ChatGPT apps.
- **The new web paradigm**: Instead of navigating multiple websites to plan an anniversary, a personal assistant pulls atomic UI chunks from Google Calendar, Amazon, Booking.com, and composes them into one experience. Apps no longer own the user journey.
- **Win-win-win**: Companies keep their brand identity, users recognize familiar interfaces, and hosts don't need to generate all UIs themselves.
- **Reusable views (upcoming)**: Currently each render creates a new view. Working on referencing the same view and pushing data into it, solving performance issues for heavy apps like Autodesk.
- **Agent-to-UI interaction (upcoming)**: Standardizing how models can interact with views — clicking buttons, filling forms — by having apps expose tools for the model.
- **UI generation spectrum**: MCP Apps is agnostic to how UI is generated. Three approaches: predefined UI (black box, company-built), declarative UI (structured JSON, host renders components), generative UI (model generates UI on the fly). Claude's generative UI feature uses MCP Apps under the hood.
- **Interoperability**: Working on compatibility with A2UI (Google's generative UI protocol) and WebMCP to build a unified standard for UI in chat apps.
- **Distribution opportunity**: 1 billion weekly ChatGPT users — 160x the iPhone user base when the App Store launched. MCP Apps is a new distribution channel for applications.
- **Getting started**: For servers, use the XApps SDK with built-in skills (let coding agents generate the app). For hosts, use the MCP UI SDK's React component for out-of-the-box app support.
- **Community**: Official MCP Apps repo (XApps), tri-weekly work group meetings, official Discord for the committee, community Discord for users and builders.

## Related
- [[IdoSalomon]] — co-presenter, creator of MCP UI, co-creator of MCP Apps
- [[Liad Yosef]] — co-presenter, co-creator of MCP Apps, co-founder of Ergo Labs
- [[Ergo Labs]] — Liad Yosef's company, human agentic interfaces
- [[MCPUI]] — the original project that became MCP Apps
- [[MCP Apps]] — the standardized MCP extension for UI
- [[MCP]] — the underlying protocol
- [[MCPApplications]] — concept page for MCP Applications
- [[Anthropic]] — co-developer of the MCP Apps spec
- [[OpenAI]] — co-developer of the MCP Apps spec
- [[Shopify]] — early adopter, sent MCP UI chunks for millions of stores
- [[HuggingFace]] — early adopter, all Spaces as MCP UI widgets
- [[PostHog]] — example used in demo (funnel visualization)
- [[Spotify]] — example used (playlist creation)
- [[BookingCom]] — example used (venue booking with map)
- [[Amazon]] — example used (product display)
- [[Google]] — example used (Google Calendar chunk)
- [[ClaudeCode]] — host supporting MCP Apps
- [[Cursor]] — host supporting MCP Apps
- [[GitHub]] — host supporting MCP Apps (Copilot)
- [[Microsoft]] — host supporting MCP Apps (Copilot)
- [[AgentCraft]] — also created by Ido Salomon
- [[MCI]] — also created by Ido Salomon
- [[MC apps]] — also created/co-maintained by Ido Salomon
- [[GenerativeUI]] — related UI paradigm, Claude's feature uses MCP Apps
- [[End of Apps]] — related vision of apps being replaced by UI chunks
- [[XApps]] — official MCP Apps SDK and repo
- [[A2UI]] — Google's generative UI protocol, interoperability target
- [[WebMCP]] — related protocol, interoperability target
- [[Sam Altman]] — cited for 800M weekly ChatGPT users statistic
- [[Postman]] — host supporting MCP Apps
- [[Goose]] — host supporting MCP Apps
- [[LibreChat]] — host supporting MCP Apps
- [[Spy]] — terminal with MCP Apps support
- [[Autodesk]] — example of heavy app needing reusable views
- [[Expedia]] — example company whose UI could be sent as chunks
- [[Monday]] — example company whose UI could be sent as chunks
- [[MCP Apps Message Passing]] — standardized message passing between UI and host
- [[MCP Apps UI Spectrum]] — notification, tool call, prompt message types
- [[Reusable Views]] — upcoming MCP Apps feature
- [[Agent-to-UI Interaction]] — upcoming MCP Apps feature for model-driven UI interaction
- [[Predefined UI]] — black-box company-built UI in MCP Apps
- [[Declarative UI]] — structured JSON UI with host-rendered components
