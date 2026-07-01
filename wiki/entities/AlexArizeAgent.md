---
title: "AlexArizeAgent"
type: entity
tags: [ai-agent, arize, product, agent, context-management]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260510 - How we solved Context Management in Agents — Sally-Ann Delucia.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260607 - LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize.md"]
last_updated: 2026-06-29
---

## Definition
Alex is Arize's internal AI agent, built into the Arize observability platform. It serves as an AI harness to help users build AI applications, with advanced planning, 40+ built-in skills, and core workflows across prompt engineering (optimization, data gen, augmentation, annotations). Arize uses Alex to build Alex itself — a dogfooding approach.

## Key Information
- Built over the course of approximately one year by SallyAnn DeLucia's team at Arize.
- Functions as an "AI harness" integrated into the Arize observability platform.
- Has 40+ built-in skills covering prompt optimization, data generation, data augmentation, and annotations.
- Operates on Arize's own trace and span data, creating a self-referential data problem.
- Uses smart truncation with memory as its primary context management strategy.
- Employs sub-agents for heavy data operations (searching over hundreds of spans), keeping the main conversation context light.
- Uses long session evals (testing turn 11 after loading 10 turns) to catch context degradation.
- Currently lacks long-term cross-session memory — users cannot reference issues from previous chats.
- Context selection is still heuristic-based (first 100, last 100 characters).
- Conversations are growing from <10 turns to 20+ turns as users find Alex more helpful and use it across the Arize application.
- Dat Ngo (AI Architect) describes Alex as part of Arize's automated flywheel vision: Alex can be asked "Hey, do you see any issues with my application?" and will plan and run tasks autonomously. Alex can detect high latency, errors, and other issues from trace data, and the ultimate goal is for Alex to create evals on the fly and automate users out of the observability loop entirely.

## Related
- [[Arize]] — parent platform
- [[DatNgo]] — AI Architect who described Alex's role in automation
- [[SallyAnnDeLucia]] — Head of Product and core contributor
- [[SmartTruncation]] — context management strategy used by Alex
- [[LongSessionEvals]] — evaluation technique for Alex
- [[SubAgents]] — architectural pattern used by Alex
- [[Context Management]] — core challenge Alex addresses
- [[AutomatedObservabilityFlywheel]] — Arize's automation vision powered by Alex
- [[summary-20260510 - How we solved Context Management in Agents — Sally-Ann Delucia]] — primary source
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — previous talk
- [[summary-20260607 - LLM Observability, Evaluation, Experimentation Platform — Dat Ngo, Arize]] — source
