---
title: "summary-20260319 - Open Source in the age of AI Panel – PyAI Conf 2026"
type: source
tags: [source, pydantic, pyai-conf, open-source, panel]
sources: ["raw/03-transcripts/Pydantic/Channel Only/20260319 - Open Source in the age of AI Panel – PyAI Conf 2026.md"]
last_updated: 2026-06-25
---

## Core Summary

A panel at PyAI Conf 2026 featuring Guido van Rossum (Python creator), Samuel Colvin (Pydantic), Sebastián Ramírez (FastAPI), and Jeremiah Lowin (Prefect/FastMCP). Discussion covers: the AI slop problem overwhelming open source maintainers, proposed solutions (reputation systems, constructive friction, AI disclaimers in PRs), how to review AI-generated code at scale, and how big companies should invest back in open source.

## Key Points

- AI slop PRs are a "DDoS on maintainer attention" — the cost to open a PR has gone to zero while review cost remains high
- Jeremiah Lowin's most effective heuristic: close PRs with overly long descriptions (LLMs love verbose explanations)
- Samuel Colvin proposes a federated reputation system where submitting PRs costs reputation, merging earns it back
- Guido van Rossum reveals he's building "Type Agent" — a long-term agent memory system using PydanticAI
- Sebastián Ramírez advocates including AI disclaimers in PRs: what model, what prompt, full conversation
- Samuel Colvin's four rules for when AI can produce mergable 10,000-line PRs: known internals, known interface, existing tests, no bikeshedding
- Panel agrees companies should fund open source through the Open Source Pledge ($2,000/engineer/year) and by providing space/food for meetups
- Sebastián notes lawyers often block employees from contributing to open source — legal reform needed

## Related

- [[GuidoVanRossum]] — Python creator, building Type Agent
- [[SamuelColvin]] — Pydantic creator
- [[SebastianRamirez]] — FastAPI creator
- [[JeremiahLowin]] — Prefect CEO, FastMCP author
- [[OpenSourceSustainability]] — the funding and maintenance crisis
- [[AISlop]] — AI-generated low-quality contributions
