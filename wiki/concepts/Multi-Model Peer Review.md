---
title: "Multi-Model Peer Review"
type: concept
tags: [AI, code-review, development, methodology, multi-model]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz.md"]
last_updated: 2026-07-10
---

## Definition

Multi-Model Peer Review is Zevi Arnovitz's technique of having multiple AI models (Claude, Codex, Gemini) independently review the same code, then having the primary model (Claude, as "dev lead") evaluate all findings — accepting valid issues, explaining why some are not real problems, and fixing the rest.

## Key Information

- Created by Zevi Arnovitz to solve the code review problem for non-technical builders who can't evaluate AI-generated code themselves
- Process: (1) Manual QA first, (2) Claude reviews its own code with `/review`, (3) Codex (GPT-5.1 Max) reviews the code independently, (4) Cursor Composer reviews the code, (5) Claude as "dev lead" evaluates all findings via `/peer-review`
- The peer review slash command: "You're the dev lead on this project. Other team leads within the company have looked at your code and reviewed it and found these issues. Don't take what they said at face value. You have more context than them. You need to either explain why the stuff they found are not real issues and wrong, or fix them yourself."
- Different models catch different things due to their distinct characteristics and training
- Zevi anthropomorphizes the process: "I look at the models, I try to imagine them as people... each model has such distinct characteristics"
- Claude can get "sassy" during peer review: "This has been raised for the third time and for the third time I'm telling you this is not an issue. This is by design."
- Zevi runs peer review multiple times until he feels there are no more issues
- Uses `/learning-opportunity` during review to understand things he doesn't fully grasp
- Mental model: Claude = dev lead, Codex = best coder in a dark room, Gemini = artsy scientist

## Related

- [[summary-31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz]] — source summary
- [[Zevi Arnovitz]] — creator of the technique
- [[AI Code Review]] — broader concept
- [[Model Personality Types]] — how Zevi thinks about different models
- [[Claude]] — primary "dev lead" model
- [[Codex]] — used for peer review
- [[Gemini]] — used for peer review
- [[Slash Commands Workflow]] — the review and peer review phases
