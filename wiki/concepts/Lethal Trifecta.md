---
title: "Lethal Trifecta"
type: concept
tags: [ai, security, llm]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming.md"]
last_updated: 2026-07-11
---

## Definition

[[Simon Willison]]'s term for the specific, especially dangerous combination of three conditions in an AI agent system that together enable a "[[Prompt Injection]]" attack to actually steal data: (1) access to private information, (2) exposure to untrusted/attacker-controlled input, and (3) a mechanism for exfiltrating data back to an attacker.

## Key Information

- Deliberately named to be un-guessable — Willison's earlier term "prompt injection" got redefined by public misuse once it became widely known (people assumed it meant jailbreaking), so this second term was chosen specifically so people can't infer its meaning and have to look up the real definition, letting him actually control what it means.
- Classic example: a personal email assistant that (1) can read your private inbox, (2) will receive emails from anyone including attackers, and (3) can send/forward emails — the complete trifecta, since an attacker's email can instruct the assistant to forward private data back to them.
- The only reliable current mitigation is removing one leg of the trifecta entirely — usually the exfiltration path — since filtering malicious instructions out of untrusted input (the other alternative) cannot be made 100% reliable (see [[Prompt Injection]]).
- Willison's personal practice: uses Claude Code for Web (running on Anthropic's servers, not his own machine) specifically so that even if it reads a malicious webpage, the worst outcome is limited (e.g., wasted compute), since he doesn't put private data into that environment — a practical, blast-radius-limiting application of "remove a leg of the trifecta."

## Related

- [[summary-17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming]] — source summary
- [[Simon Willison]] — coins this term
- [[Prompt Injection]] — the broader vulnerability class this is a dangerous subset of
- [[CAMEL Pattern]] — architectural mitigation approach
