---
title: "summary-2026-05-12 - How Anthropic&#39;s cybersecurity team built a threat detection platform with Claude Code"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-05-12 - How Anthropic&#39;s cybersecurity team built a threat detection platform with Claude Code.md"]
last_updated: 2026-07-04
---

## Core Summary

Jackie Bow, Technical Lead for Anthropic's Detection Platform Engineering team, describes building CLUE (Claude Looks Up Evidence), a detection-and-response platform that gives security analysts a natural-language interface — powered by Claude via tool use — into Anthropic's internal systems (Slack, internal docs, code repositories, data warehouses). Built almost entirely through conversation with [[ClaudeCode|Claude Code]] (proof of concept in a day, design docs and implementation within a week), CLUE has two main components: **CLUE Triage**, which auto-enriches and dispositions every incoming alert (false positive / true positive / malicious / expected behavior) with a confidence score before a human ever sees it; and **CLUE Investigate**, which lets analysts query all security-critical logs in natural language via an orchestrator that dispatches sub-agents to run queries in parallel and synthesize findings. Quantified impact over 30 days: the false-positive rate on triaged alerts dropped from roughly 1-in-3 to 7%, CLUE automated ~12,000 queries and ~27,000 tool calls (an estimated 1,870 hours / 234 person-days of manual work), for an estimated 5-10x time savings; a typical investigation now runs 3-4 minutes with an average of 25 tool calls and ~11 queries per session. The piece closes on where the team is headed: applying the "bitter lesson" to security operations by giving Claude goals and tool access rather than rigid playbooks, moving from reactive alert-response toward continuous proactive threat-hunting, building organizational memory from stored investigation transcripts, and deliberately embracing non-deterministic, parallel investigation strategies rather than treating variation as a bug.

## Key Points

- **Author/role**: Jackie Bow, Technical Lead, Anthropic Detection Platform Engineering team (defensive cybersecurity — detection and response, not offensive vulnerability probing).
- **CLUE** = "Claude Looks Up Evidence." Built with Claude Code over several months; proof of concept in one day, design docs + implementation finished within a week.
- **CLUE Triage**: performs first-pass triage on every incoming alert before a human analyst sees it — enriches each alert with context from Slack, internal docs, code repos, and data warehouses; assigns a disposition (false positive / true positive / malicious / expected behavior) plus a confidence score.
- **CLUE Investigate**: natural-language query interface over all security-critical logs; an orchestrator issues commands to sub-agents that execute queries in parallel, gather findings, and synthesize results into investigation summaries — an instance of the orchestrator-subagent multi-agent pattern.
- **Data governance case study**: checking whether three contractors accessed documents they shouldn't have over two months — normally at least half a day of manual work (querying access logs, cross-referencing permissions, reviewing document classifications) — completed in minutes with CLUE, with full transparency into every query run.
- **Metrics (30-day usage window, generated using Claude Sonnet and Opus models per the article's footnote)**:
  - False positive rate on triaged alerts: ~33% ("roughly one in three") before CLUE Triage → 7% after.
  - ~12,000 automated queries and ~27,000 tool calls over 30 days.
  - Estimated manual-equivalent effort: 1,870 hours (234 person-days).
  - Estimated time savings: 5-10x versus manual triage.
  - Per-investigation average: 25 tool calls, ~11 queries; investigations that took hours to days manually now complete in 3-4 minutes.
- **Design philosophy — "the bitter lesson" applied to SecOps**: the team debated constraining Claude's investigation paths with rigid SOAR-style playbooks, but found that giving Claude a goal plus tool/data access (rather than a prescribed sequence) surfaced investigation paths and context the team wouldn't have specified themselves.
- **Future direction — reactive to proactive**: architecture could support continuous exploration/threat-hunting (agents actively hunting anomalies) rather than only responding to fired alerts.
- **Future direction — organizational memory**: every investigation transcript is stored, forming a corpus Claude can query for patterns across past investigations.
- **Future direction — embracing non-determinism**: the team is experimenting with running multiple investigation strategies in parallel on the same alert and comparing results, treating variation as a feature rather than a bug (in contrast to traditional SecOps tooling, which treats inconsistency as a bug).
- **Accuracy measurement acknowledged as unsolved**: the team is still building feedback loops to quantify how often Claude catches things analysts would have missed (and vice versa); audit trails via transcripts help.
- **Anthropic's Responsible Scaling Policy** ties product releases directly to this team's security commitments — i.e., Bow's team's work gates what Anthropic can safely ship.
- **Anomaly**: the raw article ends with two soft calls-to-action ("Check out our best practices for preparing your security program..." linking to the AI-accelerated-offense piece, and "Get started with Claude Code today... Stay tuned for more stories in the 'How Anthropic uses Claude' series") — standard marketing-page boilerplate, not a prompt-injection attempt, but noted per ingestion protocol since it reads as a directive appended to page content.

## Related

- [[summary-02 - How Anthropic uses Claude in Cybersecurity]] — earlier, shorter source summary covering the same CLUE platform at an earlier stage
- [[ClaudeCode]] — the tool CLUE was built with
- [[Anthropic]] — the company; publisher and internal user
- [[MultiAgentSystem]] — CLUE Investigate's orchestrator/sub-agent parallel-query architecture is a production instance of this pattern
- [[AIAcceleratedOffense]] — linked companion piece on security-program preparation, referenced at the end of the article
- [[VulnerabilityDetection]] — related but distinct: that concept covers code-vulnerability classes; this article covers runtime threat detection/SOC operations
- [[ModelContextProtocol]] — the likely tool-use mechanism connecting Claude to Slack, docs, code repos, and data warehouses (not named explicitly as MCP in this article, but consistent with the pattern documented elsewhere in the wiki)
