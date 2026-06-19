---
title: "Rasmus"
type: entity
tags: [person, framework-creator, prp, dynamis, product-manager]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20250703 - Context Engineering is the New Vibe Coding (Learn this Now).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250717 - Context Engineering 101 - The Simple Strategy to 100x AI Coding.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250724 - Build ANY AI Agent with this Context Engineering Blueprint.md"
last_updated: 2026-06-19
---

## Definition

Rasmus is the creator of the **[[PRPFramework]]** (Product Requirements Prompts) — the specific [[ContextEngineering]] methodology [[ColeMedin]] adopted in mid-2025 and uses as the canonical context-engineering toolkit across his subsequent content. A member of Cole's Dynamis.ai community; former product manager / business analyst whose PRD-writing background led directly to PRP design.

> Last name not used in Cole's videos — recorded here as "Rasmus" only. If you find a more specific reference in later ingests, update this entry.

## Key Information

### Background → PRP origin story

In `summary-context-engineering-101` Rasmus describes the path:

- **Years as a product manager / business analyst** — wrote a lot of technical documentation and PRDs (Product Requirements Documents). Knows from doing it that good PRDs reduce ambiguity and make implementation tractable.
- **Existing project, valuation engine** — wanted to use AI coding assistants on a real codebase, found PRD-style descriptions helped but lacked agent-specific runbook details.
- **Iterated for over a year** — across Aider, Cline, eventually [[ClaudeCode]]. Watched the framework grow more reliable as Claude moved from 3.5 → 3.7 → 4 (his quote: *"100-line PRPs reliably nine times out of ten on 3.7. With Claude 4, 500-line reliably, 1000-line semi-reliably, 1500-line experimentally."*).
- **Released publicly via Cole's channel** — Cole's three context-engineering videos are the canonical public artifacts.

### What's distinctively his

- **"PRP = PRD + curated codebase intelligence + agent runbook."** The one-line definition.
- **The minimum viable packet framing** — a PRP is "the minimum viable packet an AI needs to plausibly ship production-ready code on the first pass." Not maximum context — *minimum* sufficient context. Less ceremony than over-spec'd PRDs.
- **Context placement heuristic** — what goes in `CLAUDE.md` (forever-true things) vs. slash commands (domain-agnostic workflows) vs. base PRP (domain-specific) vs. generated PRP (feature-specific).
- **Validation-by-default** — [[ValidationGates]] in every PRP. The AI is never trusted to declare done without running the gates.
- **Use-case templates as a scaling primitive** — instead of one universal PRP, a library of (language × project type) starter templates. The Dynamis-community project Cole and Rasmus committed to building.

### Style — pragmatic over evangelical

Reading the transcript with Cole, Rasmus consistently:
- **Reminds the audience to validate.** "Read your PRPs before you run the execute command."
- **Acknowledges what's not perfect.** "It ain't perfect. It definitely isn't, but it feels close."
- **Grounds in real-world existing-codebase work.** PRP framework was built for working on existing code, not greenfield demos.

### Relationship to [[ColeMedin]]

Rasmus and Cole are colleagues in the Dynamis.ai community where Cole originally encountered the PRP framework via Rasmus's workshop. Cole has been the primary public amplifier; Rasmus continues developing the framework. They've co-shipped at least two use-case templates (MCP servers, Pydantic AI agents) as a public collaboration.

## Related

- [[PRPFramework]] — his framework
- [[ContextEngineering]] — the discipline PRP framework operationalizes
- [[ColeMedin]] — primary amplifier of his work
- [[ClaudeCode]] — primary execution surface for PRPs
- [[ValidationGates]] — sub-pattern central to PRP execution
- [[summary-context-engineering-101]] — primary source (Rasmus appears as guest)
- [[summary-context-engineering-is-new-vibe-coding]] — first introduction
- [[summary-context-engineering-blueprint-for-ai-agents]] — collaborative use-case template
