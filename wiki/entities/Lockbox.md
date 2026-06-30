---
title: "Lockbox"
type: entity
tags: [tool, security, sandboxing, ai, claude-code]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick.md"]
last_updated: 2026-06-29
---

## Definition
Lockbox is a sandboxing tool built by Chris Parsons that prevents file system access or other dangerous operations after an AI agent reads untrusted tokens, helping to mitigate the Lethal Trifecta risk.

## Key Information
- Built by Chris Parsons as part of Cherrypick
- Designed to prevent AI agents from doing "stupid stuff" when they encounter untrusted tokens
- When untrusted tokens are read, Lockbox prevents any further file system access or dangerous operations
- Part of Parsons' layered sandboxing approach alongside VPS isolation, fine-grained Claude permissions, and Docker sandbox
- Addresses the Lethal Trifecta concern (untrusted tokens + internet access + secret data = data loss)

## Related
- [[ChrisParsons]] — creator
- [[Cherrypick]] — parent company
- [[Lethal Trifecta]] — security concept it addresses
- [[Agent Sandboxing]] — broader concept
- [[Docker Sandbox]] — complementary sandboxing approach
- [[summary-20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick]] — source transcript
