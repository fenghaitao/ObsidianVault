---
title: "Saved Mini-Scripts"
type: concept
tags: [agents, code-generation, automation, cron, reuse]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - MCP = Mega Context Problem - Matt Carey.md"]
last_updated: 2026-06-29
---

## Definition
Saved Mini-Scripts are LLM-generated code snippets that users save for reuse in recurring tasks. They enable faster execution of repeated actions, self-healing automation, and cron-like scheduled jobs without requiring the user to know how to program.

## Key Information
- Emerges from programmatic tool calling: as agents generate code, users can save that code for later reuse
- Users can decide: "This action that the LLM generated for me, I want to keep that for later"
- Saved scripts are much faster than regenerating code each time
- Enable cron-like scheduled jobs: a user sets up a web scraping job without knowing how web scraping works, the agent generates a script, and the script runs on schedule
- Self-healing: when the script breaks (e.g., web scraping is brittle), the agent fixes it and re-saves the script
- Only works when programmatic tool calling is embraced as a pattern
- Matt Carey predicts this will become a common pattern as more clients implement programmatic tool calling

## Related
- [[summary-20260425 - MCP = Mega Context Problem - Matt Carey]] — source
- [[ProgrammaticToolCalling]] — pattern that enables saved scripts
- [[CodeMode]] — paradigm that generates the scripts
- [[AgentRoutines]] — related concept in Paperclip for reusable templated tasks
- [[Untrusted Code Execution]] — required for safely running saved scripts
