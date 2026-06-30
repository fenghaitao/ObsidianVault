---
title: "Call Options Schema"
type: concept
tags: [ai-sdk, agents, zod, type-safety, architecture]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Give Your Agent a Computer — Nico Albanese, Vercel.md"]
last_updated: 2026-06-30
---

## Definition
Call Options Schema is an AI SDK v6 pattern for defining structured, type-safe inputs that are passed to an agent at call time (rather than at definition time). It uses Zod schemas to declare what dynamic parameters an agent expects per invocation, and the type safety flows end-to-end from the agent definition through the route handler to the UI.

## Key Information
- **Syntax**: `callOptionsSchema: z.object({ sandbox: z.instanceof(Sandbox) })` on the `ToolLoopAgent` definition.
- **Purpose**: Allows agents to accept dynamic inputs that change per invocation — sandbox instances, customer IDs, user tiers, model selection, etc. — without resorting to functional factory patterns (`createAgent(input)`).
- **Type Safety**: The schema creates a type-safe contract. In the route handler, `createAgentUIStreamResponse` requires the `options` key to match the schema. Missing required options produce TypeScript errors.
- **Use Cases**:
  - **Customer tier-based model selection**: Pass customer tier to select GPT-5-4-Mini for free users vs. GPT-5-4-Pro for premium users
  - **Sandbox injection**: Pass the sandbox instance the agent should interact with
  - **Session/user context**: Pass user ID, session data, or other runtime context
- **Access in Agent**: Call options are accessed in the `prepareCall` function via `callOptions`, which can then inject values into the agent runtime context for use by tools.
- **Contrast with Old Pattern**: Previously, developers used functional factories: `const createAgent = (input) => new Agent({...})` with if-statements for configuration. Call options schema makes this declarative and type-safe.
- **Reacts to Community Feedback**: Nico noted this feature was built because "it frustrated some people online" who found the functional approach cumbersome.

## Related
- [[summary-20260512 - Give Your Agent a Computer — Nico Albanese, Vercel]] — source
- [[AISDK]] — the framework
- [[Tool Loop Agent]] — the agent primitive using this pattern
- [[Agent Runtime Context]] — where call options are injected for tool access
- [[Prepare Call]] — lifecycle callback where call options are processed
- [[End-to-End Type Safety in Agents]] — the broader type safety system
