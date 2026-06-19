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

## Entities

*(People, companies, tools, products — TitleCase filenames)*

- [[Archon]] — Open-source AI agent that builds other AI agents using PydanticAI and LangGraph.
- [[ColeMedin]] — AI engineer and YouTube creator; built Archon and the LocalAIPackage; advocate for PydanticAI + LangGraph.
- [[PydanticAI]] — Python framework for building AI agents with type-safe LLM interactions, MCP support, and structured outputs.
- [[LangGraph]] — Python framework for orchestrating multi-step agentic workflows as state-machine graphs.
- [[LangChain]] — Popular high-level LLM framework that Cole considers "abstraction distraction" and avoids in favor of LangGraph + PydanticAI.
- [[ModelContextProtocol]] — Anthropic's protocol for standardizing how LLMs discover and call external tools; powers MCP server ecosystem.
- [[Anthropic]] — AI lab behind Claude and the Model Context Protocol; author of the "Building Effective Agents" article Cole frequently cites.
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
- [[HumanInTheLoop]] — Workflow pattern where execution pauses for human confirmation, correction, or input before resuming.
- [[ToolUse]] — Mechanism by which an LLM invokes external functionality; the foundation of every AI agent.
- [[AICodingAssistant]] — IDE-integrated AI tools (Cursor, Windsurf, etc.); "generalists" that benefit from delegating to specialist sub-agents.
- [[StructuredOutputs]] — LLM responses constrained to a predefined schema; used for downstream consumption and conditional branching.

## Syntheses

*(Cross-document analyses and deep dives — kebab-case filenames)*

*(empty)*
