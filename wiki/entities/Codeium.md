---
title: "Codeium"
type: entity
tags: [company, ai-developer-tools, code-generation, retrieval, embeddings, ide-plugin]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240731 - How Codeium Breaks Through the Ceiling for Retrieval： Kevin Hou.md"]
last_updated: 2026-06-26
---

## Definition
Codeium is an AI developer tools company building an IDE plugin for code generation, autocomplete, chat, and search. They are vertically integrated, training their own models and building custom infrastructure down to bare metal, which enables them to run computationally intensive retrieval (M-Query) at a fraction of competitors' costs.

## Key Information
- **Product**: Free unlimited autocomplete, chat, and search across 70+ languages and 40+ IDEs (VS Code, JetBrains, Vim, Emacs, etc.)
- **Downloads**: Over 1.5 million as of mid-2024
- **Rating**: Highest-rated developer tool in the 2024 Stack Overflow survey, ranked above ChatGPT and GitHub Copilot
- **Enterprise**: Trusted by Fortune 500s with top-grade security, licensing, and attribution
- **Origin**: Pivoted from ExaFunction, an ML infrastructure company, giving them deep infrastructure expertise
- **Vertical Integration**: (1) trains own models customized to workflows, (2) builds custom infrastructure to bare metal, (3) product-driven, not research-driven
- **Key Technology**: M-Query — runs thousands of parallel LLM calls over codebase items for high-dimensional reasoning-based retrieval
- **Compute Advantage**: Claims computation costs 1/100th of competitors using APIs, enabling 100x more compute per user
- **Iteration Cycle**: Product-driven data and eval → massive compute → ship to users → measure production signals → repeat
- **Goal**: Empower every developer with superpowers both inside the IDE and beyond

## Related
- [[KevinHou]] — product engineering lead
- [[summary-20240731 - How Codeium Breaks Through the Ceiling for Retrieval： Kevin Hou]] — source transcript
- [[FullVerticalIntegration]] — company strategy
- [[Recall@50]] — retrieval metric used
- [[ProductDriven Benchmarks]] — evaluation approach
- [[Embedding Ceiling]] — problem they address
- [[RAG]] — retrieval augmented generation
- [[GitHubCopilot]] — competitor
