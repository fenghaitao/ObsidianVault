---
title: "AISlop"
type: concept
tags: [open-source, ai, quality, maintainers]
sources: [raw/03-transcripts/Pydantic/Channel Only/20260319 - Open Source in the age of AI Panel – PyAI Conf 2026.md, raw/03-transcripts/Pydantic/Channel Only/20260512 - Pablo Galindo Salgado & David Hewitt - Maintaining OSS in the age of AI - PyAI London at AIE 2026.md]
last_updated: 2026-06-25
---

## Definition

AI slop refers to low-quality, AI-generated contributions (PRs, issues, security reports) that flood open source projects. The term captures both the volume problem (too many) and the quality problem (not actually useful). Described as a "DDoS on maintainer attention."

## Key Information

### Scale

- 4% of public GitHub commits were AI-generated as of February 2026, growing exponentially
- ~91% increase in code review time with high AI adoption
- Kernel maintainers receiving ~10 correct AI-found vulnerabilities per day
- "Good first issues" are claimed by bots within nanoseconds

### The Asymmetry Problem

- Creating an AI-generated PR: ~2 minutes
- Reviewing that PR: 30 minutes to 3 hours
- The cost to participate has gone to zero while the cost to maintain has not

### Proposed Solutions

- **Reputation systems**: submitting PRs costs reputation, merging earns it back (Samuel Colvin)
- **Constructive friction**: micro-computation tax before submitting (Jeremiah Lowin)
- **Heuristics**: close PRs with overly long descriptions (LLMs love verbose explanations)
- **AI disclaimers**: include model, prompt, and full conversation in PRs (Sebastián Ramírez)
- **Human attestation networks**: Seth Larson's proposal for cryptographically proving humanity
- **GitHub-level**: AI/human identity system, reputation metrics on profiles

### Secondary Effects

- Killing the new-contributor pipeline: first PRs that built future maintainers are now impossible
- Trust erosion: maintainers must scrutinize every contributor as a potential attacker
- Security: AI makes finding real vulnerabilities easier, overwhelming security teams
- Reputation farming: bots build credible GitHub profiles for future supply chain attacks

## Related

- [[OpenSourceSustainability]] — the broader crisis
- [[SupplyChainSecurity]] — the security dimension
- [[SamuelColvin]] — proposed reputation system
- [[JeremiahLowin]] — proposed constructive friction
- [[SebastianRamirez]] — proposed AI disclaimers
- [[PabloGalindoSalgado]] — CPython maintainer perspective
- [[cole-brian-pydantic-open-source-crisis]] — cross-cutting synthesis
