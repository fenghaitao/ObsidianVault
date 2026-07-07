---
title: "DoerVerifier"
type: concept
tags: [agent-pattern, verification, quality, trust, multi-agent]
sources: ["raw/01-articles/claude/2026-06-24 - Building effective human-agent teams.md"]
last_updated: 2026-07-07
---

## Definition

The Doer-Verifier pattern is an agent harness where one agent performs a task (the "doer") and a separate agent checks the first agent's work against explicit criteria (the "verifier"). It is a key mechanism for building trust in agent output within human-agent teams.

## Key Information

### Role in Building Trust

The Doer-Verifier pattern is one of several mechanisms Anthropic recommends for building trust with agents over time. The best long-running agents have many different ways to verify their work before a human looks at it.

### Verification Methods

- **Code**: tests serve as the verification layer
- **Technical docs**: rubrics and style guides can be applied as verification criteria
- **General work**: humans set the bar and ensure all work assigned to an agent can be vetted, preventing quality drift from the original intention

### Trust-Building Progression

Anthropic's recommended progression for building trust with agents:

1. Review agent work manually in the beginning to vet quality, provide feedback, and design task verification checklists
2. Tell the agent to use a verifier agent to check its work as part of the task
3. Build reflection into the cycle: ask agents to review their own misses so work improves over time
4. Track which kinds of tasks each agent has earned autonomy on and expand scope per task type after repeated successes

### Practical Example

One engineering leader at Anthropic took on a new team with a big backlog. The team had one set of agents read through backlog items, determine ownership, and assign complexity scores. Another set read from the list, filtered to medium and low complexity items, and created code changes. At the beginning, humans reviewed every decision. Then humans taught the agents to surface hard-tradeoff decisions directly to humans. Weekly "lessons & missteps" reports helped agents track mistakes and avoid repeating them.

### Relationship to Other Patterns

The Doer-Verifier pattern overlaps with the evaluator-optimizer workflow pattern ([[AgentWorkflowPatterns]]) and the generator-verifier coordination pattern ([[MultiAgentSystem]]). In the human-agent teams context, it is specifically framed as a trust-building mechanism: the verifier gives humans confidence before they review agent output themselves.

## Related

- [[summary-2026-06-24 - Building effective human-agent teams]] — source article
- [[HumanAgentTeams]] — the broader collaboration model this pattern supports
- [[AgentWorkflowPatterns]] — the evaluator-optimizer workflow pattern (same mechanic, different framing)
- [[MultiAgentSystem]] — the generator-verifier coordination pattern (same mechanic, architectural lens)
- [[NorthStar]] — the complementary practice of giving agents direction
- [[WorkingInPublic]] — the complementary practice of giving agents broad context
- [[Anthropic]] — the company whose internal practices are described
