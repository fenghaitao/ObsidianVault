---
title: "Personal Digital Assistant"
type: concept
tags: [AI, agent, assistant, consumer, security]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We've passed the inflection point & dark factories are coming.md"]
last_updated: 2026-07-11
---

## Definition

A personal digital assistant is an AI agent that has access to your email, calendar, and other personal tools to take actions on your behalf. Simon Wilson argues that demand for this is "enormous" — demonstrated by the explosive growth of Open Claw — but the security challenges (the lethal trifecta) remain unsolved. The biggest opportunity in AI is building a safe version.

## Key Information

- "Everyone wants a digital assistant that can look after your email"
- The demand is "enormous" — demonstrated by Open Claw going from first line of code to Super Bowl ad in ~3.5 months, with hundreds of thousands of users setting it up despite complexity and security risks
- "The reason Open Claw took off is Anthropic and OpenAI could have built this and they didn't because they didn't know how to build it securely"
- "If you can build safe Open Claw, if you can deploy a version of Open Claw that does all the things people love about it and won't randomly leak people's data and delete their files, that's a huge opportunity"
- The generic term "claws" has emerged for this category (Open Claw, Nano Claw, etc.)
- Simon predicts "building your own claw" will be the new "Hello World" of AI engineering
- The lethal trifecta is the fundamental security challenge: access to private data, exposure to malicious instructions, and exfiltration capability
- Simon's personal approach: runs Open Claw in a Docker container, gave it read-only access to work email, got it its own email address — "that's the way to do it"
- The analogy: "Open Claw is basically a Tamagotchi... a digital pet, and you buy the Mac mini as an aquarium that your digital pet lives in"

## Related

- [[Open Claw]] — the canonical example
- [[Nano Claw]] — a variant
- [[Lethal Trifecta]] — the security challenge for personal digital assistants
- [[Simon Wilson]] — discussed this concept extensively
- [[summary-17 - An AI state of the union： We've passed the inflection point & dark factories are coming]] — source summary
