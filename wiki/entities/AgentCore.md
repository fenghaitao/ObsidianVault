---
title: "AgentCore"
type: entity
tags: [tool, aws, agent-deployment, cloud]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro.md"]
last_updated: 2026-06-26
---

## Definition
AWS Agent Core is an AWS service for deploying and running AI agents. It was used as the deployment target in Al Harris's Kiro demo project "Gramps" (a dad joke generator).

## Key Information
- AWS service for deploying AI agents to the cloud
- Has a built-in memory/persistence feature that Kiro's spec-driven workflow discovered as an alternative to custom S3-based checkpointing
- Used as the deployment target in the Kiro live demo: a dad joke generator built with CDK and LangGraph
- Al Harris admitted he was not familiar enough with Agent Core and used Kiro + MCP (AWS documentation server) to learn about it
- The demo revealed that Agent Core's native memory feature was more idiomatic than the initially proposed S3-based approach

## Related
- [[summary-20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro]] — source
- [[AWS]] — parent cloud platform
- [[AmazonKiro]] — the IDE used to build and deploy to Agent Core
- [[LangGraph]] — agent framework used in the demo
