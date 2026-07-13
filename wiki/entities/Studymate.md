---
title: "Studymate"
type: entity
tags: [product, side-project, ai, education]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz.md"]
last_updated: 2026-07-11
---

## Definition

[[Zevi Arnovitz]]'s side-project app: a platform for students to upload their own study materials and generate interactive practice tests from them, built and run as a monetized "company of one" entirely via AI coding agents.

## Key Information

- Core flow: a student uploads a PDF, selects which pages/topics to be quizzed on, sets the number of questions and difficulty, and the app sends that context plus a system prompt to [[Gemini]] to generate comprehension-testing questions (with hints and detailed right/wrong explanations); at time of the episode only multiple-choice questions were supported.
- Used live on the podcast as the demo project for building a new feature (fill-in-the-blank questions with a drag-and-drop interface, 30% of generated tests, two blanks with one correct/two incorrect answers each) via Zevi's [[Slash Command Development Workflow]].
- Fully localized from Hebrew to English in two days — work Zevi estimates would take a dedicated dev team multiple weeks — cited as one of his [[Time Machine Moments]].
- Built and maintained entirely by Zevi as a "weekend project" alongside his full-time Meta PM job, with no engineering team; he describes doing competitor research (finding rivals offering true/false and fill-in-the-blank formats) as the direct trigger for the live feature build.

## Related

- [[summary-31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz]] — source summary
- [[Zevi Arnovitz]] — sole builder and owner
- [[Slash Command Development Workflow]] — the process used to build its features
- [[Gemini]] — model powering its quiz generation
- [[Time Machine Moments]] — includes its Hebrew-to-English localization
