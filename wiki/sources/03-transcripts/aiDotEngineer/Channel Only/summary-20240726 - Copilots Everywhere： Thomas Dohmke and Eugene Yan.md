---
title: "summary-20240726 - Copilots Everywhere： Thomas Dohmke and Eugene Yan"
type: source
tags: [source, transcript, ai-engineering, copilot, github, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240726 - Copilots Everywhere： Thomas Dohmke and Eugene Yan.md"]
last_updated: 2026-06-26
---

## Core Summary
Thomas Dohmke (GitHub CEO) in conversation with Eugene Yan discusses the origin and philosophy of GitHub Copilot, the evolution of AI-assisted software development, and the vision for where AI tools are heading. The central philosophy is "AI for engineers, not an AI engineer" — a human-centric approach where AI augments developers rather than replacing them. Copilot started as an auto-completion experiment with OpenAI's Codex model during the 2020 lockdown, evolved through chat integration in 2023, and expanded into GitHub Copilot Workspace which bridges GitHub issues to pull requests. Dohmke defines agents as "AI dishwashers" — autonomous tools that handle tedious, repetitive work so developers can focus on creative tasks. He emphasizes that natural language programming democratizes access to technology across languages and skill levels, and that the next frontier is AI systems that burn down security and compliance backlogs automatically.

## Key Points
- Copilot originated during the 2020 lockdown with early access to OpenAI's Codex (GPT-3 variant), built entirely remotely
- First "aha moment": the model could write both JavaScript and Python without a syntax tree, just like humans know languages
- Internal staff ship NPS was ~72-73, unusually high for an early-stage LLM product with hallucinations
- By mid-2021, Copilot was writing ~25% of code in enabled files; now it is approximately 50%
- Core philosophy: "we're not trying to build an AI engineer, we're trying to build AI for engineers" — human-centric
- Strategy: constantly reconfigure approach as the AI world changes daily; operate as agile as possible even at 3,000-person scale
- Copilot's design: meet developers where they are — IDE integration via ghost text auto-completions sidesteps hallucination concerns, since developers are already used to adjusting auto-completions
- Keeping the developer "in the flow" is the core value — avoiding constant editor-to-browser context switching
- GitHub Copilot Workspace takes a GitHub issue and helps figure out implementation: specification → codebase analysis → plan → implementation (diff view), with human interaction at every step
- Workspace helps non-developers (PMs, program managers) understand what implementing a user story would mean in code
- Natural language programming democratizes coding: models speak almost any major human language, enabling kids and non-English speakers to learn coding in their native language
- AI also democratizes institutional knowledge access, reducing anxiety for new employees who hesitate to ask questions
- Agent definition: "like an AI dishwasher" — you fill it, let it run, then put the output back on the shelves
- Already-existing agents include CI/CD pipelines, monitoring — they get a job done autonomously
- Security tooling currently adds to backlog rather than reducing it; AI autofix is needed to burn down security/compliance debt
- Developers should see themselves as artists and creators, not production workers; AI should take over the things we don't want to do
- Software development has experienced multiple step functions: PC emergence, open source and internet, GitHub collaboration, mobile wave — and now AI is the next one

## Related
- [[Thomas Dohmke]] — speaker, CEO of GitHub
- [[Eugene Yan]] — host, aiDotEngineer
- [[GitHubCopilot]] — the AI developer tool discussed throughout
- [[GitHub]] — the company
- [[GitHub Workspace]] — the issue-to-PR product
- [[OpenAI]] — provided Codex model that powered early Copilot
- [[AI for Engineers]] — human-centric AI philosophy
- [[Developer Flow]] — staying in the IDE without context-switching
- [[Natural Language Programming]] — democratizing access to coding across languages
- [[AI as Pair Programmer]] — AI augmenting developers as a collaborator
- [[AgentAsDishwasher]] — the dishwasher metaphor for AI agents
- [[Security Autofix]] — AI burning down security backlogs
- [[Institutional Knowledge Democratization]] — AI making organizational knowledge accessible
- [[Software Development Step Functions]] — historical transformational epochs in development
