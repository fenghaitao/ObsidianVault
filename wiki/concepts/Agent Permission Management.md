---
title: "Agent Permission Management"
type: concept
tags: [ai, agents, security, permissions, safety]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick.md"]
last_updated: 2026-06-29
---

## Definition
Agent Permission Management is the practice of controlling what AI agents are allowed to do, particularly around irreversible or embarrassing actions. It encompasses both technical permission systems (like Claude Code's permission modes) and policy rules (like "Reversible Without Embarrassment").

## Key Information
- Chris Parsons uses a combination of technical and policy-based permission management
- Technical: Claude Code permissions (not "dangerously skip permissions"), fine-grained tool access, read-only access to developer tools
- Policy: the "Reversible Without Embarrassment" rule — agents can do reversible things autonomously, must prepare irreversible things for human review
- Specific restrictions: never send emails (only draft), never post on LinkedIn, never send messages, never run production database migrations without review
- For Ralph loops to run continuously without stopping, permissions must be configured to allow autonomous operation within boundaries
- Parsons runs most AI work on a separate VPS with AI-specific keys (not personal keys) for audit trail
- The permission system is described as "a bit broken, but it mostly works"
- OpenClaw is noted as "unfortunately insecure by default" though improving

## Related
- [[Reversible Without Embarrassment]] — the policy rule
- [[Agent Sandboxing]] — technical enforcement
- [[Lethal Trifecta]] — security concern driving permissions
- [[ChrisParsons]] — his approach
- [[ClaudeCode]] — the permission system used
- [[summary-20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick]] — source transcript
