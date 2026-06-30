---
title: "Ash Prabaker"
type: entity
tags: [person, engineer, anthropic, applied-ai]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson.md"]
last_updated: 2026-06-30
---

## Definition
Ash Prabaker is an engineer on Anthropic's Applied AI team who presented the generator-evaluator harness pattern for long-running autonomous agents at the 2026 AI Engineer conference.

## Key Information
- Works as an engineer in Anthropic's Applied AI team
- Presented the generator-evaluator (GAN-style) harness pattern: splitting builder and QA critic into separate context windows with adversarial pressure
- Advocated for rubric-based evaluation with four criteria: design, originality, craft, functionality — weighted toward design and originality to prevent "AI slop"
- Demonstrated the Retro Forge game maker built with the generator-evaluator harness (6 hours, ~$200) vs a solo loop that produced broken play mode
- Key insight: tuning a standalone critic to be harsh is tractable; tuning a builder to be self-critical is not — exploiting the gap between LLM-as-critic and LLM-as-generator
- Emphasized that the primary debugging loop for agent harnesses is reading traces by hand, not running more experiments
- Advocated for file system as shared state between agents rather than relying on context windows
- Five takeaways: (1) self-evaluation is a trap, (2) compaction doesn't equal coherence, (3) structured hand-offs and clean contexts work, (4) subjective quality is gradable with written rubrics, (5) sit with the model and read traces
- Co-presented with Andrew Wilson

## Related
- [[summary-20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson]] — source
- [[Andrew Wilson]] — co-presenter
- [[Anthropic]] — company
- [[Generator-Evaluator Pattern]] — core harness pattern presented
- [[Self-Evaluation Trap]] — key warning
- [[Contract Negotiation]] — generator-evaluator contract mechanism
- [[Rubric-Based Evaluation]] — four-criteria grading framework
- [[Trace Reading]] — debugging methodology emphasized
- [[File System as Shared State]] — inter-agent communication pattern
- [[Context Anxiety]] — model behavior discussed
- [[Harness Evolution]] — how harnesses adapt as models improve
