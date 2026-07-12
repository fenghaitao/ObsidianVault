---
title: "Sorcerer's Apprentice Problem (AI)"
type: concept
tags: [AI, agents, risk, metaphor, coding]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/26 - OpenAI's head of platform engineering on the next 12-24 months of AI ｜ Sherwin Wu.md"]
last_updated: 2026-07-10
---

## Definition

The "Sorcerer's Apprentice Problem" is Sherwin Wu's metaphor for the risk of AI agents running wild when insufficiently supervised. Drawing from the Fantasia segment where Mickey Mouse sets enchanted brooms to work and falls asleep, the analogy captures both the extreme power and the danger of AI coding agents: they are incredibly high-leverage, but you need to know what you're doing and supervise them, or the "brooms go crazy and everything's flooding."

## Key Information

- From Disney's Fantasia (1940): Mickey Mouse finds the sorcerer's hat, casts a spell to make brooms do his chores, falls asleep, and the brooms flood the workshop. The old sorcerer returns to clean everything up.
- Sherwin uses this as the perfect analogy for AI coding (vibe coding)
- The power: "it's just really powerful now, these incantations you can do are extremely high leverage"
- The risk: "you kind of have to know what you're doing... you want to make sure that the models aren't going off the rails"
- The seniority factor: "there is some skill and some seniority and a lot of thought that needs to go into this"
- Extends the SICP "wizard book" metaphor: programming has always been like sorcery, but AI makes it "literally incantations"
- The balancing act: you don't want to "completely go away and ignore the thing" but you also don't want to micromanage
- The circular trust problem: Codex reviewing its own code creates a potential Sorcerer's Apprentice scenario — you need to be thoughtful about which PRs are fully automated
- The metaphor also applies to the 100% Codex codebase experiment: the team has no escape hatch, so they must learn to "steer the brooms" through better context and documentation

## Related

- [[SICP]] — the "wizard book" that originated the sorcery metaphor
- [[Fantasia]] — the source of the Sorcerer's Apprentice segment
- [[Vibe Coding]] — the practice this metaphor warns about
- [[Multi-Hour Coherent AI Tasks]] — the risk scales with task duration
- [[Sherwin Wu]] — coined the analogy
- [[summary-26 - OpenAI's head of platform engineering on the next 12-24 months of AI ｜ Sherwin Wu]] — source summary
