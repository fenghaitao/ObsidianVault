---
title: "LoginHandler"
type: concept
tags: [harness, agents, browser-use, patterns, security, authentication]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260517 - Harnesses in AI： A Deep Dive — Tejas Kumar, IBM.md"]
last_updated: 2026-06-30
---

## Definition
The Login Handler is a harness pattern demonstrated by Tejas Kumar where authentication is handled programmatically by the harness rather than by the LLM agent. It runs on every agent loop iteration, checks the browser's current URL, and if on a login page, deterministically injects credentials and submits the form — then pushes a message into the agent queue confirming the login was handled.

## Key Information
- Runs as a hook in the agent loop, just before traces are pushed
- Checks the browser session's current URL on every iteration
- If NOT on a login page: returns immediately (computationally cheap no-op)
- If on a login page: fills in credentials (from environment variables or secrets), submits the form programmatically, then pushes a message into the agent message queue: "I'm the harness. I logged in. You're good now"
- Credentials are handled securely by the harness file, which has access to secrets that the LLM agent does not
- Avoids the anti-pattern of putting credentials in system prompts
- Enables agents to navigate sites requiring authentication without the LLM needing to know credentials
- Demonstrated in the context of a Hacker News upvote task where the agent needed to log in before upvoting

## Related
- [[summary-20260517 - Harnesses in AI： A Deep Dive — Tejas Kumar, IBM]] — source
- [[TejasKumar]] — demonstrated the pattern
- [[AgentHarness]] — the harness that contains the login handler
- [[AgentHarnessComponents]] — login handler hooks into the agent loop component
- [[AgentLoop]] — where the login handler runs
- [[HackerNews]] — demo target requiring login
- [[Computer Use]] — browser-use agent capability
- [[DeterministicGuardrails]] — programmatic harness functions vs. LLM-driven behavior
