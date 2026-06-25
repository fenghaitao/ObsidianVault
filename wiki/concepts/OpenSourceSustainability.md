---
title: "OpenSourceSustainability"
type: concept
tags: [open-source, funding, maintainers, community]
sources: [raw/03-transcripts/Pydantic/Channel Only/20260319 - Open Source in the age of AI Panel – PyAI Conf 2026.md, raw/03-transcripts/Pydantic/Channel Only/20260512 - Pablo Galindo Salgado & David Hewitt - Maintaining OSS in the age of AI - PyAI London at AIE 2026.md]
last_updated: 2026-06-25
---

## Definition

Open source sustainability is the challenge of keeping open source projects healthy — funded, maintained, and secure — in an era where AI has dramatically increased the volume of contributions while maintainer resources remain constant or shrink.

## Key Information

### The Crisis

- Maintainers are mostly unpaid volunteers ("every time they double our salary, we start at zero")
- AI has automated code generation but not code review — asymmetric cost structure
- 4% of public GitHub commits are AI-generated and growing exponentially
- Maintainer burnout: "our ability to care is a global resource that is depleting"

### Funding Solutions

- **Open Source Pledge**: companies donate $2,000/year/engineer to open source (started by Sentry, joined by Prefect and others)
- **Direct donations**: Anthropic donated $1.5M to the Python Software Foundation for security
- **Corporate sponsorship**: providing space, food, and logistics for meetups and events
- **Commercial open source**: Pydantic's model — open source core, commercial services

### Community Solutions

- **Human attestation networks**: cryptographically proving humanity to build trust (Seth Larson)
- **Reputation systems**: federated reputation that costs to spend, earns on merge
- **Constructive friction**: making contributions slightly harder to deter bots without blocking newcomers
- **AI disclaimers**: requiring disclosure of AI use in contributions

### The Pipeline Problem

The traditional path from first-time contributor to maintainer is breaking:
- "Good first issues" are claimed by bots in nanoseconds
- New contributors can't establish reputation through small fixes
- The human connection that built open source communities is being replaced by bot interactions
- Underrepresented groups and juniors are disproportionately affected

## Related

- [[AISlop]] — the contribution quality crisis
- [[SupplyChainSecurity]] — the security dimension
- [[SamuelColvin]] — proposed reputation system
- [[JeremiahLowin]] — Open Source Pledge member
- [[PabloGalindoSalgado]] — CPython maintainer perspective
