---
title: "Tool Calls in Evals"
type: concept
category: methodology
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust.md"]
last_updated: 2026-06-30
---

## Definition

Tool Calls in Evals refers to the unique evaluation challenges that arise when AI agents interact with external systems through tool calls. Unlike simple model-call evaluations that only assess final outputs, tool-call evaluation requires examining entire agent traces and accounting for external system state, making it a defining challenge of Phase 3 in eval practice maturity.

## Key Information

### Two Types of Tool Calls

1. **Context-gathering tools**: Gather data from external sources and inject it into the LLM context. These affect the quality of the agent's information but don't modify external state.

2. **CRUD-based tools**: Create, read, update, or delete information in databases or external systems. These have side effects that complicate offline evaluation.

### Evaluation Challenges

- **Trace complexity**: Instead of evaluating a single output, evaluators must assess the entire agent trace, including each tool call and MCP interaction
- **State representation**: It's challenging to represent the state that external systems were in at the time the eval input was created
- **Production safety**: CRUD tools risk overwriting production data when replayed during offline evals
- **Tool-level targeting**: Evals may need to target individual tool calls within a trace, not just the final output

### Mitigation Strategies

- **Mock APIs**: Approximate real production environments with mock-level APIs for offline eval runs
- **Trace injection**: Cram external system state into agent traces and inject that state into the eval task
- **Timestamp queries**: Use version queries (e.g., query a vector database at a specific point in time) to represent the state as it was when the original task ran
- **Trace tooling**: Use platforms that capture large, arbitrarily-sized traces and allow introspection at each step

### Relationship to Maturity

This is the defining challenge of [[EvalPracticePhases|Phase 3]] in eval practice maturity. As agents grow more complex and interact with more external systems, the number of failure vectors increases, necessitating more sophisticated evaluation approaches.

## Related

- [[summary-20260527 - The maturity phases of running evals — Phil Hetzel, Braintrust]] — source
- [[EvalPracticePhases]] — Phase 3 where tool call evaluation becomes necessary
- [[TraceLinkedEvaluations]] — evaluating entire agent traces, not just outputs
- [[ToolCalling]] — the general concept of tool calling in agents
- [[AgentObservability]] — capturing traces for evaluation
