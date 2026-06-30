---
title: "Nico Albanese"
type: entity
category: person
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Give Your Agent a Computer — Nico Albanese, Vercel.md"]
last_updated: 2026-06-30
---

# Nico Albanese

## Definition

Nico Albanese is a developer at Vercel who works on the AI SDK. He presented at the AI Engineer Summit in London (May 2026) on building agents with computers/sandboxes using AI SDK v6.

## Key Information

- **Role**: Works on the AI SDK at Vercel
- **Focus Areas**: Agent runtimes, tool systems, sandbox-based agent computers, file system memory for agents
- **Personal Coding Agent**: Built a complex coding agent system using AI SDK patterns that runs with durable workflow steps, used by 23 people at Vercel, processing 3.8 billion tokens with a 91% cache read ratio, responsible for approximately 350 PRs
- **Agent Stats**: His coding agent ran for 104 minutes in a single turn, used 316 tool calls, changed 29 files, and used only 32% of GPT-4's context window with 95% cache token read ratio — with zero compaction
- **Website**: nicoalbanese.com/aie (redirects to workshop materials)
- **Notable Contributions**:
  - Advocated for and influenced context typing in AI SDK v7 (so tools can declare required context, and agents throw errors if it's missing)
  - Demonstrated the three-building-blocks framework for agents: runtime, tools, computer/sandbox
  - Built persistent file-system-based memory systems using Vercel Sandboxes

## Related

- [[summary-20260512 - Give Your Agent a Computer — Nico Albanese, Vercel]] — source
- [[Vercel]] — employer
- [[AISDK]] — product he works on
- [[VercelSandbox]] — sandbox product used in his demos
- [[Tool Loop Agent]] — AI SDK v6 primitive he demonstrated
- [[Persistent Sandboxes]] — sandbox pattern he demonstrated
- [[File System Memory]] — memory pattern he demonstrated
- [[SubAgents]] — context management pattern he uses
- [[Last Gammel]] — AI SDK lead he referenced
