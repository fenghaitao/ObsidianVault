---
title: "summary-2026-06-17 - Meet the winners of our Claude Opus 4.8 Build Day hackathon"
type: source
tags: [source, claude-blog, hackathon]
sources: ["raw/01-articles/claude/2026-06-17 - Meet the winners of our Claude Opus 4.8 Build Day hackathon.md"]
last_updated: 2026-07-07
---

## Core Summary

Anthropic held a 12-hour hackathon in San Francisco on June 13, 2026, with 310 builders (selected from 1,500+ applicants) using Claude Opus 4.8 and $500 in credits each. The article profiles three winning teams: Tekton (3D reconstruction of historical buildings with evidence-chain verification), Sim Francisco (synthetic San Francisco population of 10,000 residents for polling and prediction-market forecasting), and Custom Universe (phone-photo-to-3D pipeline for robotics training data generation). Each team used Claude Opus 4.8 for both building and operating their projects, employing agentic patterns like sub-agent verification, adversarial testing, parallel workflows, and self-correction loops. The article includes practical builder advice: map the entire project before coding, don't settle for the first (expensive) approach, and use Claude to choose tools, not just write code.

## Key Points

- 310 builders from 1,500+ applicants participated in a 12-hour hackathon in San Francisco, each with $500 in Claude credits.
- **Tekton** (Holly Tang, Austin Burgess): reconstructs historical buildings in 3D with 339 incremental construction states, using independent verifier sub-agents in isolated context windows and self-correction loops until all 20 tests passed. Built for academic validation, restoration, and cultural preservation; starting with Tang Dynasty architecture and the Notre-Dame spire.
- **Sim Francisco** (Tanmayi Priya Dasari, Tejas Prabhune): 10,000 synthetic residents drawn from US Census data, placed on a city map, reacting to news in real time. Forecast the 2024 presidential vote at 81.3% Democratic (actual 83.8%) and SF Prop A at 70% (actual 70.38%). Used an evolutionary clustering algorithm to batch 10,000 residents into ~300 representative personas, cutting inference cost 10-100x.
- **Custom Universe** (Jake Stevens, Mauricio Pereira): phone photo to 3D object pipeline for robotics labs needing synthetic training data. Opus 4.8 built the project end-to-end and operated a remote NVIDIA H100. Uses Apple RealityKit for object scanning; relies on open-source models and is free to use.
- Builder advice: (1) map the whole project before building any of it — build a PRD and ticket board first; (2) don't settle for the first approach, especially when expensive — let Claude find cheaper alternatives; (3) use Claude to choose tools and research approaches, not just write code.

## Related

- [[Anthropic]] — hackathon organizer
- [[ClaudeOpus4.8]] — the model used in the hackathon
- [[Tekton]] — winning project: 3D historical building reconstruction
- [[SimFrancisco]] — winning project: synthetic San Francisco population
- [[CustomUniverse]] — winning project: phone-to-3D robotics data pipeline
- [[EvidenceChain]] — verification pattern used by Tekton
- [[SyntheticPopulation]] — concept underlying Sim Francisco
- [[SyntheticData]] — concept underlying Custom Universe
- [[AgenticCoding]] — agentic patterns used throughout the hackathon
- [[AgentWorkflowPatterns]] — parallel workflows, verifier, and adversarial agent patterns
- [[Sandboxing]] — isolated context windows for verifier sub-agents
