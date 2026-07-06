---
title: "summary-2026-03-30 - Audit Claude Platform activity with the Compliance API"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-03-30 - Audit Claude Platform activity with the Compliance API.md"]
last_updated: 2026-07-04
---

## Core Summary

The Compliance API is now available across the Claude Platform (not just Claude Enterprise, where it first launched), giving admins programmatic access to an audit-log activity feed for their organization. The feed covers security-relevant events — user login/logout, account setting updates, workspace changes, and other organizational audit events — filterable by time range, user, or API key, but explicitly excludes inference activity such as user-model interactions or model activity. It targets regulated industries (financial services, healthcare, legal) that need detailed, scalable audit trails instead of manual exports and periodic reviews. Enabling the API requires contacting the account team; logging only begins once enabled, so historical activity isn't retroactively available. Organizations already using the Compliance API for Claude Enterprise can add their Claude API organization under the same parent organization to see combined activity in a single feed.

## Key Points

- Compliance API is now generally available on the Claude Platform broadly, expanding beyond its original Claude Enterprise-only scope (announced August 2025).
- Provides an "activity feed" of security-relevant events across two tracked categories, filterable by time range, specific users, or API keys.
- Covers: user login/logout events, account setting updates, workspace changes, and other organizational audit events.
- Explicitly does **not** log inference activity — no user-model interaction content or model activity is captured. This narrows/conflicts with the original Compliance API description (see [[ComplianceAPI]] and Knowledge Conflicts there), which described "real-time access to Claude usage data and customer content."
- Access requires contacting the account team to enable it; an admin API key is then used to query the activity feed endpoint. Logging starts only from the point of enablement — no historical backfill.
- Organizations running both Claude Enterprise and a Claude API organization can merge them under one parent organization to get a single combined activity feed.
- Full documentation is hosted on the Anthropic Trust Center (trust.anthropic.com).
- Anomaly: the raw source file contains scraped-page artifacts — an identical opening paragraph duplicated back-to-back, and a trailing newsletter-signup widget ("Get the developer newsletter... Delivered monthly to your inbox."). No prompt-injection content was found; these are just page-boilerplate remnants and were ignored.

## Related

- [[ComplianceAPI]] — the feature this article describes, now expanded to Claude Platform scope
- [[Anthropic]] — provider of the Claude Platform and Compliance API
- [[ClaudeEnterprise]] — plan where the Compliance API first launched (August 2025)
