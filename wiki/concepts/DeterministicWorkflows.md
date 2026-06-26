---
title: "Deterministic Workflows"
type: concept
category: methodology
---

# Deterministic Workflows

## Definition

Deterministic workflows are workflow orchestration layers that are compiled into side-effect-free bundles, ensuring that replaying the orchestration logic always produces the same sequence of step invocations. This property enables reliable retry, state rehydration, and migration of in-flight workflows.

## Key Information

- **How it works in Workflow DevKit**:
  - The `use workflow` directive marks a function for special compilation
  - The compiler extracts the orchestration code into a separate bundle
  - All imports with side effects are blocked -- the orchestration layer must be pure
  - Steps (marked with `use step`) are the only places where side effects (API calls, DB writes) can occur
- **Why determinism matters**:
  - When a workflow resumes after a `sleep` or failure, the orchestration layer replays to determine which step to execute next
  - Since the orchestration is deterministic and step results are cached, replay is instantaneous and cost-free
  - Enables version migration: the system can check whether a new version's step signatures are compatible with cached step results
- **Contrast with steps**: Steps are explicitly allowed to have side effects -- that's their purpose. The workflow ensures each step runs exactly once (or retries on failure) via caching.

## Related

- [[WorkflowPattern]]
- [[WorkflowDevKit]]
- [[StepCaching]]
- [[DurableAgents]]
