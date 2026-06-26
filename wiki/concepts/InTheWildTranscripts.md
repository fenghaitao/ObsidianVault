---
title: "InTheWildTranscripts"
type: concept
tags: [evaluation, ai-capabilities, data-source, agents]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260119 - How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR.md"]
last_updated: 2026-06-26
---

## Definition
In-the-Wild Transcripts are the traces and logs left behind by AI agents operating in real production environments (Cursor, Codex, etc.), proposed by Joel Becker as an alternative evidence source for measuring AI capabilities with different pros and cons than benchmarks or RCTs.

## Key Information
- Agents in tools like Cursor and Codex leave behind traces of their actions, reasoning chains, and contributions to code
- These transcripts capture "whatever real crap shows up in the wild" rather than neatly packaged benchmark tasks
- Advantages: enormous data volume, more representative of real-world usage, captures messy real-world complexity
- Disadvantages: not experimental (observational data), hard to know exactly what to make of it, selection bias in what gets recorded
- Represents a third evidence source in Becker's triangulation strategy alongside benchmarks and RCTs
- The data "is enormous perhaps" — the scale could enable insights not possible with small controlled studies
- Complements other sources by having different failure modes and biases

## Related
- [[summary-20260119 - How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR]] — source
- [[CapabilityExtrapolation]] — triangulation framework this fits into
- [[Cursor]] — one source of in-the-wild transcripts
- [[FuzzyGoalCompletion]] — complementary evidence source
- [[JoelBecker]] — proposed this evidence source
