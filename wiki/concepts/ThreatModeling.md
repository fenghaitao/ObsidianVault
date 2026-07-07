---
title: "ThreatModeling"
type: concept
tags: [security, threat-modeling, trust-boundaries, vulnerability-scanning, llm-security]
sources: ["raw/01-articles/claude/2026-05-27 - Using LLMs to secure source code.md"]
last_updated: 2026-07-07
---

## Definition

Threat modeling is the process of defining a system's context, assets, entry points, and trust boundaries to guide security analysis — telling a model what types of vulnerabilities matter for a specific system and what can safely be ignored.

## Key Information

- Threat modeling is the first and foundational step in Anthropic's six-step workflow for using LLMs to secure source code. It is done once per codebase and revisited when the underlying system changes.
- **Why it matters for LLM-based scanning**: the most common cause of false positives is the model lacking a good understanding of trust boundaries. The model may flag code as vulnerable because it assumes an attacker controls an input that is actually trusted in the environment, or conversely assume an internet-facing service is internal-only and under-report true vulnerabilities. In both cases, the model is wrong about the threat model, not the code.
- **Impact on precision**: one team found that with a well-defined threat model, the model's findings "were exploitable 90 percent of the time." Another team scanning a large project had a 40% false positive rate because findings, while reproducible and exploitable, didn't fit the project's threat model.
- **Two-step process with Claude**:
  1. **Bootstrap from code, docs, and vulnerability history**: feed the model architecture docs, wikis, entry points, git history, and past CVEs — what you would hand a new security engineer on day one. Have the model produce a threat model including system context, assets, entry points, trust boundaries, and relevant vulnerability classes. One team reviewed hundreds of past CVE and security-fix commits, distilled them into "bug-shape" hints, and found three exploitable issues in an hour.
  2. **Interview a system owner** (optional but recommended): have the model interview someone who knows the system well using [[Adam Shostack]]'s four questions: *What are we building? What can go wrong? What are we doing about it? Did we do a good job?* Run the bootstrap step first so the interviewee starts from a draft rather than scratch.
- **Artifacts**: produce a `security.md` or `THREAT_MODEL.md` file stored with the code. This is used in two places: during discovery as scope (partition the code, prioritize targets, skip what is out of scope) and during triage as a filter (calibrate severity to your system and environment).
- **Role in the broader workflow**: the threat model documents what vulnerabilities you do and don't care about, and why. Without it, models may inflate severity (e.g., treating a SQL injection triggered by an admin-only config file as critical) or miss vulnerabilities by assuming internal-only access patterns.
- The `threat-model` skill in the [defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness) implements both the bootstrap and interview steps.

## Related

- [[summary-2026-05-27 - Using LLMs to secure source code]] — source article describing the full six-step workflow
- [[VulnerabilityDetection]] — the discovery phase that consumes the threat model
- [[VulnerabilityTriage]] — the triage phase that uses the threat model as a severity filter
- [[Sandboxing]] — the second step in the workflow, providing isolation and exploitability proof
- [[Claude4.7Opus]] — the model used for threat modeling and scanning
- [[AIAcceleratedOffense]] — the broader defensive paradigm motivating this workflow
- [[ClaudeSecurity]] — the enterprise product that operationalizes this workflow
