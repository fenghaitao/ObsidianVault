---
title: "Scaling Laws"
type: concept
tags: [ML, theory, LLM]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg.md"]
last_updated: 2026-09-22
---
## Definition
Scaling laws describe how to predict an LLM's final test loss as a function of the flops (and other factors) invested in its pre-training run — the central question Vlad Feinberg says pre-training research answers.
## Key Information
- The functional/power-law form matters less than predictiveness: for a given recipe, as you invest more flops you must predict the final test loss.
- In classical ML you iterate on ImageNet with a cheap validation/cross-validation loop; each LLM pre-training run is a one-shot ImageNet problem because you always commit more flops than ever before.
- The one-shot analogy: practice on MNIST, then CIFAR, then a method that must work on ImageNet the first time — many methods break at scale.
- A "recipe" is a function from desired flops to a training routine; coupling it with a prediction rule lets you improve the recipe.
- Foundational works: the Kaplan scaling paper and Chinchilla; earlier roots include the original GPTs and Google's PaLM papers; later work adds factors like the number of unique tokens.
- Vlad names scaling-law familiarity as table stakes, and the Scaling Book exercises test this.
## Related
- [[summary-20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg]] — source summary
- [[Vlad Feinberg]] — source
- [[The Scaling Book]] — reference
- [[ImageNet]] — analogy
- [[Pre-training]] — application
- [[Mathematical Maturity]] — prerequisite
