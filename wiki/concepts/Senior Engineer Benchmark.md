---
title: "Senior Engineer Benchmark"
type: concept
tags: [benchmark, ai-model-evaluation, coding-agents]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/08 - AI predictions： Job markets, Codex beats Claude, and the death of org charts ｜ Dan Shipper.md"]
last_updated: 2026-07-10
---

## Definition

The Senior Engineer Benchmark is a personal benchmark [[Dan Shipper]] built to test how close AI coding models are to a human senior engineer, based on rewriting the vibe-coded codebase of his product [[Proof]] from first principles.

## Key Information

- Origin: Proof was vibe-coded and broke repeatedly right after launch; Dan had two senior engineers independently rewrite the codebase from scratch, giving him two reference "ground truth" rewrites to score against.
- Method: give each new model the same prompt — "this is vibe-coded slop, if you wanted to rewrite it from first principles, how would you write it, go do it" — and score the output against the human senior-engineer rewrites (high-80s/low-90s out of 100).
- Results as of this episode: every model prior to GPT-5.5 scored around 30/100; [[GPT-5.5]] scored 62/100 (partly using an "Opus 4.7 plan"), the first roughly 30-point jump Dan has observed.
- Key differentiator GPT-5.5 showed: the willingness/agency to actually rip out and rewrite bad code from first principles, rather than papering over problems with small patches — which Dan Shipper says every other coding model still defaults to, and predicts most coding models will *still* default to a year from this recording, even as the underlying capability keeps rising.
- Dan Shipper notes the exact prompt phrasing mattered a lot to get a model to reveal this behavior without being told the answer outright, and that he plans to keep "zeroing out" the benchmark (making it harder) as models improve, so the benchmark's headline score doesn't overstate real automation of the senior-engineer job.
- Used by Dan Shipper as his central argument for why benchmark saturation doesn't equal full replacement of human engineers: benchmarks measure problems that have already been framed, articulated, and scored, whereas the deeper act of recognizing that a codebase needs an architectural rewrite (not asked for) is a distinct, harder-to-measure human skill.

## Related

- [[summary-08 - AI predictions： Job markets, Codex beats Claude, and the death of org charts ｜ Dan Shipper]] — source summary
- [[Dan Shipper]] — creator of the benchmark
- [[Proof]] — codebase used for the benchmark
- [[GPT-5.5]] — model that first scored significantly higher
- [[Vibe Coding]] — how the original codebase was produced
- [[AI Job Apocalypse]] — myth this benchmark is used to push back against
