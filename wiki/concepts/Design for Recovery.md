---
title: "Design for Recovery"
type: concept
tags: [agents, error-handling, resilience, long-running-agents, recovery]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition

Design for Recovery is the principle that agent systems must be built to recover from failures mid-execution rather than restarting from the beginning. Unlike traditional software where failed requests are cheap to retry, agent runs can take 5-15 minutes and consume significant compute — restarting wastes resources and loses accumulated context.

## Key Information

- **Traditional software**: HTTP requests were cheap. If a product search failed, you just reran the request — all work was redone, but the cost was negligible
- **Agent systems**: An agent run can take 5-15 minutes. If something breaks mid-flow and you start over, you waste significant compute redoing all previous steps and lose the context that was built up
- **Go's error pattern as inspiration**: Go treats errors as values alongside success values — a function call returns either an error or a value, and both are handled equally. Agent systems should treat errors similarly: as normal inputs to the model
- **Errors must be fed back to the model**: When something fails, provide the error to the LLM as context so it can attempt recovery, try alternative approaches, or work around the failure — rather than triggering a full restart
- **Workarounds and additional checks**: Recovery design includes fallback strategies, retry with different parameters, alternative tool paths, and progressive degradation
- **Keep moving forward**: The goal is to continue progressing through the flow rather than starting over. This preserves context and compute
- **Longer-running agents amplify the need**: The longer an agent runs, the more critical recovery design becomes. Weird failures are inevitable in long-running autonomous systems

## Related

- [[summary-20260530 - Why (Senior) Engineers Struggle to Build AI Agents — Philipp Schmid, Google DeepMind]] — source
- [[PhilippSchmid]] — speaker
- [[Errors as Prompts]] — related concept: error messages as guidance for the model
- [[DurableAgents]] — related concept: agents that survive failures
- [[DurableAgenticLoop]] — Temporal-based approach to durable agent loops
- [[Circuit Breaker Pattern]] — related resilience pattern
- [[Agent Robustness Testing]] — testing recovery paths
- [[Self-healing Agents]] — agents that fix their own failures
