---
title: "SupplyChainSecurity"
type: concept
tags: [security, open-source, supply-chain, vulnerabilities]
sources: [raw/03-transcripts/Pydantic/Channel Only/20260512 - Pablo Galindo Salgado & David Hewitt - Maintaining OSS in the age of AI - PyAI London at AIE 2026.md, raw/03-transcripts/Pydantic/Channel Only/20260319 - Open Source in the age of AI Panel – PyAI Conf 2026.md]
last_updated: 2026-06-25
---

## Definition

Supply chain security is the practice of protecting software from vulnerabilities introduced through dependencies, contributions, or build processes. In the AI era, AI-generated code dramatically increases the attack surface — every PR is a potential vector, and bots can farm GitHub reputation to build trust for future attacks.

## Key Information

- The XZ vulnerability demonstrated how sophisticated attacks can hide in plain sight over years
- AI makes finding real vulnerabilities easier, overwhelming security teams with valid reports
- Reputation farming: bots build credible GitHub profiles through many small contributions, then submit malicious PRs
- Maintainers must now scrutinize every contributor as a potential threat
- Kernel maintainers receiving ~10 correct AI-found vulnerabilities per day

## Related

- [[AISlop]] — the contribution quality crisis
- [[OpenSourceSustainability]] — the broader challenge
- [[LethalTrifecta]] — Cole Medin's security model
