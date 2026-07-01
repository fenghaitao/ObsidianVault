---
title: "Intent and Plan"
type: concept
tags: [agents, development-workflow, specs, planning]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner.md"]
last_updated: 2026-06-30
---

## Definition
Intent and Plan is the codified goal that replaces the Pull Request as the unit of work in agentic software development. It captures what the developer wants to achieve (intent) and how it will be accomplished (plan), and is consumed by an agent harness that iterates toward implementation.

## Key Information
- Proposed by [[HugoSantos]] as the replacement for PR-based workflows in [[Continuous Compute]]
- Can be codified in various forms: Linear tickets, Slack messages, specs, or any written goal
- Feeds into the agent harness loop: the agent checks out a well-known commit and iterates toward the plan
- The plan can adapt: if world signals change (another change lands, plan changes), the harness adapts its intent and plan
- Creates a new loop rather than stopping the current one
- Human interaction becomes: "Does it look good? Should I change something else?" → "Continue"
- Relates to the broader [[Plan and Review Shift]] in software engineering
- Enables parallel agents working on independent features that semantically group at the [[PreMerge Queue]]

## Related
- [[summary-20260513 - CI⧸CD Is Dead, Agents Need Continuous Compute and Computers — Hugo Santos and Madison Faulkner]] — source
- [[Continuous Compute]] — paradigm that uses Intent and Plan as work unit
- [[Plan and Review Shift]] — broader industry shift toward plan-based development
- [[SpecificationDrivenDevelopment]] — related approach using formal specs
- [[AgentHarness]] — the loop that consumes intent and plan
- [[PreMerge Queue]] — where semantically grouped plans are approved
