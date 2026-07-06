---
title: "CrossBeam"
type: entity
tags: [hackathon, claude-code, housing, government-tech, permitting]
sources: [raw/01-articles/claude/2026-04-20 - Meet the winners of our Built with Opus 4.6 Claude Code hackathon.md]
last_updated: 2026-07-04
---

## Definition

CrossBeam is an AI tool built by personal injury lawyer Mike Brown, winner of Anthropic's "Built with Opus 4.6" Claude Code hackathon, that helps break California's housing-permit bottleneck — California's permit process has a 90%+ first-submission rejection rate and an average six-month delay costing homeowners $30,000, typically due to bureaucratic issues like missing signatures or incorrect code citations rather than substantive problems.

## Key Information

- Builders drag and drop blueprints and correction letters into the tool; parallel Claude sub-agents parse the documents, build a spatial index, and assign targeted agents to each discrete correction, producing a precise action plan for approval in about 20 minutes.
- Also serves municipalities: lets administrators batch-process submitted permits and generate draft correction letters automatically.
- Buena Park, a Southern California city needing to permit 8,900+ housing units by 2029 (only ~120 permitted in 2024), is evaluating adoption for both builders and administrators.
- Built entirely by prompting [[ClaudeCode]] and having Claude write its own tests; Brown, a non-developer, says he "didn't write a single line of code" and "didn't even read a line of code."
- Source code: github.com/mikeOnBreeze/cc-crossbeam.

## Related

- [[summary-2026-04-20 - Meet the winners of our Built with Opus 4.6 Claude Code hackathon]] — source summary
- [[ClaudeCode]] — tool used to build CrossBeam
