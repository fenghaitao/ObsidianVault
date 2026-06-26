---
title: "AgentHooks"
type: concept
tags: [agents, verification, events, determinism]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro.md"]
last_updated: 2026-06-26
---

## Definition
Agent hooks are event-driven extension points in Amazon Kiro that fire at specific moments in the agent loop. They enable deterministic verification, such as ensuring test cases pass before a task is marked complete.

## Key Information
- Kiro supports software hooks as a feature alongside steering, MCP, and image support
- Can be used to ensure test cases pass before a task is marked complete
- Example use case: after including explicit unit test cases in task definitions, hooks verify those tests actually pass before the agent claims completion
- Addresses the common problem of LLMs being "very good at saying I'm done" even when tests don't pass
- Provides determinism to complement the model's own (sometimes overly optimistic) reasoning

## Related
- [[summary-20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro]] — source
- [[AmazonKiro]] — IDE with hooks feature
- [[Hooks]] — related concept from Claude Agent SDK
- [[Verification in Agentic Loops]] — primary use case
- [[PropertyBasedTesting]] — complementary verification approach
