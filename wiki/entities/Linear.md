---
title: "Linear"
type: entity
tags: [project-management, tool, issue-tracking, agents]
sources: []
last_updated: 2026-06-25
---

## Definition

Linear is a project management and issue tracking tool. Frequently used as the source of truth for AI agent workflows — agents claim issues, update status, and report progress through Linear's API. Referenced across Cole Medin's and Brian Casel's content as the task-tracking layer in agent harnesses.

## Key Information

- Used by Cole Medin's harness engineering: the initializer creates Linear projects + issues, agents claim and update them
- Used by Brennan Dunn's sub-agent team for task tracking
- MCP integration available through Arcade gateway
- Replaces local progress files as the shared source of truth between agents and humans

## Related

- [[AgentHarness]] — Linear as the task-tracking layer
- [[Arcade]] — MCP gateway for Linear integration
- [[ColeMedin]] — uses Linear in harness engineering
- [[BrennanDunn]] — uses Linear with sub-agent teams
