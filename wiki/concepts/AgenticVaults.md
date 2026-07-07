---
title: "AgenticVaults"
type: concept
tags: [security, secrets-management, agent-infrastructure, managed-agents]
sources: ["raw/01-articles/claude/2026-06-09 - New in Claude Managed Agents run agents on a schedule and store environment variables in vaults.md"]
last_updated: 2026-07-07
---

## Definition

Agentic vaults are a secure credential management feature of [[ClaudeManagedAgents]] that stores API keys, OAuth tokens, and environment variables for agent use without exposing secrets to the model. The agent's sandbox holds only a placeholder; the real credential is injected at the network boundary and only on requests to approved domains.

## Key Information

- Vaults initially supported MCP OAuth token registration (April 2026), where developers reference a vault by ID at session creation and the platform injects and refreshes credentials automatically.
- In June 2026, vaults were extended to support environment variables, enabling CLI tools and other shell-based integrations to make authenticated API calls.
- **Security model**: the agent never sees the real key. The sandbox holds a placeholder. The real key is attached at the network boundary and only on requests to domains the developer has explicitly allowed.
- **Key rotation**: to change a key, update it in the vault; running sessions pick up the new value on their next call without requiring a restart.
- **CLI compatibility**: most CLIs that send their key in an HTTP request work with vaults, including Browserbase, KERNEL, Notion, Ramp, and Sentry CLIs.
- **Browser capabilities**: [[Browserbase]] and [[KERNEL]] CLIs, authenticated through vaults, give Managed Agents browser capabilities for the first time, enabling agents to navigate and interact with the web alongside their other tools.

### Customer Adoption

- **[[Notion]]**: uses environment variables in vaults to roll out its CLI alongside MCP tools, adding file-upload capabilities to its agents without API tokens ever being handed to the model.
- **[[Browserbase]]**: built its public catalog of browser skills using the browse CLI, authenticated through vaults. A scheduled deployment periodically validates the catalog.
- **[[KERNEL]]**: uses environment variables in vaults to securely connect agents to databases tracking usage and customer conversations, flagging usage surges as they happen.
- **[[Milana]]**: uses environment variables in vaults to securely connect its AI product engineer to customer codebases, enabling automated bug finding and fixing with large-scale data analysis.

## Related

- [[ClaudeManagedAgents]] — the platform providing vaults
- [[ScheduledDeployments]] — complementary scheduling feature
- [[Sandboxing]] — the sandbox architecture that enables placeholder key injection
- [[ModelContextProtocol]] — MCP integration that vaults also support for OAuth
- [[summary-2026-06-09 - New in Claude Managed Agents run agents on a schedule and store environment variables in vaults]] — source announcement
