---
title: "Dreaming (Agents)"
type: concept
tags: [ai, agents, memory, learning]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - State of the Claw — Peter Steinberger.md"]
last_updated: 2026-06-26
---

## Definition
Dreaming is a memory reconciliation feature for AI agents that processes session logs to convert local memories into long-term storage and drop irrelevant ones, analogous to how human brains consolidate memories during sleep.

## Key Information
- Peter Steinberger wanted to work on dreaming for OpenClaw but his maintainers built it while he was busy with other responsibilities
- The feature "reconciles memories and creates a dream log going through session logs"
- Analogy: how humans learn — experience during the day, sleep does garbage collection, converts local memories to long-term storage, drops others
- The first step of dreaming has been shipped in OpenClaw
- Anthropic is also working on a similar concept (per their source code leak)
- Peter: "I'm pretty sure there's more companies working on that"
- Related to the wiki/memory concept Andrej Karpathy has discussed — "wiki is more memory but everything kind of blends a little bit together"
- Part of OpenClaw's extensible architecture: dreaming is one of many plugins users can add or replace

## Related
- [[summary-20260417 - State of the Claw — Peter Steinberger]] — source
- [[OpenClaw]] — project with dreaming feature
- [[PeterSteinberger]] — conceived the feature
- [[AndrejKarpathy]] — discussed related wiki/memory concepts
- [[Anthropic]] — also working on dreaming
- [[Agent Memory]] — broader concept
