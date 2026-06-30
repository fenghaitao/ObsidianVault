---
title: "ContextDistribution"
type: concept
tags: [context, packaging, registry, skills, distribution]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - Context Is the New Code — Patrick Debois, Tessl.md"]
last_updated: 2026-06-29
---

## Definition
Context Distribution is the practice of sharing AI context (prompts, skills, instructions) across projects, teams, and organizations through version-controlled repositories, package formats, registries, and dependency management — analogous to software library distribution.

## Key Information
- Part of the Context Development Life Cycle (CDLC) Distribute phase, introduced by Patrick Debois
- Multiple distribution mechanisms:
  - **Repo check-in**: Committing context files (agent.md, Claude.md) to repositories for zero-friction sharing with colleagues
  - **Packages**: Packaging context as reusable libraries (skills) that can be installed across projects and teams
  - **Registries**: Marketplaces for discovering context packages (e.g., Tessl registry, skills.sh)
  - **Dependency management**: Context packages have dependencies that can conflict (e.g., frontend context conflicting with React context)
- Skills are emerging as a standard package format for context, supported across multiple coding agents
- 99.9% of publicly available skills are low quality — organizations will want private registries
- Context packages can contain not just text but scripts, documents, and other artifacts
- Distribution introduces security concerns: who built the skill, with what model, and does it contain malicious content?

## Related
- [[summary-20260503 - Context Is the New Code — Patrick Debois, Tessl]] — source
- [[ContextDevelopmentLifeCycle]] — the Distribute phase
- [[ContextPackageRegistry]] — registries for context discovery
- [[ContextDependencyHell]] — version conflicts between context packages
- [[ContextSecurity]] — security scanning for distributed context
- [[Skills]] — the emerging package format for context
- [[AISBOM]] — tracking provenance of context packages
