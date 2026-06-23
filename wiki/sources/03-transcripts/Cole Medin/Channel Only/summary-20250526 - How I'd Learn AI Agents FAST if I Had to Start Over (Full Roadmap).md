---
title: "summary-20250526 - How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap)"
type: source
tags: [source, transcript, learning, roadmap, ai-agents]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20250526 - How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap).md"]
last_updated: 2026-06-19
---

## Core Summary

[[ColeMedin]] lays out a 10-phase roadmap for learning to build AI agents from scratch in roughly two months. The framing principle is **[[CapabilitiesOverTools]]** — focus on transferable skills, not specific frameworks that will be replaced. Phases progress: foundations → no-code prototyping → AI-coded prototypes → coded agents → advanced architecture → deployment → observability → evaluation → community → leverage.

## Key Points

**The 10 phases:**

| # | Phase | Key skills |
|---|---|---|
| 1 | **Foundations** | LLMs, agents vs. automations, effective prompting, leverage out-of-the-box AI before building |
| 2 | **No-code prototypes** | [[N8N]] (preferred), Flowise, Voiceflow, Relevance AI; tools, RAG, basic memory |
| 3 | **AI-coded prototypes** | [[Cursor]], [[Windsurf]], Cline, Roo Code; prompting AI IDEs; [[ModelContextProtocol]] |
| 4 | **Coded agents** | Python; [[PydanticAI]], [[LangGraph]], OpenAI Agents SDK, Agno, CrewAI |
| 5 | **Advanced architecture** | Multi-agent systems, long-term memory, [[Guardrails]] (input + output), fallback mechanisms |
| 6 | **Deployment** | Docker; cloud platforms (Digital Ocean, Hostinger, AWS, GCP, Vast AI, RunPod, Render) |
| 7 | **[[AgentObservability]]** | Langfuse, Helicone, Langsmith, Logfire — required for production |
| 8 | **[[AgentEvaluation]]** | "75% of the work is evaluation, 25% is coding"; LLM-as-judge, task completion testing, human eval |
| 9 | **Community / mastering with others** | Cole's regret: learning alone slowed him down; pitches Dynamis.ai |
| 10 | **Leverage** | Sell templates, build SaaS, consult, content creation, AI-automation agency |

- **Capabilities over Tools** is the through-line: every phase warns against over-mastering a specific framework. Frameworks change; the underlying skill (e.g. "give an agent tool access," "implement RAG with metadata-aware chunking") is durable.
- **No-code → coded** is deliberate. Cole recommends starting in [[N8N]] even if you're a senior engineer, then porting prototypes to Python. The visual flow makes patterns visible; Python provides flexibility/performance.
- **Multi-agent architectures**: Cole references Anthropic's "[[summary-building-effective-agents]]" article (the same one cited in the [[ParallelAgentArchitecture]] page).
- **Eval is the bottleneck**: "your agent isn't done when it works once; it's done when you've measured it." [[AgentEvaluation]] is treated as the most underrated phase.
- **Tools Cole personally uses** (mentioned in passing, not the focus): Claude Desktop (chat), Aqua Voice (dictation), Mem (notes), Perplexity (research).

## Related

- [[ColeMedin]] — author
- [[CapabilitiesOverTools]] — central principle
- [[AgentEvaluation]] — phase 8 deep dive
- [[AgentObservability]] — phase 7 deep dive
- [[Guardrails]] — phase 5 deep dive
- [[N8N]] — phase 2 primary tool
- [[PydanticAI]], [[LangGraph]] — phase 4 frameworks
- [[Cursor]], [[Windsurf]] — phase 3 AI IDEs
- [[ModelContextProtocol]] — phase 3 augmentation
- [[summary-building-effective-agents]] — Anthropic article cited
