---
title: "AgentIdentity"
type: concept
tags: [access-model, security, permissions, agent, multiplayer-ai]
sources: ["raw/01-articles/claude/2026-06-24 - Agent identity in Claude Tag a new access model for autonomous, team-wide AI.md"]
last_updated: 2026-07-07
---

## Definition

Agent identity is an access model where an AI agent has its own credentials and permissions tied to a workspace, rather than acting on behalf of an individual user. It replaces the question "what can this user do?" with "what can this agent do in this compartment?"

## Key Information

- Contrasts with the "single player" model where an AI assistant uses a user's personal credentials (e.g., Google Drive, GitHub, calendar) to read and write on their behalf.
- In the agent identity model, the agent posts as its own app identity (e.g., "Claude" app in Slack), opens PRs as a GitHub App, and queries databases under a service account provisioned by an admin.
- Because no personal user credentials are involved, a shared channel cannot become a side door into someone's private documents.
- **Workspace-level identity**: admins define a baseline set of connections and skills that Claude holds everywhere; every channel inherits it by default.
- **Channel-level overrides**: admins can scope additional access to specific channels (e.g., GitHub for the engineering channel, CRM for a private channel).
- **Revocation**: revoking an agent identity terminates Claude's access everywhere that identity was used, simplifying security management compared to auditing individual user accounts.
- **Memory and access boundaries**: what Claude learns in a private channel never appears in the wider workspace. Each channel's identity is isolated.
- **Auditability**: every routine, memory write, and network call made with agent credentials is recorded; actions also appear in each connected system's own logs since Claude acts under its own service accounts.
- **Credential storage**: when an admin adds a connection to a channel's profile, the credential is stored independently and mapped to that channel's identity, injected at the network boundary at request time.
- **Network egress**: outbound traffic to any host an admin hasn't explicitly allowed is blocked.

### Future Directions

- **Just-in-time credential grants**: a user can approve a single sensitive action in the moment without permanently widening the agent's scope.
- **Identity-aware overlay**: for organizations with complex clearance structures, user-level permission checks layered on top of agent scope, so Claude only acts when both the channel's profile and the requesting user's own permissions allow it.

## Related

- [[summary-2026-06-24 - Agent identity in Claude Tag a new access model for autonomous, team-wide AI]] — source article
- [[ClaudeTag]] — the product that implements agent identity
- [[MultiplayerAI]] — the broader paradigm agent identity enables
- [[Anthropic]] — the company that developed agent identity
