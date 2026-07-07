---
title: "TravisBryant"
type: entity
tags: [person, sales, anthropic, claude-cowork]
sources: ["raw/01-articles/claude/2026-05-20 - How an Anthropic sales leader uses Claude Cowork to run a 4,000-account book.md"]
last_updated: 2026-07-07
---

## Definition

Travis Bryant is Head of US Mid-Market GTM (Go-To-Market) at [[Anthropic]], responsible for approximately 4,000 accounts split between mid-market tech and industries. He is profiled as a power user of [[ClaudeCowork]] for sales workflows.

## Key Information

- **Role**: Head of US Mid-Market GTM at [[Anthropic]]
- **Scope**: 4,000 accounts across mid-market tech (post-startup, pre-enterprise companies) and industries (financial services, healthcare, retail, manufacturing, and more)
- **Claude Cowork usage spans three cadences**:
  - **Daily**: Scheduled skills prepare customer call briefs (pulling spend from [[BigQuery]] and pipeline from [[Salesforce]]) and auto-book conference rooms for external meetings via [[Google Calendar]].
  - **Weekly**: A scheduled Friday forecast skill assembles a single-page web report (top-line metrics, top deals, movers/decliners, forecast snapshot) in leadership's preferred format, deployed to a shared link before Monday's forecast call. Saves ~3 hours/week.
  - **Quarterly**: Overnight account propensity scoring across the full 4,000-account book using AI-driven dimensional rubrics — work that previously took hundreds of hours across RevOps, FP&A, and marketing. Output feeds an interactive dashboard for AEs.
- **Claude Code experience**: Tried [[ClaudeCode]] but never got comfortable with the terminal; Claude Cowork's interface (English prompts, familiar output formats, built-in human-in-the-loop) was the breakthrough.
- **Philosophy**: Sales leaders should make judgment calls (where to invest hours, what to tell leadership about the quarter); Claude Cowork handles the data assembly and reformatting that surrounds those decisions.
- **Advice for sales teams**: Put prep on a schedule so it runs itself; encode the team's required format into skills so human time goes to commentary not formatting; run big strategic projects as overnight Cowork routines.

## Related

- [[ClaudeCowork]] — the product Travis uses across all workflows
- [[Anthropic]] — the company
- [[summary-2026-05-20 - How an Anthropic sales leader uses Claude Cowork to run a 4,000-account book]] — source article
- [[AccountPropensityScoring]] — the scoring methodology used in quarterly territory work
- [[BigQuery]] — data source for spend analysis
- [[Salesforce]] — CRM data source for pipeline and opportunity data
