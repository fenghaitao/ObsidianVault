---
title: "summary-31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz"
type: source
tags: [source, original-material, vibe-coding, ai, product-management]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz.md"]
last_updated: 2026-07-11
---

## Core Summary

[[Lenny Rachitsky]] interviews [[Zevi Arnovitz]], a PM at [[Meta]] (previously at [[Wix]]) with zero technical background, who has spent the past year building and shipping real products — including his own side business, [[Studymate]] — entirely by directing AI coding agents rather than writing code himself. The episode is a live, hands-on screen-share walkthrough of his personal "[[Slash Command Development Workflow]]": a chain of custom slash commands (create issue → exploration → plan → execute → review → peer review → update docs) built around treating an AI agent as a persona — first a [[CTO Persona Pattern|"CTO" living inside a ChatGPT project]], later folded directly into [[Claude Code]] running inside [[Cursor]]. He demonstrates building a real feature live, describes a distinctive practice of [[Multi-Model Peer Review|having multiple AI models peer-review each other's code]] (each personified with a distinct "personality"), and lays out a recommended [[Exposure Therapy Onboarding|gradual onboarding path]] for non-technical people intimidated by code. Beyond the technical workflow, Zevi discusses using AI to prep for (and land) his Meta PM interview, argues against the idea that AI-assisted work is "outsourcing your thinking," and reframes the anxiety around junior roles: this is, in his view, the best time in history to be a junior builder.

## Key Points

- **The CTO persona**: early on, Zevi created a ChatGPT project prompted to act as a non-sycophantic, opinionated "complete technical owner" of his projects — explicitly countering ChatGPT's tendency toward people-pleasing (illustrated by an anecdote where it falsely agreed his Bun JavaScript question was "the same" as an unrelated framework, then admitted "I thought you were just making this up and I was riffing with you"). As coding tools improved, this persona folded directly into [[Claude Code]] via a project `claude.md` file, since the same agent could now both explore and execute. See [[CTO Persona Pattern]].
- **The six-stage slash-command workflow**: (1) create issue (quickly captures a bug/idea into [[Linear]] mid-flow), (2) exploration phase (agent reads the codebase and current ticket, asks clarifying questions — Zevi answers these in a batch, prepared in advance), (3) create plan (produces a markdown plan file with a TL;DR, key decisions, and a task list with status tracking), (4) execute (often via Cursor's fast "Composer" model), (5) review + peer review, (6) update docs — closing the loop so agents don't repeat past mistakes. See [[Slash Command Development Workflow]].
- **[[Multi-Model Peer Review]]**: after Claude reviews its own code (`/review`), Zevi runs the same review with [[Codex]] and Cursor's Composer, then feeds each model's findings back to Claude via a `/peer review` command framed as "other team leads reviewed your code" — Claude must either justify why a flagged issue isn't real or fix it. He personifies each model distinctly: Claude as a communicative, opinionated "dev lead"; Codex as an uncommunicative but highly effective solo problem-solver; Gemini (in Google's Antigravity) as a talented-but-erratic "crazy scientist" whose visible reasoning steps are alarming to watch even when the end result is excellent design.
- **[[Exposure Therapy Onboarding]]**: his recommended path for non-technical builders — start in a ChatGPT project (pure conversation, no code visible), graduate to a "vibe coding"-style builder like Bolt/Lovable, then to Cursor, easing into looking at actual code and eventually a full terminal/dark-mode setup, rather than diving straight into a code editor.
- **Post-mortem tooling updates**: whenever an agent makes a significant mistake, Zevi asks it to introspect on what in its own system prompt or tooling caused the error, then updates that documentation/slash-command so the mistake can't recur — treating the prompt/tooling stack itself as a continuously improving asset, distinct from the underlying model improving.
- **AI-assisted interview prep**: used a [[Claude]] project as an interview coach for his Meta PM interview (explicitly instructed not to be encouraging, just effective), built a custom quiz web app in Base 44 to drill product-segmentation questions, used Perplexity's Comet browser to analyze a public interview-question bank for prioritization, and still considers live human mock interviews the most valuable single input.
- **On "outsourcing your thinking"**: rejects the critique that using an AI co-pilot for PM work is intellectually lazy — frames the PM job as harnessing whatever gets you fastest to the right solution for users, not performing visible effort, and argues junior PMs specifically benefit by using AI to "play at a higher level" (e.g., reasoning about company-wide strategy on a side project) than their actual seniority would otherwise allow.
- **Failure Corner**: recounts bombing his first product review at Wix by trying to work alone and impress senior PMs, then realizing the real expectation was to be [[10x Learner Vs 10x Doer|"a 10x learner," not a 10x doer]] — after which he deliberately sought out each teammate's individual strength as a mentorship resource.
- **[[Time Machine Moments]]**: his term for stretches where he runs several AI agents in parallel on unrelated projects (podcast prep, localizing Studymate, standing up a personal site) and, with nothing left to actively do but wait, feels like he's "stuck his head out of a time machine" into the near future — a recurring, almost disorienting marker of how much unsupervised agent work has become possible.
- Lightning round: recommends *[[The Fountainhead]]* (Ayn Rand), *[[Shoe Dog]]* (Phil Knight), and *[[Mindset (book)|Mindset]]* (Carol Dweck, see [[Growth Mindset]]); loves *[[Severance]]* and *The Pit*; recently discovered [[CAP]] (an open-source Loom alternative); mottos "you can just do things" and his brother's "nobody knows what they're doing."

## Related

- [[Zevi Arnovitz]] — guest
- [[Lenny Rachitsky]] — host
- [[Meta]] — his current employer
- [[Wix]] — his former employer, site of the Failure Corner story
- [[Studymate]] — his side-project app, built live on in the episode
- [[Cursor]] / [[Claude Code]] / [[Codex]] / [[Claude]] / [[ChatGPT]] — the AI coding tools central to his workflow
- [[Linear]] — issue tracker integrated into his slash-command workflow
- [[Slash Command Development Workflow]] — the episode's central six-stage framework
- [[CTO Persona Pattern]] — his foundational technique
- [[Multi-Model Peer Review]] — his distinctive code-review practice
- [[Exposure Therapy Onboarding]] — his recommended non-technical onboarding path
- [[10x Learner Vs 10x Doer]] — his Failure Corner takeaway
- [[Time Machine Moments]] — his term for parallel-agent flow states
- [[Tal Riv]] — mentor who introduced him to Lenny and taught PM-copilot techniques
- [[Ben Arez]] — guest-post author on AI interview prep, cited as a resource
