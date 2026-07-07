---
title: "ProjectGlasswing"
type: entity
tags: [anthropic, cybersecurity, initiative, offensive-security]
sources: [raw/01-articles/claude/2026-04-10 - Preparing your security program for AI-accelerated offense.md, raw/01-articles/claude/2026-05-27 - Using LLMs to secure source code.md]
last_updated: 2026-07-07
---

## Definition

Project Glasswing is Anthropic's initiative to apply the cybersecurity capabilities of its frontier model, Claude Mythos Preview, to defensive purposes — helping organizations find and fix vulnerabilities before attackers using AI can exploit them.

## Key Information

- Announced alongside a technical blog post describing how AI models are rapidly reducing the resources, time, and skill required to find and exploit software vulnerabilities.
- Uses Claude Mythos Preview — described as Anthropic's "newest frontier model" at time of announcement (April 2026) — for defensive security work; sub-Mythos-level models have already found serious vulnerabilities missed by traditional review (e.g., in Mozilla Firefox).
- Motivates the [[AIAcceleratedOffense]] playbook: a set of prioritized security-program recommendations Anthropic published based on what its security teams learned securing real codebases and systems with frontier models.
- Anthropic states it will update this guidance as it and its "Project Glasswing partners" continue cybersecurity work — implying an external partner program, not solely an internal initiative.
- **Scanning results (as of May 22, 2026)**: as part of Glasswing's open source software scanning, Anthropic had disclosed 1,596 vulnerabilities. To their knowledge, only 97 of these had been patched — a 6% patch rate that illustrates the discovery-to-remediation gap and validates the thesis that verification, triage, and patching are now the bottleneck, not discovery.
- **Inferred connection**: [[ClaudeFable5]]'s page notes that Mythos 5 (launched at Code with Claude Tokyo 2026) has the "same foundation [as Fable 5], safeguards lifted for Glasswing partners" — suggesting "Claude Mythos Preview" (this article, April 2026) is an earlier preview build that the general-availability "Mythos 5" model later succeeded. Not explicitly confirmed in either source; flagged as inferred.

## Related

- [[ClaudeSecurity]] — the broadly-available (Opus 4.7-based) counterpart product; Glasswing is reserved for a narrower partner set on Claude Mythos Preview
- [[summary-2026-04-10 - Preparing your security program for AI-accelerated offense]] — source summary
- [[summary-2026-05-27 - Using LLMs to secure source code]] — updated scanning statistics and workflow guidance
- [[AIAcceleratedOffense]] — the defensive playbook this initiative produced
- [[Anthropic]] — the company behind the initiative
- [[ClaudeFable5]] — sibling model page referencing "Glasswing partners" and Mythos 5
- [[VulnerabilityDetection]] — the discovery phase that Glasswing operationalizes at scale
- [[VulnerabilityVerification]] — the verification bottleneck Glasswing's statistics illustrate
- [[VulnerabilityTriage]] — the triage bottleneck Glasswing's statistics illustrate
