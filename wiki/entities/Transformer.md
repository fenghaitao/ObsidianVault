---
title: "Transformer"
type: entity
tags: [architecture, AI, ML]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg.md"]
last_updated: 2026-09-22
---
## Definition
The Transformer is the neural-network architecture underlying modern LLMs like Gemini; inference co-design chooses its network topology, matrix shapes, attention shapes, and number of heads.
## Key Information
- Inference co-design picks the shapes of the matmul matrices in gating and linear layers, and the attention shape and number of heads, to saturate the serving hardware.
- Implementing a real transformer is part of Vlad's scaling-book hiring exercise — evidence of engineering willingness to "get into the weeds."
- Transformer weights are typically stored in FP32 during training and can be quantized to ~4-bit without much quality loss.
- Gemini models are Transformer-based, including the mixture-of-experts Gemini 2.0 series.
## Related
- [[summary-20260615 - Google DeepMind Distinguished Eng (L9)： How To Land a Job at a Frontier Lab ｜ Vlad Feinberg]] — source summary
- [[Gemini]] — model class
- [[Inference Co-Design]] — attention/head shapes
- [[Mixture of Experts]] — architecture variant
- [[Pre-training]] — training phase
- [[Model Quantization]] — weight precision
