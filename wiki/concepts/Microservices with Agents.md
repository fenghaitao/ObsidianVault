---
title: "Microservices with Agents"
type: concept
tags: [agents, architecture, microservices, evolution]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner.md"]
last_updated: 2026-06-30
---

## Definition
Microservices with Agents is the evolution from monolithic AI agents (single LLM as one engine) to specialized, composable agent microservices, each handling distinct concerns in the software development lifecycle. It mirrors the microservices architectural shift in traditional software.

## Key Information
- Described by [[MadisonFaulkner]] as the right side of the agentic software evolution
- Left side (past): monolithic agents using the LLM as one engine for everything
- Right side (future): microservices with agents — specialized agents for different concerns
- Mirrors the historical shift from monoliths to microservices in service architecture
- Examples of agent microservices: security review agents, API conformance agents, build agents, test agents
- Enables the [[External Validation]] pattern: specialized agents review changes within the loop
- Part of the broader architectural shift that makes [[Continuous Compute]] possible
- Enables parallel, specialized agent work that feeds into the [[PreMerge Queue]]

## Related
- [[summary-20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner]] — source
- [[Continuous Compute]] — paradigm enabled by microservices with agents
- [[External Validation]] — pattern enabled by specialized agent microservices
- [[Agent Specialization]] — related concept of specialized agent roles
- [[Reviewer Agents]] — a specific type of agent microservice
- [[AgentHarness]] — the loop that orchestrates agent microservices
- [[MultiAgentArchitecture]] — broader architectural pattern
