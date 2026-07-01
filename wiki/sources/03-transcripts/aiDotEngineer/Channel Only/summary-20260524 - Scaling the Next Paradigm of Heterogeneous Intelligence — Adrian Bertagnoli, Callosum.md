---
title: "summary-20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum"
type: source
tags: [source, transcript, heterogeneous-intelligence, multi-agent, hardware, inference]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum.md"]
last_updated: 2026-06-30
---

## Core Summary

Adrian Bertagnoli, founding engineer at Callosum (formerly Colossyan), presents the case for heterogeneous intelligence as the next paradigm beyond homogeneous scaling of single models on identical chips. He argues that real-world problems are complex, multi-step, and open-ended -- they decompose into sub-problems requiring different types of intelligence, making heterogeneous multi-agent systems mathematically provable to outperform homogeneous ones. Callosum operationalizes this by optimizing at three levels: hardware selection per agent, agent interaction workflows, and workflow construction. Two practical demonstrations are presented: **heterogeneous recursion** (extending recursive language models with different models/chips for long-context tasks, achieving 7-12x cheaper and 3-5x faster than GPT-5.2 on ULong benchmark) and **multi-modal web navigation** (beating GPT-5.2 and Gemini 2.5 on Video Web Arena by 18-25% while being 3.7x cheaper and 3x faster through heterogeneous model composition). The talk frames three eras of compute: CPU (quicker), GPU/parallel (Nvidia), and the emerging heterogeneous era where models, workflows, and silicon co-evolve.

## Key Points

- Homogeneous intelligence (single models on identical chips, driven by neural scaling laws) is giving way to heterogeneity across architecture (Mixture of Experts), workflow (multi-agent systems), and hardware (prefill-decode disaggregation).
- Three stages of heterogeneity: mild (variety in prompts, different LLMs per sub-agent), moderate (different chips for different models, diverse model architectures), and full (co-evolution of hardware, software, and systems with vertical integration).
- **Principle of Maximum Heterogeneity**: mathematically formalized proof that heterogeneous systems outperform homogeneous ones across domains including neuroscience, economics, and ecology.
- **Heterogeneous Recursion**: extending recursive language models (MIT, Oct 2024) by mapping sub-contexts to different chips and models. On ULong benchmark: 7x cheaper/5x faster on Cerebras, 12x cheaper/3x faster on SambaNova vs GPT-5.2.
- **Visual Web Navigation**: heterogeneous mixture of video action language models beats GPT-5.2 by 18% and Gemini 2.5 by 25% on Video Web Arena. Simple subtasks (e.g., zooming) offloaded to cheaper models, making those subtasks alone 11x faster and 43x cheaper.
- Callosum is working with Aria (UK Institute) on a £3M grant for the first heterogeneous collocated cluster in the UK.
- The speaker identifies himself as Adrian Berczynski (transcription) / Adrian Bertagnoli (title), founding engineer at Callosum.

## Related

- [[Adrian Bertagnoli]] — speaker, founding engineer at Callosum
- [[Callosum]] — company building heterogeneous intelligence infrastructure
- [[Heterogeneous Intelligence]] — core paradigm
- [[Homogeneous Intelligence]] — contrasting paradigm
- [[Heterogeneous Recursion]] — key technique for long-context tasks
- [[Principle of Maximum Heterogeneity]] — mathematical formalization
- [[Mixture of Experts]] — architectural heterogeneity
- [[MultiAgent Systems]] — workflow heterogeneity
- [[Recursive Language Models]] — base technique extended by heterogeneous recursion
- [[Video Action Language Models]] — models used for web navigation
- [[Three Eras of Compute]] — framework for compute evolution
- [[PrefillDecode Disaggregation]] — hardware-level heterogeneity
- [[Cerebras]] — hardware partner
- [[SambaNova]] — hardware partner
- [[Aria UK Institute]] — research partner for heterogeneous cluster
- [[Pareto Frontier]] — heterogeneous models shift the frontier vs singular models
