---
title: "ClaudeCowork"
type: entity
tags: [product, claude, anthropic, cowork, automation, knowledge-work]
sources: [raw/03-transcripts/Claude/How Anthropic uses Claude Cowork/01 - Claude Cowork for legal teams.md, raw/03-transcripts/Claude/How Anthropic uses Claude Cowork/02 - Claude Cowork for marketing ops.md, raw/03-transcripts/Claude/How Anthropic uses Claude Cowork/03 - Claude Cowork for sales.md]
last_updated: 2026-06-23
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

## Related

- [[summary-cowork-legal-teams]] — legal team use case
- [[summary-cowork-marketing-ops]] — marketing ops use case
- [[summary-cowork-sales]] — sales use case
- [[ClaudeCode]] — the developer-focused agent tool
- [[ClaudeManagedAgents]] — the production agent platform
- [[ClaudeCodeSkills]] — skills as the reusable process mechanism
- [[Anthropic]] — the company behind the product
