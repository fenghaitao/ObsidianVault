---
title: "cole-brian-pydantic-open-source-crisis"
type: synthesis
tags: [synthesis, comparison, open-source, sustainability, ai-slop, cole-medin, brian-casel, pydantic]
sources: []
last_updated: 2026-06-25
---

# How Cole, Brian, and Pydantic Speakers Diagnose the Open Source Sustainability Crisis

## The Shared Diagnosis

The open source sustainability crisis, as articulated across the PyAI Conf 2026 panel [[summary-20260319 - Open Source in the age of AI Panel – PyAI Conf 2026]] and Pablo Galindo Salgado & David Hewitt's talk [[summary-20260512 - Pablo Galindo Salgado & David Hewitt - Maintaining OSS in the age of AI - PyAI London at AIE 2026]], centers on one asymmetric relationship: AI has automated code generation but not code review. A PR costs 2 minutes to generate and 30 minutes to 3 hours to review. 4% of public GitHub commits are AI-generated and growing exponentially. "Good first issues" are claimed by bots in nanoseconds, killing the new-contributor pipeline that historically produced future maintainers.

The crisis has a security dimension: AI makes finding real vulnerabilities easier, overwhelming security teams. Kernel maintainers receive ~10 correct AI-found vulnerabilities per day. Every PR is now a potential attack vector — the XZ vulnerability demonstrated that sophisticated supply chain attacks can hide in plain sight.

## Cole Medin: The Consumer Perspective

Cole Medin's content doesn't directly address the open source crisis — his focus is on building with AI, not maintaining projects that receive AI contributions. However, his [[SystemEvolution]] philosophy (fix the system, not blame the agent) and [[AdversarialDev]] pattern (a separate critic agent reviews code) could be applied to automated PR review. His [[LethalTrifecta]] security model (private data + untrusted content + exfiltration vector) is directly relevant to the supply chain security dimension.

## Brian Casel: Also a Consumer

Brian Casel's content is largely silent on the open source crisis. As a solo builder consuming open source rather than maintaining widely-used projects, the slop PR problem doesn't directly affect him. His [[AgentPlatformPortability]] strategy — betting on portable patterns over specific platforms — is a consumer-side adaptation to the instability the crisis creates.

## The Pydantic Ecosystem: The Maintainer Perspective

The crisis is most directly addressed by the Pydantic-affiliated speakers, who are predominantly *maintainers* of widely-used open source projects:

**Samuel Colvin** (Pydantic, ~300M downloads/month) proposes a federated reputation system: submitting PRs costs reputation, merging earns it back. His four rules for when AI can produce mergable large PRs: known internals, known interface, existing tests, no bikeshedding. He notes that Monty itself is largely AI-generated — the crisis has a productive side when managed well.

**Jeremiah Lowin** (Prefect, FastMCP) advocates for "constructive friction" — a micro-computation tax before submitting, like the old email spam proposal. His most effective heuristic: close PRs with overly long descriptions (LLMs love verbose explanations). He tried requiring issues before PRs — bots just opened issues 1 second before PRs.

**Sebastián Ramírez** (FastAPI, ~12M downloads/day) pushes for AI disclaimers in PRs: disclose the model, prompt, and full conversation in collapsible HTML details. His philosophy: "I don't need my PR to be accepted. I want this problem to be solved." He also notes that lawyers often block employees from contributing to open source — legal reform is needed.

**Guido van Rossum** (Python creator) describes CPython's pragmatic approach: AI tools are fine, but PRs must show human involvement — no response to follow-up questions means the PR gets closed after 2 weeks. He notes this isn't entirely new: CPython has always received low-effort contributions from people wanting "Python contributor" on their resume.

**Pablo Galindo Salgado** (CPython core developer) delivers the most emotional diagnosis: "our ability to care is a global resource that is depleting." The old contributor-to-maintainer pipeline may be gone forever. Every interaction is now potentially antagonistic — is this contributor a human or a bot farming reputation for a future supply chain attack?

**David Hewitt** (PyO3, Pydantic) notes the irony: he now produces drive-by AI PRs himself on other projects, potentially contributing to the same problem he complains about. Trust is established over long time and is now eroding from both sides.

## Proposed Solutions

The solutions span three categories:

**Technical**: reputation systems (Samuel Colvin), constructive friction (Jeremiah Lowin), AI detection heuristics (long descriptions, em-dash counting), human attestation networks (Seth Larson's proposal for cryptographically proving humanity).

**Social**: AI disclaimers in PRs (Sebastián Ramírez), requiring human response to follow-up questions (Guido van Rossum), community building through meetups and conferences.

**Economic**: the Open Source Pledge ($2,000/engineer/year, started by Sentry, joined by Prefect), direct donations (Anthropic gave $1.5M to PSF), legal reform to allow employees to contribute, corporate sponsorship of events and spaces.

No single solution is sufficient. The panel's consensus: the genie is out of the bottle, and something new must emerge — but nobody knows exactly what.

## Related

- [[AISlop]] — the contribution quality crisis
- [[OpenSourceSustainability]] — the broader challenge
- [[SamuelColvin]] — reputation system proposal
- [[JeremiahLowin]] — constructive friction proposal
- [[SebastianRamirez]] — AI disclaimer proposal
- [[GuidoVanRossum]] — CPython's pragmatic approach
- [[PabloGalindoSalgado]] — the emotional diagnosis
- [[DavidHewitt]] — the trust erosion perspective
- [[SupplyChainSecurity]] — the security dimension
- [[LethalTrifecta]] — Cole's security model
- [[SystemEvolution]] — Cole's fix-the-system philosophy
