---
title: "ClaudeEnterprise"
type: entity
tags: [claude, product, enterprise, security, context-window]
sources: [raw/01-articles/claude/2024-09-10 - Claude for Enterprise.md, raw/01-articles/claude/2025-08-20 - Claude Code and new admin controls for business plans.md]
last_updated: 2026-06-28
---

## Definition

Claude Enterprise is [[Anthropic]]'s plan for organizations that need secure, scaled collaboration with Claude using internal knowledge. Announced September 2024, it combines expanded context capacity with enterprise-grade security and integrations.

## Key Features

- **500K Context Window** — Expanded capacity for processing large documents, codebases, and internal knowledge bases.
- **Native GitHub Integration** (beta) — Sync GitHub repositories with Claude to work on entire codebases for feature development, debugging, and engineer onboarding.
- **Enterprise Security Controls** — SSO (Single Sign-On), role-based permissions, admin tooling, data isolation.
- **No Training on Customer Data** — Anthropic does not train Claude models on customer conversations or content.
- **Projects & Artifacts** — End-to-end workflows for team productivity (marketing campaigns, product prototypes, code debugging).
- **Knowledge Integration** — Securely share and reuse organizational knowledge across teams.
- **Research** — In-depth agentic research across web and organizational sources via [[Research|Research capability]].
- **Google Workspace Integration** — Access to Gmail, Calendar, and Google Docs for contextual awareness via [[GoogleWorkspaceIntegration|Google Workspace integration]].
- **Enterprise Cataloging** — Specialized indexing of organizational documents using [[RetrievalAugmentedGeneration|Retrieval Augmented Generation (RAG)]] for improved retrieval accuracy.

## Memory (September 2025)

- Enterprise plan users received [[ClaudeMemory|Claude Memory]] at launch on September 11, 2025.
- Memory is project-scoped: each project maintains an isolated memory store so confidential discussions stay separate from general operations.
- **Admin disable:** Enterprise admins can disable memory for the entire organization at any time.
- Users retain full control: the memory summary is viewable and editable in Settings; [[IncognitoChat|Incognito chat]] is available for sessions that should not be saved to memory.
- Standard data retention settings apply to Incognito chats on Enterprise plans.

## Premium Seats & Claude Code Integration (August 2025)

- Enterprise customers can now upgrade to **premium seats** that bundle Claude and [[ClaudeCode]] under one subscription.
- Admins assign standard or premium seats per user based on role and requirements.
- Premium seat users move seamlessly between Claude (conversational ideation) and Claude Code (terminal implementation) in a single development workflow.
- **Extra usage** available at standard API rates with admin-controlled per-user spend caps for predictable billing.
- Includes **Claude Code usage analytics**, granular spend caps, and self-serve seat management.
- Accompanied by the new [[ComplianceAPI]] for real-time programmatic access to usage data for governance and auditing.

## Early Customers

- [[GitLab]] — Uses for brainstorming, process streamlining, content translation, and code writing.
- [[Midjourney]] — Uses for research summarization, user feedback Q&A, and moderation policy iteration.
- [[Behavox]] — Compliance and security company; rolled out to hundreds of developers as primary pair programmer; reports Claude Code outperforms other agents.
- [[Altana]] — AI-powered supply chain network; reports 2–10x development velocity acceleration for AI/ML systems.

## Access

Available to organizations; requires contacting Anthropic sales team.

## Related

- [[Anthropic]] — Company offering Claude Enterprise
- [[ContextWindow]] — 500K context window feature
- [[GitHubIntegration]] — Native integration for engineering teams
- [[Research]] — Agentic research capability
- [[GoogleWorkspaceIntegration]] — Google Workspace integration
- [[RetrievalAugmentedGeneration]] — Underlying pattern for enterprise cataloging
- [[ComplianceAPI]] — New programmatic compliance and governance feature (August 2025)
- [[ClaudeCode]] — Now bundled in premium seats
- [[Behavox]] — Customer: compliance/security company using Claude Code as pair programmer
- [[Altana]] — Customer: supply chain AI company achieving 2–10x dev velocity gains
- [[summary-2024-09-10 - Claude for Enterprise]] — Source article
- [[summary-2025-08-20 - Claude Code and new admin controls for business plans]] — Premium seats and Compliance API announcement
- [[ClaudeMemory]] — persistent cross-conversation memory feature launched for Enterprise September 2025
- [[IncognitoChat]] — private chat mode introduced alongside memory
- [[summary-2025-09-11 - Bringing memory to Claude]] — memory launch announcement
