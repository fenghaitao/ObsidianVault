---
title: "Agent Memory"
type: concept
tags: [agents, context, personalization, memory, crewai, shared-memory, training]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20240808 - Using agents to build an agent company： Joao Moura.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence).md"]
last_updated: 2026-06-26
---

## Definition
Agent memory is the capability for an AI agent to remember user preferences, profile information, and past interactions across conversations, enabling personalized and context-aware responses without requiring the user to re-state information.

## Key Information
- Demonstrated in the French learning app: Manus built a user profile tracking age, workplace, strengths, and weaknesses
- Profile was built implicitly from user interactions over time
- In language learning, memory of user gender and preferences is critical for grammatical agreement
- Manus was exploring memory as a feature as of December 2025 but it was not yet available
- Users currently need to be explicit about context in each conversation
- Memory is distinct from multi-turn conversations (same session) — it spans across separate sessions
- Ivan Leo described it as "something we're actively looking at" for future releases
- **Shared memory in CrewAI**: Agents within a crew share memory and caching, enabling coordinated context across the crew. When multiple crews talk to each other, shared memory becomes a critical complexity layer.
- **Training as memory**: CrewAI's "Train Your Crew" CLI bakes instructions directly into agent memory so they produce consistent results over time, analogous to training a new employee.

## Related
- [[summary-20240808 - Using agents to build an agent company： Joao Moura]] — source (CrewAI shared memory + training)
- [[summary-20251230 - Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)]] — source
- [[ManusAI]] — platform exploring memory
- [[CrewAI]] — framework with shared memory and training features
- [[AgentCrewOrchestration]] — orchestration pattern relying on shared memory
- [[AgentTraining]] — baking instructions into agent memory for consistency
- [[Multi-Turn Conversations]] — related but distinct (same-session context)
- [[Context Management]] — broader context handling techniques
- [[General AI Agent]] — philosophy that benefits from memory
