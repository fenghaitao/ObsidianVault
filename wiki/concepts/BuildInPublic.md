---
title: "BuildInPublic"
type: concept
tags: [concept, philosophy, open-source, community, content-creation]
sources:
  - "raw/03-transcripts/Cole Medin/Archon - The AI Agent Builder/04 - Introducing Archon - an AI Agent that BUILDS AI Agents.md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20250414 - The ULTIMATE Guide to Building Your Own MCP Servers (Free Template).md"
  - "raw/03-transcripts/Cole Medin/Channel Only/20260507 - AI YouTube Is Only Claude Hype Now.md"
last_updated: 2026-06-20
---

## Definition

Build in Public is the practice of developing a project openly — open-source from day one, iterating visibly, sharing the journey, and inviting contribution — rather than building privately and releasing a finished product. It's one of [[ColeMedin]]'s recurring philosophies, most visible in how he develops [[Archon]].

## Key Information

- **Open-source from the start** — the project is public while it's still experimental and unfinished, not just at release.
- **Iterate visibly** — each version ships publicly with its rough edges; the audience watches the evolution. [[Archon]]'s numbered-version roadmap (v1 → v13+) is build-in-public as a teaching device.
- **Invite contribution** — the community can use, critique, and contribute. Cole explicitly invites PRs and feedback on Archon.
- **Templates and resources are shared freely** — Cole's MCP server template, [[PRPFramework]] templates, [[Crawl4AIRAG]], and [[SecondBrain]] starter repos are all given away. The teaching *is* the product; the code is free.
- **Education through transparency** — by building in public, Cole turns his own development process into content. The audience learns agentic engineering by watching real (not toy) projects evolve.

### Tension with the "build your own" stance

Note a deliberate nuance: Cole builds *some* things fully in public (Archon, templates) but withholds others (his actual [[SecondBrain]] code base). For the second brain he ships a PRD-generation skill instead of the code, because giving away the code "defeats the purpose" (you'd just have another [[OpenClaw]] to run blindly rather than building your own). So build-in-public is a default, not an absolute — moderated by whether sharing the artifact helps or replaces the learner's own building.

## Related

- [[ColeMedin]] — primary practitioner
- [[Archon]] — the flagship build-in-public project
- [[PRPFramework]], [[Crawl4AIRAG]], [[SecondBrain]] — shared templates/resources
- [[OpenClaw]] — the "don't just run someone else's code" counterpoint
- [[summary-introducing-archon-ai-agent-builder]] — build-in-public articulated
- [[summary-ai-youtube-claude-hype]] — building Archon / Dark Factory live on stream
