---
title: "Heterogeneous Intelligence"
type: concept
tags: [ai-paradigm, multi-agent, hardware, optimization, scaling]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum.md"]
last_updated: 2026-06-30
---

## Definition
Heterogeneous Intelligence is the AI paradigm where different model architectures, sizes, and hardware types work together in coordinated multi-agent systems to solve complex problems. It contrasts with homogeneous intelligence (scaling single models on identical chips) and is mathematically provable to outperform homogeneous approaches under reasonable constraints.

## Key Information
- Three levels of optimization: hardware selection per agent, agent interaction workflows, and workflow construction
- Three stages of increasing heterogeneity: mild (variety in prompts, different LLMs per sub-agent, MoE), moderate (different chips for different models, diverse architectures like state-space and diffusion models), and full (co-evolution of hardware, software, and systems with vertical integration)
- Real-world problems are complex, multi-step, and open-ended — they decompose into sub-problems requiring different types of intelligence
- The **Principle of Maximum Heterogeneity** provides mathematical proof that heterogeneous systems outperform homogeneous ones across domains (neuroscience, economics, ecology)
- Production function: heterogeneous agent collectives can match diverse demand functions that homogeneous systems cannot
- Demonstrated in practice by [[Callosum]] with heterogeneous recursion (7-12x cheaper, 3-5x faster than GPT-5.2) and visual web navigation (18-25% better than frontier models, 3.7x cheaper)
- Enables shifting the [[Pareto Frontier]] beyond what any singular model can achieve

## Related
- [[Homogeneous Intelligence]] — contrasting paradigm
- [[Heterogeneous Recursion]] — practical technique for long-context tasks
- [[Principle of Maximum Heterogeneity]] — mathematical foundation
- [[Mixture of Experts]] — architectural heterogeneity
- [[MultiAgent Systems]] — workflow heterogeneity
- [[PrefillDecode Disaggregation]] — hardware-level heterogeneity
- [[Three Eras of Compute]] — framing heterogeneous as the third era
- [[Callosum]] — company building heterogeneous intelligence infrastructure
- [[summary-20260524 - Scaling the Next Paradigm of Heterogeneous Intelligence — Adrian Bertagnoli, Callosum]] — source
