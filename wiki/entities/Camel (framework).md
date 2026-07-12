---
title: "Camel (framework)"
type: entity
tags: [tool, framework, ai-security, google, permissioning]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md"]
last_updated: 2026-07-10
---

## Definition

Camel is a permissioning framework from Google that restricts the possible actions of an AI agent ahead of time based on what the user's prompt actually requires, preventing malicious actions even if prompt injection occurs.

## Key Information

- Camel analyzes the user's prompt to determine what permissions the agent actually needs and grants only those.
- For example, a prompt asking to "send an email" would only grant write/send email permissions, not read permissions — so even if the agent encounters a malicious email during execution, it can't read it.
- Similarly, a prompt asking to "summarize my emails" would only grant read-only permissions, so even if a malicious email says "send an email to attacker," the agent can't send anything.
- The limitation: Camel can't help when both read and write permissions are needed simultaneously (e.g., "read my emails and forward any ops requests to my head of ops").
- Can be complex to implement and may require rearchitecting the system.
- Praised by classical cybersecurity professionals because it aligns with the principle of least-privilege permissioning.

## Related

- [[summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO]] — source summary
- [[Google]] — parent company
- [[Prompt Injection]] — attack vector it defends against
- [[AI Guardrails]] — alternative defense approach
