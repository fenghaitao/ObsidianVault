---
title: "CVE Remediation at Scale"
type: concept
tags: [security, agents, orchestration, automation, openhands]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands.md"]
last_updated: 2026-06-26
---

## Definition
CVE remediation at scale is the practice of using parallel AI agents to automatically scan repositories for known vulnerabilities (CVEs), fix them, and open pull requests. It is one of the most successful applications of agent orchestration, with reported 30x improvements in resolution time.

## Key Information
- An initial scanning agent detects the programming language and chooses appropriate scanning tools (Trivy for Docker images, npm audit for Node.js, etc.).
- For each vulnerability found, a separate agent is dispatched to research solvability, update dependencies, fix breaking API changes, and open a PR.
- Running solvers in parallel means individual PRs can be merged as they're ready; if one agent gets stuck, others still succeed.
- Even 90-95% resolution provides significant value — perfection is not required.
- One OpenHands client with tens of thousands of developers and thousands of repos achieved a 30x improvement in CVE resolution time.
- The workflow: new CVE announced → kick off scan agents → identify vulnerable repos → dispatch fixer agents → open PRs → downstream teams click merge.
- Cloud-based sandboxes enable running hundreds or thousands of remediation agents concurrently.
- The OpenHands workshop demonstrates building this pipeline: scan repo → get vulnerability list → dispatch parallel solver agents.

## Related
- [[summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — source
- [[Agent Orchestration]] — broader practice
- [[OpenHands]] — platform used for remediation
- [[Trivy]] — vulnerability scanner used
- [[CloudBased Agent Sandboxes]] — infrastructure for scale
- [[Parallel Agents]] — execution model
