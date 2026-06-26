---
title: "Workflow Pattern"
type: concept
category: methodology
---

# Workflow Pattern

## Definition

The workflow pattern is an orchestration architecture that separates application code into a deterministic orchestration layer (the "workflow") and isolated, retryable execution units (the "steps"). The orchestration layer coordinates step execution, persists state between steps, and can be replayed deterministically, while each step runs in isolation with its inputs and outputs cached for retry and recovery.

## Key Information

- **Core Components**:
  - **Orchestration layer (workflow)**: Deterministic code that coordinates step execution; compiled into a side-effect-free bundle to ensure replayability
  - **Steps**: Isolated execution units that can have side effects (API calls, database writes, etc.); inputs and outputs are cached
- **Key Properties**:
  - **Durability**: Steps can be retried on failure without re-executing completed steps
  - **Resumability**: Workflows can pause (via `sleep`) and resume from the exact point where they paused
  - **Observability**: Every step execution is tracked with inputs, outputs, and events
  - **Scalability**: Each step runs in its own serverless instance; only the orchestration layer is briefly invoked between steps
- **In the Workflow DevKit**: The `use workflow` directive marks the orchestration function; `use step` marks individual steps; the compiler ensures the orchestration layer has no side-effect imports
- **Comparison to traditional approaches**: Replaces manual wiring of queues, databases, error/retry code, state storage, and observability layers with a single library

## Related

- [[WorkflowDevKit]]
- [[DurableAgents]]
- [[DeterministicWorkflows]]
- [[StepCaching]]
- [[ResumableStreams]]
- [[HumanInTheLoopWorkflows]]
