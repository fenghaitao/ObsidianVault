---
title: "SoulMD"
type: concept
tags: [agents, configuration, personality, openclaw, personal-agent]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com).md"]
last_updated: 2026-06-29
---

## Definition
Soul MD is an AI agent's personality and behavior configuration file that defines how the agent communicates and behaves. Radek Sienkiewicz identifies it as one of the key files requiring active optimization, alongside critical rules MD and agent MD, to prevent agent misbehavior and ensure appropriate interactions.

## Key Information
- Radek lists soul.md as one of the configuration files that needs active optimization
- Part of the layered configuration approach: soul.md (personality), agent.md (general config), critical rules MD (non-negotiable constraints)
- Even with instructions in soul.md, the agent can still forget or not do something — hence the need for critical rules
- The concept originated with Peter Steinberger, who created soul.md after noticing Claude Code's default personality didn't fit WhatsApp conversations
- Peter iterated on making the agent "write more like a human" — less wordy, fewer dots, matching how friends text
- Radek evolved from one memory file to a memory folder, with soul.md as part of the broader memory configuration
- OpenClaw's inspectability makes soul.md easy to work with: it's a plain text file, editable, readable, understandable

## Related
- [[summary-20260502 - I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com)]] — source
- [[RadekSienkiewicz]] — user who optimizes soul.md
- [[PeterSteinberger]] — originator of the soul.md concept
- [[CriticalRules]] — complementary configuration for non-negotiable behaviors
- [[AgentMemoryOptimization]] — broader memory management practice
- [[AgentPersonality]] — broader concept of agent personality design
- [[OpenClaw]] — the agent framework
