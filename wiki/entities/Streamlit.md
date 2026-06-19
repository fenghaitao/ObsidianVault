---
title: "Streamlit"
type: entity
tags: [tool, framework, python, ui, frontend]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/01 - Build an ARMY of AI Agents on Autopilot with Archon, Here's How.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/02 - 10x Your AI Agents with this ONE Agent Architecture.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/03 - Coding Subagents - The Next Evolution of AI IDEs.md"
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
last_updated: 2026-06-19
---

## Definition

Streamlit is a Python framework for building data and AI app interfaces with minimal frontend code. It's [[ColeMedin]]'s default UI choice for prototyping AI agents — including [[Archon]]'s admin interface and the Travel Planner demo.

## Key Information

### Role in the playlist

- **Archon's admin interface** — the multi-tab Streamlit app for setting environment variables, configuring database, crawling the docs, viewing MCP server logs, and reviewing Archon's roadmap is built in Streamlit.
- **Travel Planner demo UI** — chat interface for interacting with the parallel-agent travel planner.
- **Demo output streaming** — Streamlit's `st.write_stream` (and custom writer integration with [[LangGraph]]) is the mechanism that lets users watch tokens stream in real time as parallel agents emit results.

### Pattern Cole uses

```python
async def invoke_agent_graph(user_input):
    config = {"configurable": {"thread_id": ...}}
    if first_message:
        # Initial state, normal stream call
        async for chunk in graph.astream(initial_state, config, stream_mode="custom"):
            yield chunk
    else:
        # Resume from interrupt
        async for chunk in graph.astream(Command(resume=user_input), config, stream_mode="custom"):
            yield chunk
```

Combined with `st.write_stream(invoke_agent_graph(user_input))` in the Streamlit app, this gives a chat UI with token streaming and human-in-the-loop interruption.

### Why Cole defaults to Streamlit

- Python-only — no JavaScript or React needed for an AI engineer's quick UI.
- First-class async streaming (matches LangGraph's streaming model).
- Trivial to add controls (sliders, file uploads, sidebars) for agent inputs without learning a frontend framework.

## Related

- [[Archon]] — admin UI built in Streamlit
- [[ColeMedin]] — frequent advocate
- [[LangGraph]] — pairs with Streamlit for streaming agent output
- [[PydanticAI]] — agents whose output Streamlit renders
- [[HumanInTheLoop]] — pattern Streamlit + LangGraph `interrupt()` enable
