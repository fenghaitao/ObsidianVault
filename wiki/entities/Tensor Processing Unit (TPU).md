---
title: "Tensor Processing Unit (TPU)"
type: entity
tags: [hardware, ML, Google, infrastructure]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260123 - Meta Senior Staff (IC7) Eng's Honest Demotion Story.md"]
last_updated: 2026-09-14
---

## Definition

The Tensor Processing Unit (TPU) is Google's custom machine-learning accelerator hardware, specialized for matrix multiplication, which Igor's team used to move Google ads training from CPUs to first-generation TPUs.

## Key Information

- First-generation TPUs were about two orders of magnitude faster than the CPUs previously used for ads training, which shifted the bottleneck to input reading and processing.
- TPUs are specialized (less generic than GPUs); sparse/random access such as embedding lookups is hard on the chip, while matrix multiplication and large sequential memory access are its strengths.
- Igor's L7 promotion project involved building new training infrastructure to run ads ML on TPUs and testing input pipelines with an "infinite-speed TPU" bottleneck test.
- TPU chips had to be ordered ~18 months in advance; ads teams usually under-ordered to avoid provisioning waste in a mature, profitability-focused business.

## Related

- [[summary-20260123 - Meta Senior Staff (IC7) Eng's Honest Demotion Story]] — source summary
- [[Igor]] — led TPU adoption for ads training
- [[Google]] — developed the TPU
- [[Machine Learning]] — concept
- [[Model Training]] — workload the TPU accelerates
