---
title: "Lightweight Design Document"
type: concept
tags: [concept, design-document, agent-workflow, spec-driven-development, process]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260515 - Agents Don't Do Standups： Building the Post-Engineer Engineering Org — Mike Spitz, PFF.md"]
last_updated: 2026-06-30
---

## Definition
A Lightweight Design Document (LDD) is an agent-generated design document that captures how a feature will be built, including architecture, approach, and implementation details. It is produced after an AI agent interviews stakeholders on the spec, analyzes prior LDDs to maintain consistency with the engineering org's ethos, and is distributed to all engineers for feedback before tickets and PRs are auto-generated.

## Key Information
- **Origin**: Presented by [[MikeSpitz]] as part of the [[PostEngineer Engineering Org]] model at [[PFF]]
- **Generation Process**: Agent interviews stakeholders on the spec → agent generates LDD → agent analyzes prior LDDs to maintain consistency → LDD distributed for engineer feedback
- **Purpose**: Replaces sprint planning and refinement by front-loading design decisions into a single document
- **Key Benefit**: Prevents AI agents from over-engineering or producing inconsistent code by being prescriptive about architecture and approach upfront
- **Consistency**: The agent learns from all previous LDDs, ensuring new features are built in the same ethos as existing ones — not a generic "cloud code" feel
- **Feedback Loop**: LDDs are shared with all engineers for review before implementation begins
- **Downstream Automation**: After LDD approval, tickets are auto-created (structured to avoid blocking dependencies) and PRs are auto-generated
- **Scale Control**: Being prescriptive in the LDD prevents agents from generating thousand-line code dumps or over-engineering solutions
- **Relationship to Spec**: The spec defines *what* to build; the LDD defines *how* to build it

## Related
- [[MikeSpitz]] — presented the concept
- [[PFF]] — company using LDDs in their workflow
- [[PostEngineer Engineering Org]] — organizational model the LDD fits within
- [[Spec-Driven Development]] — broader methodology
- [[Composable Skills]] — LDD generation is implemented as a skill
- [[ClaudeCode]] — coding agent used to generate LDDs
- [[summary-20260515 - Agents Don't Do Standups： Building the Post-Engineer Engineering Org — Mike Spitz, PFF]]
