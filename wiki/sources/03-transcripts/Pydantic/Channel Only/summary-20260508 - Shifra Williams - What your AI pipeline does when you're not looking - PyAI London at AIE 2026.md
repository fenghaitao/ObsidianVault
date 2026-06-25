---
title: "summary-20260508 - Shifra Williams - What your AI pipeline does when you're not looking - PyAI London at AIE 2026"
type: source
tags: [source, pydantic, pyai-london, render, observability, rag]
sources: ["raw/03-transcripts/Pydantic/Channel Only/20260508 - Shifra Williams - What your AI pipeline does when you're not looking - PyAI London at AIE 2026.md"]
last_updated: 2026-06-25
---

## Core Summary

Shifra Williams (Render) demos an observable RAG pipeline deployed on Render using PydanticAI, Logfire, and Pydantic's embedder. The pipeline performs multi-query retrieval with claims verification: embed the question, retrieve docs, build an answer, isolate each claim, and verify against source context. Tracks costs per stage using Pydantic GenAI prices. Deployed via render.yaml with zero-downtime deploys. Even when the database was empty (broken demo), the agent still provided useful answers at ~80% value.

## Key Points

- Observable RAG pipeline: question embedding -> multi-query retrieval -> answer generation -> claims extraction -> claims verification
- Cost tracking per pipeline stage using Pydantic GenAI prices from GitHub
- Logfire auto-instruments OpenAI, PydanticAI, and async processes globally
- Render Workflows (new service in open beta): durable, resilient, long-running with checkpoint and recovery
- render.yaml: simple declarative infra config with auto-injected database secrets
- Broken demo still useful: agent without context still gave correct high-level deployment advice
- Free credits offered for Render signups

## Related

- [[Render]] — deployment platform
- [[Logfire]] — observability
- [[PydanticAI]] — agent framework
- [[RetrievalAugmentedGeneration]] — the RAG pattern demonstrated
