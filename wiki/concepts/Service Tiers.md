---
title: "Service Tiers"
type: concept
tags: [pricing, api, google, genmedia, priority, flex, performance]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind.md"]
last_updated: 2026-06-29
---

## Definition
Service Tiers are Google DeepMind's pricing and performance levels for API model access, offering trade-offs between cost, speed, and queue priority. Three tiers were available as of May 2026: Normal, Flex, and Priority.

## Key Information
- **Normal tier**: Standard pricing, standard queue — you wait in line with everyone else
- **Flex tier**: 50% discount, but requests can be delayed up to a few minutes; suitable for non-urgent batch work
- **Priority tier**: 2x the normal price, but guaranteed fast-track processing (like airport priority lanes)
- Shipped the week of the aiDotEngineer conference (mid-May 2026)
- Not all models support all tiers (VEO and Lyria support was uncertain at launch)
- Usage is set via a service tier priority parameter in the API client configuration
- Recommended for demos and production where latency matters; Flex is suitable for cost-sensitive batch processing

## Related
- [[summary-20260518 - Let's go Bananas with GenMedia — Guillaume Vernade, Google DeepMind]] — source
- [[GenMedia]] — product suite using service tiers
- [[GoogleDeepMind]] — provider
