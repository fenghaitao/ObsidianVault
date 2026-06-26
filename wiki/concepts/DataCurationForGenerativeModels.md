---
title: "DataCurationForGenerativeModels"
type: concept
tags: [data, generative-models, training, best-practices, diffusion]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind.md"]
last_updated: 2026-06-26
---

## Definition
Data curation is the process of selecting, filtering, and improving training data for generative models. Sander Dieleman emphasizes it as critically important yet under-incentivized in research culture, arguing that time spent on data improvement is often a better investment than tweaking model architecture.

## Key Information
- **Critical importance**: Essential for high-quality results from large-scale generative models
- **Under-incentivized in research**: Academic culture rewards using standard benchmarks for fair comparison, not looking at or improving data
- **Cultural shift needed**: The field is collectively "unlearning" the habit of ignoring data quality
- **Better ROI than architecture**: Time spent improving data is sometimes a better investment than optimizing model architecture
- **Proprietary nature**: Data curation details are rarely published and are considered part of the "secret sauce" of what makes models good
- **Limited publications**: Very few papers exist on data curation techniques for generative models
- **Applicable across modalities**: Relevant for both image and video generation models

## Related
- [[summary-20260421 - Building Generative Image & Video models at Scale - Sander Dieleman, Google DeepMind]] — source
- [[DiffusionModels]] — models that benefit from curation
- [[LatentDiffusion]] — training approach affected by data quality
- [[SanderDieleman]] — emphasized this topic
