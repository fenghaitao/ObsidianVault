---
title: "Model Serving"
type: concept
tags: [inference, deployment, ml-ops, ai-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - What Lies Beneath the API — Benjamin Cowen, Modal.md"]
last_updated: 2026-06-30
---

## Definition
Model Serving is the deployment phase where a trained or fine-tuned model is hosted behind an API endpoint to handle inference requests. Modern serving can be accomplished with open-source frameworks (vLLM, SG-Lang, Triton Inference Server) and auto-scaled on serverless platforms to match traffic.

## Key Information
- The necessary follow-up to fine-tuning: after training, you must serve the model
- Open-source serving options: vLLM, SG-Lang, Triton Inference Server, or custom Python inference workflows
- Serverless platforms can auto-scale serving endpoints to match incoming traffic patterns
- Frontier APIs handle serving under the hood — custom serving gives you the same capability for your own models
- Enables cost optimization: Intercom runs custom models at 1/5 the cost of frontier API equivalents
- Custom serving allows optimization for specific latency, throughput, and cost requirements

## Related
- [[summary-20260602 - What Lies Beneath the API — Benjamin Cowen, Modal]] — source
- [[Custom Inference Endpoint]] — the deployed result
- [[Fine-tuning]] — prerequisite training step
- [[Frontier API]] — the alternative (managed serving)
- [[vLLM]] — open-source serving framework
- [[Domain-Specific Models]] — what gets served
