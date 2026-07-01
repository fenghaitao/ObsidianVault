---
title: "Cloud-Based Agent Sandboxes"
type: concept
tags: [agents, infrastructure, cloud, docker, security]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands.md"]
last_updated: 2026-06-26
---

## Definition
Cloud-based agent sandboxes are containerized execution environments running in the cloud that provide isolated, secure workspaces for AI coding agents. They enable running agents more autonomously and scalably than local execution, and are essential infrastructure for agent orchestration at scale.

## Key Information
- Each agent gets its own Docker container in the cloud, preventing it from affecting the host system or other agents.
- More secure than local execution: the worst an agent can do is ruin its own environment, and no human babysitting is needed to approve every command.
- More scalable than local execution: cloud sandboxes can be orchestrated via Kubernetes to run hundreds or thousands of agents concurrently.
- Enables running agents much more autonomously since there's no risk of `rm -rf /` or installing malicious software on a developer's machine.
- OpenHands provides an agent server (Docker container) that houses all agent work, with remote workspaces connecting to it.
- The OpenHands SDK allows creating remote workspaces that connect to Docker containers, giving agents terminal and file editor tools within the sandbox.
- Cloud-based sandboxes are a key enabler for the right side of the AI coding evolution: from local agents to cloud agents to orchestrated parallel agents.

## Related
- [[summary-20260108 - Automating Large Scale Refactors with Parallel Agents - Robert Brennan, OpenHands]] — source
- [[Agent Orchestration]] — practice enabled by cloud sandboxes
- [[Agent Sandbox]] — related concept
- [[Docker]] — containerization technology
- [[Kubernetes]] — orchestration for scaling
- [[OpenHands]] — platform providing cloud sandboxes
- [[Sandboxing]] — broader security concept
