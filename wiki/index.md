# Wiki Index

This is the global directory of all wiki pages. Every new page must be registered here under its category, with a one-sentence description.

Format: `[[Page Name]] — One-sentence description.`

---

## Sources

*(Summaries of `raw/` files — kebab-case filenames)*

- [[summary-introducing-archon-ai-agent-builder]] — Cole Medin's official intro to Archon, an open-source meta-agent that builds other AI agents.
- [[summary-build-an-army-of-ai-agents-archon]] — Demo of an "MCP Agent Army": primary agent + 6 specialized sub-agents each owning one MCP server.
- [[summary-10x-your-ai-agents-parallel-architecture]] — Deep dive on the parallel agent architecture; Travel Planner demo with PydanticAI + LangGraph.
- [[summary-coding-subagents-mcp-evolution]] — Argument that the next evolution of AI IDEs is generalists delegating to specialized sub-agents over MCP.
- [[summary-build-your-own-mcp-servers-template]] — Cole's open-source MCP server template using FastMCP, demonstrated with a Mem0 long-term-memory server.
- [[summary-easiest-strategy-for-accurate-rag]] — Walkthrough of Anthropic's Contextual Retrieval pattern in N8N and Python.
- [[summary-3-must-have-mcp-servers-for-ai-coding]] — Cole's recommended MCP triad: documentation RAG, database management, web search.
- [[summary-how-to-learn-ai-agents-roadmap]] — 10-phase roadmap for learning to build AI agents from scratch.
- [[summary-context-engineering-is-new-vibe-coding]] — Cole introduces Context Engineering as the successor to Vibe Coding; demos Rasmus's PRP framework in Claude Code.
- [[summary-context-engineering-101]] — Deep dive on the PRP framework with Rasmus as guest; ships an MCP-server use-case template.
- [[summary-context-engineering-blueprint-for-ai-agents]] — Cole ships a PydanticAI-specific PRP template; builds a Research + Email-Draft agent end-to-end.

## Entities

*(People, companies, tools, products — TitleCase filenames)*

- [[Archon]] — Open-source AI agent that builds other AI agents using PydanticAI and LangGraph.
- [[ColeMedin]] — AI engineer and YouTube creator; built Archon, Crawl4AIRAG, the LocalAIPackage; advocate for PydanticAI + LangGraph + N8N-first prototyping.
- [[Crawl4AIRAG]] — Cole's open-source MCP server that crawls websites and serves contextual-retrieval-enhanced RAG to AI IDEs.
- [[Mem0]] — Long-term memory library for AI agents; featured in Cole's MCP server template.
- [[N8N]] — Open-source visual workflow automation platform; Cole's preferred prototyping tool for AI agents and RAG pipelines.
- [[PydanticAI]] — Python framework for building AI agents with type-safe LLM interactions, MCP support, and structured outputs.
- [[LangGraph]] — Python framework for orchestrating multi-step agentic workflows as state-machine graphs.
- [[LangChain]] — Popular high-level LLM framework that Cole considers "abstraction distraction" and avoids in favor of LangGraph + PydanticAI.
- [[ModelContextProtocol]] — Anthropic's protocol for standardizing how LLMs discover and call external tools; powers MCP server ecosystem.
- [[Anthropic]] — AI lab behind Claude, MCP, and the Contextual Retrieval and Building Effective Agents articles Cole frequently cites.
- [[AndrejKarpathy]] — AI researcher who coined "vibe coding" and articulated the canonical definition of "context engineering"; foundational LLM-Wiki pattern is his.
- [[ClaudeCode]] — Anthropic's terminal-based AI coding agent; Cole's primary AI coding driver from mid-2025 and the canonical execution surface for the PRP framework.
- [[Rasmus]] — Creator of the PRP Framework (Product Requirements Prompts); collaborator with Cole on use-case templates.
- [[OpenAI]] — Provider of the GPT model family used as default LLMs (GPT-4o, GPT-4o-mini, o3-mini) in most of Cole's demos.
- [[Windsurf]] — AI-powered IDE (Codeium) used as the primary demo target for Archon's MCP integration.
- [[Cursor]] — AI-powered IDE; functionally equivalent to Windsurf as an MCP-aware host for Archon.
- [[Supabase]] — Open-source Postgres-with-pgvector database used as Archon's RAG knowledge backend.
- [[Streamlit]] — Python UI framework Cole defaults to for building chat interfaces over agentic workflows.

## Concepts

*(Frameworks, methodologies, theories — TitleCase filenames)*

- [[AIAgent]] — A large language model given the ability to interact with the outside world via tool use.
- [[AgenticWorkflow]] — Multi-step orchestration of one or more AI agents with explicit control flow and shared state.
- [[SubAgent]] — A specialized agent invoked by a primary agent to handle a narrow part of a larger task; solves the LLM tool-overload problem.
- [[ParallelAgentArchitecture]] — Multi-agent pattern where specialized sub-agents execute simultaneously; outputs combined by a synthesizer.
- [[MetaAgent]] — An AI agent whose purpose is to design or generate other AI agents (Cole calls these "agenteers"); Archon is the canonical example.
- [[RetrievalAugmentedGeneration]] — Pattern of grounding LLM responses in retrieved external documents via vector search.
- [[ContextualRetrieval]] — Anthropic's RAG enhancement: prepend each chunk with LLM-generated context positioning it within its source document.
- [[HumanInTheLoop]] — Workflow pattern where execution pauses for human confirmation, correction, or input before resuming.
- [[ToolUse]] — Mechanism by which an LLM invokes external functionality; the foundation of every AI agent.
- [[AICodingAssistant]] — IDE-integrated AI tools (Cursor, Windsurf, etc.); "generalists" that benefit from delegating to specialist sub-agents.
- [[StructuredOutputs]] — LLM responses constrained to a predefined schema; used for downstream consumption and conditional branching.
- [[CapabilitiesOverTools]] — Cole Medin's heuristic: focus on transferable skills rather than mastering specific frameworks that churn rapidly.
- [[AgentEvaluation]] — Measuring agent behavior correctness (vs. code correctness); Cole's "75% of agent dev time is evaluation" rule.
- [[AgentObservability]] — Production-side capture of every input/output/tool-call/cost/latency for an agent; Cole's "100% necessary for production".
- [[Guardrails]] — Input and output validation layers wrapped around an agent; the reliability primitive that makes agents production-ready.
- [[ContextEngineering]] — The discipline of supplying an AI coding assistant with all the context it needs to plausibly solve a task on the first attempt; mid-2025-onwards successor to Vibe Coding.
- [[VibeCoding]] — Letting the AI write code with minimal context and review; coined by Karpathy; great for prototypes, breaks at production.
- [[PRPFramework]] — Rasmus's Product Requirements Prompt methodology; Cole's canonical context-engineering toolkit. Two-pass plan-then-execute with use-case templates.
- [[ValidationGates]] — Explicit lint/test/iterate checks the AI runs before declaring done; the inner correctness loop of the PRP framework.

## Syntheses

*(Cross-document analyses and deep dives — kebab-case filenames)*

*(empty)*
