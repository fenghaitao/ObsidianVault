---
title: "ClaudeCowork"
type: entity
tags: [product, claude, anthropic, cowork, automation, knowledge-work]
sources: [raw/03-transcripts/Claude/How Anthropic uses Claude Cowork/01 - Claude Cowork for legal teams.md, raw/03-transcripts/Claude/How Anthropic uses Claude Cowork/02 - Claude Cowork for marketing ops.md, raw/03-transcripts/Claude/How Anthropic uses Claude Cowork/03 - Claude Cowork for sales.md, raw/01-articles/claude/2026-01-26 - Your favorite work tools are now interactive connectors inside Claude.md, raw/01-articles/claude/2026-01-30 - Customize Cowork with plugins.md, raw/01-articles/claude/2026-02-05 - Advancing finance with Claude Opus 4.6.md, raw/01-articles/claude/2026-02-24 - Cowork and plugins for finance.md, "raw/01-articles/claude/2026-02-24 - Cowork and plugins for teams across the enterprise.md"]
last_updated: 2026-07-04
---

## Definition

Claude Cowork is Anthropic's product for knowledge workers that enables Claude to use a local computer to create, edit, and manage files (Word documents, Excel spreadsheets, PowerPoints) and connect to enterprise systems (Gmail, Slack, Salesforce, data warehouses) through skills and scheduled tasks. It acts as an autonomous assistant that can run tasks on a schedule, pull data from multiple sources, and produce structured outputs.

## Key Information

- **Skills-based:** Reusable text files that capture repeatable processes (e.g., /brief for legal memos, account strategy builder for sales prep, weekly metrics review for marketing ops).
- **Scheduled tasks:** Cron-triggered autonomous runs — e.g., Sunday evening prep for Monday morning metrics review.
- **Multi-system integration:** Connects to Gmail, Slack, Salesforce, data warehouses, Jira, Google Drive, and web sources.
- **Human-in-the-loop:** Outputs require approval before sending (e.g., customer follow-up emails, Slack messages).
- **Use cases:** Legal (/brief for rapid context), marketing ops (weekly metrics reviews), sales (account strategy briefs, post-meeting follow-ups), and general knowledge work.
- **Skills are shareable:** Anyone on a team can run the same skill and get consistent results.
- **Continuous improvement:** Learnings from each run are saved back into skills for next time.
- **MCP Apps (January 2026):** supports interactive connectors — opening and using tools like Asana, Slack, and Figma with a live in-conversation UI rather than only background data/actions. See [[ModelContextProtocol]].
- **Plugins (January 2026, research preview):** bundles of skills, connectors, slash commands, and sub-agents that turn Claude into a role/team/company-specific specialist; launched with 11 open-sourced plugins (Productivity, Enterprise search, Plugin Create/Customize, Sales, Finance, Data, Legal, Marketing, Customer support, Product management, Biology research). Every component is file-based, so plugins are easy to build/edit/share; install from Cowork, browse the full collection online, or upload a custom plugin. Currently saved locally; org-wide sharing/private marketplaces planned. See [[ClaudeCodePlugins]] for the analogous Claude Code mechanism.
- **Claude Opus 4.6 (February 2026):** delivers more polished first-pass outputs (financial models, presentations); the corporate finance plugin pre-teaches workflows like journal entries, variance analyses, and reconciliation. Desktop-only research preview in beta on all paid plans.
- **Excel + PowerPoint cross-app orchestration (February 2026):** Claude carries context between the two Office add-ins to complete multi-step tasks end-to-end (e.g., analyze earnings → update a model → build a summary slide, propagating changes automatically when inputs change) — research preview, all paid plans, Mac and Windows.
- **Finance plugins and connectors (February 2026):** five new Anthropic-built finance plugins (financial analysis, investment banking, equity research, private equity, wealth management) in a public repository, plus new MCP connectors for FactSet and MSCI and partner-built plugins from LSEG and S&P Global.
- **Private plugin marketplaces and admin controls (February 2026):** org-specific marketplaces, private GitHub repos as plugin sources (private beta), per-user provisioning, auto-install, and a unified "Customize" menu consolidating plugins/skills/connectors. New connectors added: Google Workspace (Calendar, Drive, Gmail), Docusign, Apollo, Clay, Outreach, Similarweb, LegalZoom, WordPress, Harvey. Partner plugins from Slack (Salesforce), LSEG, S&P Global, Apollo, Common Room, Tribe AI. Slash commands now launch structured forms; company branding throughout; OpenTelemetry support for usage/cost/tool-activity tracking.
- **Computer use (March 2026, research preview):** Claude can control a user's local computer directly — pointing, clicking, and navigating open apps, the browser, and dev tools — for tasks with no available connector; it reaches for connectors (Slack, Google Calendar) first, falling back to full screen/mouse/keyboard control with explicit per-app permission requests. Paired with [[Dispatch]] (phone-initiated task assignment) so Claude can complete computer-use tasks autonomously while the user is away. Available for Claude Pro and Max subscribers on macOS and Windows; requires the desktop app to be running. See [[ComputerUse]].
- **Organization controls (April 2026):** GA on all paid plans, alongside Claude Code on Desktop (macOS/Windows). Enterprise admins gained role-based access controls (group users manually or via SCIM, assign per-group capability roles), group-level spend limits, usage analytics in the admin dashboard and Analytics API (sessions, active users, skill/connector invocations, DAU/WAU/MAU), expanded OpenTelemetry events (tool/connector calls, file reads/writes, skills used, manual-vs-automatic approval — SIEM-compatible, correlatable with [[ComplianceAPI]] via shared user ID), a new Zoom MCP connector (AI Companion summaries, action items, transcripts, smart recordings), and per-connector tool controls (e.g., allow read/disable write org-wide). Early data: the majority of Cowork usage comes from outside engineering (ops, marketing, finance, legal), handling work that surrounds — not replaces — each team's core deliverables. Customer stories: [[Zapier]] (engineering-bottleneck dashboard from Slack/Jira/org DB), [[Jamf]] (performance-review and incident-response workflows), [[Airtree]] (VC board-prep workflow).
- **Enterprise deployment guide (April 29, 2026):** Anthropic published a guide for deploying Cowork across a business function — where to start, how to structure a pilot, common use cases, and adoption best practices at scale — drawing on examples from Anthropic's own teams and customers [[ThomsonReuters|Thomson Reuters]], [[Zapier]], and [[Jamf]]. The blog announcement itself is a teaser with no extractable use-case detail; paired with [[ClaudeForExcelPowerPoint|Claude for Excel and PowerPoint]] for cross-app context and customizable via plugins/skills/commands.

## Related

- [[summary-01 - Claude Cowork for legal teams]] — legal team use case
- [[summary-02 - Claude Cowork for marketing ops]] — marketing ops use case
- [[summary-03 - Claude Cowork for sales]] — sales use case
- [[ClaudeCode]] — the developer-focused agent tool
- [[ClaudeManagedAgents]] — the production agent platform
- [[ClaudeCodeSkills]] — skills as the reusable process mechanism
- [[Anthropic]] — the company behind the product
- [[analysis-claude-product-landscape]] — comparison with Claude Code and Managed Agents
- [[summary-11 - Claude works inside your Word document]] — product-launch teaser for Word document integration
- [[summary-12 - Cowork is now generally available]] — GA launch announcement
- [[summary-18 - Scheduled Tasks in Cowork： Set it once, Claude handles the rest]] — scheduled-tasks feature launch
- [[summary-19 - Dispatch tasks to Claude Cowork from anywhere]] — remote task dispatch feature launch
- [[summary-05 - New agents for financial services ｜ Claude Cowork + Claude Managed Agents]] — financial-services agents launch
- [[ModelContextProtocol]] — protocol underlying MCP Apps interactive connectors
- [[summary-2026-01-26 - Your favorite work tools are now interactive connectors inside Claude]] — MCP Apps announcement
- [[ClaudeCodePlugins]] — the analogous plugin mechanism in Claude Code
- [[summary-2026-01-30 - Customize Cowork with plugins]] — Cowork plugins announcement
- [[Claude4.6Opus]] — model powering Cowork's finance capabilities
- [[summary-2026-02-05 - Advancing finance with Claude Opus 4.6]] — finance-focused Cowork update
- [[summary-2026-02-24 - Cowork and plugins for finance]] — finance plugins and Excel+PowerPoint orchestration
- [[summary-2026-02-24 - Cowork and plugins for teams across the enterprise]] — private marketplaces and admin controls
- [[PwC]] — customer quote
- [[BlankMetal]] — customer quote
- [[summary-2026-03-23 - Put Claude to work on your computer]] — computer use and Dispatch feature launch
- [[ComputerUse]] — the underlying capability added to Cowork
- [[Dispatch]] — phone-based task assignment feature paired with computer use
- [[summary-2026-04-09 - Making Claude Cowork ready for enterprise]] — organization controls and GA announcement
- [[Jamf]] — customer story: performance reviews, vendor reviews, incident response
- [[Airtree]] — customer story: board-prep workflow
- [[Zoom]] — new MCP connector for meeting intelligence
- [[ThomsonReuters]] — cited as a customer example in the April 29, 2026 enterprise deployment guide
- [[summary-2026-04-29 - Deploying agentic AI across the enterprise with Claude Cowork]] — enterprise deployment guide announcement
- [[summary-2026-04-30 - Building AI agents for the enterprise]] — teaser positioning Cowork as bringing enterprise-transformation capabilities to every team without a custom build per team
- [[Kepler]] — financial-services customer using Claude for reasoning atop a deterministic verification layer
