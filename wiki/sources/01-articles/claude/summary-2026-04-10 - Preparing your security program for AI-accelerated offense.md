---
title: "summary-2026-04-10 - Preparing your security program for AI-accelerated offense"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-04-10 - Preparing your security program for AI-accelerated offense.md"]
last_updated: 2026-07-04
---

## Core Summary

Written in the wake of Anthropic's Project Glasswing announcement (which put its frontier model, Claude Mythos Preview, to defensive cybersecurity use), this post argues that AI is collapsing the time, cost, and skill needed to find and chain software vulnerabilities into working exploits — and that within roughly 24 months, models of similar capability will be widely available to attackers. Because the same capability helps defenders, Anthropic offers a prioritized playbook based on its own security teams' experience: close the patch gap, prepare for a much higher volume of vulnerability reports, find bugs before shipping, find vulnerabilities already latent in production code, design systems to survive a breach, reduce and inventory attack surface, and shorten incident response time. It closes with etiquette for submitting vulnerability reports to third parties, and a simplified checklist for solo developers and organizations without a dedicated security team.

## Key Points

- **Premise**: AI models can already recognize patch signatures and reverse them into working exploits faster than defenders can patch; sub-frontier models have already found real vulnerabilities missed by traditional review (e.g., in Mozilla Firefox). The patch-to-exploit window is shrinking toward hours.
- **1. Close the patch gap**: patch everything on CISA's Known Exploited Vulnerabilities (KEV) catalog immediately; use EPSS (Exploit Prediction Scoring System) to prioritize the rest; aim for 24-hour patching on internet-facing systems; automate patch deployment.
- **2. Prepare for much higher vulnerability report volume**: expect an order-of-magnitude increase in findings over ~2 years; use OpenSSF Scorecard to assess open-source dependency risk; hold vendors to the same standard. AI can speed triage, flag redundant dependencies, auto-generate/validate patches, and even "AI-vendor" (reimplement) poorly-maintained small dependencies.
- **3. Find bugs before shipping**: add static analysis/AI code review to CI (gated on OWASP ASVS levels); add automated penetration testing to CD; secure the build pipeline (SLSA framework); adopt CISA Secure by Design practices; prefer memory-safe languages (Rust, Go) for new code, with AI-assisted rewrites increasingly viable for legacy C/C++.
- **4. Find vulnerabilities already in your code**: proactively scan production code (especially legacy/unowned code and internet-reachable input-parsing/auth paths) with frontier models, since it surfaces issues human review has missed for years; budget engineering time for remediation, since model scans of old code yield fewer but higher-precision findings.
- **5. Design for breach**: favor controls that hold against infinitely patient attackers (hardware-bound credentials, expiring tokens, non-existent network paths) over friction-based mitigations (rate limits, non-standard ports, SMS MFA); adopt zero trust architecture (per CISA/NCSC models), phishing-resistant hardware-bound 2FA, per-workload cryptographic identity, and short-lived tokens instead of long-lived secrets.
- **6. Reduce and inventory exposure**: maintain a current inventory of all internet-facing assets; decommission unused systems; default-deny network ingress; use AI to find dead code/endpoints and to run autonomous external red-teaming against your own perimeter.
- **7. Shorten incident response time**: put a triage model at the front of the alert queue for 100% first-pass coverage; use models as incident scribes/parallel investigators (freeing humans for containment/disclosure/comms decisions); let AI drive the detection flywheel (threat intel ingestion, candidate detections, tuning); map detection coverage to MITRE ATT&CK; run tabletop exercises for simultaneous incidents; pre-establish emergency change procedures.
- **Reporting vulnerabilities to others**: only report after human verification; state the bug's impact plainly, walk through the code path, provide a working reproduction, include a proposed patch, disclose AI involvement upfront, and defer to maintainer judgment — because low-quality automated reports are already degrading maintainer trust in AI-assisted findings.
- **If you don't have a security team**: enable automatic updates everywhere, prefer managed services over self-hosting, use passkeys/hardware security keys, and turn on free code-host security tooling (GitHub Dependabot, secret scanning, CodeQL); publish a `SECURITY.md` to triage incoming AI-assisted reports.
- Authored by Anthropic's Security Engineering and Research teams (Donny Greenberg, Jason Clinton, Michael Moore, Abel Ribbink, Jackie Bow, with contributions from Jannet Park, Gabby Curtis, Stuart Ritchie).

## Related

- [[ProjectGlasswing]] — Anthropic's defensive-cybersecurity initiative that prompted this guidance
- [[AIAcceleratedOffense]] — the concept this article's playbook addresses
- [[AutomatedSecurityReview]] — Claude Code's own security-review feature, a narrower instance of the "find bugs before shipping" recommendation
- [[CodeSecurity]] — broader development-workflow security practices this article's recommendations extend
- [[VulnerabilityDetection]] — vulnerability classes and detection patterns referenced by this article's scanning recommendations
- [[Anthropic]] — publisher and author of this guidance
