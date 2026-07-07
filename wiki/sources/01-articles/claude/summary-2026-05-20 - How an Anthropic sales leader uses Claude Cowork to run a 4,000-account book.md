---
title: "summary-2026-05-20 - How an Anthropic sales leader uses Claude Cowork to run a 4,000-account book"
type: source
tags: [source, claude-blog]
sources: ["raw/01-articles/claude/2026-05-20 - How an Anthropic sales leader uses Claude Cowork to run a 4,000-account book.md"]
last_updated: 2026-07-07
---

## Core Summary

Travis Bryant, Head of US Mid-Market GTM at [[Anthropic]], details how he uses [[ClaudeCowork]] to automate three sales cadences across a 4,000-account book: daily customer call prep (scheduled skills scanning Google Calendar, pulling spend from BigQuery and pipeline from Salesforce), weekly forecast rollups (scheduled skills assembling a single-page web report in leadership's exact format), and quarterly territory-wide account propensity scoring (overnight AI runs scoring every account against dimensional rubrics). The core thesis is that Claude Cowork handles data assembly and report formatting so sales leaders can dedicate their time to customer conversations and strategic judgment calls rather than operational busywork.

## Key Points

- Claude Cowork's scheduled tasks are the key unlock: once prep becomes a scheduled task instead of a slash command to remember, it stops being forgotten.
- The Friday forecast skill saves ~3 hours/week by pulling opportunity records, commits, token spend, and internal notes into a formatted web report deployed to a shared link; the human adds commentary ("Claude builds the what; I do the why").
- Account propensity scoring for 4,000 accounts ran overnight using two five-dimension scoring rubrics (one for tech accounts, one for industries), producing numerical scores and written rationales per dimension — work that previously consumed hundreds of hours across RevOps, FP&A, and marketing.
- The scoring output was turned into an interactive dashboard where each AE clicks into their territory, sees accounts ranked by score with rationales, and can hover for potential use cases and case studies.
- Travis tried Claude Code but preferred Cowork's interface: prompts read like English, outputs land in familiar formats (docs, web pages, Salesforce), and human-in-the-loop approval is built in.
- Two recommended starting patterns for sales teams: (1) put prep on a schedule with the team's required format encoded into the skill; (2) run big strategic projects (TAM sizing, account research, comp benchmarking) as overnight Cowork routines.

## Related

- [[ClaudeCowork]] — the product used across all three cadences
- [[TravisBryant]] — the sales leader profiled
- [[Anthropic]] — the company where this workflow runs
- [[Salesforce]] — CRM data source for call prep and forecasts
- [[BigQuery]] — data warehouse for token spend analysis
- [[AccountPropensityScoring]] — the overnight scoring methodology
- [[ClaudeCode]] — terminal-based agent Travis tried before settling on Cowork
