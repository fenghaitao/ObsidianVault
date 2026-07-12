---
title: "Red/Green TDD"
type: concept
tags: [software-engineering, testing, AI, coding, agentic-engineering]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We've passed the inflection point & dark factories are coming.md"]
last_updated: 2026-07-11
---

## Definition

Red/Green TDD (Test-Driven Development) is a concise prompt pattern for AI coding agents. By using the jargon phrase "red/green TDD" instead of lengthy instructions, engineers can tell AI agents to: write the test first, run it and watch it fail (red), implement the code, then run the test and watch it pass (green). This is a key agentic engineering pattern recommended by Simon Wilson.

## Key Information

- A key agentic engineering pattern from Simon Wilson's blog/book
- The phrase "red/green TDD" is programming jargon that AI agents understand — it reduces a lengthy paragraph of instructions to a few words
- "If you use the term red/green TDD, that's programming jargon which I didn't used to use, but it is jargon for run the test and watch them fail. The agents know what that means"
- Why it works: agents are less likely to forget to test something or add unnecessary code when they write tests first
- Simon hated doing TDD as a human ("It just slowed me down and frustrated me"), but "I don't care if [the agents] are bored. If you get them to write the test first, you do get better results"
- Tests compound over time, giving confidence that new features won't break old ones
- Simon's tolerance for verbose tests has increased because "updating 1,000 lines of tests is now the job of the coding agent"
- "The most important thing when you're working with coding agents is they have to test the code. If they haven't run the code, you're back to copying and pasting out of ChatGPT and crossing your fingers"

## Related

- [[Agentic Engineering]] — the broader practice this pattern belongs to
- [[Hoarding Things You Know How to Do]] — another agentic engineering pattern
- [[Simon Wilson]] — recommends this pattern
- [[summary-17 - An AI state of the union： We've passed the inflection point & dark factories are coming]] — source summary
