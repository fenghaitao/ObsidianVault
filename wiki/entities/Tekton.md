---
title: "Tekton"
type: entity
tags: [project, hackathon, 3d-reconstruction, cultural-preservation, claude-opus]
sources: ["raw/01-articles/claude/2026-06-17 - Meet the winners of our Claude Opus 4.8 Build Day hackathon.md"]
last_updated: 2026-07-07
---

## Definition

Tekton is a winning project from [[Anthropic]]'s [[ClaudeOpus4.8]] Build Day hackathon (June 2026) that reconstructs historical buildings in 3D and traces every component back to a documented source. It was built by [[HollyTang]] and [[AustinBurgess]].

## Key Information

- **Purpose**: academic validation, restoration work, and cultural preservation — starting with Tang Dynasty architecture and the spire of Notre-Dame.
- **Input**: give Tekton a historical building, and [[Claude]] researches it, pulling together schematics, construction documents, photographs, and diagrams.
- **Output**: a 3D model assembled across 339 incremental construction states. Clicking any component shows where the detail came from and why it was placed there.
- **Evidence chain**: the core methodology — every model component traces back to a documented source, running from source material to verified model.
- **Verification**: ran entirely on [[ClaudeOpus4.8]]. Independent verifier sub-agents graded each reconstruction in isolated context windows, and self-correction loops rechecked component placement until all 20 tests passed. Every build was measured against the historical record and its citations.
- **Build approach**: the team mapped the project end-to-end before building — they created a full PRD and a Notion board with ~50 tickets, then broke the build into separate workflows and ran them in parallel.
- **Team**: [[HollyTang]] (designer) prototyped a single reconstruction on her own; [[AustinBurgess]] (founder of [[Pearl]]) scaled it to work on any building end-to-end. They met in line for coffee at a Code with Claude event a month earlier.
- **Future plans**: the team wants to make Tekton open source so museums, historians, nonprofits, and governments can build on it.

## Related

- [[summary-2026-06-17 - Meet the winners of our Claude Opus 4.8 Build Day hackathon]] — source summary
- [[ClaudeOpus4.8]] — the model used to build and verify Tekton
- [[EvidenceChain]] — the verification methodology Tekton uses
- [[HollyTang]] — co-creator (designer)
- [[AustinBurgess]] — co-creator (engineer, Pearl founder)
- [[Pearl]] — Austin Burgess's startup
- [[SimFrancisco]] — fellow winning hackathon project
- [[CustomUniverse]] — fellow winning hackathon project
