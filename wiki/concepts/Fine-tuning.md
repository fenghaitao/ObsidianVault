---
title: "Fine-tuning"
type: concept
tags: [llm, model-customization, machine-learning]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240724 - From Software Developer to AI Engineer： Antje Barth.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - What Lies Beneath the API — Benjamin Cowen, Modal.md"]
last_updated: 2026-06-30
---
## Definition
Fine-tuning is the process of further training a pre-trained foundation model on a specific dataset to adapt its behavior to particular use cases and data. It is one of the three main techniques for model customization.

## Key Information
- One of three main model customization approaches alongside prompt engineering and RAG
- Supported on Amazon Bedrock as a model customization capability
- Used when prompt engineering and RAG are insufficient for a specific use case
- Requires domain-specific data to adapt model behavior
- More involved than prompt engineering but can produce more specialized results
- Modern open-source libraries enable supervised fine-tuning in ~300 lines of Python
- Serverless platforms (like Modal) make training accessible without dedicated infrastructure engineers
- Key signals it's time to fine-tune: API costs exceeding revenue, plateauing evals, unmet latency/throughput requirements
- Prerequisites: mature data collection pipeline and developed eval systems
- Real-world results: Intercom beating frontier API at 1/5 the cost, Pentress seeing orders of magnitude improvement
- Accessible RL libraries exist for reinforcement learning fine-tuning as well

## Related
- [[summary-20240724 - From Software Developer to AI Engineer： Antje Barth]] — source
- [[summary-20260602 - What Lies Beneath the API — Benjamin Cowen, Modal]] — source
- [[Foundation Models]]
- [[Prompt Engineering]]
- [[RAG]]
- [[Model Customization]]
- [[ParameterEfficientFineTuning]] — related technique
- [[Supervised Fine-Tuning]] — primary implementation approach
- [[Domain-Specific Models]] — the output of fine-tuning
- [[Model Spectrum]] — where fine-tuning sits
- [[Serverless Training]] — modern infrastructure for fine-tuning
- [[Frontier API]] — what fine-tuning replaces
- [[Custom Inference Endpoint]] — serving after fine-tuning
