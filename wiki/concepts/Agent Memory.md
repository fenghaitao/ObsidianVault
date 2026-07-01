---
title: "Agent Memory"
type: concept
tags: [agents, context, personalization, memory, crewai, shared-memory, training, multi-user, file-system, sandbox]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240808 - Using agents to build an agent company： Joao Moura.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Viktor： AI Coworker That Lives in Slack — Fryderyk Wiatrowski.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Give Your Agent a Computer — Nico Albanese, Vercel.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260516 - Connecting the Dots with Context Graphs — Stephen Chin, Neo4j.md"]
last_updated: 2026-06-30
---

## Definition
Agent memory is the capability for an AI agent to remember user preferences, profile information, and past interactions across conversations, enabling personalized and context-aware responses without requiring the user to re-state information. In multi-user company agents, memory must scale across hundreds of users without cluttering or leaking between contexts. A newer approach uses the agent's file system (sandbox) as memory, storing facts in files that the agent reads and writes via bash.

## Key Information
- Demonstrated in the French learning app: Manus built a user profile tracking age, workplace, strengths, and weaknesses
- Profile was built implicitly from user interactions over time
- In language learning, memory of user gender and preferences is critical for grammatical agreement
- Manus was exploring memory as a feature as of December 2025 but it was not yet available
- Users currently need to be explicit about context in each conversation
- Memory is distinct from multi-turn conversations (same session) — it spans across separate sessions
- Ivan Leo described it as "something we're actively looking at" for future releases
- **Shared memory in CrewAI**: Agents within a crew share memory and caching, enabling coordinated context across the crew. When multiple crews talk to each other, shared memory becomes a critical complexity layer.
- **Training as memory**: CrewAI's "Train Your Crew" CLI bakes instructions directly into agent memory so they produce consistent results over time, analogous to training a new employee.
- **n8n Simple Memory**: n8n provides a built-in "Simple Memory" option that stores messages in n8n with a configurable context window length (default 5, should be higher for real use). Memory works via a session ID passed from the chat trigger. For integration with existing systems, n8n also supports Postgres and Redis as external memory backends — messages are saved to a table that other applications can query (e.g., displaying chat history in a custom dashboard)
- **Multi-user memory at scale (Viktor)**: Fryderyk Wiatrowski identifies memory as a critical scaling challenge for company agents. With OpenClaw (personal agent), memory clutter over time is a concern for one user. With a company agent like Viktor serving 100+ users, "it's probably running out of memory a hundred times faster." Viktor solved this multi-user memory problem, which Fryderyk describes as a "big challenge to be solved"
- **File System Memory (Nico Albanese, Vercel)**: Memory implemented as files in the agent's sandbox — a `memories.md` file read on startup and injected into the system prompt via `prepareCall`, with new memories written via bash. The agent can also generate and store reusable scripts. This approach is used across all Vercel internal agents (GTM, data, customer support with 90% ticket deflection). Key advantage: deterministic access via Unix primitives (find, grep, ls) rather than black-box vector search. Nico describes this as a "hot take: memory is a file that you store in your sandbox."
- **Neo4j Three-Layer Memory (Stephen Chin, Neo4j)**: Neo4j's context graph architecture organizes agent memory into three layers stored in a knowledge graph:
  - **Short-Term Memory**: Current pipeline state, conversation context, and ongoing agent activities — persisted for use during the execution pipeline
  - **Long-Term Memory**: Organized domain model representing business processes, entities, and users across multiple interactions — requires aggregation and a good schema to be effective at scale
  - **Reasoning Traces**: Captures the "why" behind decisions, making LLM reasoning repeatable and providing decision provenance for compliance, debugging, and future decisions
  - The Neo4j Agent Memory open-source package implements this three-layer architecture, providing APIs for agents to access memory as tools. Relationships are first-class in the graph (no joins needed), multi-hop traversal is highly performant, and graph embeddings enable vector lookups as entry points.

## Related
- [[summary-20240808 - Using agents to build an agent company： Joao Moura]] — source (CrewAI shared memory + training)
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source
- [[summary-20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle]] — source
- [[summary-20260511 - Viktor： AI Coworker That Lives in Slack — Fryderyk Wiatrowski]] — source (multi-user memory scaling)
- [[summary-20260512 - Give Your Agent a Computer — Nico Albanese, Vercel]] — source (file system memory)
- [[ManusAI]] — platform exploring memory
- [[CrewAI]] — framework with shared memory and training features
- [[AgentCrewOrchestration]] — orchestration pattern relying on shared memory
- [[AgentTraining]] — baking instructions into agent memory for consistency
- [[MultiTurn Conversations]] — related but distinct (same-session context)
- [[Context Management]] — broader context handling techniques
- [[General AI Agent]] — philosophy that benefits from memory
- [[n8n]] — platform with built-in simple memory and external memory options
- [[Postgres]] — external memory backend option in n8n
- [[Context Management]] — broader context handling including memory
- [[Company Agent]] — agent type with multi-user memory scaling challenges
- [[Viktor]] — platform that solved multi-user memory at scale
- [[Context Isolation]] — preventing memory leakage across user boundaries
- [[File System Memory]] — file-system-based memory approach
- [[Persistent Sandboxes]] — infrastructure enabling file system memory
- [[BashTool]] — tool used to read/write memory files
- [[NicoAlbanese]] — demonstrated file system memory pattern
- [[Context Graphs]] — Neo4j's three-layer graph-based memory architecture
- [[Knowledge Graphs]] — foundational data structure for graph-based memory
- [[Reasoning Traces]] — the memory layer capturing decision provenance
- [[Neo4j]] — Agent Memory package implementing graph-based agent memory
- [[Stephen Chin]] — presented the three-layer memory model
- [[summary-20260516 - Connecting the Dots with Context Graphs — Stephen Chin, Neo4j]] — source
