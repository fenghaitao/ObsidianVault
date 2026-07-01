---
title: "Docker"
type: entity
tags: [tool, containerization, infrastructure, devops]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands.md"]
last_updated: 2026-06-26
---

## Definition
Docker is a containerization platform. In the OpenHands architecture, Docker containers serve as isolated sandbox environments for running agents securely and scalably in the cloud.

## Key Information
- Used by OpenHands to provide isolated agent sandboxes in the cloud
- Each agent runs in its own Docker container, preventing it from affecting the host system or other agents
- Enables running agents more autonomously since the worst they can do is ruin their own environment
- For large-scale deployments with thousands of agents, Kubernetes can orchestrate the Docker containers

## Related
- [[summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — source
- [[OpenHands]] — platform using Docker for agent sandboxes
- [[Kubernetes]] — container orchestration for scaling
- [[CloudBased Agent Sandboxes]] — concept enabled by Docker
- [[Agent Sandbox]] — related concept
