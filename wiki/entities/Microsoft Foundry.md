---
title: "Microsoft Foundry"
type: entity
tags: [platform, microsoft, agents, observability, evaluations, tracing]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft.md"]
last_updated: 2026-06-30
---

## Definition
Microsoft Foundry (ai.azure.com) is Microsoft's cloud agent platform for end-to-end agent development, providing capabilities to build, host, observe, evaluate, and manage AI agents. It uses OpenTelemetry for tracing and offers built-in evaluators, red teaming, and workflow agent orchestration.

## Key Information
- **URL**: ai.azure.com, part of the Azure cloud
- **End-to-end platform**: Build agents, host agents, observe agents, and manage/monitor agents
- **Use as much or as little as you wish** — agents can be built elsewhere and hosted/observed in Foundry
- **OpenTelemetry**: Tracing built on the OpenTelemetry standard; agents from anywhere can be instrumented and managed in the Foundry control plane
- **Agent types**: Prompt agents (simple declarative), workflow agents (multi-agent orchestration via YAML), hosted agents (bring your own framework like LangGraph)

### Built-in Evaluators
- **Quality**: Coherence, fluency, groundedness, relevance
- **Safety**: Content safety, jailbreak detection
- **Agentic**: Intent resolution, tool call evaluation, task adherence
- **Custom evaluators**: Supported alongside built-ins

### Observability Features
- **Tracing**: Local console traces and cloud traces via Azure Monitor/App Insights
- **Trace-linked evaluations**: Traces and evaluations visible together for rapid diagnosis
- **Red teaming**: Proactive adversarial testing with multiple attack strategies (leetspeak, crescendo, prompt manipulation)
- **Agentic red teaming**: Prohibited actions taxonomy for agent-specific vulnerabilities
- **Ask AI**: Portal agent that knows project state for natural language queries
- **Observability Agent**: Natural language interface for App Insights log queries

### Workflow Agents
- Declarative YAML composition of specialist agents (e.g., flight, hotel, car agents with concierge orchestrator)
- Traces show per-agent performance, token costs, and bottlenecks
- Version management with rollback capability

### Observe Skill
- Coding agent (GitHub Copilot) skill that automates the observability loop
- Generates eval datasets, runs batch evals, optimizes prompts, compares versions
- Human-in-the-loop with reasoning transparency
- Released ~May 2026, PM is Felicia Shaw

### Integration
- **Azure Monitor**: Combine AI telemetry with infrastructure/data telemetry
- **Dev containers**: GitHub Codespaces with pre-configured environments
- **AI Toolkit extension**: VS Code integration for local development
- **MCP server**: Foundry MCP server for skill-based interactions

## Related
- [[Microsoft]] — parent company
- [[MicrosoftAzure]] — underlying cloud platform
- [[Amy Boyd]] — Foundry developer relations lead
- [[Nitya Narasimhan]] — observability expert
- [[AgentObservability]] — core capability
- [[WorkflowAgents]] — multi-agent orchestration
- [[ObserveSkill]] — automated observability loop
- [[AgenticEvaluations]] — agent-specific evaluation metrics
- [[AgenticRedTeaming]] — adversarial testing for agents
- [[OpenTelemetry]] — tracing standard
- [[ApplicationInsights]] — tracing backend
- [[AzureMonitor]] — monitoring integration
- [[GitHub Codespaces]] — development environment
- [[PyRIT]] — open-source red teaming tool
- [[summary-20260514 - Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft]] — source
