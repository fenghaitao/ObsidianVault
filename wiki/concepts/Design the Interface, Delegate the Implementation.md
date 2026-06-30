---
title: "Design the Interface, Delegate the Implementation"
type: concept
tags: [software-design, ai-coding, architecture, delegation, strategy]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - ＂Software Fundamentals Matter More Than Ever＂ — Matt Pocock.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock.md"]
last_updated: 2026-06-29
---

## Definition
"Design the interface, delegate the implementation" is a strategy for AI-assisted development where the human engineer carefully designs module interfaces (boundaries, contracts) and lets the AI handle the internal implementation. This preserves human cognitive load while leveraging AI's code generation capabilities.

## Key Information
- Articulated by Matt Pocock as his fifth tip for effective AI-assisted development
- Based on the deep modules concept from John Ousterhout: modules with simple interfaces and complex internals
- The human designs the interface — this is where design judgment and strategic thinking matter most
- The AI handles the implementation inside the module — the tactical coding work
- The interface serves as a testable boundary: you verify the module works by testing at the interface
- This approach saves human cognitive load: you can treat modules as "gray boxes" without reviewing every implementation detail
- Cannot be applied to critical modules (finance, security) where implementation details matter — but works for most application modules
- Requires the codebase to be structured with deep modules first
- Aligns with Kent Beck's principle: "Invest in the design of the system every day"
- Contrasts with specs-to-code, which divests from design entirely

## Related
- [[summary-20260423 - ＂Software Fundamentals Matter More Than Ever＂ — Matt Pocock]] — source transcript
- [[summary-20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock]] — source transcript
- [[Deep Modules]] — the architectural prerequisite
- [[MattPocock]] — originator of the strategy
- [[KentBeck]] — "invest in the design of the system every day"
- [[JohnOusterhout]] — deep modules concept
- [[Harness Engineering]] — related paradigm from Ryan Lopopolo
- [[AgenticEngineering]] — broader paradigm
