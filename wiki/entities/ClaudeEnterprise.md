---
title: "ClaudeEnterprise"
type: entity
tags: [claude, product, enterprise, security, context-window]
sources: [raw/01-articles/claude/2024-09-10 - Claude for Enterprise.md, raw/01-articles/claude/2025-08-20 - Claude Code and new admin controls for business plans.md, "raw/01-articles/claude/2026-02-12 - Claude Enterprise, now available self-serve.md"]
last_updated: 2026-07-04
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

## 1M Context and Auto Mode (March 2026)

- Claude Code sessions for Enterprise users on [[Claude4.6Opus|Opus 4.6]] now default automatically to the full 1M-token context window (previously extra usage), reducing compactions and preserving more conversation history.
- **Auto mode** (announced March 2026): after its Team-plan research preview, [[ClaudeCode]]'s classifier-based auto-mode permissions feature is rolling out to Enterprise plan users "in the coming days." See [[PermissionModes]].
- **Compliance API platform-wide (March 2026):** The Compliance API, first launched for Enterprise in August 2025, is now available across the full Claude Platform (not Enterprise-exclusive). Organizations using it for Claude Enterprise can merge their Claude API organization under the same parent org for one combined activity feed. See [[summary-2026-03-30 - Audit Claude Platform activity with the Compliance API]].

## Claude Security Public Beta (April 2026)

- **Claude Security** (formerly "Claude Code Security") entered public beta exclusively for Enterprise customers on April 30, 2026 — a repository vulnerability-scanning and patch-generation product built on [[Claude4.7Opus|Opus 4.7]], accessed via the Claude.ai sidebar or claude.ai/security. Team and Max access is "coming soon." See [[ClaudeSecurity]].

## Cowork Organization Controls (April 2026)

- Admins can organize users into groups — manually or via SCIM — and assign each group a custom role defining which Claude capabilities (including [[ClaudeCowork|Cowork]]) members can access, enabling phased team-by-team rollout.
- Group-level spend limits configurable from the admin console.
- Cowork usage analytics added to the admin dashboard and Analytics API (sessions, active users, skill/connector invocations, DAU/WAU/MAU).
- Expanded OpenTelemetry event coverage for Cowork (tool/connector calls, file changes, skill usage, approval mode), with a shared user identifier enabling correlation with [[ComplianceAPI]] records.

## Early Customers

- [[GitLab]] — Uses for brainstorming, process streamlining, content translation, and code writing.
- [[Midjourney]] — Uses for research summarization, user feedback Q&A, and moderation policy iteration.
- [[Behavox]] — Compliance and security company; rolled out to hundreds of developers as primary pair programmer; reports Claude Code outperforms other agents.
- [[Altana]] — AI-powered supply chain network; reports 2–10x development velocity acceleration for AI/ML systems.

## Self-Serve Availability (February 2026)

Any organization can now purchase Claude Enterprise directly on Anthropic's website with no sales conversation required — set up a workspace, configure SSO, and invite team members in minutes. Bundles Claude, [[ClaudeCode]], and [[ClaudeCowork|Cowork]] (with role-specific plugins for sales, finance, legal, marketing) under enterprise security controls: SSO/domain capture, SCIM provisioning, audit logs, a Compliance API, custom data-retention policies, and usage analytics. **Pricing**: seat-plus-usage model billed at API rates, with spend caps configurable at org and per-user levels. Tailored terms, tiered usage incentives, HIPAA-readiness, or dedicated support still route through Anthropic's sales team. Customer quotes: [[Canva]], [[Quantium]], [[Zapier]], [[Deloitte]], [[NBIM]].

## Access

Self-serve purchase available directly on Anthropic's website as of February 2026 (see above); organizations needing tailored terms still contact Anthropic sales.

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
- [[ClaudeCowork]] — bundled product, now with role-specific plugins
- [[Canva]] — customer quote (self-serve announcement)
- [[Quantium]] — customer quote (self-serve announcement)
- [[Zapier]] — customer quote (self-serve announcement)
- [[Deloitte]] — customer quote (self-serve announcement)
- [[NBIM]] — customer quote (self-serve announcement)
- [[summary-2026-02-12 - Claude Enterprise, now available self-serve]] — self-serve purchasing announcement
- [[PermissionModes]] — auto mode permission system rolling out to Enterprise
- [[summary-2026-03-13 - 1M context is now generally available for Opus 4.6 and Sonnet 4.6]] — 1M context GA announcement
- [[summary-2026-03-24 - Auto mode for Claude Code]] — auto mode rollout announcement
- [[summary-2026-03-30 - Audit Claude Platform activity with the Compliance API]] — Compliance API expansion to full Claude Platform
- [[summary-2026-04-09 - Making Claude Cowork ready for enterprise]] — Cowork organization controls announcement
- [[ClaudeSecurity]] — Enterprise-exclusive public beta product (April 2026)
- [[summary-2026-04-30 - Claude Security is now in public beta]] — Claude Security public beta announcement
