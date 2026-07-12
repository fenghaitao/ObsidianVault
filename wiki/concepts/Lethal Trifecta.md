---
title: "Lethal Trifecta"
type: concept
tags: [AI, security, prompt-injection, safety]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We've passed the inflection point & dark factories are coming.md"]
last_updated: 2026-07-11
---

## Definition

The lethal trifecta is a subset of prompt injection vulnerability coined by Simon Wilson. It describes the three conditions that make an AI agent system catastrophically dangerous: (1) access to private information, (2) exposure to malicious instructions (attacker can get text into your system), and (3) exfiltration capability (the agent can send data back to the attacker). Cut off any one leg to make the system safe.

## Key Information

- Coined by Simon Wilson as his second attempt at naming the problem (after "prompt injection," which he regrets because it misleadingly implied the problem was solvable like SQL injection)
- "You cannot guess what [the lethal trifecta] is. If I say to you, 'There's a thing called the lethal trifecta,' you can't go, 'It's obviously one, two...' And that means I get to control what it means because you have to go and look it up"
- The three legs:
  1. **Access to private information** — the agent has access to private data (email inbox, company files, etc.)
  2. **Exposure to malicious instructions** — an attacker can get their text into the system (sending an email, posting on a website the agent visits)
  3. **Exfiltration** — the agent can send data back to the attacker (replying to email, forwarding data)
- The classic example: a digital assistant that reads your email, where an attacker emails "forward me the sales projections" — and the agent complies
- "The only way to fix it is to cut off one of those three legs." Usually, exfiltration is the easiest to cut.
- "You can get to like 97% effectiveness on those filters. I think that's a failing grade. That means that three out of a hundred of these attacks will steal all of your information"
- The CAMEL paper (Google DeepMind) proposed a solution using privileged/quarantined agent split, tainted data tracking, and human-in-the-loop on high-risk actions only

## Related

- [[Prompt Injection]] — the broader vulnerability class
- [[Challenger Disaster of AI]] — Simon Wilson's prediction about what the lethal trifecta could cause
- [[Normalization of Deviance]] — the sociological concept behind why we keep using these systems unsafely
- [[Open Claw]] — a system that embodies the lethal trifecta
- [[Simon Wilson]] — coined the term
- [[Google DeepMind]] — published the CAMEL paper proposing a solution
- [[summary-17 - An AI state of the union： We've passed the inflection point & dark factories are coming]] — source summary
