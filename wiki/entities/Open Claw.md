---
title: "Open Claw"
type: entity
tags: [product, tool, ai-agent, personal-agent, harness]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/08 - AI predictions： Job markets, Codex beats Claude, and the death of org charts ｜ Dan Shipper.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/13 - How Anthropic’s product team moves faster than anyone else ｜ Cat Wu (Head of Product, Claude Code).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming.md"]
last_updated: 2026-07-11
---

## Definition

"Open Claw" (as transcribed — likely an auto-transcription rendering of a real personal-AI-agent harness product name; treated here as named in the source) is a self-hosted personal AI agent harness that [[Dan Shipper]] and [[Every]] adopted early and broadly, and which Dan cites as the pivotal experience behind his flip from expecting "everyone has their own agent" to predicting a single shared company "super agent" instead.

## Key Information

- Requires real setup/maintenance effort (e.g., SSHing into a server), breaks frequently, and needs ongoing "gardening" — Dan Shipper's central illustration of "[[Automation Is A Lie|automation is a lie]]": in order for an agent like this to stay useful, it needs a human who personally cares about and maintains it; the moment that human connection is severed, the agent stops being useful.
- Everyone at Every adopted it when it first came out; Dan was initially convinced this personal-agent model ("a parallel a parallel org chart," each agent a small reflection of its owner — he compares it to a daemon from *The Golden Compass*) was the future, then completely reversed his view once he saw how much upkeep it demanded from ordinary (non-technical) users.
- Every separately built and offered a hosted version of an Open-Claw-like product (on a waitlist, later paused/limited) — described as "a very hard agent harness to make work" because the underlying tooling moves so fast that things break in ways that are hard for a hosting platform to fix.
- Referenced again in the lightning round alongside [[Hermes]] as options for people who want to try a personal/agent-harness product, with lighter-weight alternatives mentioned for less technical users.
- Per [[Cat Wu]] (episode 13): Anthropic restricted using Claude subscriptions with third-party harnesses like Open Claw, since Claude's harness/token efficiency work was designed for first-party usage patterns rather than the different demand profile of third-party products. Framed as a hard trade-off under infrastructure scaling pressure — Anthropic offered transition credits alongside subscriptions but had to prioritize first-party products and the API, which caused real frustration in the open-source community.
- Per [[Simon Willison]] (episode 17): its first line of code was written November 25; by the following Super Bowl (~3.5 months later) it had inspired a (vaporware) white-labeled hosting-provider Super Bowl ad — an unusually fast rise Willison says he's never seen matched. Over 1,000 people had contributed code to it by the time of this episode.
- Willison argues Open Claw's success demonstrates enormous latent demand for a personal AI assistant: Anthropic and OpenAI could plausibly have built something similar, but hadn't, specifically because they didn't know how to do it securely — leaving the opportunity open for an independent third party willing to accept the security risk.
- It is, per Willison, "almost exactly" the architecture he warns against as a security researcher — a personal assistant with broad access to private data (email, accounts) and the ability to take real-world actions — and has already caused real harm (reported cases of people losing cryptocurrency wallets). He credits Claude Opus's built-in tendency to often (not always) refuse unsafe instructions with preventing worse outcomes so far.
- Willison's personal setup: runs his own instance in a sandboxed Docker container on a dedicated Mac mini (bought specifically for this purpose — likened by a friend to "buying an aquarium for your digital pet/Tamagotchi"), with only read-only access to his work email specifically to limit blast radius.
- Popularized "claws" as a generic term for this whole category of personal-agent-harness products (e.g., "Nano Claw" and others following Open Claw's example) — Willison predicts "build your own claw" will become the new introductory/"Hello World" project for AI engineering, and plans to build one himself.
- The "claw" naming is linked (per Lenny) to the AI-controlled mechanical claws wielded by the villain Doctor Octopus in *Spider-Man 2* — claws that act autonomously once their inhibitor chip fails, an analogy both Lenny and Willison find fitting.

## Related

- [[summary-08 - AI predictions： Job markets, Codex beats Claude, and the death of org charts ｜ Dan Shipper]] — source summary
- [[summary-13 - How Anthropic’s product team moves faster than anyone else ｜ Cat Wu (Head of Product, Claude Code)]] — source summary
- [[summary-17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming]] — source summary
- [[Dan Shipper]] — early adopter who reversed his view on personal agents because of this product
- [[Every]] — company that adopted it broadly and built a hosted variant
- [[Automation Is A Lie]] — core thesis this product's fragility illustrates
- [[Parallel Org Chart]] — the "everyone has their own agent" model this product originally represented
- [[Forward Deployed Engineer]] — role that emerged partly to solve the maintenance burden this product exposed
- [[Cat Wu]] — discusses Anthropic's token-access decision affecting this product
- [[Anthropic]] — restricted first-party token access for this and similar harnesses
- [[Simon Willison]] — extensive commentary on its rise, security risk, and his own sandboxed setup
- [[Lethal Trifecta]] / [[Prompt Injection]] — security risk category this product exemplifies
- [[CAMEL Pattern]] — proposed mitigation that could make products like this safer
