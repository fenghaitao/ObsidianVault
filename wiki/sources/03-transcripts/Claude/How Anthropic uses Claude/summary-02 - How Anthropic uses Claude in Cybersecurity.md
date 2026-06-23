---
title: "How Anthropic Uses Claude in Cybersecurity"
type: source
tags: [anthropic, cybersecurity, security-operations, claude-code, internal-tools]
sources: [raw/03-transcripts/Claude/How Anthropic uses Claude/02 - How Anthropic uses Claude in Cybersecurity.md]
last_updated: 2026-06-23
---

## Core Summary

An Anthropic cybersecurity team member describes building "Clue," a detection and response platform built with Claude Code that connects to internal data warehouses, Slack, and codebases via tool use. The platform lets analysts ask natural language questions about security events, automatically generates investigation plans, executes queries across multiple systems, and produces investigation summaries with findings and after-action items. A suppression engine that was planned for 1-2 months was built by a new hire in one week using Claude Code. The theme is moving from practitioner to researcher as Claude handles the mechanical work of security investigations.

## Key Points

- **Clue:** Detection and response platform built with Claude Code, connected to internal data warehouses, Slack, and codebases via tool use.
- **Investigation workflow:** Analyst asks natural language question → Claude generates investigation plan → executes queries across systems → produces findings summary with after-action items.
- **Before Clue:** Simple investigations took hours to days, jumping between 5-6 tools with 3-4 query languages.
- **Onboarding acceleration:** New hire built a suppression engine in 1 week that was planned for 1-2 months, because Claude Code explained the system setup.
- **Practitioner to researcher:** Claude handles immense data processing, letting security professionals focus on higher-level analysis and testing new approaches.

## Related

- [[Anthropic]] — the company using Claude internally
- [[ClaudeCode]] — the tool used to build Clue
- [[ModelContextProtocol]] — tool use for connecting to internal systems
