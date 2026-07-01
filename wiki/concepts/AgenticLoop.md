---
title: "Agentic Loop"
type: concept
tags: [agents, llm, loop, temporal, openai, architecture]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - MCP = Mega Context Problem - Matt Carey.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260501 - Agents on the Canvas in tldraw — Steve Ruiz, tldraw.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - Human-in-the-Loop Automation with n8n — Liam McGarrigle.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260527 - Why Rust is the Ideal Language for Vibe-Coding — Daniel Szoke, Sentry.md"]
last_updated: 2026-06-30
---

## Definition
The agentic loop is the core execution pattern where an LLM has agency — it decides the flow of the application by choosing which tools to call and when to stop. Each `runner.run()` call in the OpenAI Agents SDK corresponds to an independent agentic loop: the LLM is called, it may decide to invoke tools, the tool results are routed back to the LLM, and the cycle continues until the LLM decides it's done.

## Key Information
- **LLM agency**: The defining characteristic — the LLM, not the developer, decides the application flow
- **Distinction from GenAI apps**: A GenAI application becomes an agent when the LLM has agency over the flow
- **Standard pattern**: The agentic loop is fairly standardized across frameworks; what varies is what gets inserted into the loop (tools, guardrails, handoffs)
- **Loop structure**: Call LLM → LLM decides to invoke tools or finish → if tools, execute them → route results back to LLM → repeat
- **Runner.run()**: In the OpenAI Agents SDK, each `runner.run()` is its own independent agentic loop
- **Handoffs**: When using handoffs, there is still only one agentic loop — the context/persona changes but the loop continues
- **Temporal integration**: By wrapping the agentic loop in a Temporal Workflow and tool calls in Temporal Activities, the loop becomes durable — crash recovery, retries, and scaling are automatic
- **Generic implementation**: Using Temporal's dynamic activities, a single agentic loop workflow can work with any set of tools by looking up tool handlers by name at runtime

### Stateless Agent Loop (Matt Carey)
- Cloud-native approach where agent state can be toggled on/off
- Essential when scaling to 100 agents per person — local sandboxes for every agent become unsustainable
- Related to the Stateless Transport Protocol for MCP, enabling MCP servers to be treated like stateless REST servers

### Demand-Driven Context Extension
- The standard agentic loop is extended with a failure-and-curation cycle: after the LLM decides it's done (or can't proceed), it surfaces knowledge gaps, requests input from domain experts, and curates new knowledge for future loops
- This transforms the agentic loop from pure execution into a knowledge-building cycle

### Compile-Fix Loop (Daniel Szoke)
- A specialized agentic loop for compiled languages: the agent generates code, compiles it, reads compiler errors, fixes the code, and repeats until compilation succeeds
- Each compiler error resolved is potentially a production bug prevented
- This loop leverages the compiler as a deterministic guardrail — the compiler catches what the LLM misses
- Rust's detailed compiler errors make this loop particularly effective: errors explain what went wrong and how to fix it
- Szoke argues this makes Rust the ideal vibe coding language: harder first-try generation but safer overall outcome
- The compile-fix loop is faster and more thorough than waiting for AI code review

## Related
- [[AgentLoop]] — distinct concept: Claude Agent SDK's three-part loop (gather, act, verify)
- [[DurableAgenticLoop]] — the Temporal-durable version
- [[Stateless Agent Loop]] — cloud-native scaling pattern
- [[OpenAIAgentsSDK]] — the framework
- [[MicroAgents]] — multiple agentic loops orchestrated together
- [[AgentHandoffs]] — context switching within a single agentic loop
- [[DynamicActivity]] — enabling generic tool sets in the loop
- [[summary-20260112 - OpenAI + @Temporalio ： Building Durable, Production Ready Agents - Cornelia Davis, Temporal]] — source
- [[summary-20260425 - MCP = Mega Context Problem - Matt Carey]] — source (stateless agent loops)
- [[summary-20260501 - Agents on the Canvas in tldraw — Steve Ruiz, tldraw]] — source (canvas-based agentic loop)
- [[summary-20260505 - Demand-Driven Context： A Methodology for Coherent Knowledge Bases Through Agent Failure]] — source
- [[StatelessTransportProtocol]] — related MCP transport proposal
- [[Agents on Canvas]] — spatial visualization of agentic loops
- [[Fairies]] — multi-agent canvas implementation using agentic loops
- [[DemandDriven Context]] — methodology extending the agentic loop
- [[summary-20260527 - Why Rust is the Ideal Language for Vibe-Coding — Daniel Szoke, Sentry]] — source (compile-fix loop)
- [[CompilerGuardrails]] — the deterministic safety net in the compile-fix loop
- [[Rust]] — language where the compile-fix loop is most powerful
- [[VibeCoding]] — the practice the compile-fix loop is argued to improve
