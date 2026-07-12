---
title: "Google DeepMind"
type: entity
tags: [company, AI, Google, research]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We've passed the inflection point & dark factories are coming.md"]
last_updated: 2026-07-11
---

## Definition

Google DeepMind is Google's AI research lab, responsible for the Gemini model family. Simon Wilson references their CAMEL paper, which proposed a solution for building safe AI agents that can handle prompt injection by splitting the agent into privileged and quarantined components.

## Key Information

- Google's AI research lab behind the Gemini models
- Published the CAMEL paper, proposing a mechanism for safe AI agents:
  - Split the agent into a privileged agent (can do interesting things) and a quarantined agent (exposed to malicious instructions, but can't do anything useful)
  - The privileged agent writes code for the quarantined agent to execute
  - Tainted data is tracked; when a potentially dangerous instruction enters, the human must approve the next action
  - Human-in-the-loop is filtered to only high-risk activities, not constant approval
- Simon Wilson: "There are paths forward. They're very complicated. I've not seen good implementations of them just yet"
- Sander Schulhoff also recommended the CAMEL approach as the best solution to prompt injection

## Related

- [[Google]] — parent company
- [[Gemini 3.1]] — their latest model
- [[Prompt Injection]] — the security problem the CAMEL paper addresses
- [[Lethal Trifecta]] — the subset of prompt injection the CAMEL approach helps with
- [[summary-17 - An AI state of the union： We've passed the inflection point & dark factories are coming]] — source summary
