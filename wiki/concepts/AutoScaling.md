---
title: "Auto-scaling"
type: concept
tags: [scaling, serverless, infrastructure, deployment, workers]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260607 - Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod.md"]
last_updated: 2026-06-30
---

## Definition
Auto-scaling is a mechanism that dynamically adjusts the number of active compute workers based on incoming demand. In the context of LLM inference, it allows serverless endpoints to scale up workers during traffic spikes and scale down to zero when idle, so users only pay for compute while requests are being processed.

## Key Information
- Workers automatically spin up when requests arrive and spin down when idle, eliminating the need to pre-provision compute
- Configurable max workers caps the upper bound of concurrent workers to control costs
- Active (always-on) workers can be set to keep a minimum number of workers warm, avoiding cold start for baseline traffic
- Spending caps prevent runaway costs from unexpected traffic surges
- RunPod's serverless workers scale on H100 GPUs by default with A100s as backup
- Workers transition through states: initializing (provisioning + model download) → running (handling requests) → idle (spun down)
- Contrasts with always-on Pod containers, which remain running regardless of demand
- Provides observability into scaling behavior via request count, execution time, and delay time metrics

## Related
- [[Serverless Inference]] — the deployment model built on auto-scaling
- [[Cold Start]] — latency incurred when auto-scaling spins up new workers
- [[GPU Infrastructure]] — the hardware layer workers are provisioned on
- [[RunPod]] — platform implementing auto-scaling for LLM endpoints
- [[summary-20260607 - Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod]] — source
