---
title: "ToolUse"
type: concept
tags: [concept, function-calling, tools, llm, agents]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/01 - Build an ARMY of AI Agents on Autopilot with Archon, Here's How.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/02 - 10x Your AI Agents with this ONE Agent Architecture.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/03 - Coding Subagents - The Next Evolution of AI IDEs.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
last_updated: 2026-06-19
---

## Definition

Tool use (sometimes called "function calling") is the mechanism by which an LLM invokes external functionality. The LLM is given a manifest of tools, each with a name, description, and parameter schema. When the LLM judges a tool relevant, it emits a structured tool-call request; the host runtime executes the tool and feeds the result back into the conversation. Tool use is what turns a chat model into an [[AIAgent]].

## Key Information

### Anatomy of a tool definition

A tool, as the LLM sees it, has three parts:

1. **Name** — short identifier the LLM emits when calling it.
2. **Description (docstring)** — natural-language guidance on *when* and *how* to use this tool. This is the most important part — it's what the LLM reads to decide.
3. **Parameter schema** — the shape of arguments the LLM must produce (typically JSON Schema). Includes per-parameter descriptions for the LLM to reason about what to pass.

```python
@agent.tool
async def search_flights(
    ctx: RunContext[FlightDeps],
    origin: str,
    destination: str,
    date: str,
) -> str:
    """Search for available flights between two cities on a given date.

    Use this when the user asks about flight options, pricing, or schedules.
    """
    ...
```

The docstring becomes the LLM-visible description. The parameter names and types become the schema.

### Tool-call lifecycle

1. **LLM emits tool-call** — name + arguments, in a structured format.
2. **Runtime parses & dispatches** — your code, e.g. PydanticAI, parses the call and invokes the matching Python function.
3. **Tool runs** — function executes, returns a result (typically a string or JSON-serializable object).
4. **Result returned to LLM** — appended to the message history as a `tool_result` (or equivalent role).
5. **LLM continues** — usually emits a final assistant message answering the original user query, optionally with more tool calls.

### Tool-overload problem

The recurring theme of this playlist: LLMs degrade as the number of tools grows. Each tool's description bloats the prompt; the LLM gets confused which one to pick. The fix throughout the playlist is the [[SubAgent]] pattern — split the tool surface across specialized agents so the orchestrator picks among agents (a smaller decision space) and each sub-agent handles a narrow tool set.

### Standardization layers

| Layer | Role |
|---|---|
| OpenAI's function-calling API | Original spec; de facto template the others followed |
| Anthropic's tool use | Same shape, slightly different field names |
| [[ModelContextProtocol]] | Server-side standard for *exposing* tools |
| [[PydanticAI]]'s `@agent.tool` | Python-side ergonomic wrapper |

### Cole's tool-design heuristics

- **Write the docstring for the LLM, not the human.** The docstring is the most-read piece of the tool by the LLM.
- **Use precise parameter names** — they're sent to the LLM as schema field names and influence how it reasons.
- **Keep the parameter set small** — every parameter is more reasoning load.
- **Return strings.** LLMs handle natural-language results best. JSON is fine but prose tends to be cleaner.
- **Optional parameters with sensible defaults** — let the LLM omit when not needed.

### Adjacent concepts

- **Server-side tools** ([[ModelContextProtocol]]) — instead of defining tools per-agent in code, mount a server full of tools.
- **Sub-agent as tool** — wrap an entire agentic workflow as a single "tool" the parent agent invokes. Pattern in Archon-as-MCP-server.
- **[[StructuredOutputs]]** — sometimes you want the agent's *response* shape constrained, not its tool calls. Different mechanism (PydanticAI's `result_type=`).

## Related

- [[AIAgent]] — what tool use enables
- [[ModelContextProtocol]] — protocol for exposing tools at scale
- [[SubAgent]] — pattern for managing tool-overload
- [[StructuredOutputs]] — adjacent constraint mechanism
- [[PydanticAI]] — Python framework wrapping tool-use ergonomically
- [[OpenAI]] — author of the original function-calling spec
- [[Anthropic]] — provides MCP and Claude tool use
