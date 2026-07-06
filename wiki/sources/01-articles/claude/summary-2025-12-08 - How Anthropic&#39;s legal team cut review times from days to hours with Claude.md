---
title: "summary-2025-12-08 - How Anthropic's legal team cut review times from days to hours with Claude"
type: source
tags: [source, legal, skills, mcp, internal-use]
sources: ["raw/01-articles/claude/2025-12-08 - How Anthropic&#39;s legal team cut review times from days to hours with Claude.md"]
last_updated: 2026-07-04
---

## Core Summary

Mark Pike, Associate General Counsel at [[Anthropic]] (non-coder), describes building four Claude-powered workflows with [[ClaudeCodeSkills|Skills]] and [[ModelContextProtocol|MCP]] that turned the legal team from a review bottleneck into cross-functional thought partners: a marketing self-review tool, a contract redlining assistant, an outside-business-activity conflict checker, and privacy impact assessment generation.

## Key Points

- **Marketing review workflow**: a Slack-pinned self-service tool where marketers paste content; Claude uses a Skill encoding the legal team's historical guidance to flag publicity-rights issues, overstated claims, and statistical-accuracy problems (low/medium/high risk) before formal submission — cut turnaround from 2-3 days to 24 hours.
- **Contract redlining**: Claude compares document versions in Google Docs/Office 365, highlights changes, and recommends commercial-playbook language; team members can ask Claude directly inside a Google Doc for real-time suggested edits. Different Skills serve different specialties (employment, commercial, privacy, corporate).
- **Outside business activity review**: employees submit a conflict-of-interest form; Claude analyzes it against COI policy and sends recommendations to lawyers via Slack for approval, replacing manual back-and-forth interviews.
- **Privacy impact assessments**: MCP connects Claude to a Google Drive folder of previous PIAs; a Skill instructs Claude on format/concerns so a lawyer can ask Claude to draft a new PIA from the folder of precedents.
- **Best practices**: start from pain points, not technology ("what do we wish we didn't have to do?" not "what can AI do?"); use natural language, not code; keep human oversight — workflows route to lawyers for approval, not around them, because AI can still hallucinate and citations must be verified; use Skills for both workflow consistency and personal writing voice (Mark had Claude learn his style from 10 of his own memos); use MCP to connect knowledge sources (Google Drive, JIRA, Slack, Calendar).
- Envisions new hires inheriting a team's accumulated knowledge via prompt libraries and Skills instead of reading old memos to learn house style.

## Related

- [[ClaudeCodeSkills]] — the mechanism behind all four legal workflows
- [[ModelContextProtocol]] — connects Claude to Google Drive, JIRA, Slack, and Calendar for PIAs and context
- [[Anthropic]] — the company whose internal legal team is profiled
