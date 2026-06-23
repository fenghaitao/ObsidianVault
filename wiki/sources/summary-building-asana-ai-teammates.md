---
title: "Building with Claude Managed Agents and Asana AI Teammates"
type: source
tags: [asana, managed-agents, ai-teammates, enterprise, multiplayer, human-in-the-loop]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - San Francisco/12 - Building with Claude Managed Agents and Asana AI teammates.md]
last_updated: 2026-06-23
---

## Core Summary

Arnauld from Asana presents how Asana AI teammates are built on Claude Managed Agents to enable the "agentic enterprise" — where AI agents work alongside humans in multiplayer mode on complex multi-step workflows. Asana provides the enterprise context layer (work graph with 17 years of data), security, guardrails, and human interface, while Claude Managed Agents handles multi-step action execution with built-in verification loops and graders. The demo shows a marketer creating a campaign brief and landing page mock-up, then collaborating with a teammate who requests a minimalist redesign — all tracked and auditable within Asana tasks. Over 21 pre-built AI teammates are generally available across PMO, marketing, IT, HR, and R&D.

## Key Points

- **Multiplayer AI agents:** Agents are real actors in the system with sharing and access controls, working with multiple humans, receiving nudges, and retaining memory across interactions.
- **Enterprise memory:** Historical decisions, approvals, and back-and-forth on campaign briefs are tracked in Asana and provided to agents with security and auditability. An agent built by a former employee continues improving as more people use it.
- **Work graph context:** Asana's 17-year work graph (mission → goals → portfolios → projects → tasks with approvals/workflows) provides structured context for agents.
- **Claude Managed Agents role:** Handles multi-step action execution, reduces prototyping costs, provides built-in verification loops and graders for output quality. Faster than building manual agent loops with the Messages API.
- **Memory from feedback:** User corrections (e.g., "make primary color blue") are ingrained into agent memory so future users don't encounter the same issue.
- **Auditability:** All agent-human interactions are tracked as task comments, convertible to approvals with full prompt history visible.
- **Agent sponsors:** Designated humans who manage agent memory, context access, and behavior.
- **Future direction:** Proactive agents that identify work they can pick up without being assigned, dynamic dashboards, risk reports, automatic remediation suggestions.

## Related

- [[ClaudeManagedAgents]] — the platform powering multi-step actions
- [[Asana]] — the company and work management platform
- [[AgenticMemory]] — memory from user feedback across sessions
- [[Anthropic]] — the model provider
