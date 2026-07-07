---
title: "AccountPropensityScoring"
type: concept
tags: [sales, ai, scoring, claude-cowork, automation]
sources: ["raw/01-articles/claude/2026-05-20 - How an Anthropic sales leader uses Claude Cowork to run a 4,000-account book.md"]
last_updated: 2026-07-07
---

## Definition

Account propensity scoring is an AI-driven methodology for ranking and prioritizing sales accounts by their likelihood to convert or expand. Using [[ClaudeCowork]], it applies dimensional scoring rubrics to each account in a territory, combining deep web research with internal data from [[Salesforce]] and [[BigQuery]] to produce numerical scores and written rationales per dimension.

## Key Information

- **Origin**: [[TravisBryant]], Head of US Mid-Market GTM at [[Anthropic]], ran an overnight Claude Cowork routine to score all 4,000 accounts in his mid-market book — work that previously consumed hundreds of hours across RevOps, FP&A, and marketing teams at prior companies.
- **Methodology**: Two separate five-dimension rubrics were defined with Claude:
  - **Tech accounts**: agent opportunity, internal transformation, AI commitment, white space against existing spend, industry fit.
  - **Industries accounts**: knowledge-worker density (high at law firms, low in manufacturing), public AI commitments (measured via open jobs page mentions), plus additional dimensions.
- **Process**: Claude Cowork scored each account one-by-one using deep web research, Salesforce data, and BigQuery data, producing a numerical score and written rationale for every dimension.
- **Output**: An interactive dashboard where each AE clicks into their territory's pie slice, sees accounts ranked by score with rationales, and can hover for potential use cases and comparable case studies — turning scores into a working sales tool.
- **Iteration pattern**: Non-technical prompts ("score on these dimensions"), run a test territory, check output, adjust weights ("D4 is probably weighted a little heavy; bring it down"), run the next territory.
- **Generalizable pattern**: The same overnight routine approach works for TAM sizing, account research, competitive benchmarking — anything historically deferred because no team had the hours for it.

## Related

- [[ClaudeCowork]] — the product used to execute the overnight scoring
- [[TravisBryant]] — the sales leader who developed the methodology
- [[Anthropic]] — the company where this was deployed
- [[Salesforce]] — CRM data source for account and pipeline information
- [[BigQuery]] — data warehouse for spend and usage data
- [[summary-2026-05-20 - How an Anthropic sales leader uses Claude Cowork to run a 4,000-account book]] — source article
