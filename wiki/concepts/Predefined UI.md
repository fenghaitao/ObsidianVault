---
title: "Predefined UI"
type: concept
tags: [mcp, mcp-apps, ui, generative-ui]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps.md"]
last_updated: 2026-06-29
---

## Definition
Predefined UI is one of three approaches to UI generation in the MCP Apps ecosystem. It refers to classic, company-built UI that is sent as a black box to chat hosts — for example, Airbnb building its own UI and sending it to Claude or ChatGPT. It is best suited for cases where the company wants full control over branding and user experience.

## Key Information
- Classic MCP App approach: the company builds the UI, sends it as a resource to the host
- Black box: the host renders it as-is without knowing its internal structure
- Good for ~80% of cases according to the MCP Apps team
- Preserves company branding, identity, and decades of UX refinement
- Examples: Shopify sending store UI, Booking.com sending venue booking UI, Amazon sending product UI
- Contrasts with declarative UI (structured JSON, host renders components) and generative UI (model generates UI on the fly)
- MCP Apps is agnostic to which approach is used

## Related
- [[summary-20260506 - MCP UI： Extending the frontier — Liad Yosef and Ido Salomon, MCP Apps]] — source transcript
- [[MCP Apps]] — the protocol
- [[Declarative UI]] — alternative approach (structured JSON)
- [[GenerativeUI]] — alternative approach (model-generated)
- [[MCPApplications]] — concept page for MCP Applications
