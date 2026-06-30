---
title: "Autonomous Agent Feedback Loop"
type: concept
tags: [agent, feedback, automation, devops, mcp]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take.md"]
last_updated: 2026-06-30
---

## Definition
A system where user-reported issues trigger autonomous coding agents that investigate, fix, verify, and submit changes — with human-in-the-loop oversight via chat — closing the loop from user feedback to production deployment.

## Key Information
- Play Magnus implemented a closed loop from user feedback to pull request: users report bad commentary in the app, which posts to Slack and injects into a running Cloud Code Channel session
- Cloud Code Channel is an MCP server in research preview that can inject events into a running Cloud Code session (similar to Open Claw)
- The agent runs a "commentary triage skill" that outlines its process for investigating what went wrong in a position
- The agent has access to scripts that run the generation pipeline, can modify prompts, change detectors, create new detectors, regenerate commentary, and verify its own work
- The agent asks clarifying questions back to Slack, enabling human guidance from a mobile device
- Once the human approves, the agent submits a PR that can be merged from a mobile phone
- Asbjorn Steinskog demonstrated this live: reported bad commentary from his phone, watched the agent start working, answered its clarifying question via Slack, and confirmed the fix
- Anant Dole listed this as a key learning: "really try to close the loop with autonomous agents"

## Related
- [[Play Magnus]] — implemented this system
- [[Asbjorn Steinskog]] — demonstrated the system live
- [[ClaudeCode]] — the coding agent powering the feedback loop
- [[Separating Data Pipeline from Language Generation]] — the pipeline the agent modifies
- [[Chess Context Extraction]] — detectors the agent can modify
- [[summary-20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take]] — source
