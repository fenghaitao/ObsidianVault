---
title: "summary-20260512 - Pablo Galindo Salgado & David Hewitt - Maintaining OSS in the age of AI - PyAI London at AIE 2026"
type: source
tags: [source, pydantic, pyai-london, open-source, maintainers, ai-slops]
sources: ["raw/03-transcripts/Pydantic/Channel Only/20260512 - Pablo Galindo Salgado & David Hewitt - Maintaining OSS in the age of AI - PyAI London at AIE 2026.md"]
last_updated: 2026-06-25
---

## Core Summary

Pablo Galindo Salgado (CPython core developer) and David Hewitt (PyO3/Pydantic) deliver a raw, emotional talk on the crisis facing open source maintainers in the age of AI. The core problem: AI has automated the easy part (code generation) while the hard part (knowing what to change, reviewing, mentoring) remains human. The result is an asymmetric DDoS on maintainer attention — 2 minutes to generate a PR, 30 minutes to 3 hours to review it. 4% of public GitHub commits were AI-generated as of February 2026, growing exponentially.

## Key Points

- Asymmetric relationship: AI makes PR creation nearly free while review cost remains high
- "Good first issues" are being obliterated by bots within nanoseconds — killing the new-contributor pipeline
- Security: kernel maintainers receiving ~10 correct AI-found vulnerabilities per day; can't keep up
- Every PR is now a potential attack vector — maintainers must scrutinize contributors as potential threats
- Reputation farming: bots build GitHub profiles to gain trust for later supply chain attacks
- Trust erosion: the connection between contributor and maintainer that built open source communities is breaking
- 96% of developers don't trust AI-generated code, yet most use it
- Maintainer burnout: "our ability to care is a global resource that is depleting"
- The old path (first PR -> contributor -> maintainer) may be gone; something new must emerge
- Need "back pressure" — some filter or friction to reduce slop without gatekeeping newcomers
- Human attestation networks (Seth Larson's proposal) as one possible solution
- Despite the crisis, both speakers remain hopeful: AI frees maintainers from drudgery, enables projects like Monty

## Related

- [[OpenSourceSustainability]] — the funding and maintenance crisis
- [[AISlop]] — AI-generated low-quality contributions
- [[CPython]] — the Python language project
- [[PabloGalindoSalgado]] — CPython core developer
- [[DavidHewitt]] — PyO3/Pydantic developer
- [[SupplyChainSecurity]] — the security dimension
