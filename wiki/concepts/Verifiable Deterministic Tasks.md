---
title: "Verifiable Deterministic Tasks"
type: concept
tags: [concept, task-design, agent-engineering, process]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260515 - Agents Don't Do Standups： Building the Post-Engineer Engineering Org — Mike Spitz, PFF.md"]
last_updated: 2026-06-30
---

## Definition
Verifiable Deterministic Tasks are engineering tasks with clear, objectively checkable outcomes that make them suitable for AI agent execution. They range from product-agnostic tasks (like code generation) to org-specific tasks (like feature flag creation, interactive element generation, and analytics instrumentation) where success or failure is unambiguous.

## Key Information
- **Origin**: Presented by [[MikeSpitz]] as a prerequisite for effective agent-driven development at [[PFF]]
- **Core Requirement**: Tasks must have verifiable outcomes — the agent or QA system must be able to definitively determine if the task was completed correctly
- **Deterministic**: The expected output should be well-defined and non-ambiguous
- **Org-Specific Examples at PFF**: Feature flag generation (for trunk-based development), interactive element generation, analytics generation for interactive elements
- **Product-Agnostic Examples**: Standard coding tasks, API endpoint creation, test generation
- **Relationship to Acceptance Criteria**: Tasks need clear acceptance criteria for the [[Autonomous QA Agent]] to validate
- **Design Principle**: Tasks should be structured so that none block each other; blocking dependencies are flagged during auto-ticket creation
- **Contrast**: Fuzzy or open-ended tasks ("improve performance", "make it better") are not suitable for agent execution

## Related
- [[MikeSpitz]] — presented the concept
- [[PFF]] — company applying verifiable tasks
- [[Post-Engineer Engineering Org]] — organizational model
- [[Autonomous QA Agent]] — validates verifiable tasks against acceptance criteria
- [[Lightweight Design Document]] — defines verifiable tasks upfront
- [[Trunk-Based Development]] — development model requiring feature flags as verifiable tasks
- [[Composable Skills]] — skills encode patterns for generating verifiable tasks
- [[summary-20260515 - Agents Don't Do Standups： Building the Post-Engineer Engineering Org — Mike Spitz, PFF]]
