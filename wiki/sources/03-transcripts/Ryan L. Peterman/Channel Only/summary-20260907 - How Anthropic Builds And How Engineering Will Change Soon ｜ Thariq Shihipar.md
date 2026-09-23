---
title: "summary-20260907 - How Anthropic Builds And How Engineering Will Change Soon ｜ Thariq Shihipar"
type: source
tags: [source, original-material]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260907 - How Anthropic Builds And How Engineering Will Change Soon ｜ Thariq Shihipar.md"]
last_updated: 2026-09-23
---

## Core Summary

Anthropic engineer Thariq Shihipar (Claude Code team) explains how Anthropic extracts more from frontier models than the rest of the industry: treat Claude as a thought partner, invest as heavily in the "harness" (auto mode, sandboxing, artifacts, workflows) as in the model itself, and keep moving up a level of abstraction to orchestrate systems and loops instead of doing individual tasks. He argues that "coding is largely solved" only in the sense that software no longer gets stuck the way it used to, freeing engineers to do unique work while technical taste, context-building, and verification become more valuable. The conversation spans loop engineering, artifacts, the model-vs-harness relationship, computer use limits, knowledge work reduced to code, code maintenance under AI, and career advice about expanding your luck surface area.

## Key Points

- Treat Claude as a thought partner: start from "Can Claude do it? If not, why not?" and constantly ask whether you can move up an abstraction level — build the system that builds the system, not just the product.
- Onboarding buddies are still needed, but for social and cultural reasons rather than technical lift; Claude now covers most setup questions.
- The internal-external perception gap comes from culture: Anthropic treats "living in the future" as the job and is willing to spend a day automating something even if it fails, because a failure reveals "Claude is not good at this — how do we make it better?"
- The harness matters as much as the model; counterintuitively, as models improve the harness must get *more* complicated (auto mode classifier, sandboxing, workflows, artifacts) to unlock more behavior.
- Auto mode is a classifier that replaces manual permission prompts so Claude can run for hours safely; artifacts are a way for Claude to represent work it has done (and are themselves a form of prompting).
- "Harness engineering is a mix of science and art… very unintuitive," and it has ironically gotten harder to "vibe code" your own harness even as models improved.
- Anthropic's aim is for Claude to absorb the "glue work" (e.g., turning a designer's Figma file into code) so humans spend time on unique work; there is a ton of demand for unique thinking.
- "Claude Code is really good at the implementation of code, and Claude Tag is for the rest of the software development life cycle" — feedback, code review, CI/CD, incidents.
- Loop engineering: instead of prompting Claude directly, set up a system that prompts Claude; done well it needs good verification, skills, and data sources, and can autonomously run parts of an engineering job.
- "Hey Claude, here's the ticket, don't tell me till you're done" only works for a complete spec; the real work is figuring out what you actually want and what the unknowns are, not iterating on a one-line prompt forever.
- Most knowledge work is reducible to code: Thariq does accounting in Python instead of Excel and video editing via FFmpeg/scripts.
- Prompting is more than the literal prompt — it includes skills, data, and accumulated context; each model is "its own almost organic digital thing" whose quirks you learn and then unlearn (Anthropic removed ~80% of Claude Code's system prompt, and examples are now mostly negative).
- Models default to the average user's fast response; give them explicit permission to spend compute, use subagents/workflows, or "don't do work yet — brainstorm with me" ("believe in yourself" really means permission to use compute).
- Artifacts are Claude uploading an interactive web app/interface — they can call MCPs (e.g., read your inbox) and show coding plans with diagrams, snippets, and schemas; they are becoming a primary way to read and interact with Claude.
- For taste/subjective work, stay in the loop and give references with data: an HTML file beats a screenshot, and a Figma file beats a raster image; becoming a high-taste domain expert is what gets good output.
- On writing: routine data readouts and update posts increasingly go to AI (human-reviewed), while novel thought and internal essays stay human-written; disclose your prompts, and treat "prompt blame" as a missing form of git blame.
- Code maintenance is being redefined: naming/style matter less; verification harnesses, skills (e.g., simplify), and ~100x more test code (fixtures, mock databases, Storybook) matter more; consider wholesale rewrites as models improve.
- Higher code velocity raises incidents/SEVs; counter with replay-and-mock testing, chaos engineering, and a dream testing/deployment environment.
- Computer/browser use is improving (Opus 5) but runs into UX edge cases (one password, latency) and is a state machine where you don't control all the state; APIs and MCPs absorb many use cases.
- Share your work publicly to expand your luck surface area: Thariq's Anthropic role came from a Good Fire interpretability project he posted on Twitter (~500 likes), leading to DMs and an intro.
- Still learn to code: being technical (computers, programs, languages, memory, caches) remains essential; "coding is solved" just means software works far more often and can now be applied everywhere.

## Related

- [[Thariq Shihipar]]
- [[Anthropic]]
- [[Claude Code]]
- [[Claude]]
- [[Claude Tag]]
- [[Good Fire]]
- [[AI and Software Engineering]]
- [[Agentic AI]]
- [[Harness Engineering]]
- [[Loop Engineering]]
- [[Context Engineering]]
- [[Prompt Engineering]]
- [[Knowledge Work as Code]]
- [[Vibe Coding]]
- [[Luck Surface Area]]
- [[Ryan L. Peterman]]
