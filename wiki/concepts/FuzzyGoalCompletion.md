---
title: "FuzzyGoalCompletion"
type: concept
tags: [evaluation, ai-capabilities, agents, real-world-tasks]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260119 - How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR.md"]
last_updated: 2026-06-26
---

## Definition
Fuzzy Goal Completion is an evaluation approach where AI agents attempt to accomplish real-world objectives that are not clearly specified or neatly packaged, in contrast to benchmark-style tasks with well-defined success criteria.

## Key Information
- Inspired by AI Village, where agents attempt tasks like organizing events, running experiments, or operating a merch store
- Tasks are "fuzzy goals" rather than clearly specified benchmark problems
- Current results: "basically all the time the models fall on their faces and suck"
- Joel Becker proposes adapting this approach: make it text-only (not computer use), provide relevant text-based tools, optimize elicitation, remove less performant models, and qualitatively study where models fail
- Interest is in understanding failure modes: do models become incoherent? Enter "strange psychological basins" with other models? Fail to interact with external services? Mismanage resources?
- Represents a fourth evidence source in Becker's triangulation strategy
- Particularly relevant for understanding why AIs cannot currently automate R&D, which requires flexible handling of ill-defined real-world problems

## Related
- [[summary-20260119 - How METR measures Long Tasks and Experienced Open Source Dev Productivity - Joel Becker, METR]] — source
- [[AgentVillage]] — project that inspired this approach
- [[CapabilityExtrapolation]] — triangulation framework this fits into
- [[ComputerUseVsCLI]] — limitation Becker wants to address
- [[NeurodivergentAI]] — analogy for why models struggle with fuzzy goals
- [[JoelBecker]] — proposed adapting this approach
