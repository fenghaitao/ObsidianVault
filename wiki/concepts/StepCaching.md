---
title: "Step Caching"
type: concept
category: methodology
tags: [caching, workflow, optimization, denoising]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna.md"]
last_updated: 2026-06-30
---

# Step Caching

## Definition

Step caching is the automatic persistence of step inputs and outputs in a workflow system. When a step is invoked, the system records the input as an event; if the step completes successfully, the output is cached. On retry or workflow replay, cached steps are skipped entirely, and only failed or new steps are executed. In the context of image/video generation, step caching can also refer to techniques that reduce the number of denoising steps required by caching intermediate results, enabling faster generation without full recomputation.

## Key Information

- **How it works** (workflow context):
  - When a step is called, the workflow registers the input as an event
  - The step executes in its own isolated instance
  - On success, the output is cached and associated with that step invocation
  - On retry or replay, the workflow checks the cache: if a step with the same inputs already completed, it returns the cached output without re-execution
- **Benefits**:
  - Failed steps can be retried without re-executing all prior steps
  - Workflows can `sleep` for days and resume from the exact point without replay cost
  - State rehydration is instantaneous -- the workflow just reads cached outputs
- **Storage**: In production, caches can be backed by Redis, Postgres, or any storage adapter; locally, they use files
- **Observability**: Every cached step is visible in the workflow UI with its inputs and outputs
- **Denoising step caching**: [[Pruna]] uses caching methods alongside [[ModelDistillation]] to reduce denoising steps in image/video models from 50 down to 4-20, a key technique for building [[Performance Models]]

## Related

- [[WorkflowPattern]]
- [[WorkflowDevKit]]
- [[DeterministicWorkflows]]
- [[DurableAgents]]
- [[summary-20260601 - 20 days of compute vs 7 hours： rethinking what state-of-the-art means — Bertrand Charpentier, Pruna]] — source (denoising step caching)
- [[Pruna]] — uses caching for denoising step reduction
- [[Performance Models]] — concept enabled by step caching
- [[ModelDistillation]] — complementary technique for step reduction
- [[Model Efficiency]] — the broader goal
