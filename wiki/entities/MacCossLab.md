---
title: "MacCossLab"
type: entity
tags: [customer, open-source, life-sciences, claude-code, university-of-washington]
sources: [raw/01-articles/claude/2026-04-28 - Onboarding Claude Code like a new developer Lessons from 17 years of development.md]
last_updated: 2026-07-04
---

## Definition

The MacCoss Lab at the University of Washington develops and maintains **Skyline**, an open-source protein analysis software used for biomarker discovery, disease research, and drug development. Skyline has been in active development since 2008 and comprises 700,000+ lines of C#, maintained by a small team running 200,000+ automated nightly tests. Brendan MacLean is Skyline's principal developer and a Claude Developer Ambassador; the lab is part of Anthropic's Claude for Open Source program.

## Key Information

- Skyline detects and quantifies proteins in samples like blood plasma and tissue; 17 years of continuous development as of this case study (April 2026).
- Brendan MacLean has spent nearly three decades onboarding dozens of undergrads, grad students, and postdocs to the lab, using a consistent methodology: introduce a contained project, explain just enough to succeed, then expand scope as understanding grows.
- Applied that identical onboarding methodology to Claude Code rather than treating each AI session as starting from zero — building a separate context repository (`pwiz-ai`) with a root [[CLAUDE-md|CLAUDE.md]] for environment setup/documentation pointers, plus a library of [[ClaudeCodeSkills|skills]] (skyline-development, version-control, debugging) encoding domain expertise via a "reference do not embed" principle.
- Results: a year-stalled Files View panel feature finished in two weeks with Claude co-authoring commits; a three-years-dormant Java/LabKey nightly-test-management module got new features and CSS layout work in under a day; fully automated, near-100%-reproducible screenshot regression testing across 2,000+ tutorial images with custom [[ModelContextProtocol|MCP]] servers (written in C# and Python by Claude) for diff visualization and a daily test/support summary email; a previously agentic-coding-skeptical developer shipped a new mobilogram plotting pane (ion mobility data visualization).
- Footnote: Dario Amodei, Anthropic co-founder, was previously a member of the MacCoss Lab.

## Related

- [[summary-2026-04-28 - Onboarding Claude Code like a new developer Lessons from 17 years of development]] — source summary
- [[ClaudeCode]] — the tool onboarded via this methodology
- [[CLAUDE-md]] — separate-repository context pattern used (`pwiz-ai`)
- [[ClaudeCodeSkills]] — skill library central to the approach
- [[ModelContextProtocol]] — custom MCP servers for screenshot diffing and daily summaries
- [[Anthropic]] — Claude for Open Source program and Dario Amodei's prior lab affiliation
