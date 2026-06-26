---
title: "PoisonRAG"
type: concept
tags: [security, rag, attack, retrieval, poisoning]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero.md"]
last_updated: 2026-06-26
---

## Definition

PoisonRAG is an attack vector targeting retrieval-augmented generation systems by injecting a tiny number of malicious chunks into a knowledge database, causing the LLM to generate an attacker-chosen answer for a specific target question.

## Key Information

- Published in 2025, demonstrating that poisoning only 5 chunks in an 8-million-document knowledge base is sufficient for a successful attack
- Two conditions must be satisfied: (1) retrieval condition — the target answer must be semantically similar to the user query (solved by appending a potential user query to the target answer), (2) generation condition — malicious chunks must rank high after retrieval (solved by crafting a convincing-sounding answer)
- Any RAG system retrieving from a public database like the internet can be compromised
- Demonstrates the extreme asymmetry of attack: tiny adversarial input can completely override system behavior

## Related

- [[summary-20260416 - $1 AI Guardrails： The Unreasonable Effectiveness of Finetuned ModernBERTs – Diego Carpentero]] — source
- [[RAG]] — the system architecture being attacked
- [[Guardrails]] — defensive mechanism
- [[IndirectPromptInjection]] — related attack vector using external content
