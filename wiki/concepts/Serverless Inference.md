---
title: "Serverless Inference"
type: concept
tags: [serverless, inference, llm, deployment, auto-scaling]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260607 - Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod.md"]
last_updated: 2026-06-30
---

## Definition
Serverless Inference is an auto-scaling deployment model for LLM endpoints where workers spin up to handle requests and spin down when idle, so users only pay for compute while requests are actively being processed. It is best suited for real-time inference and bursty or batch workloads.

## Key Information
- Workers automatically scale up and down based on demand; idle workers incur no cost
- Configurable max workers cap the scale-out limit, and spending caps prevent runaway costs
- Active (always-on) workers can be configured to keep models pre-loaded for immediate response, eliminating cold start on frequent requests
- Cold start latency occurs on first request or after idle periods as containers initialize and models download
- RunPod's implementation provisions standard HTTP API endpoints consumable by any client
- RunPod's Serverless uses H100 GPUs by default with A100s as backup, priced at fractions of a cent per second
- Provides observability into request count, execution time, and delay time per endpoint
- Contrasts with always-on Pods (containers) and multi-node Clusters (training); Serverless fills the real-time inference niche
- Deployment can be initiated from the RunPod Hub via one-click or configured with custom vLLM flags (max model length, max loras, etc.)

## Related
- [[RunPod]] — platform providing serverless inference
- [[Cold Start]] — latency factor in serverless deployments
- [[AutoScaling]] — the scaling mechanism underlying serverless
- [[GPU Infrastructure]] — the hardware layer serverless runs on
- [[vLLM]] — inference serving engine used in serverless deployments
- [[summary-20260607 - Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod]] — source
