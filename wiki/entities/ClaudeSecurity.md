---
title: "Claude Security"
type: entity
tags: [claude, product, security, enterprise, vulnerability-scanning, opus-4.7]
sources: ["raw/01-articles/claude/2026-04-30 - Claude Security is now in public beta.md", "raw/01-articles/claude/2026-05-21 - How our partners are putting Opus to work for cybersecurity.md", "raw/01-articles/claude/2026-05-27 - Zero Trust for AI agents.md"]
last_updated: 2026-07-07
---

## Definition

Claude Security (previously "Claude Code Security") is Anthropic's code-vulnerability-scanning and patch-generation product, built on [[Claude4.7Opus|Claude Opus 4.7]], that entered public beta for [[ClaudeEnterprise|Claude Enterprise]] customers on April 30, 2026. It scans repositories for vulnerabilities and generates targeted, explained patches, accessible from the Claude.ai sidebar or claude.ai/security with no API integration or custom agent build required.

## Key Information

- **History**: tested by hundreds of organizations of all sizes during a limited research preview (under the name Claude Code Security) for about two months before this public-beta release; preview feedback shaped the release.
- **Access (as of April 30, 2026)**: public beta, Claude Enterprise customers only. Claude Team and Max access described as "coming soon."
- **Workflow**: select a repository (optionally scoped to a directory or branch) → start a scan → Claude reasons about the code like a security researcher — tracing data flows and cross-file/cross-module interactions rather than matching known vulnerability patterns → each finding reports a confidence rating, severity, likely impact, and reproduction steps, plus a proposed targeted patch openable in [[ClaudeCode|Claude Code on the Web]] to work through the fix in context.
- **Detection pipeline**: a multi-stage validation pipeline independently examines each finding before it reaches an analyst, reducing false positives; every finding carries an explicit confidence rating.
- **New in this GA release** (vs. the research preview): scheduled scans (recurring cadence, not just one-off audits), directory-level scan targeting within a repo, dismissing findings with documented reasons (auditable triage trail for future reviewers), exporting findings as CSV or Markdown, and sending scan results via webhook to Slack, Jira, or other tools.
- **Named customer**: [[DoorDash]] — Suha Can (VP and Chief Security Officer) credits it with surfacing deep vulnerabilities accurately and piping findings into existing engineering workflows.
- **Ecosystem**: technology partners (CrowdStrike, Microsoft Security, [[PaloAltoNetworks|Palo Alto Networks]], SentinelOne, TrendAI, Wiz) are embedding Opus 4.7 directly into their own security tools; services partners (Accenture, BCG, [[Deloitte]], Infosys, [[PwC]]) help enterprises deploy Claude-integrated vulnerability-management, secure-code-review, and incident-response solutions.
- **Safeguards**: Opus 4.7 runs new automatic cyber safeguards that detect and block requests suggestive of prohibited/high-risk cybersecurity use; legitimate work that trips these can be authorized via Anthropic's Cyber Verification Program.
- **Positioning vs. Project Glasswing**: [[ProjectGlasswing]] gives select partners access to Claude Mythos Preview — Anthropic's most powerful model, able to "match or surpass even elite human experts" at finding *and exploiting* vulnerabilities. Claude Security is explicitly the broadly-available counterpart, built on the strongest *generally-available* model (Opus 4.7) instead, aimed at defenders generally rather than a narrow partner set.
- **Distinct from** [[AutomatedSecurityReview]]: that feature is Claude Code's terminal `/security-review` command and GitHub Action (pre-commit / per-PR review inside a dev's existing terminal/CI workflow). Claude Security is a separate, standalone scanning product surfaced through Claude.ai, aimed at security teams doing repository-wide/scheduled scans rather than developers reviewing a single diff. Both sit under the broader [[CodeSecurity]] umbrella and target similar [[VulnerabilityDetection|vulnerability classes]].

## Related

- [[summary-2026-04-30 - Claude Security is now in public beta]] — source announcement
- [[summary-2026-05-21 - How our partners are putting Opus to work for cybersecurity]] — partner results and offerings live on Opus
- [[Claude4.7Opus]] — the model Claude Security is built on
- [[ClaudeEnterprise]] — the plan Claude Security is exclusively available to at public-beta launch
- [[ProjectGlasswing]] — Anthropic's adjacent partner-only offensive/defensive security initiative using Claude Mythos Preview
- [[AutomatedSecurityReview]] — Claude Code's terminal `/security-review` command and GitHub Action, a related but distinct security feature
- [[VulnerabilityDetection]] — vulnerability classes and detection patterns Claude Security also targets
- [[CodeSecurity]] — the broader development-workflow security concept this product belongs to
- [[AIAcceleratedOffense]] — the security-program playbook motivating this release
- [[ClaudeCode]] — hosts "Claude Code on the Web," where generated patches are opened to work through fixes
- [[DoorDash]] — named customer with attributed quote
- [[Wiz]] — named technology partner
- [[PaloAltoNetworks]] — named technology partner
- [[CrowdStrike]] — named technology partner
- [[TrendMicro]] — named technology partner (TrendAI)
- [[SentinelOne]] — named technology partner
- [[Accenture]] — named services partner
- [[BCG]] — named services partner
- [[Deloitte]] — named services partner
- [[Infosys]] — named services partner
- [[PwC]] — named services partner
- [[CTEM]] — framework underlying Deloitte's Claude Security offering
- [[VirtualPatching]] — mitigation technique underlying Trend Micro's Claude Security offering
- [[AgenticSecurity]] — governance paradigm underlying PwC's Claude Security offering
- [[ZeroTrustAIAgents]] — Zero Trust framework for AI agents, recommending Claude Security as the get-started product
- [[summary-2026-05-27 - Zero Trust for AI agents]] — source announcing the Zero Trust for AI agents framework
- [[summary-2026-05-27 - Using LLMs to secure source code]] — related security scanning workflow guidance
- [[ThreatModeling]] — the first step of the security scanning workflow Claude Security operationalizes
- [[VulnerabilityVerification]] — the verification phase Claude Security's multi-stage validation pipeline implements
- [[VulnerabilityTriage]] — the triage phase for ranked, deduplicated findings
- [[AutomatedPatching]] — the patching phase for generated, validated fixes
