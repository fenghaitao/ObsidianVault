---
title: "Trivy"
type: entity
tags: [tool, security, vulnerability-scanning, containers]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands.md"]
last_updated: 2026-06-26
---

## Definition
Trivy is an open-source vulnerability scanner for containers and other artifacts. In the OpenHands CVE remediation workshop, agents use Trivy to scan Docker images for known vulnerabilities.

## Key Information
- Open-source vulnerability scanner used for scanning container images and code dependencies
- In the OpenHands CVE remediation pipeline, the initial scanning agent can detect the programming language and choose appropriate scanning tools, including Trivy for Docker images
- Part of the automated vulnerability detection step before parallel remediation agents are dispatched

## Related
- [[summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — source
- [[CVE Remediation at Scale]] — use case
- [[OpenHands]] — platform using Trivy
- [[Docker]] — container platform scanned by Trivy
