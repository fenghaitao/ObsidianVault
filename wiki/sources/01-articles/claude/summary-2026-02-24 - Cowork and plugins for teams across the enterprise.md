---
title: "summary-2026-02-24 - Cowork and plugins for teams across the enterprise"
type: source
tags: [source, cowork, plugins, marketplace, admin]
sources: ["raw/01-articles/claude/2026-02-24 - Cowork and plugins for teams across the enterprise.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic gave admins private plugin marketplaces and a unified "Customize" menu consolidating plugins, skills, and connectors; added a wave of new enterprise connectors and partner-built plugins; and extended Claude's cross-app orchestration to Excel + PowerPoint end-to-end tasks.

## Key Points

- **Private marketplaces & admin control**: org-specific marketplaces, private GitHub repositories as plugin sources (private beta), per-user provisioning, and auto-install; a new unified "Customize" menu lets admins see and manage plugins/skills/connectors in one place.
- **Easier plugin creation**: admins start from templates or build from scratch, with Claude asking guiding questions to tailor skills/commands/connectors to the company.
- **Improved connector experience**: overhauled directory, streamlined admin controls, easier management of which connectors bundle into which plugins.
- **New connectors**: Google Workspace (Calendar, Drive, Gmail), Docusign, Apollo, Clay, Outreach, Similarweb, MSCI, LegalZoom, FactSet, WordPress, and Harvey. Partner-built plugins from Slack (by Salesforce), LSEG, S&P Global, Apollo, Common Room, and Tribe AI.
- **UX polish**: slash commands now launch structured forms (e.g., "generate report" feels like filling out a brief); company branding throughout Cowork including a redesigned home experience; OpenTelemetry support for admins tracking usage/cost/tool activity.
- **Cross-app orchestration**: Claude can now run an analysis in Excel and turn it into a PowerPoint presentation as one end-to-end task, passing context between the two Office add-ins (early research preview).
- Plugins are portable, file-based, and work across both Cowork and anything built on the [[ClaudeAgentSDK|Claude Agent SDK]], making private cross-team/cross-partner marketplaces straightforward.
- Customer quotes: [[PwC]] (Sanjay Subramanian) on partnering to bring agents into the CFO's office; [[BlankMetal|Blank Metal]] (Mark Hines) contrasting hyped "digital employee" framing with what Anthropic actually built.

## Related

- [[ClaudeCowork]] — the product these updates extend
- [[ClaudeCodePlugins]] — the plugin mechanism getting private marketplaces
- [[ClaudeAgentSDK]] — the SDK plugins are portable across
- [[PwC]] — cited customer
- [[BlankMetal]] — cited customer
- [[summary-2026-02-24 - Cowork and plugins for finance]] — companion finance-specific article
