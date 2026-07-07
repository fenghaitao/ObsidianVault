---
title: "EvidenceChain"
type: concept
tags: [verification, citation, traceability, agentic-workflow, claude-opus]
sources: ["raw/01-articles/claude/2026-06-17 - Meet the winners of our Claude Opus 4.8 Build Day hackathon.md"]
last_updated: 2026-07-07
---

## Definition

An evidence chain is a verification methodology where every component of a generated output is traced back to a documented source, creating an unbroken chain from source material to verified result. It was demonstrated in [[Tekton]]'s 3D reconstruction of historical buildings, where clicking any component of a model shows where the detail came from and why it was placed there.

## Key Information

- **Origin**: demonstrated by [[Tekton]] at [[Anthropic]]'s [[ClaudeOpus4.8]] Build Day hackathon (June 2026). The team called this an "evidence chain, running from source material to verified model."
- **Application in Tekton**: [[Claude]] researches a historical building, pulling together schematics, construction documents, photographs, and diagrams, then assembles a 3D model across 339 incremental construction states. Clicking any component reveals its documented source.
- **Verification**: independent verifier sub-agents, running in isolated context windows on [[ClaudeOpus4.8]], graded each reconstruction. Self-correction loops rechecked component placement until all 20 tests passed. Every build was measured against the historical record and its citations.
- **Use cases**: academic validation (ensuring reconstructions are defensible in peer review), restoration work (verifying that proposed restorations match historical evidence), and cultural preservation (documenting why each structural element belongs where it is).
- **Broader applicability**: the pattern generalizes beyond 3D reconstruction to any AI-generated output that needs verifiable provenance — legal documents, scientific analyses, code generation with requirement traceability, and knowledge-base entries with source grounding.

## Related

- [[summary-2026-06-17 - Meet the winners of our Claude Opus 4.8 Build Day hackathon]] — source article
- [[Tekton]] — the project that originated and demonstrated the concept
- [[ClaudeOpus4.8]] — the model used for verification
- [[AgentWorkflowPatterns]] — the verifier/self-correction loop pattern is an evaluator-optimizer workflow
- [[Sandboxing]] — isolated context windows for independent verifier sub-agents
- [[Citations]] — API feature for grounding responses in source documents, a related but different approach to traceability
