---
title: "Hardware Compile Cycle"
type: concept
tags: [hardware, engineering, product-development]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/09 - Why the next AI boom is physical AI ｜ Caitlin Kalinowski (ex-OpenAI, Meta, Apple).md"]
last_updated: 2026-07-11
---

## Definition

The long feedback loop of hardware development — where late-stage changes (unlike a quick software recompile) require rebuilding physical tooling, prototypes, and validation cycles — illustrated by [[Quest 2]]'s camera-count reduction causing a costly late-stage spec mismatch.

## Key Information

- Quest 2 case study: reducing camera count from 5 to 4 for cost, discovered at EVT (Engineering Validation Test), caused a tolerance-spec mismatch between the mechanical and computer-vision teams that could have slipped the ship date. It was fixed via an architectural redesign (locking two cameras to a shared steel bracket as a fixed baseline) without missing the deadline.
- [[Caitlin Kalinowski]] considers this one of her favorite failures because the resulting design ended up better than the original plan — illustrating how hardware teams must absorb the cost of a long compile cycle by catching and creatively resolving issues within a fixed schedule, unlike software's near-instant iteration.

## Related

- [[summary-09 - Why the next AI boom is physical AI ｜ Caitlin Kalinowski (ex-OpenAI, Meta, Apple)]] — source summary
- [[Quest 2]] — case study illustrating this concept
- [[Caitlin Kalinowski]] — recounts the story
