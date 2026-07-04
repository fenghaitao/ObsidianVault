---
title: "summary-13 - Running an AI-native engineering org (San Francisco)"
type: source
tags: [source, claude-code, engineering, management, transcript]
sources: ["raw/03-transcripts/Claude/Code with Claude 2026 - San Francisco/13 - Running an AI-native engineering org.md"]
last_updated: 2026-07-04
---

## Core Summary

Fiona Fung, who leads engineering and product for [[ClaudeCode]] and [[ClaudeCowork]], delivers this talk at Code with Claude 2026 San Francisco — a distinct recording of the same talk she gave in London (see [[summary-03 - Running an AI-native engineering org]]), with different anecdotes and phrasing but the same five-theme structure: bottlenecks have moved, team norms had to be rewritten, how those norms were rolled out, signals of success, and open questions. Core thesis: as coding throughput stopped being the bottleneck, verification, review, and maintenance became the new constraints, forcing a rewrite of planning, code-ownership, and org-design norms.

## Key Points

- **Bottleneck shift:** engineering bandwidth used to be the scarce resource (driving heavy pre-planning, waterfall/agile processes); now coding is rarely the slow part, so verification, review, cross-functional partners, and security have become the new bottlenecks.
- **"JIT planning":** the team moved away from six-month roadmaps (found to be stale within months) toward just-in-time planning, sized to match how fast prototyping and code generation now move.
- **Technical debates settled by code, not whiteboards:** rather than debating implementation approaches in a room, Fiona generated three competing PR versions with Claude to compare not just the API implementation but its impact on callers — "building is cheap, arguing is expensive."
- **Reduced design docs:** most Claude Code discussions now happen via PRs and prototypes rather than pre-code design docs, except where async cross-team alignment still needs one.
- **Doubling down on verification:** with higher throughput and new ways to break things, the team invests in "shift left" automation to catch bugs closer to the source.
- **Code ownership got fuzzier:** roles blur as non-engineers ship code and engineers do more design/content work; "who made this change" is reframed as "what question are you really trying to answer" (regression cause, expert lookup, or context-gathering) and automated accordingly (e.g., routines replacing manual morning customer-feedback summaries).
- **Human-in-the-loop where it still matters:** legal review, security-sensitive/trust-boundary code, and product taste/sense still require human judgment even as Claude handles styling, lint, PR feedback, bug fixes, and test authoring.
- **Team makeup:** two engineer archetypes indexed on — creative builders with product sense, and deep systems experts (e.g., distributed systems for Claude Code Remote) — with raw coding throughput de-emphasized as a hiring criterion.
- **Org shape and dogfooding:** every manager on the Claude Code team starts as an IC first (a policy some recruiters pushed back on); org kept as flat as possible with one shared team mission rather than per-pod missions.
- **Success signals:** faster onboarding ramp-up time, shorter PR cycle time, and rising share of Claude-assisted commits (near 100% for the author's own commits in recent months) — read alongside product outcomes, not just raw throughput.
- **Open questions raised:** whether platform-specific mobile teams (iOS/Android) still make sense as engineers flex across platforms; how much to push fully automated review as model capability improves; how to keep roles feeling equally productive as they blur.
- **Practical takeaway:** audit your "noisiest" (most dreaded/expensive) workflow and ask whether it's still serving its original purpose — illustrated by canceling a large weekly status-report meeting after realizing attendees were only half-present.

## Related

- [[ClaudeCode]] — the tool and team this talk is about
- [[ExplorePlanCodeCommit]] — the workflow whose planning/coding phases this talk describes evolving
- [[ClaudeCodeRoutines]] — the scheduled-automation practice (e.g., replacing manual morning rituals) also drawn from this talk
- [[Anthropic]] — the company
- [[summary-03 - Running an AI-native engineering org]] — the London-venue delivery of the same talk
