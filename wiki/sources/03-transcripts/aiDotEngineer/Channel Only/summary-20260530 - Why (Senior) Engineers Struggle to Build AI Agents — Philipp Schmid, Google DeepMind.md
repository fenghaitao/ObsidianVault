---
title: "summary-20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind"
type: source
tags: [source, transcript, agent-engineering, non-determinism, evals, error-handling, api-design, agent-iterative-loop, context-as-state, google-deepmind]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Core Summary

Philipp Schmid of Google DeepMind presents five fundamental differences between traditional software engineering and building AI agents, explaining why even senior engineers struggle with the transition. Traditional software follows a spec → code → test → deploy pipeline where the developer acts as a **traffic controller** with full control over every step. Agent engineering is a fundamentally different paradigm where the developer becomes a **dispatcher**: you define the goal but not the exact steps, then iteratively observe, adjust prompts/tools, and rerun. The five shifts are: (1) text/context replaces structured data as state, (2) handing over control to non-deterministic LLM decisions instead of predefined workflows, (3) treating errors as normal inputs rather than restart triggers, (4) moving from deterministic unit tests to statistical evals, and (5) building self-documenting, agent-ready APIs instead of assuming human developer context. The core principles: trust but verify, stop fighting the model, preserve meaning, design for recovery, evaluate don't just assert, and build to delete.

## Key Points

- **Traditional vs Agent Engineering**: Traditional software is like a traffic controller (control over every street light, speed, road). Agents are like a dispatcher (define the destination, not the route). The agent may take weird paths but still achieve the outcome
- **1. Text is the New State**: Traditional software used Boolean flags and data structures. LLMs understand semantic meaning, enabling dynamic, context-rich interactions. Example: a deep research plan can be approved while simultaneously providing additional constraints (focus on US market, ignore California) — no multi-step decline/replan cycle needed. Memory and personalization (e.g., Celsius vs Fahrenheit for cooking) can't be mapped to static flags
- **2. Hand Over Control**: Traditional customer support used classification models → predefined workflows (detect churn intent → run cancellation flow). Agents can dynamically understand meaning and offer alternatives mid-conversation, changing the entire intent. All possible stateful workflow branches can't be pre-modeled. We must trust the LLM rather than working in purely deterministic environments
- **3. Errors Are Just Inputs**: In traditional software, a failed HTTP request was cheap — just rerun. Agent runs can take 5-15 minutes; restarting from the beginning wastes compute and loses context. Errors must be fed back to the model as normal inputs with recovery guidance, similar to Go's pattern of treating errors as values alongside success values
- **4. From Unit Tests to Evals**: Traditional software guarantees input A → output C. Agents are non-deterministic — the same input can produce different steps and results. Success must be measured statistically (how often does it work?) rather than asserted deterministically. A customer agent that works 1/10 times is useless in production. Results are subjective (research reports, customer feedback) — requiring LLM-as-judge or human expert evaluation. Trace what the agent does, but measure success on the outcome
- **5. Agents Evolve, APIs Don't**: API endpoints feel self-explanatory to the developers who built them (e.g., `delete_item`), but agents see only function schemas and docstrings — no years of context. Tools must be built with self-documenting semantic interfaces designed for agent consumption, not assuming long-term developer expertise
- **Core Principles**: (a) Trust but verify — give agents autonomy but validate outcomes; (b) Stop fighting the model — don't force rigid step-by-step workflows; (c) Preserve meaning — everything is context now, not well-defined data structures; (d) Design for recovery — long-running agents will encounter weird failures; (e) Evaluate, don't just assert — find the right reliability balance; (f) Build to delete — the bitter lesson: software is disposable, we'll rebuild with better models

## Related

- [[PhilippSchmid]] — speaker, Google DeepMind
- [[GoogleDeepMind]] — employer
- [[Gemini API]] — the platform Philipp works on
- [[Text as State]] — concept: text replaces data structures as application state
- [[Handing Over Control]] — concept: trusting LLM decisions over predefined workflows
- [[Traffic Controller vs Dispatcher]] — concept: the paradigm shift metaphor
- [[ErrorsAsPrompts]] — concept: treating errors as normal inputs for recovery
- [[NonDeterministicAgents]] — concept: why unit tests don't work for agents
- [[Design for Recovery]] — concept: building agents that recover from failures
- [[Trust But Verify]] — concept: give autonomy but validate outcomes
- [[Build to Delete]] — concept: disposable software and the bitter lesson
- [[Stop Fighting the Model]] — concept: don't force rigid workflows on LLMs
- [[Preserve Meaning]] — concept: everything is context now
- [[Evaluate Dont Just Assert]] — concept: statistical evaluation mindset for agents
- [[DeveloperExperienceForAgents]] — concept: building APIs for agent consumption
- [[AgenticLoop]] — concept: the iterative observe-adjust-rerun cycle
- [[EvalPrimitives]] — concept: measurement as essential for agent reliability
