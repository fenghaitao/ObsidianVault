---
title: "Agent Card"
type: concept
tags: [agent, a2a, standard, discovery, metadata, agent-card]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260410 - One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca.md"]
last_updated: 2026-06-30
---

## Definition
An Agent Card is a standard metadata document that describes an AI agent's identity, endpoint, capabilities, supported modalities, and authentication requirements. It serves as the foundation for agent discovery in A2A registries, enabling agents to be self-documenting and automatically discoverable.

## Key Information
- **Standard fields**: Agent identity (name, description), endpoint URL, capabilities, supported modalities (text, image, audio, etc.), and authentication requirements
- **Self-documenting deployment**: When an agent is deployed, its agent card is automatically published to the A2A Registry via CICD integration, making the agent discoverable without manual registration
- **Discovery mechanism**: Any other agent or developer can discover available agents through the registry by reading agent cards, enabling agent-to-agent communication
- **Auto-generation via blueprints**: Blueprint repositories provide form-based creation of agent cards and preview before publishing, simplifying the process for developers
- **Inspector compatibility**: Platform includes inspector pages that check agent card compatibility for A2A agents
- **Standard-based**: The A2A Registry is "fully based on the agent card" standard, meaning the card is the canonical description of each agent in the system
- **CICD integration**: GitHub Actions pipeline publishes the agent card metadata to the registry backend when a branch is tagged, alongside publishing the Docker image

## Related
- [[A2A Registry]] — the registry that catalogs agents via their agent cards
- [[AgentToAgentCommunication]] — the protocol enabled by agent card discovery
- [[CICD Agent Publishing]] — the automated publishing mechanism
- [[Blueprint Repository]] — template repos that auto-generate agent cards
- [[Agent Discoverability]] — the broader concept of making agents findable
- [[AgentIdentity]] — the identity aspect described in agent cards
- [[Amplifon]] — organization that implemented agent card-based registry
- [[summary-20260410 - One Registry to Rule them All - Sonny Merla, Mauro Luchetti, & Mattia Redaelli, Quantyca]] — source
