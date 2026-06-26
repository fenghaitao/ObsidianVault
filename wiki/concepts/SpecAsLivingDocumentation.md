---
title: "SpecAsLivingDocumentation"
type: concept
tags: [specification, documentation, version-control, design-review]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro.md"]
last_updated: 2026-06-26
---

## Definition
Spec as living documentation is the practice of treating specifications as mutable, evolving documents rather than one-off plans. In Amazon Kiro, specs are amended over time as requirements change, producing diffs that can be reviewed like code changes.

## Key Information
- Specs are not just task lists but living documentation about what the system does
- Kiro discovers existing specs and amends them rather than creating duplicates when new related work is requested
- Goal: bidirectional sync — as you continue working with Kiro, specs evolve; changing requirements mutates previous specs
- Produces diffs of requirements (like code diffs) that can be reviewed
- At Amazon, internal teams have replaced design doc reviews with spec reviews: someone takes a spec from markdown, blasts it into the wiki via MCP, and the team reviews and comments on it
- Contrasts with ADRs (Architecture Decision Records) which are point-in-time; specs are living documentation
- On first creation (greenfield), specs produce a lot of new content; subsequent changes produce targeted diffs

## Related
- [[summary-20260109 - Spec-Driven Development： Agentic Coding at FAANG Scale and Quality — Al Harris, Amazon Kiro]] — source
- [[SpecificationDrivenDevelopment]] — the paradigm
- [[AmazonKiro]] — IDE implementing this approach
- [[MCP]] — protocol used to blast specs into wikis
