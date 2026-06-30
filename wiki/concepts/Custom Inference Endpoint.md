---
title: "Custom Inference Endpoint"
type: concept
tags: [model-serving, inference, fine-tuning, ai-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - What Lies Beneath the API — Benjamin Cowen, Modal.md"]
last_updated: 2026-06-30
---

## Definition
A Custom Inference Endpoint is a self-hosted model serving deployment that runs a fine-tuned or custom-trained model, providing control over latency, throughput, cost, and model behavior — in contrast to using a Frontier API.

## Key Information
- The natural complement to fine-tuning: after training a custom model, you need to serve it
- Can be built with open-source serving frameworks: vLLM, SG-Lang, Triton Inference Server, or custom Python inference workflows
- Serverless platforms can auto-scale custom endpoints to match incoming traffic
- Provides control over cost economics (e.g., Intercom running at 1/5 the cost of frontier APIs)
- Allows optimization for specific latency and throughput requirements (important for enterprise contracts)
- Represents the "serving" side of the fine-tuning pipeline

## Related
- [[summary-20260602 - What Lies Beneath the API — Benjamin Cowen, Modal]] — source
- [[Frontier API]] — the alternative approach
- [[Fine-tuning]] — prerequisite training step
- [[Model Serving]] — broader concept
- [[vLLM]] — open-source serving framework
- [[Domain-Specific Models]] — what gets served
