---
title: "summary-20260514 - Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft"
type: source
tags: [source, transcript, agent-observability, microsoft-foundry, evaluations, tracing, red-teaming, workflow-agents, open-telemetry, coding-agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft.md"]
last_updated: 2026-06-30
---

## Core Summary

Amy Boyd (Foundry developer relations lead) and Nitya Narasimhan (observability expert) from Microsoft present a comprehensive workshop on agent observability using the "Mind the Gap" analogy from the London Underground. The analogy maps to three observability dimensions: (1) the gap between requirements and actual agent behavior requiring continuous evaluation, (2) guardrails and safety mechanisms as warning signs for users, and (3) continuous monitoring across many agents over time. They walk through the full lifecycle from building agents in the Microsoft Foundry portal, to SDK-based development with multi-agent workflows, to tracing with OpenTelemetry, built-in and custom evaluators, red teaming for adversarial testing, and an emerging "Observe Skill" that uses coding agents to automate the eval-optimize loop.

## Key Points

### The Mind the Gap Analogy
- **Evaluation gap**: Like different train models fitting differently on the same platform, agents drift from requirements over time. Need evaluation from very early stages throughout the lifecycle.
- **Guardrails/Safety**: The "Mind the gap" sign is itself a guardrail — warning customers about risks. Same applies to safety mechanisms in agents.
- **Monitoring**: Constant announcements ("mind the gap") remind everyone — continuous monitoring across many agents is essential.

### Three Pillars of Agent Reliability
- **Evaluate**: Performance, quality, safety, and agent-specific metrics
- **Monitor**: Continuous monitoring over time as requirements, customers, and environments change
- **Optimize**: Taking all the data and doing something with it — not just scores but actionable improvements

### Microsoft Foundry Platform
- Cloud agent platform at ai.azure.com for end-to-end agent development
- Build, host, observe, and manage agents in one platform
- Uses as much or as little of the platform as desired
- Built on **OpenTelemetry** standard for tracing — agents from anywhere can be instrumented and managed in the Foundry control plane
- Three observability phases: early build stage, debug/optimize in production, fleet-wide multi-agent management

### Built-in Evaluators
- **Quality metrics**: Coherence, fluency, groundedness, relevance
- **Risk & safety**: Content safety, jailbreak detection
- **Agent-specific evaluators**: Intent resolution, tool call evaluation, task adherence — evaluating the agent holistically across its workflow, not just individual LLM calls
- **Custom evaluators**: Build your own when built-ins don't fit the scenario
- Evaluation can happen at multiple points: intent resolution → tool call → overall response

### Agent Building Journey (Portal to SDK)
- **Portal quick start**: Create project → deploy agent with default model (GPT-4 1) → add instructions and tools (web search) → enable App Insights for tracing → select evaluation metrics → test in playground
- **SDK path (4-hour workshop)**: Step through notebooks in GitHub Codespaces
  - Lab 0: Environment setup and connectivity test
  - Lab 1: Build a basic agent programmatically
  - Lab 2: Add function tools (car search, flight search, hotel search)
  - Lab 3: Build **workflow agents** — specialist agents (flight, hotel, car) orchestrated by a concierge via declarative YAML
  - Lab 4: Tracing setup (local console traces + push to Azure Monitor)
  - Lab 5: Evaluations (quality, safety, agentic) with batch evaluation
  - Lab 6: Red teaming with adversarial attacks

### Workflow Agents
- Instead of one monolithic agent, break tasks into specialist agents
- Foundry's workflow capability uses declarative YAML to compose agents
- Flight agent → Hotel agent → Car agent → Concierge orchestrates them
- Traces show which agent is underperforming, token costs per agent, enable targeted optimization
- Agent versioning: deploy specific versions, roll back to better-performing ones

### Tracing
- Built on **OpenTelemetry** standard
- **Local tracing**: Console output for debugging with custom attributes
- **Cloud tracing**: Push to Azure Monitor/App Insights for production
- **Trace-linked evaluations**: See both traces (how it executed) and evaluations (what was the result) together — critical for shortening time between detection and diagnosis
- **Azure Monitor integration**: Combine AI telemetry with other service telemetry for correlation

### Evaluations
- **Data preparation**: Use AI agents to generate evaluation datasets from agent instructions
- **Quality evaluators**: Coherence, fluency, groundedness
- **Safety evaluators**: Content safety, jailbreak detection
- **Agentic evaluators**: Intent resolution, task adherence, tool calling
- **Batch evaluation**: Run multiple evaluators against datasets, poll until complete, analyze results locally or in portal
- Example: Groundedness failure detected when response used 2024 data instead of 2025

### Red Teaming (Adversarial Testing)
- **Proactive attack**: Use a second AI to attack the first AI
- Define risk categories (violence, sensitive data leakage, prohibited actions) and attack strategies
- **Attack strategies**: Leetspeak, crescendo attacks (gradually escalating), prompt manipulation (reversing strings to bypass guardrails)
- **Agentic-specific risks**: Prohibited actions — define taxonomy of forbidden actions, red teaming agent generates prompts to test guardrail bypass
- **Crescendo attack**: Starts small, builds gradually like a frog in boiling water — comprehensive but time-consuming
- Red teaming is not done alone — Microsoft works with the **PyRIT** open-source repository

### The Observe Skill (Emerging)
- **Coding agent automation**: A GitHub Copilot skill that automates the entire observability loop
- **Capabilities**: Generates eval datasets from agent instructions → runs batch evals → identifies failures → optimizes prompts → re-evaluates → compares versions → rolls back to best version
- **Human in the loop**: Agent proposes changes, human approves; agent can iterate but eventually needs human judgment
- **Version management**: Automatically creates new versions, tracks history, identifies best-performing version
- **Reasoning transparency**: Shows what it's looking for, why failures occurred, what changed
- **Extensible**: Can convert prompt agents to hosted agents (LangGraph, etc.), guide through red teaming
- Released ~2 weeks before the talk; Felicia Shaw is the PM behind it

### Portal AI Assistants
- **Ask AI**: Agent in Foundry portal that knows project state — query traces, check model availability, quota questions
- **Observability Agent**: In Azure portal's App Insights logs — converts KQL queries to natural language interactions, analyzes log data

### Cost Optimization
- Two levers: switch models (GPT-4 1 vs mini) and optimize tool usage
- Every change should trigger immediate re-evaluation to check for regressions
- Trade off cost vs. accuracy with eval comparison

### Workshop Infrastructure
- GitHub repo with all branches (fork with all branches to get AIE Europe branch)
- **GitHub Codespaces** with dev containers: zero-install development environment, all dependencies pre-configured
- **Azure free account** usable; ~$10 cost for 2 days of running
- **Discord**: AI engineer channel for support during/after workshop
- Two paths: traditional SDK (step-by-step notebooks) and coding agent path (using the Observe Skill)

## Related
- [[Amy Boyd]] — speaker, Foundry developer relations lead at Microsoft
- [[Nitya Narasimhan]] — speaker, observability expert at Microsoft
- [[Microsoft Foundry]] — cloud agent platform
- [[Microsoft]] — parent company
- [[AgentObservability]] — core concept
- [[TraceLinkedEvaluations]] — linking traces with evaluations for rapid diagnosis
- [[AgenticEvaluations]] — intent resolution, tool call evaluation, task adherence
- [[WorkflowAgents]] — multi-agent orchestration in Foundry
- [[ObserveSkill]] — coding agent skill for automated observability loop
- [[AgenticRedTeaming]] — proactive adversarial testing for agents
- [[ContinuousEvaluation]] — evaluation throughout the agent lifecycle
- [[OpenTelemetry]] — tracing standard used by Foundry
- [[AzureMonitor]] — cloud monitoring integration
- [[ApplicationInsights]] — App Insights for agent tracing
- [[GitHub Codespaces]] — dev container-based development environment
- [[PyRIT]] — open-source red teaming tool
- [[aiDotEngineer]] — event host
- [[summary-20260507 - Everything You Need To Know About Agent Observability — Danny Gollapalli & Zubin Koticha, Raindrop]] — related observability talk
