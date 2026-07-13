---
title: "CAMEL Pattern"
type: concept
tags: [ai, security, agents, architecture]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md"]
last_updated: 2026-07-12
---

## Definition

Architectural approach to mitigating "[[Prompt Injection]]"/"[[Lethal Trifecta]]" risk, proposed in a Google DeepMind paper and cited by [[Simon Willison]] as the most credible partial mitigation he's seen: split an AI agent into a privileged agent (which the trusted user talks to and which can take meaningful actions) and a quarantined agent (which is exposed to untrusted/malicious input but cannot itself take consequential actions).

## Key Information

- Mechanism: the privileged agent writes out a plan/code describing the sequence of steps to take; that plan is executed in an environment that tracks which data is "tainted" (i.e., touched by untrusted input) — once a potentially dangerous, taint-linked action is reached, the human is asked to explicitly approve just that step, rather than being asked to approve everything.
- Addresses the core failure mode of naive human-in-the-loop safeguards: if a human is asked to click "approve" constantly, they habituate and start approving everything reflexively — filtering approval requests down to only genuinely high-risk, tainted actions makes human oversight meaningful again.
- Willison hasn't seen a good production implementation of this pattern yet as of the episode, but considers it one of the few credible paths forward for building a personal-assistant-style agent (like [[Open Claw]]) that could be used safely.
- Per [[Sander Schulhoff]] (episode 37): CAMEL works by restricting an agent's *permissions* up front based on what the user's specific request actually requires, rather than filtering/classifying inputs and outputs after the fact. Example: a request to "write and send an email wishing my head of ops happy holidays" needs only write/send permissions, not read access to the inbox — so CAMEL would grant only those, blocking any injected instruction from a different source that tries to exploit read access that was never granted. Schulhoff calls it "great" and "low downside" but notes it can require re-architecting a system to implement, and — critically — it breaks down whenever a single legitimate request needs both read *and* write access at once (e.g., "read my recent emails and forward any ops requests to my head of ops"), since CAMEL then has no way to avoid granting both permissions together, which is enough for an indirect prompt injection to succeed.

## Related

- [[summary-17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming]] — source summary
- [[summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO]] — source summary
- [[Simon Willison]] — cites and endorses this pattern
- [[Prompt Injection]] / [[Lethal Trifecta]] — the vulnerability this pattern mitigates
- [[Open Claw]] — the kind of product this pattern could make safer
- [[Sander Schulhoff]] — details CAMEL's mechanism and its read/write-combined limitation
- [[Guardrails Do Not Work]] — contrasted approach (input/output filtering) that Schulhoff argues fails
