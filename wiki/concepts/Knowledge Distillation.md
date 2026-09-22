---
title: "Knowledge Distillation"
type: concept
tags: [ML, technique, LLM]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg.md"]
last_updated: 2026-09-22
---
## Definition
Knowledge distillation transfers knowledge or statistics about the underlying dataset from a teacher model to a student model, making the student better than if it had never seen the teacher's auxiliary statistics.
## Key Information
- With statistics derived from a massive LLM over trillions of tokens, distillation represents a flops investment in the millions of dollars.
- At that scale every second and byte counts, so the distillation infrastructure is heavy, classical software engineering: design docs, abstractions for teacher statistics, storage systems, and multi-datacenter read/write.
- Vlad's distillation infrastructure has evolved through three-to-four generations; each rewrite broadened capacity and dramatically accelerated research on distillation methods.
- Those infrastructure investments enabled results "like flash 3.0," which he says would not have happened without them.
- It is one of his three pre-training verticals, alongside inference co-design and quantization.
## Related
- [[summary-20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg]] — source summary
- [[Vlad Feinberg]] — source
- [[Pre-training]] — pillar of his area
- [[Inference Co-Design]] — related pillar
- [[Model Quantization]] — related pillar
