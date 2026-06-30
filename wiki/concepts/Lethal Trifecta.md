---
title: "Lethal Trifecta"
type: concept
tags: [security, ai, agents, sandboxing]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick.md"]
last_updated: 2026-06-29
---

## Definition
The Lethal Trifecta is a security concept coined by Simon Willison. It states that if an AI agent has untrusted tokens, internet access, and access to secret/important data in the same context, you will lose that data. The three elements together create an unavoidable security risk.

## Key Information
- Coined by Simon Willison
- The three elements: untrusted tokens (e.g., from web pages, emails, user input), internet access (ability to exfiltrate data), and access to secret important data (API keys, customer data, credentials)
- When all three collide in the same context, data loss is essentially guaranteed
- Chris Parsons uses this as a guiding principle for agent sandboxing — minimize the number of times these three things collide
- Mitigation strategies: separate VPS with limited keys, fine-grained permissions, Docker sandboxing, lockbox (prevents file system access after reading untrusted tokens)
- Parsons runs most AI work on a separate VPS with keys specific to AI use (not his personal keys), enabling audit trails

## Related
- [[SimonWillison]] — originator
- [[LethalTriquetra]] — alternate name for the same concept
- [[ChrisParsons]] — applies this in his workflow
- [[Agent Sandboxing]] — mitigation approach
- [[Docker Sandbox]] — one mitigation tool
- [[Lockbox]] — Parsons' mitigation tool
- [[summary-20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick]] — source transcript
