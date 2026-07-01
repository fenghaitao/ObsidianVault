---
title: "Declarative UI"
type: concept
tags: [mcp, mcp-apps, ui, generative-ui, json]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - Beyond Components： Designing Generative UI for MCP Apps — Ruben Casas, Postman.md"]
last_updated: 2026-06-29
---

## Definition
Declarative UI is one of three approaches to UI generation in the MCP Apps ecosystem. In this approach, the app declares the structure of the UI (e.g., via JSON), but the components are rendered by the host. This creates a middle ground where the host and app share UI functionality and visual control.

## Key Information
- The app declares the UI structure (e.g., using JSON render or similar), but the host renders the actual components
- Middle ground between predefined UI (black box) and generative UI (model-generated)
- Good for hosts that want to control the look and feel of apps
- Example: Claude probably doesn't want a Booking UI, then an Airbnb UI, then an Expedia UI all looking different in the same chat flow
- The host maintains visual consistency while the app controls the content and structure
- MCP Apps is agnostic to which approach is used
- Related to Google's A2UI protocol for generative UI
- **Ruben Casas perspective**: Declarative UI is the "perfect balance today" between flexibility and consistency — more personalized than static UI but still constrained to design system components, making it predictable, fast, and cheaper than full generative components
- Precedent: Netflix has been doing personalized server-driven UI for years, mapping content to its component library
- **JSON Render** (Vercel) is a leading tool: maps components using JSON and YAML, recently added YAML support
- **FastMCP**: uses Python descriptors to map to predefined components

## Related
- [[summary-20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps]] — source transcript
- [[summary-20260603 - Beyond Components： Designing Generative UI for MCP Apps — Ruben Casas, Postman]] — source transcript
- [[MCP Apps]] — the protocol
- [[Predefined UI]] — alternative approach (black box)
- [[GenerativeUI]] — alternative approach (model-generated)
- [[A2UI]] — Google's generative UI protocol
- [[MCPApplications]] — concept page for MCP Applications
- [[JSON Render]] — Vercel tool for declarative UI
- [[Vercel]] — creator of JSON Render
- [[Netflix]] — precedent for server-driven personalized UI
- [[FastMCP]] — uses Python descriptors for declarative UI
- [[Static UI Generation]] — less dynamic alternative
- [[Generative Components]] — more dynamic alternative
- [[UI Generation Spectrum]] — overall framework
