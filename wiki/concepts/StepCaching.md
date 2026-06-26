---
title: "Step Caching"
type: concept
category: methodology
---

# Step Caching

## Definition

Step caching is the automatic persistence of step inputs and outputs in a workflow system. When a step is invoked, the system records the input as an event; if the step completes successfully, the output is cached. On retry or workflow replay, cached steps are skipped entirely, and only failed or new steps are executed.

## Key Information

- **How it works**:
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

## Related

- [[WorkflowPattern]]
- [[WorkflowDevKit]]
- [[DeterministicWorkflows]]
- [[DurableAgents]]
