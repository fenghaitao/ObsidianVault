---
title: "AI-Native Codebase"
type: concept
tags: [AI, development, codebase, documentation, best-practice]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/26 - OpenAI's head of platform engineering on the next 12-24 months of AI ｜ Sherwin Wu.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz.md"]
last_updated: 2026-07-10
---

## Definition

An AI-native codebase is a codebase structured to be easily navigable by AI agents, with extensive plain-text documentation (markdown files) explaining how to work in different areas, high-level architecture, and conventions. This makes AI agents more effective at writing and understanding code.

## Key Information

- Zevi Arnovitz advocates for making codebases "AI-native" as a critical step for enabling non-technical PMs to work with AI coding tools
- Key elements: markdown files explaining how agents should work in each area of the codebase, high-level structure documentation, and conventions
- This should be set up by technical people, as it requires deep understanding of the codebase
- Benefits: agents navigate the codebase more easily, write better code, and make fewer mistakes
- Zevi's codebase has "a ton of just plain text in it" — markdown files that guide agents
- Zevi recommends this as a first step for larger companies wanting to enable PMs to use AI coding tools
- Plan files from the slash commands workflow also serve as AI-native documentation, helping future agents understand what was already built in an area
- Zevi updates documentation as part of his workflow: when Claude makes a mistake, he asks what in its system prompt or tooling caused it, then updates docs to prevent recurrence

- An internal team at OpenAI is maintaining a 100% Codex-written codebase as an experiment, with no "escape hatch" to manually write code
- When the agent can't do something, the fix is to add documentation, code comments, and encode tribal knowledge into the codebase
- The team uses code comments, code structure, MD files, and skills files as additional resources for the model
- OpenAI plans to publish a blog post with learnings from this experiment
- The key insight: when agents fail, it's usually a context/underspecification problem, not a model capability problem

## Related

- [[summary-31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz]] — source summary
- [[Slash Commands Workflow]] — workflow that generates and uses AI-native docs
- [[Post-Mortems for AI Workflows]] — updating docs after mistakes
- [[Zevi Arnovitz]] — advocates for AI-native codebases
