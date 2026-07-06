---
title: "summary-2026-04-30 - Claude Security is now in public beta"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-04-30 - Claude Security is now in public beta.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic announced the public beta of **Claude Security** (formerly **Claude Code Security**), a code vulnerability scanning and patch-generation product built on [[Claude4.7Opus|Claude Opus 4.7]], now available to all [[ClaudeEnterprise|Claude Enterprise]] customers directly from the Claude.ai sidebar or at claude.ai/security. Framed against a backdrop of AI-accelerated offense — where the same models that find vulnerabilities are becoming increasingly effective at autonomously exploiting them — the post positions Claude Security as the broadly-available counterpart to [[ProjectGlasswing]], which uses Anthropic's most powerful (partner-only) model, Claude Mythos Preview, for elite offensive/defensive security work. Claude Security scans a selected repository, directory, or branch by reasoning about code the way a security researcher would (tracing data flow and cross-file/module interactions rather than pattern-matching known signatures), then reports each finding with a confidence rating, severity, likely impact, and a reproduction, plus a proposed patch that can be opened in [[ClaudeCode|Claude Code on the Web]]. After a two-month limited research preview tested by hundreds of organizations, the release adds scheduled/targeted scans, directory-level scan scoping, documented finding dismissal, CSV/Markdown export, and webhook delivery to Slack/Jira/other tools. Technology partners (CrowdStrike, Microsoft Security, Palo Alto Networks, SentinelOne, TrendAI, Wiz) are embedding Opus 4.7 into their own security tools, while services partners (Accenture, BCG, Deloitte, Infosys, PwC) help enterprises deploy Claude-integrated security solutions. Access for Claude Team and Max customers is announced as "coming soon"; Enterprise-only at launch.

## Key Points

- **Product rename**: "Claude Security" was previously called "Claude Code Security" — same underlying product, now generally released to Enterprise after limited research preview.
- **Model**: built on Claude Opus 4.7, described as "among the strongest models available for finding and patching software vulnerabilities."
- **Access**: public beta, Claude Enterprise customers only, as of April 30, 2026; Claude Team and Max access described as "coming soon." Accessed via the Claude.ai sidebar or claude.ai/security; no API integration or custom agent build required.
- **Workflow**: select a repository (optionally scoped to a directory or branch) → start a scan → Claude traces data flows and cross-file/module interactions (not signature/pattern matching) → for each finding: confidence rating, severity, likely impact, reproduction steps, and a proposed targeted patch openable in Claude Code on the Web.
- **New in this release** (vs. research preview): scheduled scans (recurring cadence), directory-level scan targeting within a repo, dismiss findings with documented reasons (auditable triage trail), export findings as CSV or Markdown, webhook delivery of scan results to Slack, Jira, or other tools.
- **Detection pipeline**: multi-stage validation independently examines each finding before it reaches an analyst, reducing false positives; every result carries a confidence rating.
- **Preview history**: tested by "hundreds of organizations of all sizes" during limited research preview prior to this public beta.
- **Named customer with attributed quote**: DoorDash — Suha Can (VP and Chief Security Officer): "Claude Security helps us accelerate how we generate and secure new code at the scale and speed of DoorDash — it surfaces deep vulnerabilities accurately, and pipes findings right into our workflows so engineers can act on them in context."
- **Other quoted individuals** (company affiliation not stated in the article text as provided): Krzysztof Katowicz-Kowalewski (Staff Product Security Engineer) — "Claude Security surfaced novel, high-quality findings during our early testing of the research preview..."; Greg Janowiak (Information Security Officer) — "Claude Security grasps the actual business logic behind our code..."; Chiara La Valle (Head of Security) — "...the strongest signal for us is how quickly a finding turns into a PR we can actually merge, not a ticket"; one further unattributed quote about closing "real vulnerabilities in minutes, not days."
- **Technology partners** embedding Opus 4.7 into their own tools: CrowdStrike, Microsoft Security, Palo Alto Networks, SentinelOne, TrendAI, Wiz.
- **Services partners** deploying Claude-integrated security solutions (vulnerability management, secure code review, incident response programs): Accenture, BCG, Deloitte, Infosys, PwC.
- **Safeguards footnote**: Claude Opus 4.7 uses "new cyber safeguards" that auto-detect and block requests suggestive of prohibited/high-risk cybersecurity uses; organizations whose legitimate work might trigger these can join Anthropic's **Cyber Verification Program** to retain frontier capability access.
- **Relationship to Project Glasswing**: Glasswing gives select partners access to Claude Mythos Preview (Anthropic's most powerful model, described as able to "match or surpass even elite human experts" at both finding and exploiting vulnerabilities); Claude Security is explicitly framed as the wider-availability counterpart using the strongest *generally-available* model (Opus 4.7) instead.
- **Anomaly noted**: the article's scraped FAQ section renders only literal placeholder text "No items found." — a content-extraction artifact from the source page, not a real empty FAQ and not a prompt-injection attempt. No embedded prompt-injection-style instructions were found anywhere in this source.

## Related

- [[ClaudeSecurity]] — new entity page for the product this article announces
- [[Claude4.7Opus]] — the model Claude Security is built on
- [[ClaudeEnterprise]] — the plan this is exclusively available to at public beta launch
- [[ProjectGlasswing]] — Anthropic's adjacent partner-only offensive/defensive security initiative using Claude Mythos Preview
- [[AutomatedSecurityReview]] — Claude Code's terminal `/security-review` command and GitHub Action, a related but distinct security feature
- [[VulnerabilityDetection]] — vulnerability classes and detection patterns Claude Security also targets
- [[CodeSecurity]] — the broader development-workflow security concept this product extends
- [[AIAcceleratedOffense]] — the security-program playbook motivating this release
- [[DoorDash]] — named customer with attributed quote
- [[PaloAltoNetworks]] — named technology partner
- [[Deloitte]] — named services partner
- [[PwC]] — named services partner
