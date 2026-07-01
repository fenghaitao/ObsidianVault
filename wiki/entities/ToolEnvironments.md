---
title: "ToolEnvironments"
type: entity
tags: [reinforcement-learning, environments, verifiers, tool-calling, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Let LLMs Wander： Engineering RL Environments — Stefano Fiorucci.md"]
last_updated: 2026-06-30
---

## Definition
Tool environments are RL environments in Verifiers where the language model is equipped with callable tools (defined as Python functions). The model can invoke tools during rollouts, receive results, and continue reasoning until it produces a final response without tool calls.

## Key Information
- **Built on multi-turn**: Tool environments extend the multi-turn foundation with tool calling
- **Tool definition**: Tools are defined as Python functions accessible to the model during rollouts
- **Interaction pattern**: Each turn consists of the model's response followed by the environment's tool execution
- **MCP integration**: The MCP environment type automatically connects to Model Context Protocol servers to expose their tools
- **Stateful tool variant**: For tools needing per-rollout persistent state (e.g., database connections, session IDs)
- **Recursive LM support**: A class implementing recursive language models — an inference strategy where LMs decompose and recursively interact with input context through REPL environments
- **Wiki search example**: A realistic example demonstrating tool use in Verifiers
- Enables agents that can run code, query APIs, and solve multi-step tasks within RL environments

## Related
- [[MultiTurnEnvironments]] — foundation type
- [[Verifiers]] — library providing this abstraction
- [[MCP]] — protocol for connecting to external tool servers
- [[summary-20260408 - Let LLMs Wander： Engineering RL Environments — Stefano Fiorucci]] — source
