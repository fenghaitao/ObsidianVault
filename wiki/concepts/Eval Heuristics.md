---
title: "Eval Heuristics"
type: concept
tags: [evals, heuristics, methodology, benchmarks, model-evaluation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline.md"]
last_updated: 2026-06-30
---

## Definition
Eval Heuristics are practical rules of thumb for interpreting and using AI evaluations effectively. Ara Khan presents three core heuristics to avoid the pitfalls of both the [[Two Camps of Wrong on Evals]].

## Key Information

### Heuristic 1: Don't Believe Model Provider Eval Numbers
- Model companies publish benchmark scores that are approximations at best
- AI researchers and engineers routinely dismiss these numbers — they are not to be taken that seriously
- Real-world trying and preferences matter more than published scores
- Many models with similar benchmark numbers perform very differently in practice
- The entire benchmark reporting ecosystem can feel like a hoax when numbers don't match reality

### Heuristic 2: Stay Current, But Don't Be the Earliest Adopter
- The frontier model changes every couple of months — keeping up is exhausting even for professionals
- Let new models settle for a couple of weeks after release
- If the model still stands the test of time after initial hype subsides, then consider switching
- Only people who work on evals for a living need to always be on the cutting edge
- The Epochs Index shows how rapidly the frontier model has shifted over the last 2 years

### Heuristic 3: Look for Very New and Very Precise Evals
- Many standardized evals have become old and no longer measure frontier capabilities
- OpenAI stated that [[SWEBench]] no longer measures frontier coding capabilities — it contains problems like Fibonacci sequences and matrix multiplication
- Old evals don't apply to real-world software engineering
- Requires discernment to identify evals that are both new and legitimately rigorous
- [[TerminalBench]] is an example of a newer, more precise eval with real-world programming problems

## Related
- [[summary-20260606 - Evals Are Broken, Use Them Anyway — Ara Khan, Cline]] — source
- [[Two Camps of Wrong on Evals]] — the misconceptions these heuristics address
- [[Hill Climbing (Evals)]] — the methodology guided by these heuristics
- [[BenchmarkSaturation]] — why Heuristic 3 is necessary
- [[Benchmark Maxing]] — what Heuristic 1 warns against
- [[SWEBench]] — example of a saturated benchmark
- [[TerminalBench]] — example of a newer, more precise eval
