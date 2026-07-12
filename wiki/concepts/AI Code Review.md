---
title: "AI Code Review"
type: concept
tags: [AI, coding, software-development, code-review]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/39 - Inside OpenAI： 2026 is the year of agents, AI's biggest bottleneck, and why compute isn't the issue.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz.md"]
last_updated: 2026-07-10
---

## Definition

AI code review is the use of AI agents to review code, catch mistakes, and validate changes. As AI writes more code, code review becomes a critical bottleneck and an area of active product development.

## Key Information

- Alexander Imbiricos identifies that writing code is one of the most fun parts of software engineering, but reviewing AI-written code is less fun — creating a product challenge
- The Codex team is actively building code review features that help users gain confidence in AI-written code
- Codex is already used for code review internally at OpenAI, catching "pretty interesting configuration mistakes"
- Codex is being used for its own training runs: reviewing training infrastructure code and catching errors
- The team is working on making agents better able to validate their own work, reducing the human review burden
- The UX question: when showing results, should you show the diff first or the image preview of what the code produced? The answer depends on the context and whether AI has already reviewed it
- At OpenAI, the code review workload is growing as Codex enables more code to be written faster
- The long-term vision is that agents validate their own work, with humans only reviewing when necessary
- [[Kiti Bottom]] (Codex team) notes that Codex's code review product has been "gaining extreme amount of traction" and catching many bugs both at OpenAI and with external customers
- When deploying new model changes to code review, they AB test to identify whether it finds the right mistakes and how users react — if users get annoyed, they switch off the product entirely
- Zevi Arnovitz pioneered a multi-model peer review approach for non-technical builders: have Claude, Codex, and Gemini each review code independently, then have Claude as "dev lead" evaluate all findings
- Zevi's review process: manual QA → Claude self-review → Codex review → Cursor Composer review → peer review (Claude evaluates all findings)
- Zevi: "It's very difficult for me to catch mistakes. So my review process has gone through a bunch of iterations to really be as good as possible."
- The peer review slash command treats Claude as the dev lead and other models as "other team leads within the company" who reviewed the code
- Claude can get "sassy" during peer review, pushing back: "This has been raised for the third time and for the third time I'm telling you this is not an issue. This is by design."

## Related

- [[Codex]] — product building AI code review features
- [[Human Typing Speed Bottleneck]] — the broader bottleneck
- [[summary-39 - Inside OpenAI： 2026 is the year of agents, AI's biggest bottleneck, and why compute isn't the issue]] — source summary
- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]] — additional source
- [[summary-31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz]] — source summary
- [[Multi-Model Peer Review]] — Zevi's approach to AI code review
- [[Zevi Arnovitz]] — non-technical PM who pioneered multi-model review
