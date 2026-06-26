---
title: "AmazonKiro"
type: entity
tags: [tool, ide, agentic-coding, spec-driven-development, amazon]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro.md"]
last_updated: 2026-06-26
---

## Definition
Amazon Kiro (also spelled "Kira" or "Curo" in the transcript) is an agentic IDE from Amazon that implements spec-driven development — a structured SDLC workflow (requirements → design → tasks → execution) with EARS-format requirements, property-based testing, and neurosymbolic reasoning for reproducible, high-quality software delivery.

## Key Information
- Launched general availability around November 17, 2025; public preview launched July 14, 2025
- Built by a very small team of 3-4 people at Amazon, purposefully distinct from Amazon Q Developer
- Core goals: scale AI dev to complex problems, improve agent control, enhance code quality and reliability
- Forked from Code OSS (the open-source VS Code base), similar to Cursor and Windsurf
- Spec-driven development workflow: prompt → requirements (EARS format) → design → property extraction → task list → execution
- Integrates property-based testing: EARS requirements are translated into system invariants that are falsified via PBT
- Uses neurosymbolic reasoning: backend may use non-LLM systems (classic automated reasoning) alongside LLMs
- Features: steering (persistent memory/rules), MCP integration, software hooks, image support, multi-group workspaces
- Kiro CLI supports custom agents and a `use AWS` tool wrapper over the AWS SDK
- Supports Java, Python, JavaScript, TypeScript, and Rust (but works with any language in practice)
- Has a task list UI with optional tasks; each task runs in a new session by default
- Prompt caching achieves 90-95% cache hit rate for fast interactions
- Currently lacks sub-agents and incremental summarization (as of January 2026)
- Internal Amazon teams use spec reviews (via Kiro-generated specs) instead of traditional design doc reviews

## Related
- [[summary-20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro]] — source
- [[AlHarris]] — Principal Engineer on Kiro
- [[Amazon]] — parent company
- [[SpecificationDrivenDevelopment]] — the paradigm Kiro implements
- [[EARS]] — requirement format used by Kiro
- [[PropertyBasedTesting]] — testing approach integrated into Kiro
- [[NeurosymbolicReasoning]] — backend strategy
- [[Steering]] — persistent memory feature
- [[CodeOSS]] — the VS Code base Kiro is forked from
