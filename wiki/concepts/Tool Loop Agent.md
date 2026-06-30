---
title: "Tool Loop Agent"
type: concept
tags: [ai-sdk, agents, vercel, agent-runtime, tools]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Give Your Agent a Computer — Nico Albanese, Vercel.md"]
last_updated: 2026-06-30
---

## Definition
The Tool Loop Agent is the core agent primitive in AI SDK v6. It is an object-oriented agent class that encapsulates model configuration, instructions, tools, and call options into a reusable definition. The agent manages the tool-calling loop — sending messages to the LLM, receiving tool calls, executing tools, and feeding results back — abstracting this complexity from the developer.

## Key Information
- **Import**: `import { ToolLoopAgent } from "ai"`
- **Minimal Definition**: Requires a model (string or provider instance) and tools. Instructions and call options schema are optional.
- **Model Specification**: Uses the global provider pattern — by default the AI Gateway — allowing model specification via plain strings like `"gpt-5-4-mini"`. Can override with any provider instance.
- **Instructions**: Passed as the `instructions` parameter. These are the system prompt. Still critical in 2026 for influencing agent behavior alongside the runtime and computer.
- **Tools**: Passed as `tools` parameter. Can include custom tools, provider-defined tools, and provider-executed tools.
- **Call Options Schema**: Optional Zod schema (`callOptionsSchema`) for structured inputs that vary per invocation (e.g., sandbox instance, customer tier).
- **Streaming**: Agents expose a `.stream()` method. For Next.js, `createAgentUIStreamResponse` handles the streaming response.
- **Separation of Concerns**: The agent definition (model, tools, instructions) lives in one file (e.g., `lib/agent.ts`), while streaming logic lives in the route handler (e.g., `app/api/chat/route.ts`). This prevents the 2,000-line route handlers common in AI SDK v4.
- **Platform Agnostic**: Plain JavaScript — works in Next.js, Bun, or any JavaScript runtime.
- **Naming**: Named by Lars (German engineer, AI SDK lead). Nico describes it as "one of our shorter APIs" and "quite obvious as to what it does — it is a tool loop using agent."

## Related
- [[summary-20260512 - Give Your Agent a Computer — Nico Albanese, Vercel]] — source
- [[AISDK]] — the framework
- [[Vercel]] — creator
- [[AgentLoop]] — the general agent execution pattern
- [[AgenticLoop]] — the broader concept of tool-using agent loops
- [[Call Options Schema]] — companion pattern for structured inputs
- [[Prepare Call]] — lifecycle callback
- [[Prepare Step]] — lifecycle callback
- [[Agent Runtime Context]] — state sharing pattern used within tool loop agents
- [[Last Gammel]] — AI SDK lead
