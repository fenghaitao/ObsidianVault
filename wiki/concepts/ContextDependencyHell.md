---
title: "ContextDependencyHell"
type: concept
tags: [context, dependencies, versioning, packaging, conflict]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - Context Is the New Code — Patrick Debois, Tessl.md"]
last_updated: 2026-06-29
---

## Definition
Context Dependency Hell is the problem of conflicting or incompatible context packages (skills, instructions, prompts) when multiple context dependencies are combined in a project — analogous to dependency hell in traditional software development.

## Key Information
- Identified by Patrick Debois as an emerging problem in context distribution
- Example: downloading a frontend context package may conflict with what's in a React context package
- Context packages will need versioning that mirrors library versions and code versions
- As context ecosystems grow, dependency resolution for context will become as complex as it is for code
- Part of the broader observation that context management inherits all the challenges of software engineering

## Related
- [[summary-20260503 - Context Is the New Code — Patrick Debois, Tessl]] — source
- [[ContextDistribution]] — the practice that creates dependency hell
- [[ContextPackageRegistry]] — registries where dependencies are resolved
- [[Skills]] — the package format subject to dependency conflicts
