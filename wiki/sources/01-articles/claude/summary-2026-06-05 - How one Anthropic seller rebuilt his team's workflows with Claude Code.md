---
title: "summary-2026-06-05 - How one Anthropic seller rebuilt his team's workflows with Claude Code"
type: source
tags: [source, claude-blog]
sources: ["raw/01-articles/claude/2026-06-05 - How one Anthropic seller rebuilt his team's workflows with Claude Code.md"]
last_updated: 2026-07-07
---

## Core Summary

Jared Sires, a former startup account executive at [[Anthropic]] with no prior coding experience, used [[ClaudeCode]] to build CLAFTS (Claude Drafts) — a Gmail-integrated application that drafts customer email replies in his voice, saving 10–15 hours per week. His tools scaled to ~80% of Anthropic's sales organization via a [[ClaudeCowork]] plugin packaging skills and MCP connectors. The success led to a role shift into GTM product manager, where he now builds Claude-powered solutions for the entire sales team, including pre-call research briefs and post-meeting follow-up generation, demonstrating how AI dissolves the technical barrier for domain experts to build and ship production tools.

## Key Points

- CLAFTS is ~4,300 lines of code, almost entirely written by Claude Code, pulling context from Google Drive, third-party tools, and Anthropic's public documentation via web search.
- CLAFTS Tones uses pattern matching to mimic Jared's voice across different relationships (customers, peers, family), validated when Claude began refusing to generate increasingly angry test emails.
- Jared's daily brief skill reads his calendar, runs web searches on meeting participants, and produces talking points before the first call each morning via MCP servers connecting to Google Calendar and CRM data.
- The daily recap skill pulls from Google Docs and meeting notes to draft follow-up emails, bookending the workday with AI-generated context and output.
- Two core skills anchor the Sales plugin: `/customer-context` (360-degree account view in ~90 seconds) and `/pipeline-management` (at-risk deals, forecasting guidance, progression recommendations).
- Roughly 80% of Anthropic's sales org adopted the plugin; the remaining 20% are largely new hires, for whom the skills are designed to accelerate ramp time.
- Jared is now experimenting with the [[ClaudeAgentSDK|Agent SDK]] to chain workflows where one Claude run's output feeds the next, pushing further into agent territory.

## Related

- [[ClaudeCode]] — the tool used to build CLAFTS and all other sales tools
- [[ClaudeCowork]] — the platform through which the Sales plugin is distributed
- [[Anthropic]] — the company where these workflows run internally
- [[ClaudeCodeSkills]] — the skills mechanism powering daily brief, daily recap, and the Sales plugin
- [[ClaudeAgentSDK]] — the SDK Jared is experimenting with for chaining agent workflows
- [[ModelContextProtocol]] — MCP servers connecting to Google Calendar and CRM data
- [[AIAcceleratedSalesWorkflows]] — the broader pattern of non-technical GTM staff building AI tools
