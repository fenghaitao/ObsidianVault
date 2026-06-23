---
title: "ColeMedin"
type: entity
tags: [person, creator, ai-engineer, content-creator, youtube]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/01 - Build an ARMY of AI Agents on Autopilot with Archon, Here's How.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/02 - 10x Your AI Agents with this ONE Agent Architecture.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/03 - Coding Subagents - The Next Evolution of AI IDEs.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250414 - The ULTIMATE Guide to Building Your Own MCP Servers (Free Template).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250508 - The EASIEST Possible Strategy for Accurate RAG (Step by Step Guide).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250515 - The 3 MUST Have MCP Servers for Any AI Coding (and How to Use Them).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250526 - How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250703 - Context Engineering is the New Vibe Coding (Learn this Now).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250717 - Context Engineering 101 - The Simple Strategy to 100x AI Coding.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250724 - Build ANY AI Agent with this Context Engineering Blueprint.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20251103 - Every RAG Strategy Explained in 13 Minutes (No Fluff).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20251218 - Are Agent Harnesses Bringing Back Vibe Coding.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260108 - The 5 Techniques Separating Top Agentic Engineers Right Now.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260126 - I Built My Second Brain with Claude Code + Obsidian + Skills (Here's How).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260507 - AI YouTube Is Only Claude Hype Now.md"
last_updated: 2026-06-20
---

## Definition

Cole Medin is an AI engineer and YouTube content creator focused on AI agent development. He is the creator of [[Archon]] (the meta-agent that builds AI agents), the LocalAIPackage, and the Dynamis.ai community. His teaching style emphasizes building real, complex tools while breaking down each component into simple, learnable pieces.

## Key Information

### Public output (drawn from playlist content)

- YouTube channel: `@ColeMedin`. Active series include:
  - **AI Agents Masterclass** — foundational tutorials on building agents from scratch.
  - **Archon - The AI Agent Builder** — build-in-public series on Archon (this playlist).
  - **n8n RAG Template**, **Local AI**, **bolt.diy**, **LangChain**, **Guide to Building AI Agents**, **No Code AI with n8n**, **AI Platform Showcases** — other playlists.
- Open-source projects:
  - **Archon** (this entity's namesake project)
  - **[[Crawl4AIRAG]]** — open-source MCP server that crawls websites, builds curated RAG knowledge bases, exposes RAG queries to AI IDEs. Cole's recommended documentation-RAG MCP slot. Has [[ContextualRetrieval]] built into the ingest pipeline.
  - **MCP server template** — Cole's reference implementation for building production-quality MCP servers (lifespan + dual-transport + best-practice tool docstrings). Demonstrated with a [[Mem0]] long-term-memory server.
  - **LocalAIPackage** — packaged stack of self-hostable AI services (vector DBs, web search, etc.) intended to plug into Archon-built agents in the v9+ self-execution roadmap.
  - **MCP Agent Army** template — reference implementation of the multi-MCP sub-agent pattern.
- Community: **Dynamis.ai** — Cole's invite-list community with workshops on agent building, including the AI Agent Mastery course covering his full agent-development process.

### Stated framework preferences

- **Favorite frameworks:** [[PydanticAI]] and [[LangGraph]]. Cole defaults to these for nearly all his agents.
- **Stated reservations about [[LangChain]]:** calls it "abstraction distraction" — argues it implements too much for the developer, costing controllability and customizability. He still acknowledges it has its place and plans Archon multi-framework support including LangChain (v10+).
- Plans to support: LangChain, Agno, CrewAI, LlamaIndex in future Archon versions.

### Engineering philosophy (recurring themes)

- **Build in public** — open-source from day one, iterate visibly, invite contribution.
- **Specialized > generalist** — small focused agents outperform mega-prompted ones.
- **[[CapabilitiesOverTools]]** — focus on transferable skills, not specific frameworks. Cole calls this his single most important learning principle.
- **[[ContextEngineering]] over [[VibeCoding]]** — from mid-2025, Cole's central frame for AI coding work. Sharpening the axe (curating context) up-front rather than diving into implementation.
- **[[PRPFramework]] (Rasmus's Product Requirements Prompts)** — Cole's preferred concrete context-engineering toolkit. Use-case templates (per language × project type) are the scaling layer.
- **Education through working tools** — every tutorial produces a real, functional artifact, not just a toy.
- **N8N first, Python after** — prototype agents in [[N8N]] before porting to Python; visual flow makes patterns visible.
- **Eval is 75% of the work** — see [[AgentEvaluation]]. Cole's stated rule of thumb for agent development time allocation.
- **"Agents will dominate the landscape of software."** — recurring framing across multiple videos.

### Tooling shift mid-2025

Cole's primary AI-coding driver shifted to [[ClaudeCode]] around July 2025 (see `summary-context-engineering-is-new-vibe-coding`). Reason: Claude Code's slash-command + `CLAUDE.md` + auto-edit primitives are first-class for [[PRPFramework]] execution in a way [[Cursor]] and [[Windsurf]] aren't. Cursor and Windsurf remain valid alternates (and the slash commands are markdown, so they port).

### The Second Brain era (Jan 2026 onwards)

By January 2026 Cole reports a "huge mistake" of thinking [[ClaudeCode]] was just for coding. He extends the same agent + filesystem + capabilities pattern to non-coding work: [[SecondBrain]] = [[ClaudeCode]] + [[Obsidian]] + [[ClaudeSkills]]. Same architecture, different content domain. This is the pattern this wiki itself was built on.

### The 5 techniques (Cole's [[AgenticEngineering]] checklist)

By Jan 2026 Cole codifies his discipline as 5 techniques: [[PRDFirstDevelopment]], [[ModularRulesArchitecture]], [[Commandification]], [[ContextReset]], and most importantly [[SystemEvolution]]. See `summary-5-techniques-top-agentic-engineers`.

### Content philosophy & the live-stream shift (May 2026)

Per `summary-ai-youtube-claude-hype`, Cole deliberately resists the "Claude hype" content cycle (creators racing to react to each release) in favor of **depth and real engineering**, moving to multi-weekly **live streams** (Mon/Thu/Sat) of live building alongside ~one polished video/week. He argues many release-reaction videos are skippable since [[ClaudeCode]] can search its own up-to-date docs on demand. He builds **[[Archon]]** live and runs the **Dark Factory** experiment — a codebase handed *entirely* to AI agents, with no human allowed to review or write code (a maximal autonomy test).

## Related

- [[Archon]] — flagship project
- [[Crawl4AIRAG]] — Cole's open-source RAG MCP server
- [[Mem0]] — featured library in his MCP template
- [[N8N]] — preferred no-code prototyping tool
- [[PydanticAI]] — preferred agent framework
- [[LangGraph]] — preferred workflow framework
- [[LangChain]] — explicitly criticized but planned for support
- [[ClaudeCode]] — primary AI coding driver from mid-2025; second-brain agent from 2026
- [[ClaudeSkills]] — preferred capability-packaging primitive
- [[Obsidian]] — canvas for his Second Brain system
- [[Rasmus]] — collaborator on the [[PRPFramework]]
- [[AndrejKarpathy]] — articulated the [[ContextEngineering]] frame Cole runs with; LLM-Wiki pattern Cole's Second Brain implements
- [[CapabilitiesOverTools]] — Cole's central learning principle
- [[ContextEngineering]], [[PRPFramework]], [[ValidationGates]] — Cole's mid-2025-onwards methodology
- [[AgenticEngineering]] — Cole's 5-techniques codification (Jan 2026)
- [[AgentHarness]] — Cole sees this as the 2026 frontier
- [[VibeCoding]] — the foil paradigm Cole argues against for production work
- [[SecondBrain]] — Cole's Jan-2026 personal-knowledge use case
- [[SystemEvolution]] — Cole's "fix the system, not the bug" mindset
- [[AgentEvaluation]], [[AgentObservability]], [[Guardrails]] — production-readiness pillars Cole emphasizes
- [[cole-vs-brian-planning-methodologies]] — synthesis comparing Cole's and Brian's planning approaches
- [[cole-vs-brian-agent-autonomy]] — synthesis comparing Cole's and Brian's autonomy patterns
- [[ContextualRetrieval]] — Cole-popularized RAG technique
- [[ParallelAgentArchitecture]] — frequently demonstrated pattern
- [[SubAgent]] — recurring architectural focus
- [[summary-introducing-archon-ai-agent-builder]] — Archon intro
- [[summary-build-an-army-of-ai-agents-archon]] — MCP agent army demo
- [[summary-10x-your-ai-agents-parallel-architecture]] — parallel architecture
- [[summary-coding-subagents-mcp-evolution]] — MCP sub-agent thesis
- [[summary-build-your-own-mcp-servers-template]] — MCP template walkthrough
- [[summary-easiest-strategy-for-accurate-rag]] — Contextual Retrieval guide
- [[summary-3-must-have-mcp-servers-for-ai-coding]] — recommended MCP triad
- [[summary-how-to-learn-ai-agents-roadmap]] — 10-phase learning roadmap
- [[summary-context-engineering-is-new-vibe-coding]] — Context Engineering intro
- [[summary-context-engineering-101]] — PRP framework deep dive with Rasmus
- [[summary-context-engineering-blueprint-for-ai-agents]] — PydanticAI use-case template
- [[summary-every-rag-strategy-explained]] — 11-RAG-strategy survey
- [[summary-agent-harnesses-and-vibe-coding]] — AgentHarness intro
- [[summary-5-techniques-top-agentic-engineers]] — agentic engineering checklist
- [[summary-second-brain-with-claude-code-obsidian-skills]] — Second Brain pattern
- [[summary-ai-youtube-claude-hype]] — content philosophy; live-stream shift; Dark Factory
