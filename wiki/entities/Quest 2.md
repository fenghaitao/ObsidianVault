---
title: "Quest 2"
type: entity
tags: [product, vr, hardware, meta]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/09 - Why the next AI boom is physical AI ｜ Caitlin Kalinowski (ex-OpenAI, Meta, Apple).md"]
last_updated: 2026-07-10
---

## Definition

VR headset built by [[Meta]]/[[Oculus]]; described as the best-selling VR headset of all time, achieved by aggressively redesigning for lower cost so Meta could "democratize VR."

## Key Information

- To hit a target price point, the team removed cameras, removed components, and changed materials/manufacturing processes — a full redesign for cost, per [[Caitlin Kalinowski]], while still shipping a high-quality product with low return rates.
- Failure story: partway through development (around EVT — Engineering Validation Test), the team reduced camera count from 5 to 4 for cost. This caused a mismatch between the mechanical team's and computer-vision team's interpretation of a tolerance spec (plus/minus 0.15mm vs. a "global" 0.15mm), breaking the ability to reliably track headset position in space.
- Fixed via an architectural change: two of the four cameras were locked to a shared bracket (fabricated in steel to hold tolerance) to create a fixed "source of truth" baseline, while the other two cameras floated and overlapped onto that baseline. The build stayed on schedule and shipped on time despite the scramble.
- Kalinowski considers this one of her favorite failures because the resulting design ended up better than the original plan.

## Related

- [[summary-09 - Why the next AI boom is physical AI ｜ Caitlin Kalinowski (ex-OpenAI, Meta, Apple)]] — source summary
- [[Meta]] — maker
- [[Oculus]] — product lineage
- [[Caitlin Kalinowski]] — led hardware development, recounts the camera-spec failure
- [[Hardware Compile Cycle]] — illustrates the cost of late-stage redesigns in hardware
