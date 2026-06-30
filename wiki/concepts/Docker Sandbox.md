---
title: "Docker Sandbox"
type: concept
tags: [docker, sandboxing, security, ai, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick.md"]
last_updated: 2026-06-29
---

## Definition
Docker Sandbox is a Docker feature that allows running code within an isolated container, restricting file system access to a specific location. It is used as a security measure for AI agents to prevent them from accessing or modifying files outside the intended workspace.

## Key Information
- Docker feature: `docker sandbox code` runs code within a sandboxed container
- Isolates AI agents to only change things within a specific place in the file system
- Chris Parsons recommends it as one of several sandboxing approaches for AI agents
- Limitation: can still leak data from one system to another if the agent has access to both
- Part of a layered security approach alongside VPS isolation, fine-grained permissions, and lockbox
- Matt Pocock's Sandcastle library also uses Docker sandboxes for parallel agent loops

## Related
- [[Agent Sandboxing]] — broader concept
- [[Lethal Trifecta]] — security concern it addresses
- [[Lockbox]] — complementary sandboxing tool
- [[Sandcastle]] — Matt Pocock's library using Docker sandboxes
- [[ChrisParsons]] — referenced in his workshop
- [[summary-20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick]] — source transcript
