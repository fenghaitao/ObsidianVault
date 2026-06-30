---
title: "Doc Rot"
type: concept
tags: [ai, documentation, codebase, agents, maintenance]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock.md"]
last_updated: 2026-06-29
---

## Definition
Doc Rot is the phenomenon where documentation (PRDs, plans, markdown files) kept in a repository becomes increasingly out of sync with the actual code as the codebase evolves. In AI-assisted development, stale documentation can mislead agents that find and rely on outdated information.

## Key Information
- Example: a PRD for a gamification system is kept in the repo. A month later, an agent finds it and uses it as reference, but the code has changed so much the PRD is unrecognizable — names, file structure, and even requirements may have changed
- This can cause agents to make decisions based on outdated specifications
- Matt Pocock tends to delete PRDs and plans after implementation rather than keeping them in the repo
- His preferred approach: use GitHub issues, which can be marked as closed. The visual indicator of completion helps agents understand the document is historical
- This contrasts with keeping documentation permanently, which some developers prefer for reference
- The tension: documentation is valuable for human reference but dangerous for agent reference if stale
- Doc rot is a specific instance of the general problem of documentation falling out of sync with code

## Related
- [[summary-20260424 - Full Walkthrough： Workflow for AI Coding — Matt Pocock]] — source transcript
- [[MattPocock]] — advocates for deleting old docs
- [[PRD (Product Requirements Document)]] — the type of document that rots
- [[Context Rot]] — related concept for context windows
- [[SpecAsLivingDocumentation]] — alternative approach
- [[Software Entropy]] — the broader phenomenon
