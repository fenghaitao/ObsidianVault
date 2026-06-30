---
title: "BrittleAutomations"
type: concept
tags: [agents, automation, reliability, failure-modes, openclaw]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com).md"]
last_updated: 2026-06-29
---

## Definition
Brittle Automations are multi-step agent workflows (especially 10-step automations) that are prone to breakage. Radek Sienkiewicz identifies them as a key failure mode in personal agent setups and recommends either splitting them into simpler automations or adding more effective guardrails.

## Key Information
- Radek warns: "Brittle automations, especially when it's like 10-step automations, it can break and it probably will break at some point"
- Two mitigation strategies: split complex automations into simpler ones, or add guardrails that are more effective
- This is part of Radek's broader incremental adoption philosophy — small, reversible steps are more robust than large, complex automations
- Related to the concept of deterministic scripts: "if this happens, do this. It's done. You don't even need judgment, so LLM is even skipped"
- Simple deterministic scripts are more reliable than multi-step LLM-dependent automations
- The incremental approach to fixing: when something breaks, take one small step back, fix it, understand why, add safeguards, then move forward

## Related
- [[summary-20260502 - I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com)]] — source
- [[RadekSienkiewicz]] — originator
- [[IncrementalAgentAdoption]] — the methodology for avoiding brittle automations
- [[AgentBrittleSystems]] — related concept of agent-generated brittle code
- [[OpenClaw]] — the agent framework
- [[Guardrails]] — mitigation strategy
- [[WeakBoundaries]] — related failure mode in configuration
