---
title: "AISBOM"
type: concept
tags: [context, security, supply-chain, provenance, sbom]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - Context Is the New Code — Patrick Debois, Tessl.md"]
last_updated: 2026-06-29
---

## Definition
AI SBOM (AI Software Bill of Materials) is a provenance record for AI context packages (skills, prompts, instructions) that tracks how a context artifact was built — including what model generated it, what tools were used, and what dependencies it includes. It is analogous to the SBOM concept in traditional software supply chain security.

## Key Information
- Introduced by Patrick Debois as part of context security in the CDLC
- Tracks: who built the skill, what model was used, how it was constructed, what dependencies it has
- Analogous to traditional SBOM (Software Bill of Materials) for software supply chain security
- Addresses the security concern of downloading and running context from strangers
- Part of a broader context security approach alongside Snyk-like scanning and context filters

## Related
- [[summary-20260503 - Context Is the New Code — Patrick Debois, Tessl]] — source
- [[ContextSecurity]] — the broader security domain
- [[ContextDistribution]] — the practice that creates supply chain risks
- [[ContextPackageRegistry]] — registries where provenance matters
- [[SupplyChainAttack]] — the threat AI SBOM helps mitigate
