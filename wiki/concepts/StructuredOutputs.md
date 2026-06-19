---
title: "StructuredOutputs"
type: concept
tags: [concept, llm, schema, pydantic, validation]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/02 - 10x Your AI Agents with this ONE Agent Architecture.md"
last_updated: 2026-06-19
---

## Definition

Structured outputs are LLM responses constrained to a specific schema — typically a JSON object matching a predefined Pydantic model or JSON Schema. Instead of getting back free-form prose and parsing it, the runtime guarantees the response will conform to the expected shape, with field types validated.

## Key Information

### Why use structured outputs

- **Downstream consumption** — the next node in an [[AgenticWorkflow]] needs specific fields (a `bool`, a city name, a date). Free-form output requires brittle parsing; structured output guarantees the shape.
- **Conditional branching** — graph routers (e.g. in [[LangGraph]]) need to inspect a field to decide the next node. Reliable parsing is non-negotiable.
- **Validation as feedback** — if the LLM returns invalid JSON, the framework can re-prompt it to fix the structure.

### How [[PydanticAI]] implements it

```python
from pydantic import BaseModel
from pydantic_ai import Agent

class TravelDetails(BaseModel):
    destination: str
    origin: str
    departure_date: str
    return_date: str
    max_hotel_price: float
    response: str
    all_details_given: bool

info_gatherer = Agent(
    model="openai:gpt-4o-mini",
    system_prompt="...",
    result_type=TravelDetails,    # ← the constraint
)
```

The agent's `.run()` / `.run_stream()` returns a validated `TravelDetails` instance, not a string.

### Travel Planner use case

The Info Gatherer agent in the playlist's parallel architecture demo uses structured outputs as a **gatekeeper**:

- `response` → message to show the user.
- `destination`, `origin`, `departure_date`, `return_date`, `max_hotel_price` → fields the downstream parallel sub-agents need.
- `all_details_given: bool` → tells the [[LangGraph]] router whether to proceed to the parallel branch or loop back for more info.

The boolean field is the critical bit: the router uses it to decide between two edges. Without structured outputs, parsing the agent's prose to extract this would be unreliable.

### Streaming structured outputs

When you stream a structured output, you get a partial dict that builds up over time — not a clean string of tokens. PydanticAI handles this via `run_stream()` returning chunks of the partially-built object. Cole demonstrates a debounced JSON-validation pattern: validate the partial dict every ~10ms, render the latest valid `response` field to the UI.

This is harder than streaming text but valuable for chat UIs where the user expects to see the response build up live.

### Trade-offs

- **Pro**: contract enforcement, downstream reliability.
- **Pro**: forces the LLM to think about all required fields up front.
- **Con**: more rigid — sometimes you want flexible prose-and-data hybrid.
- **Con**: implementation across providers varies; PydanticAI normalizes the difference.

### Related but distinct

- **[[ToolUse]]** — also produces structured data (tool-call arguments), but the structure is per-tool and ephemeral. Structured outputs constrain the *final* response.
- **JSON mode** — older, looser constraint where the LLM is asked to "respond in JSON" but without a schema. Structured outputs add the schema validation step.

## Related

- [[PydanticAI]] — implements structured outputs ergonomically in Python
- [[LangGraph]] — typical consumer of structured outputs (router functions branch on them)
- [[AIAgent]] — what produces the structured output
- [[ToolUse]] — adjacent but distinct mechanism
- [[summary-10x-your-ai-agents-parallel-architecture]] — primary use case in this playlist
