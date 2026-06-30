---
title: "AgentHarnessComponents"
type: concept
tags: [agents, harness, architecture, design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260517 - Harnesses in AI： A Deep Dive — Tejas Kumar, IBM.md"]
last_updated: 2026-06-30
---

## Definition
Agent Harness Components are the six standard building blocks of an AI agent harness as defined by Tejas Kumar: (1) Tool Registry, (2) Model, (3) Context Management, (4) Guardrails, (5) Agent Loop, and (6) Verify Step. Together these form "everything around the model that gives it grounding in reality."

## Key Information

### 1. Tool Registry
The set of tools the agent can invoke — reading from the file system, writing, executing bash commands, browser navigation. Defined using OpenAI SDK tool format with name, description, parameters, and execute function.

### 2. Model
The LLM itself — the black box component being harnessed. The harness should work irrespective of which model is used. Cheap models (GPT-3.5 Turbo, GPT-OSS) can succeed with a strong harness.

### 3. Context Management
Primitives for managing and compacting context windows. Includes naive strategies (keep system prompt + user prompt + last 2 messages, trim everything in between) and more sophisticated approaches. The harness compacts context to prevent overflow.

### 4. Guardrails
Safety constraints: max iterations (kill the run if too many steps), max messages (compress context if too many messages), max attempts (give up after N tries). Guardrails are composable and run deterministically in the harness, not in the LLM.

### 5. Agent Loop
The execution loop that runs the agent. The harness can wrap this in an outer loop — for example, an N-attempt loop that retries the entire agent run up to max attempts. The agent loop pushes events into a trace/history for later verification.

### 6. Verify Step
Deterministic post-execution checks that inspect the agent's tool call history (traces) to verify actual success. Examples: checking if a browser click on the upvote button actually succeeded, detecting failed login attempts by inspecting tool names and messages. The verify step removes the LLM's ability to lie about outcomes.

## Related
- [[summary-20260517 - Harnesses in AI： A Deep Dive — Tejas Kumar, IBM]] — source
- [[AgentHarness]] — the overall concept
- [[TejasKumar]] — defined the six components
- [[Guardrails]] — component #4
- [[AgentLoop]] — component #5
- [[ContextManagement]] — component #3
- [[ContextCompression]] — part of context management
- [[LoginHandler]] — a harness function that hooks into the agent loop
- [[Verification in Agentic Loops]] — the verify step concept
- [[ToolCalling]] — tool registry in practice
- [[Harness Engineering]] — related discipline
