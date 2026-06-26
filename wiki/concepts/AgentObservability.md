---
title: "Agent Observability"
type: concept
category: methodology
---

# Agent Observability

## Definition

Agent observability is the built-in capability to inspect AI agent runs, including every step (LLM call, tool call), its inputs, outputs, events, and timing. In the Workflow DevKit, this is provided through a web UI accessible via the `workflow web` CLI command, which works identically for local development and production deployments.

## Key Information

- **What is observable**:
  - Every workflow run with its status (running, completed, failed, cancelled)
  - Every step within a run, displayed as spans with inputs and outputs
  - Events associated with each step
  - Timing and retry information
- **Access methods**:
  - **Local**: `npx workflow web` starts a local UI for inspecting runs
  - **Production**: `npx workflow web --backend <deployment-url>` connects to production runs
  - **API**: Programmatic access to run data for export to external monitoring (e.g., DataDog)
  - **CLI**: List, inspect, and cancel runs from the command line
- **Future capabilities**: OpenTelemetry span export for integration with existing observability stacks; end-to-end encryption for sensitive step data
- **Key insight**: Observability is a first-class feature, not an afterthought -- it comes automatically when using the workflow pattern

### Braintrust Perspective

Braintrust treats observability and evals as the same problem from a systems perspective. Observability is what you do after an agent reaches production — monitoring real user interactions to maintain confidence that the agent performs as expected. It forms one half of the "eval flywheel": production traces reveal real user behavior and failure modes, which feed back into offline evals for continuous improvement.

Key challenges of agent observability at scale:
- **Data velocity**: Production traffic generates traces at high speed
- **Data size**: Individual spans can be 10-20MB (vs. traditional spans at a few KB)
- **Structure**: Semi-structured to unstructured, heavy on text
- **Query patterns**: Need both low-latency point queries (viewing a trace) and aggregate analytics plus full-text search
- **Multimodal**: Traces may contain audio, video, and other media stored in object storage

## Related

- [[WorkflowDevKit]]
- [[DurableAgents]]
- [[WorkflowPattern]]
- [[StepCaching]]
- [[summary-20260428 - Why building eval platforms is hard — Phil Hetzel, Braintrust]] — source (Braintrust perspective)
- [[Braintrust]] — agent quality platform
- [[EvalFlywheel]] — observability-evals loop
- [[TraceDataChallenges]] — data challenges of agent traces
- [[OnlineEvals]] — scoring functions on observability traffic
