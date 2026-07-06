---
title: "LegalAI"
type: concept
tags: [legal, legal-tech, ai-agents, compliance, access-to-justice]
sources: ["raw/01-articles/claude/2026-05-12 - Claude for the legal industry.md", "raw/01-articles/claude/2025-12-08 - How Anthropic's legal team cut review times from days to hours with Claude.md", "raw/01-articles/claude/2026-05-15 - Deploying Claude across the legal industry.md"]
last_updated: 2026-07-05
---

## Definition

Legal AI refers to deploying Claude across the legal industry's fragmented technology stack — contract lifecycle systems, research platforms, document management, e-discovery, data rooms, and firm-specific precedents — via MCP connectors and practice-area plugins/skills, so legal teams get consistent, playbook-aligned output (drafting, redlining, triage, research) rather than generic chat answers.

## Key Information

- **Why connectors + plugins**: legal work runs on a specific, fragmented stack; [[MCPConnector|MCP connectors]] bring matter-specific documents/communications/records into Claude, while practice-area [[ClaudeCodePlugins|plugins]] package the tasks lawyers run most often. Both are built on open protocols so firms can customize to their own practice.
- **May 2026 expansion**: 20+ new MCP connectors (contract lifecycle and drafting, deal rooms and transaction documents, document management, expert networks and skills, e-discovery and review, fiduciary-grade workflows, legal research and case law, legal AI assistants, public service) plus 12 new practice-area plugins via a dedicated Legal Marketplace (github.com/anthropics/claude-for-legal). Legal professionals are cited as [[ClaudeCowork|Claude Cowork]]'s most engaged knowledge-work user segment since its first legal plugin shipped.
- **Setup interview pattern**: each practice-area plugin opens with a short interview capturing a team's playbook, escalation chain, risk calibration, and house style, so output is tailored rather than generic. A subset (Commercial Legal, Corporate Legal, Litigation Legal, Product Legal) are also available as cookbooks deployable as [[ClaudeManagedAgents|Managed Agents]] for programmatic use.
- **Office integration**: one shared context across Word (drafting, redlining, clause-by-clause playbook comparison, comment scrubbing, formatting checks, fallback-language lookup), Outlook (contract-request triage, response drafting, follow-up scheduling), Excel, and PowerPoint — see [[ClaudeForExcelPowerPoint]]. Projects gives matter teams a persistent workspace for precedents and prior drafts.
- **Internal case study (Dec 2025)**: Anthropic's own legal team used [[ClaudeCodeSkills|Skills]] for workflow consistency (a marketing-review skill encoding historical guidance to flag publicity-rights, overstated-claims, and statistical-accuracy issues) and for personal voice (a skill trained on ten of a lawyer's own memos to replicate his formatting/phrasing). Different Skills served different specialties (employment, commercial, privacy, corporate) — illustrating Skills as a vehicle for institutional/individual expertise transfer, cutting review times from days to hours.
- **Ecosystem**: early third-party plugin/skill/style contributors include Box, Legal Quants, Lawve AI (also spelled "Lawvable" in the same source — inconsistency, not corrected), and [[ThomsonReuters|Thomson Reuters]]. Legal-tech vendors increasingly build their own products on Claude rather than just consuming it: [[ThomsonReuters|Thomson Reuters]]' CoCounsel was rebuilt on the Claude Agent SDK; [[Harvey]] and [[SolveIntelligence|Solve Intelligence]] are cited doing the same.
- **Access to justice**: partnership with the Free Law Project, the Justice Technology Association, and other legal-aid/public-service organizations; qualifying legal aid clinics, public defenders, and nonprofit legal services organizations get discounted pricing via the Claude for Nonprofits program. Free/low-cost tools from BoardWise, [[Courtroom5]], Descrybe, and Free Law Project are available via MCP connectors. Quote: *"Most people don't know they have legal rights until it's too late to use them. Claude can now meet them where they are — in the moment they're scared and searching for answers."* — Sonja Ebron, CEO & Co-Founder, [[Courtroom5]].
- **Model**: the May 2026 expansion is built on [[Claude4.7Opus|Claude Opus 4.7]], billed as Anthropic's most capable publicly available model for legal reasoning and long-document work.
- **Named legal-AI-native companies in the wiki**: [[Harvey]] (BigLaw Bench, 90.2% on Opus 4.6), [[Legora]] (unified legal drafting workspace), [[LexisNexis]] (research/analytics, early Claude 2 adopter), [[SolveIntelligence|Solve Intelligence]] (new, May 2026).
- **Industry-wide adoption surge (May 2026 deployment guide)**: per the 2026 [[FTIConsulting|FTI Consulting]] / [[Relativity]] General Counsel Report, 87% of general counsel now report generative-AI use within their teams, up from 44% the prior year and just 20% in 2023 — attributed to matters getting more complex and clients expecting faster turnaround. Anthropic frames the firms/departments "pulling ahead" as those embedding agentic AI into how lawyers actually practice, and published a practical deployment guide covering which Claude product to use for which workflow plus a three-phase adoption roadmap.
- **Workflow coverage cited industry-wide**: contract review and redlining, M&A diligence, privacy impact assessments, regulatory monitoring, litigation prep, and outside counsel oversight — most legal teams run more than one Claude product to cover this range.

## Related

- [[FinancialServicesAI]] — sibling regulated-industry concept with a parallel build methodology
- [[HealthcareAI]] — sibling regulated-industry concept with a parallel build methodology
- [[ClaudeCowork]] — legal teams cited as its most engaged knowledge-work segment
- [[ClaudeCodeSkills]] — mechanism behind Anthropic's internal legal-team case study and practice-area plugin playbooks
- [[ClaudeCodePlugins]] — Legal Marketplace and practice-area plugin mechanism
- [[MCPConnector]] — protocol connectors that bring matter-specific systems into Claude
- [[ClaudeManagedAgents]] — deployment target for cookbook versions of legal plugins
- [[ClaudeForExcelPowerPoint]] — Office cross-app integration used by legal teams
- [[Claude4.7Opus]] — model powering the May 2026 legal release
- [[Harvey]] — legal-AI company, BigLaw Bench benchmark partner
- [[Legora]] — legal-AI drafting workspace
- [[LexisNexis]] — legal research/analytics provider
- [[ThomsonReuters]] — CoCounsel rebuilt on Claude Agent SDK; plugin/skill contributor
- [[SolveIntelligence]] — legal-AI company building on Claude
- [[Courtroom5]] — access-to-justice partner
- [[summary-2026-05-12 - Claude for the legal industry]] — May 2026 connectors/plugins expansion
- [[summary-2025-12-08 - How Anthropic&#39;s legal team cut review times from days to hours with Claude]] — internal Skills case study
- [[summary-2026-05-15 - Deploying Claude across the legal industry]] — deployment guide with GC adoption stat and three-phase roadmap
- [[FTIConsulting]] — co-author of the 2026 General Counsel Report cited for the adoption surge
- [[Relativity]] — co-author of the 2026 General Counsel Report cited for the adoption surge
