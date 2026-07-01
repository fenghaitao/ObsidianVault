---
title: "A2A Registry"
type: concept
tags: [a2a, agent-to-agent, registry, enterprise, governance, agent-card]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260410 - One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca.md"]
last_updated: 2026-06-30
---

## Definition
An A2A (Agent-to-Agent) Registry is a centralized catalog of all available AI agents within an organization, based on the agent card standard. It enables agent discovery, self-documenting deployment, and governed agent-to-agent communication at enterprise scale.

## Key Information
- **Agent card standard**: Fully based on the agent card specification describing agent identity, endpoint, capabilities, supported modalities, and authentication requirements
- **Auto-publishing via CICD**: When an agent is deployed, it automatically publishes its agent card to the registry through CICD integration (GitHub Actions on branch tag)
- **Self-documenting agents**: The CICD pipeline makes all agent development self-documenting -- any developer can discover newly deployed agents and interact with them
- **Discovery mechanism**: Any other agent or developer can discover available agents and connect to them through the registry catalog
- **Framework agnostic**: The A2A server blueprint uses interfaces and ports, not tied to a specific framework (LangChain, Agno, etc.), so teams can implement agents in their framework of choice
- **Blueprint integration**: Blueprint repositories include pre-configured FastAPI servers, Docker files, authentication, cost tracking, and LangFuse observability
- **Inspector integration**: Platform includes inspector pages for checking A2A agent card compatibility
- **Runtime architecture**: Agents call through the AI Gateway to the A2A proxy, which looks up the actual backend URL from the registry catalog before routing the request

## Related
- [[Agent Card]] — the standard used to describe agents in the registry
- [[MCP Registry]] — companion registry for MCP servers
- [[Use Case Registry]] — connects agents to business use cases
- [[AI Gateway]] — unified LLM access layer that routes to A2A proxies
- [[AgentToAgentCommunication]] — the protocol and pattern for agent-to-agent interaction
- [[Blueprint Repository]] — template repos for A2A agent development
- [[CICD Agent Publishing]] — automated metadata publishing mechanism
- [[Amplifon]] — organization that built this enterprise A2A registry
- [[Quantyca]] — consultancy that designed the registry
- [[Mauro Luchetti]] — presenter who described the A2A registry design
- [[Mattia Redaelli]] — presenter who described the CICD and runtime architecture
- [[summary-20260410 - One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca]] — source
