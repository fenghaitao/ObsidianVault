---
title: "Vercel"
type: entity
category: company
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - The New Application Layer - Malte Ubl, CTO Vercel.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260509 - Give Your Chat Agent a Voice — Luke Harries, Head of Growth, ElevenLabs.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260603 - Beyond Components： Designing Generative UI for MCP Apps — Ruben Casas, Postman.md"]
last_updated: 2026-06-26
---

# Vercel

## Definition

Vercel is a cloud platform company that provides the frontend deployment platform, the Next.js framework, the AI SDK for building AI applications, and the Workflow DevKit for building durable, production-ready workflows and agents. Its CTO is Malte Ubl.

## Key Information

- **Products**: Next.js, AI SDK, Workflow DevKit, Vercel Sandbox, JSON Render
- **Key Technologies**:
  - **AI SDK**: TypeScript toolkit for building AI applications with `streamText`, `Agent`, `useChat`, and tool integration. Led by Last Gammel (Berlin). Over 10 million downloads per week.
  - **Workflow DevKit**: Open-source library for building durable, observable workflows with step isolation, retry, caching, and human-in-the-loop patterns
  - **Vercel Sandbox**: Isolated VM service for running agent-generated code
  - **JSON Render**: Declarative UI tool that maps components using JSON and YAML descriptors, enabling dynamic UI interactions while remaining constrained to static components. Represents the declarative UI paradigm in AI-generated UI
- **Platform**: Supports deployment to Vercel, AWS, or any custom cloud stack via adapters
- **Open Source**: Workflow DevKit and its adapters are open source
- **Agent Traffic**: Over 60% of page views on vercel.com are now AI agents (as of April 2026); usage is shifting from dashboard UIs to APIs and CLIs
- **Internal Agent Use**: Vercel uses agents internally for compressed research (contact sales form analysis, abuse report investigation) and support (in-house support agent with 90% deflection rate)
- **CTO**: Malte Ubl, with over 25 years of software engineering experience, previously at Google, former organizer of JSConfEU
- Design language used alongside shadcn as the style basis for ElevenLabs Voice Engine UI components

## Related

- [[summary-20260420 - The New Application Layer - Malte Ubl, CTO Vercel]] — source
- [[summary-20260509 - Give Your Chat Agent a Voice — Luke Harries, Head of Growth, ElevenLabs]] — source (design language reference)
- [[summary-20260603 - Beyond Components： Designing Generative UI for MCP Apps — Ruben Casas, Postman]] — source (JSON Render)
- [[VoiceEngine]] — uses Vercel-style UI components
- [[Malte Ubl]] — CTO
- [[WorkflowDevKit]]
- [[AISDK]]
- [[NextJS]]
- [[VercelSandbox]]
- [[JSON Render]] — declarative UI tool
- [[PeterWielander]]
- [[DurableAgents]]
- [[WorkflowPattern]]
- [[AISDK]]
- [[Last Gammel]] — AI SDK lead
- [[Compressed Research]] — agent pattern used internally
- [[Eliminating Boring Work]] — support agent case study
- [[Agents as Software Users]] — 60% agent traffic insight
- [[Chat Agents]] — paradigm whose UI components follow Vercel design language
- [[Declarative UI]] — paradigm JSON Render represents
