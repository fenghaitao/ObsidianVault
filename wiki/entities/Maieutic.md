---
title: "Maieutic"
type: entity
tags: [hackathon, education, claude-code, ide, metacognition, computer-science]
sources: ["raw/01-articles/claude/2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon.md"]
last_updated: 2026-07-07
---

## Definition

Maieutic is an IDE designed to make computer science students slow down at key moments, forcing them to think before coding. Built by Paula Vásquez-Henríquez, it addresses the problem of students using AI to generate code they don't understand by requiring plain-language specifications, locking autocomplete, and using Intent-Diff Review to compare specs against code.

## Key Information

- **Creator**: Paula Vásquez-Henríquez, a computer science teacher at Universidad del Desarrollo in Concepción, Chile, and a PhD candidate in Artificial Intelligence researching student–AI interaction patterns.
- **Problem addressed**: Students use AI to manufacture code but have no idea what it does. The autocomplete delivers working code before they've even finished forming the question, so the metacognitive loop (thinking-about-your-thinking that creates a programmer) never closes.
- **How it works**:
  - Students must describe in plain language what their program should do before writing any code. Claude asks targeted clarifying questions and keeps the editor locked until the spec is detailed enough.
  - Students can write Python but autocomplete is off. A chat panel answers reference questions directly but responds to reasoning questions with counter-questions, refusing to do the student's thinking.
  - **Intent-Diff Review** (core of the tool): Claude compares the spec against the final code, classifies each divergence as drift, revision, or bug, and surfaces a neutral, non-accusatory question prompting the student to explain the issue themselves.
- **Instructor dashboard**: Shows one row per student with a one-sentence cognitive summary (e.g., "written the spec three times, still hasn't considered empty input"). Teachers can monitor individual student interactions with Claude and identify shared misunderstandings across the whole class.
- **Development approach**: Paula dedicated two full days to pure thought work (design spec and technical spec) before writing a single line of code — dogfooding her own philosophy of specifying before building.
- **Impact**: Researchers at the University of Houston have reached out about co-authoring a paper.

## Related

- [[summary-2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon]] — source summary
- [[ClaudeCode]] — development environment
- [[Claude4.7Opus]] — model used
- [[SpecFirstDevelopment]] — the planning methodology Paula applied and Maieutic teaches
