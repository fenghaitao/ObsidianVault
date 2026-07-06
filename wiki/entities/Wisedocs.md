---
title: "Wisedocs"
type: entity
tags: [company, insurance-tech, document-processing, agent-adopter, managed-agents]
sources: [raw/01-articles/claude/2026-04-23 - Built-in memory for Claude Managed Agents.md, raw/01-articles/claude/2026-05-19 - New in Claude Managed Agents dreaming, outcomes, and multiagent orchestration.md]
last_updated: 2026-07-05
---

## Definition

Wisedocs is a company that built a document-verification pipeline on [[ClaudeManagedAgents]], using cross-session memory to spot and remember recurring document issues, and later a document-quality-check agent using outcomes-based rubric grading.

## Key Information

- Cited by Anthropic (April 2026) as a customer using memory on Claude Managed Agents to close feedback loops and speed up verification, rather than building custom retrieval infrastructure.
- Their document-verification pipeline uses cross-session memory to spot and remember recurring document issues, speeding up verification by 30%.
- Cited again by Anthropic (May 2026) as an outcomes customer: a document quality-check agent grades each review against internal guidelines using outcomes (rubric-based grading with a separate grader); reviews reportedly run 50% faster. This is a distinct feature (outcomes) and metric (review speed) from the April 2026 memory/verification-speed figure above — both are recorded as complementary improvements to Wisedocs' broader document pipeline, not a contradiction.
- No further product detail is available from these sources; expand if a dedicated source on Wisedocs is ingested later.

## Related

- [[summary-2026-04-23 - Built-in memory for Claude Managed Agents]] — source announcement naming Wisedocs as a memory customer
- [[summary-2026-05-19 - New in Claude Managed Agents dreaming, outcomes, and multiagent orchestration]] — source announcement naming Wisedocs as an outcomes customer
- [[ClaudeManagedAgents]] — platform Wisedocs builds on
- [[AgenticMemory]] — the memory concept Wisedocs' pipeline relies on
