---
title: "summary-2026-05-27 - Using LLMs to secure source code"
type: source
tags: [source, claude-blog, security, vulnerability-scanning]
sources: ["raw/01-articles/claude/2026-05-27 - Using LLMs to secure source code.md"]
last_updated: 2026-07-07
---

## Core Summary

Anthropic shares best practices for using [[Claude4.7Opus|Claude Opus]] to secure source code through a six-step workflow: threat modeling, sandbox setup, vulnerability discovery, verification, triage, and patching. The primary takeaway is that LLM-powered vulnerability discovery is now straightforward to parallelize, and the bottleneck has shifted to verification, triage, and patching — as of May 2026, Anthropic's [[ProjectGlasswing|Glasswing]] scanning had disclosed 1,596 vulnerabilities in open source software, with only 97 patched. The article draws on experience working with security teams and partners, providing concrete guidance on each step, including prompt engineering tips, sandbox design, adversarial verification, deduplication strategies, and TDD-based patching with adversarial validation.

## Key Points

- Discovery is now easy to parallelize with frontier models; the bottleneck has shifted to verification, triage, and patching.
- Building a threat model (bootstrapped from code, docs, CVE history, and optionally refined through an interview with a system owner) dramatically improves result quality — one team saw findings become "exploitable 90 percent of the time" with a well-defined threat model.
- A sandbox serves two purposes: protecting your systems via strong isolation (containers for reading code, microVMs/VMs with no egress for running PoCs) and proving exploitability by letting the agent compile, test, and detonate proofs of concept.
- Discovery optimizes for recall with simple, non-prescriptive prompts and tool access; verification optimizes for precision with independent, adversarial agents that assume each finding is a false positive.
- Adding an adversarial verifier roughly halved the rate of non-exploitable findings; requiring a working PoC brought the false positive rate to near zero.
- Triage prevents alert fatigue through deduplication (deterministic + model-driven) and severity scoring based on preconditions and access requirements, calibrated against the threat model.
- Patching should follow TDD (write a failing test first), validate patches by re-running PoCs, fix root causes rather than symptoms, and include an adversarial check before shipping.
- A companion GitHub repository (`defending-code-reference-harness`) provides skills (`threat-model`, `vuln-scan`, `triage`, `patch`) and a demo harness for autonomous scanning.

## Related

- [[Claude4.7Opus]] — the model used for security scanning workflows
- [[ProjectGlasswing]] — Anthropic's security initiative that disclosed 1,596 vulnerabilities
- [[ClaudeSecurity]] — the standalone enterprise vulnerability-scanning product
- [[ThreatModeling]] — the first step of the six-step workflow
- [[VulnerabilityDetection]] — the discovery phase of the workflow
- [[VulnerabilityVerification]] — independent adversarial verification to reduce false positives
- [[VulnerabilityTriage]] — deduplication and severity ranking
- [[AutomatedPatching]] — LLM-generated security patches with adversarial validation
- [[Sandboxing]] — sandbox design for security scanning (microVMs, faithful-to-production environments)
- [[AIAcceleratedOffense]] — the broader context motivating this defensive workflow
- [[TestDrivenDevelopment]] — TDD applied to security patch generation
- [[GitHub]] — hosts the defending-code-reference-harness repository
