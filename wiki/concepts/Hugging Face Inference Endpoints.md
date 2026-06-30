---
title: "Hugging Face Inference Endpoints"
type: concept
tags: [hugging-face, inference, deployment, serving, cloud, infrastructure]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260529 - Reachy Mini： the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face.md"]
last_updated: 2026-06-30
---

## Definition
Hugging Face Inference Endpoints is a cloud serving infrastructure that hosts and scales AI model inference. It provides dynamic compute scaling with load balancing, allowing applications to deploy models without managing GPU infrastructure.

## Key Information
- Used to serve the Reachy Mini speech-to-speech pipeline at scale for 7,500+ robots
- Architecture: load balancer determines compute node count based on connected robots
- LLM inference endpoints separated from conversation nodes for resource efficiency
- Per-node concurrency varies widely — some nodes have 8 users talking heavily, others have 8 idle users
- Separating LLM from conversation nodes saves resources by scaling each component independently
- Coqui 3.5 27B is served via these endpoints for Reachy Mini conversations
- Enables GPU-poor users to access models without local hardware

## Related
- [[HuggingFace]] — platform providing the service
- [[Reachy Mini]] — primary consumer at scale
- [[Speech-to-Speech Pipeline]] — pipeline served via endpoints
- [[Coqui]] — models served via endpoints
- [[Load Balancer]] — infrastructure component
- [[summary-20260529 - Reachy Mini： the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face]] — source
