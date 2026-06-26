---
title: "summary-20251219 - Leadership in AI Assisted Engineering – Justin Reock, DX (acq. Atlassian)"
type: source
tags: [source, transcript, ai-engineering, leadership, developer-productivity, genai-adoption]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251219 - Leadership in AI Assisted Engineering – Justin Reock, DX (acq. Atlassian).md"]
last_updated: 2026-06-25
---

## Core Summary
Justin Reock of DX (acquired by Atlassian) presents a data-driven look at how organizations are adopting generative AI in engineering. The central finding is extreme volatility: some companies see 20% gains in change confidence and code quality, while others see 20% declines and up to 50% more defects. Success correlates with psychological safety, proper metrics beyond utilization, education with time to experiment, creative approaches to unblocking usage, and integrating AI across the full SDLC rather than just code completion. Top-down mandates and turning on the tech without enablement consistently fail.

## Key Points
- Industry averages mask extreme per-company volatility: 2.6% average change confidence gain hides swings from +20% to -20%
- Top-down mandates for 100% AI adoption do not work; they produce compliance without real impact
- Psychological safety (Google's Project Aristotle) is the biggest indicator of team productivity and applies directly to AI adoption
- Code writing has never been the bottleneck; the biggest gains come from integrating AI across the entire SDLC (spec generation, onboarding, incident response)
- Three metric classes are needed: telemetry (API data), experience sampling (PR form fields), and self-reported surveys
- The DXAI Measurement Framework organizes metrics into three dimensions: Utilization, Impact, and Cost
- System prompt feedback loops with a gatekeeper role are critical for maintaining AI output quality and trust
- Temperature control (0 to 1, avoid extremes) lets teams balance determinism vs. creativity per use case
- Stack trace analysis was the #1 most valuable AI use case in DX's study, not a generative task
- Morgan Stanley saved ~300,000 hours annually by using AI to reverse-engineer legacy code specs; Zapier reduced onboarding to 2 weeks; Spotify improved MTTR by pushing incident context into Slack channels

## Related
- [[JustinReock]] — speaker, DX/Atlassian
- [[DX]] — developer productivity measurement company, acquired by Atlassian
- [[DORA]] — research group providing AI impact benchmarks
- [[PsychologicalSafety]] — Google's Project Aristotle finding, key to AI adoption
- [[TheoryOfConstraints]] — Eli Goldratt's framework applied to SDLC bottlenecks
- [[DXAIMeasurementFramework]] — Utilization, Impact, Cost dimensions
- [[SystemPromptFeedbackLoop]] — gatekeeper-driven prompt maintenance
- [[TemperatureInAI]] — determinism vs. creativity control
- [[ChangeConfidence]] — qualitative metric for production change trust
- [[ChangeFailureRate]] — DORA metric tracking defect rates
- [[ExperienceSampling]] — PR form fields for AI usage data
