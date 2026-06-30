---
title: "ContextPackageRegistry"
type: concept
tags: [context, registry, skills, marketplace, distribution]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260503 - Context Is the New Code — Patrick Debois, Tessl.md"]
last_updated: 2026-06-29
---

## Definition
A Context Package Registry is a marketplace or repository for discovering, publishing, and distributing AI context packages (skills, instructions, prompts). Analogous to npm for JavaScript or PyPI for Python, it enables teams and organizations to share reusable context across projects.

## Key Information
- Part of the Context Development Life Cycle (CDLC) Distribute phase, introduced by Patrick Debois
- Examples include the Tessl registry/marketplace and skills.sh
- Currently, 99.9% of publicly available skills are low quality and would fail any set of evals
- Public registries are useful for learning from others' approaches, even if the skills themselves aren't production-ready
- Organizations will likely want private registries for quality-controlled, company-specific context
- Skills are emerging as the standard package format, containing not just text but scripts, documents, and other artifacts
- Registries introduce security concerns: provenance tracking (AI SBOM), dependency scanning, and credential checking

## Related
- [[summary-20260503 - Context Is the New Code — Patrick Debois, Tessl]] — source
- [[ContextDistribution]] — the broader distribution practice
- [[ContextDependencyHell]] — version conflicts between packages
- [[Skills]] — the package format
- [[Tessl]] — company providing a context registry
- [[AISBOM]] — tracking package provenance
- [[ContextSecurity]] — security scanning for registry packages
