---
title: "Red-Green TDD"
type: concept
tags: [software-engineering, testing, ai, agentic-engineering]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming.md"]
last_updated: 2026-07-11
---

## Definition

[[Simon Willison]]'s recommended compact prompt/instruction for coding agents: tell the agent to use "red/green TDD" — write a failing test first (red), confirm it fails, then write the implementation and confirm the test passes (green) — a classic test-driven-development discipline that Willison personally dislikes writing by hand but finds highly effective when delegated to an agent.

## Key Information

- Willison tried red-green TDD as a human practice for years and found it slowed him down and didn't fit his exploratory style — but coding agents, unlike him, "don't get bored," and reliably produce better results when forced through the discipline (less likely to forget edge cases or add unnecessary code).
- The specific value of naming it "red/green TDD" rather than spelling out the full instruction: it's programming jargon coding agents already understand, so a 5-second phrase reliably triggers correct, disciplined behavior that would otherwise require a lengthy prompt.
- Broader case for automated tests with agents: tests are cheap proof the agent actually ran the code (catching at least syntax-level failures), and accumulate over time into a regression safety net, letting an agent change one feature without silently breaking others.
- Willison explicitly pushes back on teams that drop automated testing entirely in the name of speed, arguing tests make agent-assisted development faster, not slower, once you account for avoided regressions.
- Notes that verbose, over-extensive test suites — historically a design smell, since maintaining thousands of lines of tests was expensive — are now much less costly, since updating tests is itself delegable to the coding agent.

## Related

- [[summary-17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming]] — source summary
- [[Simon Willison]] — recommends and practices this technique
- [[Agentic Engineering]] — broader discipline this technique supports
