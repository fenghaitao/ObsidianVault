---
title: "ImageNet"
type: entity
tags: [dataset, benchmark, ML]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg.md"]
last_updated: 2026-09-22
---
## Definition
ImageNet is the classic image-classification benchmark Vlad Feinberg uses to contrast classical ML iteration with the one-shot nature of LLM pre-training runs.
## Key Information
- In classical ML, you train a VGG or ResNet on ImageNet, run a validation set, and get a cross-validation error that estimates final test error — letting you iterate cheaply on architecture ideas.
- LLM pre-training is a one-shot version of this: you never see the full "ImageNet" training set, so you must practice on smaller proxies (MNIST, then CIFAR) and hope the method generalizes when it finally meets ImageNet.
- Methods that work on MNIST and CIFAR often break on ImageNet; scaling laws exist to predict final loss before committing the flops.
## Related
- [[summary-20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg]] — source summary
- [[Scaling Laws]] — the LLM counterpart
