---
title: "summary-20260607 - Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod"
type: source
tags: [source, transcript]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260607 - Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod.md"]
last_updated: 2026-06-30
---
## Core Summary
Audry Hsu from RunPod demonstrates how to deploy an LLM endpoint in under 5 minutes using RunPod's serverless product. RunPod is a cloud AI infrastructure company providing GPU access across 30+ data centers with over 500,000 developers. The demo walks through selecting a pre-vetted LLM listing from the RunPod Hub, deploying it via a one-click flow that provisions an HTTP API endpoint backed by vLLM on H100 GPUs, and sending the first inference request — all within minutes. The talk covers RunPod's four core product layers (Pods, Serverless, Clusters, Hub), cold start dynamics, auto-scaling configuration, and per-second fractional-cent pricing that charges only while workers actively handle requests.

## Key Points
- RunPod was founded in 2022 by Zenon and Pardeep, who repurposed failed crypto-mining GPU rigs and launched via Reddit for community feedback
- RunPod has 500,000+ developers, 30+ data centers worldwide, and $120M in annual recurring revenue
- Four core product layers: Pods (sandbox containers), Serverless (auto-scaling inference), Clusters (multi-node training), Hub (pre-vetted AI repos)
- Serverless is best for real-time inference with auto-scaling: workers spin down when idle, and you only pay while they handle requests
- The Hub provides pre-configured, community-vetted listings with Dockerfiles ready for one-click deployment
- Deployment uses vLLM as the serving engine, with H100 GPUs as default and A100s as backup
- Cold start latency (container init + model download) was ~41 seconds for the first request; subsequent execution time was ~1.5 seconds
- Max workers and active workers are configurable, with spending caps available
- Endpoints are provisioned as standard HTTP APIs, consumable by any client
- CLI and agent-skill interfaces are also available alongside the web console

## Related
- [[Audry Hsu]] — presenter, RunPod
- [[RunPod]] — cloud AI infrastructure company
- [[Zenon]] — RunPod co-founder
- [[Pardeep]] — RunPod co-founder
- [[Serverless Inference]] — RunPod's auto-scaling inference product
- [[GPU Infrastructure]] — the hardware layer RunPod abstracts
- [[Cold Start]] — initial container and model loading latency
- [[AutoScaling]] — dynamic worker scaling based on demand
- [[vLLM]] — inference serving engine used in deployment
- [[HuggingFace]] — model source for Hub listings
- [[aiDotEngineer]] — conference where talk was presented
