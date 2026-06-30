---
title: "Give Your Agent a Computer — Nico Albanese, Vercel"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260512 - Give Your Agent a Computer — Nico Albanese, Vercel.md"
date: 2026-05-12
ingested: 2026-06-30
tags: [agents, ai-sdk, vercel, sandbox, tools, bash, memory, workshop, sub-agents]
---

## Core Thesis
Nico Albanese presents the three core building blocks for building agents in 2026: (1) an agent runtime (the harness managing the loop and context), (2) tools passed into that runtime, and (3) a computer/sandbox file system for the agent to persist state and execute code. The talk is a live workshop building an agent with the AI SDK v6, starting from a basic chatbot, adding web search as context augmentation, giving the agent a Vercel Sandbox with a bash tool, and finally implementing persistent file-system-based memory.

## Key Topics
- **Three Building Blocks of Agents (2026)**: Agent runtime (loop management, context between steps), tools (custom, provider-defined, provider-executed), and a computer/sandbox file system for state persistence and code execution.
- **AI SDK v6 Tool Loop Agent**: The `ToolLoopAgent` is a reusable, object-oriented agent primitive. Define it once with a model, instructions, and tools, then use it across any JavaScript runtime (Next.js, Bun, etc.). This separates agent definition from streaming concerns.
- **Global Provider**: AI SDK v6 introduces a global provider concept — by default the AI Gateway — allowing model specification via plain strings like `"gpt-5-4-mini"` without importing provider-specific packages. Can be overridden with any provider.
- **Three Types of Tools**: (1) Custom tools — developer-defined with description, input schema, execute function. (2) Provider-defined tools — LLM providers post-train models to use effectively (e.g., Anthropic's bash tool, computer use tool); developer provides the execute function but the provider crafts the description/schema. (3) Provider-executed tools — exist in the LLM provider's infrastructure (e.g., web search); developer opts in and the provider handles execution and returns results.
- **Web Search as Context Augmentation**: Using OpenAI's web search provider-executed tool to give agents access to real-time information. Supports parameters like user location for localized results.
- **End-to-End Type Safety**: The agent definition is the source of truth. `InferAgentUIMessage` creates fully typed messages based on agent tools. This types flows through route handlers into `useChat` and down to UI component rendering with typed tool inputs/outputs.
- **Vercel Sandbox — Named Persistent Sandboxes**: Each sandbox has a name, and each sandbox can have sessions (instances). Referencing a sandbox by name either routes to an active instance or spins up a new one. After inactivity timeout, the sandbox spins down but snapshots the file system — subsequent requests spin up a new instance with the snapshot, making it feel like the same machine. This eliminates complex lifecycle management (tarring file systems, storing in blob storage, etc.).
- **Bash as Universal Tool**: For the entire workshop, only one tool is used — bash. Agents are very good at writing bash commands. The bash tool pulls the sandbox from the agent runtime context and executes commands, returning stdout, stderr, and exit code.
- **Agent Runtime Context**: Similar to React context — arbitrary data/variables/functions can be passed into a context object and accessed in tool execute functions during the agent run. The `prepareCall` function injects call options (like sandbox) into the runtime context.
- **Call Options Schema**: A Zod schema on the agent definition for structured inputs that change at call time (e.g., sandbox instance, customer ID, model selection based on user tier). Type-safe options are required when calling the agent via `createAgentUIStreamResponse`.
- **File System Memory**: Memory implemented as a `memories.md` file in the sandbox. The agent reads it via `prepareCall` and injects it into the system prompt. The agent writes new memories to the file using bash. Key insight: bash tools let agents use `find`, `ls`, `grep`, `glob` to search and manage memory deterministically.
- **Self-Extending Agents**: Agents can generate Python scripts for repeatable tasks (e.g., weather lookup), store them in the sandbox, and reuse them in future invocations. This creates agents that learn and build on themselves over time.
- **Context Compaction vs. Input Cache**: Compacting (removing old messages) invalidates the input cache. With million-token context windows, Nico finds compaction unnecessary — his coding agent ran for 104 minutes with 316 tool calls using only 32% of GPT-4's context window with a 95% cache token read ratio. Sub-agents are preferred over compaction: delegate independent work to sub-agents that return only ~500 token summaries.
- **Sub-Agents for Context Management**: Delegating independent pieces of work to sub-agents off the main context thread and receiving just a summary (~500 tokens) back. Nico's personal coding agent uses this pattern with durable workflow steps, used by 23 people at Vercel, processing 3.8 billion tokens with a 91% cache read ratio, responsible for ~350 PRs.
- **Prepare Call and Prepare Step**: `prepareCall` runs once at the start of an agent invocation (used to fetch memories from sandbox). `prepareStep` runs before every step in the agent loop, allowing modification of messages, model, or other parameters mid-run (e.g., sliding window filtering based on step number).
- **Instructions and System Prompts**: Even in 2026, system prompts remain crucial — they work alongside the runtime and computer to influence agent behavior. Nico demonstrates the "pink elephant problem" where mentioning unwanted behavior (e.g., "don't save greetings") actually triggers it.

## Entities
- [[NicoAlbanese]] — speaker, works on AI SDK at Vercel
- [[Vercel]] — company, creator of AI SDK and Vercel Sandbox
- [[VercelSandbox]] — named persistent sandbox service (beta)
- [[AISDK]] — the AI SDK (v6), TypeScript toolkit for building AI applications
- [[OpenAI]] — LLM provider, web search tool
- [[Anthropic]] — LLM provider, provider-defined tools (bash, computer use)
- [[Cursor]] — referenced for background agents
- [[Last Gammel]] — AI SDK lead ("the mastermind behind the AI SDK")
- [[GPT-5]] — model family used (GPT-5-4-Mini, GPT-4)

## Concepts
- [[Tool Loop Agent]] — AI SDK v6 agent primitive
- [[Persistent Sandboxes]] — named sandboxes with session-based state snapshots
- [[Call Options Schema]] — Zod schema for structured call-time agent inputs
- [[Agent Runtime Context]] — React-context-like pattern for sharing state across tools
- [[Provider-Executed Tools]] — tools executed on LLM provider infrastructure
- [[File System Memory]] — using file system as persistent agent memory via bash
- [[Prepare Call]] — AI SDK callback running once per agent invocation
- [[Prepare Step]] — AI SDK callback running before each agent loop step
- [[Input Cache vs Compaction]] — tradeoff between context compaction and cache invalidation
- [[SubAgents]] — delegating work to sub-agents for context management
- [[AgentLoop]] — the core agent execution cycle
- [[BashTool]] — bash as universal agent tool in sandboxes
- [[Agent Memory]] — memory systems for agents
- [[Agent Sandbox]] — sandboxed execution environments
- [[Global Provider]] — AI SDK v6 global provider pattern
- [[End-to-End Type Safety in Agents]] — type flowing from agent definition to UI
- [[AgenticLoop]] — the tool-using agent execution pattern

## Related
- [[summary-20260106 - Building durable Agents with Workflow DevKit & AI SDK - Peter Wielander, Vercel]] — related AI SDK + Workflow DevKit talk
- [[summary-20260420 - The New Application Layer - Malte Ubl, CTO Vercel]] — Vercel's agent traffic data
- [[summary-20260428 - Building your own software factory — Eric Zakariasson, Cursor]] — background agents
- [[summary-20260510 - How we solved Context Management in Agents — Sally-Ann Delucia]] — context management techniques
