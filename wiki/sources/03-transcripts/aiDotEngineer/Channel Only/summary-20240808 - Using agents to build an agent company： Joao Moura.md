---
title: "Using agents to build an agent company： Joao Moura"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20240808 - Using agents to build an agent company： Joao Moura.md"
author: "Joao Moura"
organization: "CrewAI"
date: 2024-08-08
tags: [agents, multi-agent, crewai, automation, agent-company, orchestration, marketing-automation, lead-qualification]
---

# Using agents to build an agent company： Joao Moura

## Core Thesis

Joao Moura, CEO and founder of CrewAI, presents how he built CrewAI as a company using the very multi-agent orchestration technology that CrewAI provides. Rather than hiring large teams for marketing, lead qualification, and documentation, he built specialized agent crews that handle these functions autonomously. The core argument is that agents fundamentally change how software is built — shifting from strongly-typed deterministic systems to fuzzy, adaptable workflows — and that companies should adopt agents incrementally, starting simple and expanding to low-risk, high-impact use cases.

## Key Points

1. **CrewAI Scale**: Over 10 million agents executed monthly, 100,000+ crews executed daily, 16,000+ GitHub stars, 8,000+ Discord members, and an organic Reddit community.

2. **What are AI agents**: LLMs that can make decisions, use tools, and operate autonomously. Unlike traditional automation that connects fixed dots (A→B→C→D), agents adapt to circumstances in real time, enabling automations that were previously impossible.

3. **Agent anatomy in production**: Goes beyond simple LLM + task + tools. Requires caching layers, memory layers, training, guardrails, and coordination between agents — each layer adding complexity, especially when agents share state within a crew and across multiple crews.

4. **Strongly-typed vs. fuzzy software**: Traditional software has known inputs (form fields, integers, strings) and deterministic outputs that can be tested. AI agent software is "fuzzy" — inputs can be anything (CSV, JSON, jokes), models are black boxes, and outputs are non-deterministic.

5. **Building the company with agents — three crews**:
   - **Marketing Crew**: Content creator specialist, social media analyst, senior content writer, and chief content officer. Takes rough ideas, researches LinkedIn/industry topics, and produces polished drafts. Resulted in 10x more views in 60 days.
   - **Lead Qualification Crew**: Lead analyst expert, industry researcher specialist, and strategic planner. Analyzes lead responses, compares with CRM data, researches industry, and provides scores, use cases, and talking points. Resulted in 15+ customer calls in 2 weeks.
   - **Code Documentation Crew**: Agents write and maintain CrewAI's documentation automatically.

6. **New features announced**:
   - **Code Execution**: Single flag (`allow_code_execution`) that lets agents write and execute their own code to build tools dynamically.
   - **Train Your Crew**: CLI for training agents with instructions that get baked into agent memory for consistent results over time.
   - **Third-Party Agent Integration**: Universal platform bringing any third-party agent (LlamaIndex, LangChain, AutoGen) into CrewAI with shared memory, tools, and features.
   - **CrewAI Plus**: Enterprise offering — push crews to GitHub, get a real API with autoscaling, bearer token auth, private VPC, and one-click React component export.

7. **Adoption advice**: Be an early adopter. Start simple, expand to low-risk high-impact use cases. Don't wait for others to prove out use cases.

8. **Agent that builds crews**: A meta-agent that takes an email and company name, creates a crew, and pushes it to a GitHub repository — self-referential automation where CrewAI builds CrewAI deployments.

## Entities

- [[Joao Moura]] — CEO and founder of CrewAI, presenter
- [[CrewAI]] — Multi-agent orchestration framework and company
- [[GitHub]] — Platform for CrewAI's open-source code and stars
- [[Discord]] — CrewAI community platform (8,000+ members)
- [[Reddit]] — Organic CrewAI community
- [[LinkedIn]] — Platform for AI-generated marketing content distribution

## Concepts

- [[AgentCompanyPattern]] — Using AI agent crews to run business functions instead of traditional teams
- [[AgentCrewOrchestration]] — Pattern of organizing agents into specialized crews with shared memory and caching
- [[FuzzySoftware]] — Software paradigm where inputs and outputs are non-deterministic due to LLM black boxes
- [[AgentMarketingAutomation]] — Using AI agent crews for content creation, social media analysis, and marketing
- [[LeadQualificationAgents]] — Using AI agents to analyze, score, and prepare for sales lead qualification
- [[ThirdPartyAgentIntegration]] — Universal platform approach for bringing external agents into a shared orchestration framework
- [[AgentProductionDeployment]] — Moving agents from development to production with autoscaling APIs, auth, and VPC
- [[AgentTraining]] — Baking instructions into agent memory via training CLI for consistent results

## Related

- [[summary-20251222 - Making Codebases Agent Ready – Eno Reyes, Factory AI]] — complementary on agent-ready infrastructure
- [[summary-20251226 - Shipping AI That Works： An Evaluation Framework for PMs – Aman Khan, Arize]] — multi-agent demo with LangGraph
- [[summary-20260105 - Claude Agent SDK [Full Workshop] — Thariq Shihipar, Anthropic]] — agent SDK approach
- [[MultiAgentArchitecture]] — architectural pattern for multi-agent systems
- [[AgentMemory]] — shared memory and caching for agents
- [[Code Execution (Sandboxed)]] — sandboxed code execution by agents
- [[HumanInTheLoopWorkflows]] — humans shifting from worker to overseer
