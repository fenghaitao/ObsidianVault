---
title: "PydanticAI"
type: entity
tags: [framework, python, ai-agents, llm, tool-use]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/01 - Build an ARMY of AI Agents on Autopilot with Archon, Here's How.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/02 - 10x Your AI Agents with this ONE Agent Architecture.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/03 - Coding Subagents - The Next Evolution of AI IDEs.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260129 - Claude Skills Aren't Just for Claude - Here's How to Build Them for ANY Agent.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260326 - Everything You Thought About Building AI Agents is Wrong.md"
  - "raw/03-transcripts/Pydantic/Channel Only/20250415 - Pydantic, Jason Liu & MCP Meetup - April 8, 2025.md"
  - "raw/03-transcripts/Pydantic/Channel Only/20250627 - MCP Sampling in Pydantic AI： How to Proxy LLM Calls.md"
  - "raw/03-transcripts/Pydantic/Channel Only/20260219 - Reliable and Observable AI Agents with Pydantic AI and DBOS.md"
  - "raw/03-transcripts/Pydantic/Channel Only/20260401 - Samuel Colvin Controlling the wild： Monty, from tool calling to computer use - PyAI Conf 2026.md"
last_updated: 2026-06-25
---

## Definition

PydanticAI is a Python framework for building [[AIAgent]]s, built on top of Pydantic for type-safe LLM interactions. [[ColeMedin]] cites it as one of his two favorite agent frameworks (alongside [[LangGraph]]) and uses it as the primary code-generation target for [[Archon]].

## Key Information

### Three-part agent definition pattern

PydanticAI agents are conceptually three components:

1. **Dependencies** — API keys, database connections, configuration that tools need at runtime. Defined as a dataclass and passed to tools via `RunContext`.
2. **Agent** — the agent object itself, configured with: model (LLM), system prompt, dependencies type, optional retry policy, optional `result_type` for [[StructuredOutputs]], optional `mcp_servers` list.
3. **Tools** — Python functions decorated to register them with the agent. The function's docstring becomes the tool description sent to the LLM (when/how to use the tool).

### Notable features used in the playlist

- **MCP integration** — `mcp_servers=[...]` parameter on the agent connects it to one or more [[ModelContextProtocol]] servers, exposing all the server's tools to the agent automatically. Released relatively recently and central to Cole's "MCP Agent Army" pattern.
- **Structured outputs via `result_type=ClassName`** — guarantees the agent's response conforms to a Pydantic model. Used in the Travel Planner gatekeeper agent so a downstream LangGraph router can branch on `all_details_given: bool`.
- **Streaming** — `agent.run_stream(...)` for token-by-token output. Streaming *structured* outputs requires special handling (the dict builds up incrementally) — Cole demonstrates the debounced JSON validation pattern.
- **`@agent.tool` decorator** — minimal tool registration; LLM-facing parameters and docstrings drive tool selection.

### Building a custom "skills agent" (Jan 2026)

Cole uses PydanticAI to reimplement [[ClaudeSkills]] / [[ProgressiveDisclosure]] from scratch (see `summary-build-skills-for-any-agent`), showing off three features:

- **Dynamic system prompt** — the `@agent.system_prompt` decorator lets you build the prompt at runtime. Cole's version scans a `skills/` directory, extracts every `skill.md`'s YAML description + path, and injects them with the static base prompt.
- **Toolsets** — a reusable bundle of tools (`load_skill`, `read_reference`, `list_references`) attached to the agent; portable enough to copy into another PydanticAI agent in minutes.
- **Model flexibility** — the same agent runs on OpenRouter, Ollama (local), or OpenAI, underscoring that the pattern isn't tied to the Claude ecosystem.

### Built-in evals and observability

- **Evaluation framework** — PydanticAI ships a robust [[AgentEvaluation]] framework: define YAML test cases (a "golden dataset") with custom evaluators (e.g. assert the correct skill loaded for a question), then run a single cheap smoke test (Cole uses Haiku). Run on every prompt/skill change.
- **Logfire** — the Pydantic team's [[AgentObservability]] tool integrates natively: a few lines instrument every tool call, LLM interaction, token count, and cost as traces, locally and in production.

### Why Cole prefers it

- Less abstraction than [[LangChain]] — closer to "just call the API" with type safety.
- Composes cleanly with LangGraph: each LangGraph node typically wraps one PydanticAI `agent.run()` call.
- Type-safe end to end — Pydantic validates dependencies in, tool args, and structured outputs.

### Use in Archon

Archon's primary code-generation target is PydanticAI agents. Archon ingests the PydanticAI documentation into [[Supabase]] for RAG, then the Coder agent drafts new agents using doc-grounded patterns. Future versions will add LangGraph, LangChain, CrewAI, and LlamaIndex as additional generation targets.

### Framework vs SDK (when to reach for it)

Per `summary-sdk-vs-framework-agents`, PydanticAI is Cole's go-to **framework** when an agent must be fast, cheap, and scalable for production / multi-user use — where a batteries-included [[ClaudeAgentSDK]] is too slow, token-heavy, and subscription-ToS-limited. It buys sub-second responses and full control (including owning your own message history for [[AgentObservability]]). You give up "out of the box" convenience but can add modern niceties yourself (skills, MCP). See [[AgentSDKvsFramework]].

### MCP Sampling (mid-2025)

PydanticAI supports MCP sampling: MCP servers can proxy LLM calls through the client rather than requiring their own API keys. Enabled automatically when running as an MCP client. Distributed tracing in Logfire shows the full call chain across client/server boundaries.

### Pydantic Graph

Part of PydanticAI, Pydantic Graph provides finite state machine functionality for multi-step agent workflows. Uses type annotations to define graph structure (no separate edge-definition functions). Supports snapshotting between nodes for durable execution and debugging. Can generate Mermaid diagrams of graph structure.

### DBOS Integration (early 2026)

One-line durable execution: wrap any PydanticAI agent with `DBOSAgent` for automatic checkpointing of every tool call and agent step to Postgres. Supports parallel workflows and workflow forking.

### Pydantic AI Gateway Integration

Use `gateway/` prefix on model names to route through the unified inference layer. No other code changes needed.

### Monty Integration

PydanticAI agents can use Monty for safe code execution. External functions registered as callbacks enable DuckDB queries, Matplotlib plotting, and arbitrary host functionality from within the sandboxed interpreter.

## Related

- [[LangGraph]] — typical pairing for multi-step workflows
- [[LangChain]] — alternative, criticized by Cole for over-abstraction
- [[Archon]] — primary tool that generates PydanticAI agents
- [[ColeMedin]] — frequent advocate
- [[ModelContextProtocol]] — first-class MCP integration
- [[StructuredOutputs]] — feature used for gatekeeper agents
- [[ToolUse]] — what `@agent.tool` enables
- [[AIAgent]] — what PydanticAI builds
- [[ClaudeSkills]], [[ProgressiveDisclosure]] — pattern reimplemented in the skills-agent template
- [[AgentSDKvsFramework]] — PydanticAI as the framework option vs SDKs
- [[ClaudeAgentSDK]] — the batteries-included alternative
- [[AgentEvaluation]], [[AgentObservability]] — built-in eval framework + Logfire
- [[Monty]] — secure code execution integration
- [[DBOS]] — durable execution integration
- [[PydanticAIGateway]] — unified inference integration
- [[Logfire]] — native observability
- [[SamuelColvin]] — creator
- [[summary-20260129 - Claude Skills Aren't Just for Claude - Here's How to Build Them for ANY Agent]] — skills agent, evals, and Logfire walkthrough
- [[summary-20260326 - Everything You Thought About Building AI Agents is Wrong]] — framework vs SDK decision
