---
title: "Build AI Agents Using Claude in Microsoft Foundry"
type: source
tags: [microsoft-foundry, agents, MCP, workshop, enterprise]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London/20 - Build AI agents using Claude in Microsoft Foundry.md]
last_updated: 2026-06-23
---

## Core Summary

Marlene Mungami and colleagues from Microsoft present a hands-on workshop demonstrating how to build AI agents using Claude models within Microsoft Foundry, Microsoft's unified platform for AI application development. The workshop walks through deploying Claude Sonnet 4.6 in Foundry, connecting it to an MCP server for a cupcake ordering system, and using the Microsoft Agent Framework (open-source Python SDK) to orchestrate the agent. Key themes include enterprise-ready features (built-in security, observability, governance), the partnership between Microsoft and Anthropic, and the shift from single-turn AI to agentic systems.

## Key Points

- **Microsoft Foundry:** Unified platform for building AI agents at scale, supporting GitHub, VS Code, Visual Studio, and Copilot Studio workflows.
- **Claude in Foundry:** Access Claude models (Sonnet 4.6, Opus 4.7) with enterprise features: Microsoft Defender, Purview, Entra ID integration (no .env files needed).
- **Agent Framework:** Open-source Python/Typescript SDK for building agents that detect environment variables and connect to MCP servers.
- **MCP integration:** Connect agents to external systems via MCP server URLs; access tools, prompts (reusable instruction snippets), and resources (structured data over HTTP).
- **1,400+ built-in connectors:** Agents can interact with SAP, ServiceNow, and other enterprise systems.
- **Workshop flow:** Deploy model in Foundry playground → test system prompts → connect to MCP server → load custom instructions and welcome banners → build ordering agent.
- **Enterprise benefits:** Centralized billing, built-in auth (SSO, OAuth, IAM), observability (CloudWatch, CloudTrail), SLAs, private networking.

## Related

- [[ClaudeCode]] — the developer tool used alongside Foundry
- [[ModelContextProtocol]] — the MCP standard used for tool integration
- [[MicrosoftFoundry]] — the platform entity
- [[Anthropic]] — the model provider in this partnership
