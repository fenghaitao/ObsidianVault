---
title: "Auto Scaling for Voice Agents"
type: concept
tags: [voice-agents, infrastructure, scaling, reliability, stateful-connections]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI.md"]
last_updated: 2026-06-30
---

## Definition
Auto scaling for voice agents is the practice of dynamically adjusting compute resources to match demand for voice agent workloads, with unique challenges due to the stateful, long-lived nature of voice connections compared to traditional asynchronous systems.

## Key Information
- Scale up must be more aggressive than async systems — the last thing you want is requests slowing down or backing up during a live voice conversation
- Scale down is tricky because voice connections are stateful and long-lived — you cannot arbitrarily kill a pod mid-conversation
- Must wait for active conversations to finish before scaling down instances
- Night/weekend demand may be lower, enabling scale-down during off-peak hours
- Contrast with traditional async request/response systems where connections are short-lived and stateless
- Global deployments add complexity: models should be geographically distributed for latency and data residency

## Related
- [[Voice Agent Pipeline Architecture]] — the system being auto-scaled
- [[CoLocation (Voice AI)]] — related infrastructure concern
- [[summary-20260531 - Engineering voice agents： Latency, quality, and scale — Rishabh Bhargava, Together AI]] — source
