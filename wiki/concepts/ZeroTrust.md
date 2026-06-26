---
title: "ZeroTrust"
type: concept
tags: [security, architecture, principle, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero.md"]
last_updated: 2026-06-26
---

## Definition

Zero Trust is a mature security principle whose core rule is "trust nothing, verify everything." In the context of LLM-based AI systems, there is a fundamental "zero trust gap" because LLMs natively lack separation of concerns between system controls (trusted instructions) and data (untrusted user/external input).

## Key Information

- The industry has followed Zero Trust principles for many years in traditional security architectures
- LLMs natively have "nothing out of it" — no built-in mechanism to distinguish trusted developer instructions from untrusted data
- This gap is the root cause enabling all major LLM attack vectors: prompt injection, indirect injection, RAG poisoning, MCP exploitation, and agentic attacks
- AI-based decisions can be overruled by the very data being evaluated, violating the Zero Trust principle
- Attackers don't need code or direct infrastructure access — they just need to place malicious instructions and wait for an LLM to fetch them
- Closing the zero trust gap requires external defensive layers (guardrails, discriminators, constrained decoding) since it cannot be solved by model alignment alone

## Related

- [[summary-20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero]] — source
- [[Guardrails]] — defensive mechanism to enforce zero trust
- [[PromptInjection]] — attack exploiting the zero trust gap
- [[DeterministicGuardrails]] — implementation approach for zero trust enforcement
