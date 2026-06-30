---
title: "Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure.md"
date: 2026-05-05
ingested: 2026-06-29
tags: [workshop, context-management, knowledge-base, agents, enterprise-ai, institutional-knowledge, demand-driven-context, agent-failure]
---

## Core Thesis
Raj (Staff Software Engineer at IKEA) presents Demand-Driven Context, a methodology for transforming monolithic institutional knowledge bases into coherent, agent-usable context blocks. Instead of the industry-standard push approach (building MCP servers and RAG pipelines to feed all knowledge to agents), Demand-Driven Context uses a pull approach: give agents real work items, let them fail, surface what knowledge is missing, have domain experts fill the gaps, and let the agent curate the new knowledge. This mirrors TDD (write failing tests first, then implement) and microservices decomposition (break monoliths into manageable pieces). Published as a preprint on RXP in March 2026.

## Key Topics
- **The Enterprise AI Gap**: 88% of companies use AI but only see ~6% value creation (McKinsey 2026). Jira tickets don't move despite AI's code generation capabilities because institutional knowledge is missing.
- **Three Types of Knowledge in Tickets**: Green (general knowledge LLMs already know), Orange (teachable via agent skills/extensions), Red (institutional knowledge that sits within the company and people). Agents excel at green and orange but fail on red.
- **The Memento Analogy**: The movie Memento (protagonist can't hold memory beyond 15 minutes) perfectly describes current AI agents — highly skilled but lacking institutional memory.
- **The Industry Pipeline Problem**: Current ROI pipeline: LLM quality → agents → agent harness → retrieval layer (RAG, knowledge graphs) → institutional knowledge (Confluence, Jira, SharePoint, GitHub). The retrieval layer is supposed to fix everything but doesn't.
- **MCP/RAG Limitations**: Building 10-20 MCP servers doesn't solve the problem because the data coming out is undeterministic, unreliable, and untested. Engineers don't do evals on MCP outputs. 10-30% accuracy at best; the rest of the time, humans do data entry for the agents.
- **Enterprise Knowledge Reality**: 20% outdated, 20% unreliable, 10% duplicated, 40% tribal knowledge (never documented). Building 100 MCP servers against this monolith won't work.
- **Monolith to Microservices Analogy**: Just as monolithic legacy systems were decomposed into microservices, institutional knowledge monoliths must be broken into context blocks useful for agents.
- **Push vs Pull Strategy**: Current approach pushes all knowledge to agents. Demand-Driven Context pulls — assign work items, let agents fail, surface gaps, fill them, curate.
- **The Demand-Driven Context Cycle**: (1) Give agent a problem → (2) Agent attempts and fails → (3) Agent produces a checklist of missing information → (4) Domain expert fills the gaps → (5) Agent solves the problem → (6) Agent curates the new knowledge for reuse. Repeat across multiple cycles.
- **TDD Analogy**: Write failing test cases first, then implement to make them pass. Similarly, give problems agents will definitely fail on, fill gaps, and gradually build institutional knowledge.
- **Confidence Score Progression**: Starting from 1.5 confidence (everything critical/missing), after 14 incident cycles, confidence reaches 4.4. The agent discovers undocumented entities, gets answers, and documents everything.
- **Agent as Knowledge Manager**: The agent transitions from consumer to knowledge manager — it doesn't just consume knowledge, it manages the entire knowledge lifecycle including discovery, curation, and documentation.
- **Context Gap Scanner (Automation)**: Rather than manual cycles (painful), automate by running past work items (Jira tickets, incidents, customer support tickets) against the knowledge base. The scanner generates probes (tests), runs them, analyzes gaps, and produces a consolidated report.
- **Scanner Output**: Classifies knowledge as clean, stale, incomplete, or entirely missing. Identifies what's tribal knowledge. Creates a Kanban board of documentation gaps organized by critical/high/medium priority.
- **Knowledge Storage**: Prefers GitHub repository for knowledge base storage because it provides built-in PR processes, review workflows, and conflict resolution for multi-agent, multi-team contributions. Can also publish to Confluence or Slack.
- **Meta Model**: An optional but recommended add-on — a structured map of how the domain is organized (business processes → systems → APIs → business/tech jargon). Gives agents a navigation map for the knowledge base. Without it, agents are "dumping files" with no way to navigate.
- **Key Values**: (1) Knowing the unknown — surfacing what was never documented. (2) Delegating knowledge management to agents rather than humans doing it.
- **Limitations**: Not relevant for small teams with already-good documentation. Manual process is painful — automation is essential. The approach is early-stage and may be superseded.
- **80/20 Rule**: 20% of documentation is most useful; 80% is corner cases. Rather than giving agents 100%, curate the critical 20% as a cache database (context blocks) and leave the rest as links for when agents need more.
- **Implementation**: Demonstrated using Claude Code with skills, rules, agents, hooks, and a file-system knowledge base. Can be implemented with any agent (Copilot, Claude Code, etc.).
- **Code vs Documentation Conflict**: When combining codebase and Confluence as knowledge sources, conflicts arise — code says one thing, documentation says another. Requires ranking rules (e.g., code is source of truth).
- **Scope Recommendation**: Start at the smallest team level with scoped Jira tickets, incidents, and Confluence pages. At enterprise or domain level, no single person has all the domain expertise needed.
- **Cost Consideration**: Per domain, knowledge bases average ~96K tokens — fits easily in modern context windows (Claude Code announced 1M tokens). Running the scanner is inexpensive.

## Entities
- [[Raj]] — speaker, Staff Software Engineer at IKEA, Delivery and Services domain
- [[IKEA]] — company where Raj works; 100+ engineers, 6 product teams in Delivery and Services
- [[McKinsey]] — cited for 88% AI adoption / 6% value creation statistic (2026)
- [[Confluence]] — enterprise knowledge source, part of the institutional knowledge monolith
- [[SharePoint]] — enterprise knowledge source
- [[Miro]] — referenced for endless boards of documentation gap tickets
- [[RXP]] — preprint platform where the Demand-Driven Context paper was published (March 2026)
- [[YouTube]] — referenced as a source of rapidly evolving AI approaches
- [[aiDotEngineer]] — conference where the workshop was presented
- [[ClaudeCode]] — agent used for the demo implementation
- [[Replit]] — referenced as building full-stack apps in 10 minutes
- [[Jira]] — ticketing system; tickets not moving despite AI capabilities
- [[GitHub]] — preferred storage for curated knowledge base
- [[Slack]] — enterprise communication, knowledge source
- [[Copilot]] — agent used at work for the approach
- [[MCP]] — retrieval mechanism; building many MCP servers doesn't solve the knowledge problem
- [[RAG]] — retrieval mechanism; 40% factual accuracy with documented knowledge bases
- [[TDD]] — analogy for the demand-driven approach (write failing tests first)

## Concepts
- [[Demand-Driven Context]] — the core methodology: pull knowledge by giving agents problems, let them fail, surface gaps, fill them, curate
- [[Institutional Knowledge]] — domain knowledge within companies and people that agents lack; the "red" category
- [[Knowledge Base Monolith]] — enterprise institutional knowledge as an undifferentiated monolith (20% outdated, 20% unreliable, 10% duplicated, 40% tribal)
- [[Context Blocks]] — curated, agent-usable chunks of knowledge, analogous to microservices decomposed from a monolith
- [[Meta Model]] — structured domain map (business processes → systems → APIs → jargon) for agent navigation
- [[Context Gap Scanner]] — automated tool that runs past work items against knowledge base to identify gaps
- [[Pull vs Push Context]] — pull approach (agents request missing knowledge) vs push approach (pre-build all MCP/RAG servers)
- [[Agent as Knowledge Manager]] — agent transitions from consumer to curator of institutional knowledge
- [[Knowledge Curation]] — the process of agents discovering, documenting, and organizing knowledge during problem-solving
- [[Agent Failure as Discovery]] — using agent failures to surface undocumented institutional knowledge
- [[Knowledge Base Kanban]] — Kanban board of documentation gaps organized by priority (critical/high/medium)
- [[TribalKnowledge]] — 40% of enterprise knowledge never documented; surfaced through agent failure
- [[AgentHarness]] — the agent execution layer in the ROI pipeline
- [[AgentLoop]] — the cycle of problem → failure → gap identification → human input → resolution → curation
- [[EvalEngineering]] — engineering evaluations for MCP/RAG outputs; rarely done in practice
- [[Agent Skills]] — teachable knowledge (the "orange" category); skills, rules, hooks used in the demo
- [[AgenticLoop]] — the broader agent execution pattern
- [[Context Management]] — managing what knowledge agents have access to
- [[Agent-Human Collaboration]] — domain experts filling gaps surfaced by agent failures
- [[TDD with AI]] — the analogy: write failing tests (problems agents fail on), then implement (fill knowledge gaps)
- [[Kanban Board for AI Tasks]] — documentation gap tracking board
- [[KnowledgeGraph]] — retrieval technique; 40% factual accuracy
- [[MCPEnterpriseChallenges]] — undeterministic, unreliable, untested MCP outputs
- [[ContinuousImprovement]] — gradual knowledge base improvement through repeated cycles
- [[AgenticWorkflows]] — the broader category of agent-driven processes

## Related
- [[summary-20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock]] — TDD with AI, Kanban boards
- [[summary-20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary]] — context engineering
- [[summary-20260112 - Your MCP Server is Bad (and you should feel bad) - Jeremiah Lowin, Prefect]] — MCP limitations
- [[summary-20251223 - Developer Experience in the Age of AI Coding Agents – Max Kanat-Alexander, Capital One]] — tribal knowledge
- [[summary-20260426 - Collaborative AI Engineering： One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub]] — agent collaboration
