---
title: "ModelHandoff"
type: concept
tags: [model-selection, on-device-ai, cloud-ai, hybrid-ai]
sources: ["raw/01-articles/claude/2026-06-08 - Building intelligent apps for Apple platforms with Claude in the Foundation Models framework.md"]
last_updated: 2026-07-07
---

## Definition

Model handoff is the pattern of routing a user request to the most appropriate AI model for each step — using on-device models for fast, local, privacy-sensitive tasks and escalating to cloud-based models for complex multi-step reasoning, code generation, and data analysis — all within a single seamless user experience.

## Key Information

### Apple Foundation Models to Claude Handoff

The canonical example is Apple's [[AppleFoundationModels|Foundation Models framework]] integrating with [[Claude]] via a Swift package from [[Anthropic]]. Developers use Apple's on-device models for fast tasks (summarization, extraction, definition) and hand off to Claude when a request calls for deeper reasoning.

Because Apple's framework returns typed Swift values from @Generable annotations, Claude receives clean structured inputs rather than raw user text, improving reliability of the handoff.

### Use Cases

- **Journaling apps**: generate daily prompts on-device, then ask Claude to find thematic threads across months of entries.
- **Study apps**: define a term on-device, then hand off to Claude when the student follows up with "why does this matter for everything else we've covered?"
- **Document apps**: summarize contracts on-device, escalate to Claude for multi-document analysis and cross-referencing.

### Design Principles

- The user experiences one seamless interaction, not two separate model calls.
- On-device models handle latency-sensitive and privacy-critical operations.
- Cloud models handle reasoning-intensive work that exceeds on-device capabilities.
- Structured typed outputs from the on-device pass provide clean inputs to the cloud model.

## Related

- [[summary-2026-06-08 - Building intelligent apps for Apple platforms with Claude in the Foundation Models framework]] — source summary
- [[AppleFoundationModels]] — Apple's on-device framework that initiates the handoff
- [[Claude]] — the cloud model receiving the handoff
- [[Anthropic]] — creator of the Swift package enabling the handoff
- [[ModelTiering]] — related concept of matching model capability to task complexity within agent systems
