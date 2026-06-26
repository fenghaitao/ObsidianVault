---
title: "Computer Use"
type: concept
tags: [testing, browser, agents, ui-automation, ai-capability]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251222 - No More Slop – swyx.md"]
last_updated: 2026-06-25
---

## Definition
Computer Use is an AI capability, debuted by Anthropic, that enables AI models to autonomously operate complex desktop applications including IDEs, browsers, and other software through visual understanding and action execution. In testing contexts, it refers to a browser-based approach where the model interacts via screenshots.

## Key Information
- Debuted by Anthropic around late 2024
- Has significantly improved since its debut — "getting really really good now"
- Can autonomously operate the most complex apps including IDEs
- Used by swyx and the AI Engineer team to automate website updates via Devin
- Represents a key tool in the fight against slop by enabling AI to handle commoditized, repetitive tasks
- In testing: model directly interacts with the application via screenshots; tends to be expensive and slow compared to programmatic approaches
- Used by Replit as a fallback when Playwright-based programmatic testing cannot handle a particular interaction
- Contrasted with browser use, which simulates the UI and interacts through DOM abstractions

## Related
- [[summary-20251222 - No More Slop – swyx]] — source
- [[summary-20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit]] — source
- [[Anthropic]] — company that debuted computer use
- [[Devin]] — AI coding tool using computer use capabilities
- [[Browser-based Autonomous Testing]] — parent concept
- [[Browser Use]] — alternative approach
- [[CodeSlop]] — computer use can both produce and fight this
- [[SubAgents]] — related agent-based approach
