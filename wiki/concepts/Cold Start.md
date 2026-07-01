---
title: "Cold Start"
type: concept
tags: [latency, serverless, inference, deployment, llm]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260607 - Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod.md"]
last_updated: 2026-06-30
---

## Definition
Cold Start is the initial latency incurred when a serverless inference worker is provisioned for the first time or after an idle period. It includes container initialization and model download time, and affects only the first request in a session — subsequent requests benefit from warm workers with models already loaded.

## Key Information
- In RunPod's serverless demo, cold start added ~41 seconds to the first request (container creation + model download from HuggingFace)
- Subsequent execution time was only ~1.5 seconds once workers were warm
- Cold start can be mitigated by configuring active (always-on) workers that keep models pre-loaded
- Workers transition through states: initializing (container creation, model download) → running (ready to handle requests)
- RunPod provides telemetry on request count, execution time, and delay time to give observability into cold start impact
- Cold start is a key tradeoff in serverless architectures: pay nothing when idle, but accept latency on first request after inactivity

## Related
- [[Serverless Inference]] — deployment model where cold start occurs
- [[AutoScaling]] — determines when new workers (and thus cold starts) are triggered
- [[GPU Infrastructure]] — the hardware being provisioned during cold start
- [[RunPod]] — platform demonstrating cold start dynamics
- [[summary-20260607 - Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod]] — source
