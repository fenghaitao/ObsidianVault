---
title: "summary-2026-04-28 - Onboarding Claude Code like a new developer Lessons from 17 years of development"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-04-28 - Onboarding Claude Code like a new developer Lessons from 17 years of development.md"]
last_updated: 2026-07-04
---

## Core Summary

Brendan MacLean, principal developer of the open-source protein-analysis software Skyline (700,000+ lines of C#, maintained since 2008 at the University of Washington's MacCoss Lab), applied the same methodology he'd used for 17 years to onboard human developers — introduce a contained project, explain just enough to succeed, then expand scope — to onboarding Claude Code onto Skyline's legacy codebase. Rather than treating each Claude.ai session as starting from zero, he built a separate context repository (`pwiz-ai`) holding a root CLAUDE.md (environment setup and documentation pointers) plus a library of skills encoding domain expertise (a "reference do not embed" principle: skills point to a central knowledgebase rather than duplicating it). The payoff: a year-stalled Files View panel feature was finished in two weeks; a three-years-dormant Java test-management module got new features in under a day; screenshot-diff tooling, an MCP-driven daily summary email, and a new mobilogram plotting pane were all built with Claude Code, including by a previously skeptical developer. Brendan's core thesis: context doesn't persist automatically across sessions and must be deliberately built, versioned, and maintained as its own project artifact — this matters most for open-source projects with high contributor turnover and no institutional memory.

## Key Points

- Skyline: 700,000+ lines of C#, 17 years old, 200,000+ automated nightly tests, maintained by a small team at the University of Washington's MacCoss Lab; part of Anthropic's Claude for Open Source program, with Brendan MacLean as a Claude Developer Ambassador.
- Early Claude.ai (browser) usage was laborious for incremental changes — each session had no memory of what Skyline was or how its 17 years of components related.
- Brendan's insight: introduce Claude through Claude Code "as I would a trainee developer" — a contained first project, explained context, then expanding scope.
- Built a separate repository, `pwiz-ai`, holding all AI context (kept apart from the code repo so it applies across all branches/time points). Root CLAUDE.md handles environment setup and points to documentation ("lay of the land," not the expertise itself).
- Expertise lives in skills following a "reference do not embed" principle — each skill points into a central documentation knowledgebase instead of duplicating content. Most-used: a `skyline-development` skill (orients Claude to project/docs), a `version-control` skill (project-specific commit/PR conventions), and a `debugging` skill tuned with an explicit trigger ("ALWAYS load when investigating bugs, failures, or unexpected behavior") that pushes Claude toward root-cause analysis instead of "guess and test" mode.
- Concrete wins: a year-abandoned Files View panel (file system monitoring, drag-and-drop) finished in two weeks with Claude co-authoring final commits; a Java-based nightly-test-management module (dormant three years) got long-wanted features and CSS layout work in under a day after a LabKey developer used Claude Code to write setup documentation.
- New infrastructure built with Claude Code: fully automated, nearly 100%-reproducible screenshot regression testing for 2,000+ tutorial images, extended with diff-only views and pixel-change amplification via a custom MCP server (written in C# by Claude) so Claude can "see" the diffs; a second MCP server (written in Python by Claude) pulls from LabKey Server, team email, and GitHub release tags to generate a daily summary email of test failures, exceptions, and open support threads.
- A previously agentic-coding-skeptical developer on the team built and shipped a new mobilogram plotting pane (ion mobility data visualization) using Claude Code.
- Brendan's advice for legacy codebases: (1) context is what persists across sessions, not Claude's to-do lists/plans — it must be deliberately built, versioned, and maintained like any other project artifact; (2) invest in a skill library encoding domain knowledge, following "reference do not embed"; (3) use MCP integrations specifically where Claude needs access to real external data (test results, exceptions, support threads).
- For open-source projects specifically, context carries extra weight: no onboarding budget, no institutional memory beyond what's written down, no guarantee of contributor continuity — a maintained context layer belongs to the project rather than any one person and outlasts every individual contributor.
- Footnote: Dario Amodei, Anthropic co-founder, was previously a member of the MacCoss Lab.
- **Anomaly**: no prompt-injection-style boilerplate or scraped widget text was found in this raw file — it reads as a clean, complete article capture with only image captions interspersed. Noted per instructions since none was actually present.

## Related

- [[ClaudeCode]] — the tool onboarded via this methodology
- [[CLAUDE-md]] — the root context file pattern used in the separate `pwiz-ai` repository
- [[ClaudeCodeSkills]] — the skill library (debugging, version-control, skyline-development) central to the approach
- [[ModelContextProtocol]] — custom MCP servers built for screenshot diffing and daily test/support summaries
- [[MacCossLab]] — the lab and Skyline codebase profiled in this case study
