---
title: "summary-20260408 - Abhishyant Khare Agent Native Engineering With Cofounder⧸CTO - PyAI Conf 2026"
type: source
tags: [source, pydantic, pyai-conf, multi-agent, orchestration, startup]
sources: ["raw/03-transcripts/Pydantic/Channel Only/20260408 - Abhishyant Khare Agent Native Engineering With Cofounder⧸CTO - PyAI Conf 2026.md"]
last_updated: 2026-06-25
---

## Core Summary

Abhishyant "Abby" Khare (General Intelligence Company) presents principles for building resilient multi-agent systems. Their product "Co-Founder CTO" aims to let one person run an entire business autonomously via agent departments (engineering, support, finance, marketing) coordinated by a CTO agent. Three core principles: agents control the full lifecycle of sub-agents, delegation is async not synchronous, and agents have full visibility into the system via observability tools.

## Key Points

- Multi-agent coordination in production is far messier than demos — things always go wrong
- Principle 1: parent agents can stop, message, restart sub-agents with added context
- Principle 2: async delegation — parent agent does other work while awaiting sub-agents; timeouts prevent forgotten sub-agents
- Principle 3: agents query their own observability (Logfire with SQL), access child session traces, and query their own database
- Middle management layer emerges naturally — similar to human org structures
- No inter-agent communication: all reports go up the management chain, not sideways
- Demo: CTO agent managing engineering department, firing off task agents that spin up coding and browser agents
- Agent can query Logfire to debug why a sub-agent timed out

## Related

- [[MultiAgentSystems]] — the architecture pattern
- [[Logfire]] — observability used for agent self-inspection
- [[AgentOrchestration]] — coordinating multiple agents
- [[GeneralIntelligenceCompany]] — Abby's startup
