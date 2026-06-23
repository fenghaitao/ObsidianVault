---
title: "Guardrails"
type: concept
tags: [concept, agents, safety, validation, production]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20250526 - How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap).md"
last_invocations: 2026-06-19
last_updated: 2026-06-19
---

## Definition

Guardrails are validation and filtering layers wrapped around an [[AIAgent]]'s inputs and outputs to constrain what gets in and what gets out. [[ColeMedin]] calls guardrails one of the most important reliability primitives — without them, the unpredictability gap between traditional automations and AI agents stays open.

## Key Information

### Two-sided pattern

| Side | Purpose | Examples |
|---|---|---|
| **Input guardrails** | Reject or sanitize bad prompts before the agent sees them | PII detection, prompt-injection filters, off-topic rejection, rate limiting per user, jailbreak pattern detection |
| **Output guardrails** | Reject or sanitize bad responses before users see them | Toxic content filter, fact-check against authoritative source, schema validation, hallucination detection on grounded queries |

### Why both halves matter

Cole's framing: with traditional automations, the inputs and outputs were typed. The system literally couldn't accept a malformed input or emit a malformed output. With agents driven by natural-language LLMs, both ends become trust boundaries.

- **Input guardrails** prevent garbage-in: a user trying to extract your system prompt, off-topic queries that waste tokens, prompt-injection attacks via included documents, and so on.
- **Output guardrails** prevent garbage-out: factually wrong but confident answers, toxic outputs, JSON that's almost-but-not-quite valid, responses that violate a content policy.

### Implementation patterns

- **Rule-based filters**: regex, blocklists, schema validators ([[StructuredOutputs]] is a form of output guardrail).
- **Classifier guardrails**: small fast LLMs or trained classifiers gate the input/output.
- **Adjacent agent**: a separate "validator" agent reviews the primary agent's output before it goes to the user. Sometimes plays the role Cole calls a "synthesizer-as-validator" in [[ParallelAgentArchitecture]].
- **Fallback mechanisms**: if the primary agent's output fails the guardrail, fall back to a safer (typically smaller, more constrained) agent or a canned response.

### Where guardrails sit in the stack

In Cole's [[summary-20250526 - How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap)]], guardrails appear in **Phase 5 (advanced architecture)** — after you've built coded agents but before deploying. Cole's framing: prototype agents don't need guardrails; production agents *cannot ship* without them.

### Connection to [[AgentObservability]] and [[AgentEvaluation]]

- **Observability** lets you see when guardrails fired (and why).
- **Evaluation** lets you measure whether guardrails over- or under-trigger.
- A good guardrail catches real problems without filtering legitimate traffic; only evaluation tells you which mode you're in.

## Related

- [[AIAgent]] — what's being protected
- [[AgentEvaluation]] — measures guardrail effectiveness
- [[AgentObservability]] — surfaces guardrail activity
- [[StructuredOutputs]] — one form of output guardrail
- [[ColeMedin]] — author of the framing here
- [[summary-20250526 - How I'd Learn AI Agents FAST if I Had to Start Over (Full Roadmap)]] — primary source (phase 5)
