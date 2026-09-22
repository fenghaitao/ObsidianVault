---
title: "Tensor Processing Unit (TPU)"
type: entity
tags: [hardware, ML, Google, infrastructure]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260123 - Meta Senior Staff (IC7) Eng's Honest Demotion Story.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260713 - Turing Award Winner： TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC ｜ David Patterson.md"]
last_updated: 2026-09-23
---

## Definition

The Tensor Processing Unit (TPU) is Google's custom machine-learning accelerator hardware, specialized for matrix multiplication, which Igor's team used to move Google ads training from CPUs to first-generation TPUs.

## Key Information

- First-generation TPUs were about two orders of magnitude faster than the CPUs previously used for ads training, which shifted the bottleneck to input reading and processing.
- TPUs are specialized (less generic than GPUs); sparse/random access such as embedding lookups is hard on the chip, while matrix multiplication and large sequential memory access are its strengths.
- Igor's L7 promotion project involved building new training infrastructure to run ads ML on TPUs and testing input pipelines with an "infinite-speed TPU" bottleneck test.
- TPU chips had to be ordered ~18 months in advance; ads teams usually under-ordered to avoid provisioning waste in a mature, profitability-focused business.
- Vlad Feinberg's team served the MoE-based Flash 2.0 by sharding experts across TPUs, then made it viable with pipeline prefill that moves layers (not experts) across the chips.
- David Patterson: the TPU was a clean-slate design — a giant matrix-multiply unit at its heart, no hardware caches (the software schedules memory because ML knows its access pattern), and bfloat16 (Brain Float 16), the first floating-point format with a larger exponent than fraction, prioritizing range over precision.
- The 2016 TPU debut was the watershed: ~30x faster than a contemporary GPU and ~80x faster than a CPU at inference, which persuaded the whole industry (Intel bought companies, Nvidia adapted, hyperscalers built their own) to design ML-specific hardware.
- Google's training-TPU block diagram (matrix-multiply unit, high-bandwidth memory, and a vector unit) has stayed essentially constant for a decade.

## Related

- [[summary-20260123 - Meta Senior Staff (IC7) Eng's Honest Demotion Story]] — source summary
- [[Igor]] — led TPU adoption for ads training
- [[Google]] — developed the TPU
- [[Machine Learning]] — concept
- [[Model Training]] — workload the TPU accelerates
- [[summary-20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg]] — source summary
- [[Gemini Flash]] — served across TPUs
- [[Mixture of Experts]] — sharded across TPUs
- [[Pipeline Parallelism]] — moves layers across TPUs
- [[summary-20260713 - Turing Award Winner： TPU vs GPU vs CPU, Computer Architecture, RISC vs CISC ｜ David Patterson]] — source summary
- [[David Patterson]] — led Google's TPU effort
- [[Domain-Specific Architecture]] — what the TPU exemplifies
- [[Nvidia]] — the GPU it outpaced at inference
