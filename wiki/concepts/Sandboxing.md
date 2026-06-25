---
title: "Sandboxing"
type: concept
tags: [security, code-execution, agents, infrastructure]
sources: [raw/03-transcripts/Pydantic/Channel Only/20260401 - Samuel Colvin Controlling the wild： Monty, from tool calling to computer use - PyAI Conf 2026.md]
last_updated: 2026-06-25
---

## Definition

Sandboxing is the practice of running untrusted code in an isolated environment to prevent it from accessing the host system. Critical for AI agents that execute generated code. Approaches range from full VMs (Docker, Daytona, E2B) to from-scratch interpreters (Monty, QuickJS).

## Key Information

- Full VM sandboxes (Docker, Daytona, E2B, Modal) are expensive at scale and problematic for enterprises
- From-scratch interpreters (Monty, QuickJS) offer a middle ground: start with nothing, add capabilities
- White-list approach is safer than blacklisting from a full VM
- Monty: ~1 microsecond startup vs ~1 second for sandbox VMs
- Sandboxing is a central primitive for ambient agents that run autonomously

## Related

- [[Monty]] — Pydantic's secure Python interpreter
- [[CodeExecution]] — the paradigm sandboxing enables
- [[AgentInfrastructure]] — sandboxing as a key primitive
