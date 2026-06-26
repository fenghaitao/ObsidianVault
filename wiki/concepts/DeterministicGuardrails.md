---
title: "DeterministicGuardrails"
type: concept
tags: [agentic-tools, security, validation, guardrails]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz.md"]
last_updated: 2026-06-26
---

## Definition
Deterministic guardrails are non-agentic, rule-based validation checks inserted into agentic tool invocations to enforce safety and correctness constraints on sensitive or mission-critical operations, preventing agents from taking harmful actions even when they ignore instructions.

## Key Information
- Agents are non-deterministic and can ignore instructions due to phenomena like needle-in-the-haystack and lost-in-the-middle.
- Guardrails intercept tool invocations before execution, validate parameters against deterministic rules, and block invalid calls with friendly agent-facing error messages.
- The error messages guide the agent to retry with corrected parameters rather than crashing the entire workflow.
- In Baz's spec reviewer example, a path validation guardrail ensures screenshots are only saved within an allowed directory, preventing agents from writing files to arbitrary locations.
- Particularly important for multi-tenant architectures where agents might not understand folder/database/schema boundaries and could leak data between clients.
- Guardrails are implemented by wrapping the tool's callable function with pre-invocation validation logic.

## Related
- [[summary-20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz]] — source
- [[ThirdPartyToolOptimization]] — parent framework
- [[ToolComposition]] — related practice (composed tools can include guardrails)
- [[Sandboxing]] — related security concept
- [[PromptInjection]] — related security concern
