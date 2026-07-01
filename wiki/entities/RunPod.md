---
title: "RunPod"
type: entity
tags: [company, cloud, ai-infrastructure, gpu, serverless]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260607 - Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod.md"]
last_updated: 2026-06-30
---

## Definition
RunPod is a cloud AI infrastructure company that provides GPU access and makes it easy for developers to deploy models — private, open-source from HuggingFace, or custom — across 30+ data centers worldwide with over 500,000 developers on the platform.

## Key Information
- Founded in 2022 by Zenon and Pardeep, who repurposed failed crypto-mining GPU rigs and launched via Reddit for community feedback
- Over 500,000 developers on the platform across 30+ data centers including Europe and the EU
- $120 million in annual recurring revenue
- Customers include AI cloud-native companies who come for flexible and reliable GPU infrastructure
- Community-engaged: active on Reddit and Discord for user feedback
- Four core product layers:
  - **Pods**: Sandbox virtual environments — containers with allocated GPUs, user brings Dockerfiles and code
  - **Serverless**: Auto-scaling product for bursty/batch workloads; workers spin down when idle, pay only for active request handling
  - **Clusters**: Multi-node clusters with high-speed networking for heavy-duty training
  - **Hub**: Central repository of pre-configured, pre-vetted AI repos with community contributions; listings can be forked, watched, starred, and deployed
- Serverless endpoints are provisioned as standard HTTP APIs with configurable max workers, active (always-on) workers, and spending caps
- Default deployment uses H100 GPUs with A100s as backup; pricing is fraction of a cent per second
- Provides console, CLI, and agent-skill interfaces for interacting with the platform

## Related
- [[Audry Hsu]] — RunPod representative and presenter
- [[Zenon]] — co-founder
- [[Pardeep]] — co-founder
- [[Serverless Inference]] — core product for real-time inference
- [[GPU Infrastructure]] — the hardware layer RunPod abstracts
- [[Cold Start]] — latency factor in serverless deployments
- [[AutoScaling]] — worker scaling mechanism in serverless
- [[vLLM]] — inference engine used in Hub deployments
- [[HuggingFace]] — model source for Hub listings
- [[summary-20260607 - Under 5 minutes to a deployed LLM endpoint — Audry Hsu, RunPod]] — source
