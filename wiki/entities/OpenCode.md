---
title: "OpenCode"
type: entity
tags: [tool, coding-agent, open-source]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - Building pi in a World of Slop — Mario Zechner.md"]
last_updated: 2026-06-26
---

## Definition
Open Code is an open-source coding agent harness that Mario Zechner evaluated before building Pi. While he praised the team's brilliance and execution velocity, he found several design issues that made it unsuitable for his workflow.

## Key Information
- Open-source coding agent harness with a "brilliant team" and "super high execution velocity"
- Mario gravitated toward it due to his history in OSS
- Issues Mario identified:
  - Tool output pruning: under certain conditions, Open Code prunes tool outputs after a minimum token threshold, which "lobotomizes" the model
  - LSP server integration: every time the model calls the edit tool, Open Code queries the LSP server for errors and injects them into the edit tool result — confusing the model because humans don't check errors line-by-line while editing
  - Per-message JSON files: each message in a session is stored as a separate JSON file on disk
  - CORS misconfiguration: by default, the server spins up with CORS headers set so any website in the browser can access the Open Code server
- Mario noted these issues happen to all projects and placed no blame, but they contributed to his decision to build Pi

## Related
- [[summary-20260416 - Building pi in a World of Slop — Mario Zechner]] — source transcript
- [[MarioZechner]] — evaluator
- [[Pi (coding agent)]] — what Mario built instead
- [[ClaudeCode]] — another harness Mario compared against
