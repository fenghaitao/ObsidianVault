---
title: "summary-2026-03-03 - Improving skill-creator Test, measure, and refine Agent Skills"
type: source
tags: [source, skills, skill-creator, evals, testing]
sources: ["raw/01-articles/claude/2026-03-03 - Improving skill-creator Test, measure, and refine Agent Skills.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic brought software-testing rigor to Skill authoring without requiring code: skill-creator now writes evals, runs a standardized benchmark mode, supports parallel multi-agent eval execution, and tunes skill descriptions for more reliable triggering — aimed at the fact that most skill authors are subject-matter experts, not engineers.

## Key Points

- **Two skill categories with different testing needs**: **capability uplift** skills teach Claude something the base model can't do reliably alone (e.g., document-creation skills); **encoded preference** skills sequence steps Claude can already do individually according to a team's specific process (e.g., an NDA-review checklist).
- **Evals**: define test prompts (plus files) and describe what "good" looks like; skill-creator reports whether the skill holds up — used to isolate real failures (e.g., the PDF skill's struggle with non-fillable forms was traced to missing coordinate anchoring, then fixed).
- **Two key eval uses**: catching quality regressions as models/infrastructure evolve, and detecting when a capability-uplift skill has become unnecessary because the base model now passes the evals without it loaded (the skill's techniques were absorbed into default model behavior).
- **Benchmark mode**: a standardized assessment run after model updates or skill iteration, tracking eval pass rate, elapsed time, and token usage; results can be stored locally, wired into a dashboard, or plugged into CI.
- **Multi-agent eval support**: runs evals in parallel via independent agents, each in a clean context with its own token/timing metrics, avoiding cross-run context bleed and slow sequential execution.
- **Comparator agents**: blind A/B judges comparing two skill versions (or skill vs. no skill) without knowing which is which, to confirm whether a change actually helped.
- **Description tuning**: analyzes a skill's current description against sample prompts and suggests edits reducing both false-positive and false-negative triggering; applied across Anthropic's own document-creation skills, improving triggering on 5 of 6 public skills.
- Frames a longer-term trajectory: today's SKILL.md is essentially an implementation plan (the "how"); as models improve, a natural-language description of the "what" (i.e., the evals themselves) may eventually be the skill.
- Available now in Claude.ai and Cowork; Claude Code users install via the skill-creator plugin or the public skills repo.

## Related

- [[ClaudeCodeSkills]] — the concept this article substantially expands with testing/eval tooling
