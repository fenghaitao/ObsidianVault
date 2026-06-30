---
title: "Agent Sandboxing"
type: concept
tags: [ai, agents, security, sandboxing, isolation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick.md"]
last_updated: 2026-06-29
---

## Definition
Agent Sandboxing is the practice of isolating AI agents from sensitive systems and data to prevent accidental or malicious damage. It encompasses multiple techniques including separate machines, container isolation, permission systems, and specialized tools.

## Key Information
- Chris Parsons uses a layered sandboxing approach:
  1. Separate VPS away from main machine with limited, AI-specific keys
  2. Fine-grained Claude Code permissions (read-only for developer tools, no email sending)
  3. Docker sandbox (`docker sandbox code`) for file system isolation
  4. Lockbox (custom tool) to prevent file system access after reading untrusted tokens
- The Lethal Trifecta (Simon Willison) is the guiding principle: minimize collisions between untrusted tokens, internet access, and secret data
- For small projects like the Pomodoro timer workshop, sandboxing is less critical because the project scope is limited
- Parsons recommends reading about the Lethal Trifecta and being "thoughtful about how much power and permission you're giving to your agents"
- Different risk profiles require different sandboxing levels — production database migrations need more caution than slide deck generation

## Related
- [[Lethal Trifecta]] — guiding security principle
- [[Docker Sandbox]] — one technique
- [[Lockbox]] — Parsons' custom tool
- [[Agent Permission Management]] — policy layer
- [[ChrisParsons]] — his approach
- [[Sandcastle]] — Matt Pocock's Docker-based sandboxing for agent loops
- [[summary-20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick]] — source transcript
