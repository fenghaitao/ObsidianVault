---
title: "Harshil Agrawal"
type: entity
tags: [person, cloudflare, security, sandboxing, developer-advocate]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Why, and how you need to sandbox AI-Generated Code — Harshil Agrawal, Cloudflare.md"]
last_updated: 2026-06-30
---

## Definition
Harshil Agrawal is a Senior Developer Advocate at Cloudflare who builds things with AI and educates others on AI security practices. He is the creator of Prompt Motion, a video generation app that uses container-based sandboxing, and an OpenClaw alternative built on Cloudflare's developer platform.

## Key Information
- Senior Developer Advocate at Cloudflare
- Created Prompt Motion (promptmotion.app), a video generator app where users describe motion graphics in natural language and AI generates a running application with live preview
- Built an OpenClaw alternative on Cloudflare's developer platform using Dynamic Worker Isolates for sandboxed skill execution
- Advocates for capability-based security: default deny everything, explicitly grant minimal capabilities
- Presented a comprehensive framework for sandboxing AI-generated code covering three threat vectors, two concrete approaches (isolates and containers), and a universal eight-point checklist
- Emphasizes that AI-generated code is functionally untrusted code from the internet and should be treated accordingly
- Demonstrates practical implementations using Cloudflare's Dynamic Worker Isolates (WorkerD) and Container VMs

## Related
- [[summary-20260408 - Why, and how you need to sandbox AI-Generated Code — Harshil Agrawal, Cloudflare]] — source
- [[Cloudflare]] — employer
- [[Prompt Motion]] — video generator app
- [[WorkerD]] — isolate sandbox used in OpenClaw alternative
- [[CapabilityBasedSecurity]] — core security principle advocated
- [[Sandboxing]] — broader topic
- [[V8Isolates]] — execution environment
- [[ContainerBased Sandboxing]] — container approach used in Prompt Motion
- [[aiDotEngineer]] — conference where he presented
