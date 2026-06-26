---
title: "Fine-Grained Authorization"
type: concept
tags: [identity, authorization, access-control, security]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0.md"]
last_updated: 2026-06-26
---

# Fine-Grained Authorization

## Definition

Fine-Grained Authorization (FGA) is an access control approach that gives resource owners precise control over what an AI agent can access, down to individual resources, collections, or documents, rather than granting broad all-or-nothing access.

## Key Information

- **Auth0 Product**: FGA is a sub-product of Auth0 focused on role-based access control (RBAC), distinct from scope-based API access
- **Open Source**: There is an open-source project around FGA that extends the feature set
- **Scopes vs. Roles**: Scopes are for API access control (what APIs an agent can call); roles are for persona-based access (what kind of user the agent represents)
- **User Control**: "AI access should be fine-grained. I need to give the agent control to access my resources, but not any resource, not any collection or document."
- **Enterprise Context**: Okta provides the enterprise layer where companies control what agents acting on behalf of employees can do

## Related

- [[Auth0]]
- [[Okta]]
- [[ScopeBasedAccessControl]]
- [[AgentIdentity]]
- [[summary-20260114 - Identity for AI Agents - Patrick Riley & Carlos Galan, Auth0]]
