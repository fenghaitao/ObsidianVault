---
title: "CriticalRules"
type: concept
tags: [agents, configuration, guardrails, openclaw, personal-agent]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com).md"]
last_updated: 2026-06-29
---

## Definition
Critical Rules are non-negotiable behavioral rules for AI agents, stored in a dedicated configuration file (critical rules MD) and mentioned prominently in the agent's main configuration. They serve as hard constraints that the agent must follow, addressing the problem of agents forgetting or ignoring instructions in soul.md or agent.md.

## Key Information
- Radek Sienkiewicz uses a critical rules MD file in his OpenClaw setup
- Purpose: "even if I had something in agent MD or in soul MD, it still managed to forget something or not do something"
- Key implementation detail: having critical rules "mentioned quite high in the agent MD file" improves compliance
- Represents a hardening of agent configuration beyond standard personality and memory files
- Part of the evolution from simple to sophisticated agent setups
- Addresses the weak boundaries problem — critical rules provide stronger guardrails
- Works alongside soul.md (personality) and agent.md (general configuration) as a layered configuration approach

## Related
- [[summary-20260502 - I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com)]] — source
- [[RadekSienkiewicz]] — originator
- [[SoulMD]] — complementary personality configuration
- [[WeakBoundaries]] — the problem critical rules address
- [[AgentMemoryOptimization]] — broader memory management practice
- [[Guardrails]] — broader concept of agent constraints
- [[OpenClaw]] — the agent framework
