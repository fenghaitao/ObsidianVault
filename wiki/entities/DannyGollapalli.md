---
title: "Danny Gollapalli"
type: entity
tags: [person, engineer, agent-observability, raindrop]
sources:
  - "raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop.md"
last_updated: 2026-06-29
---

## Definition
Danny Gollapalli is a back-end engineer at Raindrop, working on SDK development and platform engineering. He co-presented the workshop on self-diagnostics at aiDotEngineer, demonstrating how agents can self-report misbehavior using a simple report tool and system prompt.

## Key Information
- **Role**: Back-end engineer at Raindrop
- **Work**: SDK development, platform engineering
- **Workshop contribution**: Led the self-diagnostics workshop section, demonstrating a coding agent that self-reports bypassing a broken write tool via bash heredoc syntax
- **Key insights on self-diagnostics**:
  - Models are trained to look polished and avoid self-incrimination
  - Tool naming matters: "report" works better than "unsafe bash use"
  - Framing as "giving feedback to creators" improves compliance
  - Self-diagnostics can catch tool failures, user frustration, capability gaps, and self-correction
  - Raindrop's SDK has self-diagnostics built in (tool injected automatically)
- **On SDKs**: Acknowledged Python SDK support is "fairly weak right now" but actively improving with a dedicated developer

## Related
- [[summary-20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop]] — source transcript
- [[Raindrop]] — company
- [[ZubinKoticha]] — co-presenter, CEO
- [[SelfDiagnostics]] — workshop topic
- [[AgentObservability]] — domain
