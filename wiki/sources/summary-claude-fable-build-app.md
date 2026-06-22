---
title: "summary-claude-fable-build-app"
type: source
tags: [source, brian-casel, claude-fable, model-evaluation, spec-driven-development]
sources: [raw/03-transcripts/Brian Casel/Channel Only/20260611 - Claude Fable： Build me an app.md]
last_updated: 2026-06-22
---

## Core Summary

Brian Casel tests Anthropic's new Claude Fable model (from the Claude Mythos family) on a real business tool: expanding his Resonance Radar app with an external trend-monitoring engine. He contrasts his normal spec-driven, milestone-based workflow with a more ambitious single-prompt approach to stress-test Fable. Key findings: Fable is a genuine step-change in capability, the refinement stage is shrinking, but planning matters more than ever. He also highlights the new skill of model selection — choosing when to use expensive heavy-hitter models vs daily drivers.

## Key Points

- Claude Fable is a new model class from Anthropic (Claude Mythos family), available under Max plans only until June 22, 2026, then API-only at ~2x Opus cost.
- Brian spent half a day planning in claude.ai before writing any code — using Claude as a "thought partner" for strategic decisions.
- The shaping document included a "Verification Criteria / Definition of Done" checklist so Fable could self-check its work.
- Fable caught details in Brian's spec that he thinks Opus would have missed.
- Observation 1: The refinement stage is shrinking — Fable is good at checking its own work when given clear done criteria.
- Observation 2: Model selection is now a skill — not every job warrants the expensive model; daily drivers (Opus) vs heavy hitters (Fable).
- Brian skipped his normal PRD + milestones process as an experiment; the result was good but he'll likely return to the stepped approach for complex builds.
- The tool being built (Resonance Radar expansion) follows the Night Shift pattern: custom app + agent skills on recurring schedules.

## Related

- [[BrianCasel]] — creator and author
- [[ClaudeCode]] — the coding agent used
- [[Anthropic]] — creator of Claude Fable
- [[SpecDrivenDevelopment]] — the methodology Brian normally uses
- [[VerificationCriteria]] — the definition-of-done checklist pattern
- [[NightShiftModel]] — the pattern behind Resonance Radar
- [[ResonanceRadar]] — the app being expanded
