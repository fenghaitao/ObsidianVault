---
title: "Agentic Coding"
type: concept
tags: [ai-development, automation, workflow, autonomous-systems]
sources: ["raw/01-articles/claude/2025-10-15 - How to scale agentic coding across your engineering organization.md"]
last_updated: 2026-07-04
---

# Agentic Coding

Agentic coding refers to the use of autonomous AI agents to assist with software development tasks. These agents can analyze code, generate solutions, run tests, and iterate independently, with human developers providing guidance and validation.

## Pattern

Agentic coding dissolves the boundary between technical and non-technical work, enabling anyone who can describe a problem to build solutions. Rather than acting as a simple code generator, agentic tools work best as thought partners that explore possibilities, prototype rapidly, and collaborate with humans through iterative refinement.

## Applications at Anthropic

[[ClaudeCode]] is used across [[Anthropic]] teams for:
- **Onboarding & Navigation** — Accelerating codebase comprehension for new hires
- **Testing & Review** — Automating unit test creation and code review through [[TestDrivenDevelopment]]
- **Production Debugging** — Diagnosing and fixing incidents 3x faster
- **Rapid Prototyping** — Building features and full applications quickly
- **Knowledge Consolidation** — Creating runbooks and documentation from scattered sources
- **Custom Automation** — Building tools without dedicated development resources

## Key Success Factor

The most successful teams treat agentic coding tools as thought partners rather than code generators, exploring possibilities, prototyping rapidly, and sharing discoveries across technical and non-technical users.

## Scaling Across an Organization (October 2025)

Anthropic's guidance for moving agentic coding from isolated experiments to org-wide adoption:

- **Common applications**: legacy system modernization, faster onboarding (querying codebases directly for architecture/dependencies), SRE/DevOps incident-response assistance, and broader technical participation (PMs, designers prototyping directly).
- **Pilot phase**: start with 20-50 developers already using AI-assisted tools; validate against the codebase, identify useful workflows, and build internal expertise; have them document what works and what doesn't.
- **Kickoff over phased rollout**: a shared kickoff/hackathon event (with food) tends to work better than staggered access — skeptical engineers often change their view after hands-on experience.
- **Pilot group as advisors**: once adoption broadens, the pilot group transitions into running workshops and creating educational content — internal champions tend to outperform external training since they know the org's specific pain points.
- **Success metrics beyond lines of code**: sprint throughput, task completion time, migration velocity, developer satisfaction, onboarding duration, cross-functional efficiency. [[ClaudeCode]]'s **Activity Metrics** track lines of code accepted, suggestion acceptance rates, daily active users/sessions, and org-wide/per-user spend.
- **Common pitfalls and fixes**: overly broad tasks without structure (fix: [[TestDrivenDevelopment]] — write tests defining success first, implement incrementally); vague bug reports (fix: share complete error info, screenshots, and expected-vs-actual behavior); vague prompting generally (fix: high-level goal first then details, concrete examples, sequential prompts, specific feedback).
- **[[CLAUDE-md|CLAUDE.md]] as shared documentation**: check project-level files into the repo root, update them alongside architectural changes in the same PRs, and include them in onboarding.

## Related

- [[ClaudeCode]] — Primary agentic coding tool
- [[TestDrivenDevelopment]] — Methodology accelerated by agentic coding
- [[Anthropic]] — Company pioneering agentic coding workflows
- [[CLAUDE-md]] — recommended as shared, version-controlled living documentation during rollout
- [[summary-2025-10-15 - How to scale agentic coding across your engineering organization]] — organizational rollout methodology article
