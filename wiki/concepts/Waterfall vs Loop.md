---
title: "Waterfall vs Loop"
type: concept
tags: [ai, agents, methodology, planning, waterfall, agile]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick.md"]
last_updated: 2026-06-29
---

## Definition
Waterfall vs Loop contrasts two approaches to AI-driven development: pre-computing all dependencies and specifications upfront (waterfall) versus letting the AI figure out the next most important task on the fly in a continuous loop. Chris Parsons argues that waterfall approaches fail with AI just as they failed with humans.

## Key Information
- Chris Parsons tried the waterfall approach: had AI break a big project into tickets, break those into smaller tickets, compute all dependencies, then orchestrate 6-7 parallel agents
- Result: "It just failed horribly" — agents collided on shared tickets, duplicated work, produced a mess
- Parsons realized he had "recreated the waterfall processes that were seen in some of the worst companies back in the '90s"
- The loop approach: just say "pick the next most important ticket" — AI figures out dependencies on the fly based on what's just been done
- "If humans can't do that, how was AI supposed to do any better?"
- Parsons extends this concern to spec-driven development: worries it risks recreating waterfall by over-specifying projects upfront
- Advocates for just-in-time specs and iterative loop-based development instead
- The loop approach is simpler, more robust, and produces better results

## Related
- [[Ralph Loop]] — the loop approach
- [[ChrisParsons]] — discussed in his workshop
- [[SpecificationDrivenDevelopment]] — the approach he critiques
- [[Just-in-Time Specs]] — his preferred alternative
- [[Theory of Constraints]] — why parallelism often isn't the answer
- [[summary-20260504 - Ralph Loops： Build Dumb AI Loops That Ship — Chris Parsons, Cherrypick]] — source transcript
