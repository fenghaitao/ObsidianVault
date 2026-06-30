---
title: "Output Complexity"
type: concept
tags: [benchmarks, agents, outputs, reward-signals, evaluation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260604 - The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI.md"]
last_updated: 2026-06-30
---

## Definition
Output Complexity is one of the three "next wave" benchmark dimensions identified by [[SnorkelAI]]. It refers to capturing nuanced, differentiated reward signals beyond simple chat or document outputs — including trustworthy outputs, uncertainty expression, strategic recommendations, and new form factors for agent-human and agent-agent interaction.

## Key Information
- Currently under-explored: most benchmarks focus on chat-based or document-based outputs
- Real artifacts from day-to-day work require more nuanced evaluation (e.g., strategic proposals, roadmaps)
- Key sub-dimensions: (1) trustworthy outputs — agents capturing their own uncertainty, knowing when to stop or ask for more information, (2) new form factors for agent-human interaction, (3) agent-to-agent interaction outputs
- Complex outputs can serve as both evaluation signals and reward signals for training
- Non-trivial and subjective to define what makes a "good" recommendation or strategic proposal
- One of three axes Snorkel is most excited about for the next generation of benchmarks

## Related
- [[Benchmarking Agents]] — parent framework
- [[Environment Complexity]] — complementary next-wave dimension
- [[Autonomy Horizon]] — complementary next-wave dimension
- [[SnorkelAI]] — organization identifying this dimension
- [[summary-20260604 - The Art & Science of Benchmarking Agents — Vincent Chen, Snorkel AI]] — source transcript
