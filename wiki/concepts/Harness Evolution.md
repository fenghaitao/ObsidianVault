---
title: "Harness Evolution"
type: concept
tags: [ai, agents, harness, models, co-evolution, anthropic, claude]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson.md"]
last_updated: 2026-06-30
---

## Definition
Harness Evolution is the process by which agent harnesses (scaffolding around models) co-evolve with model capabilities over time. As models improve, harness components that compensated for model weaknesses can be simplified or removed, while new harness patterns emerge for remaining gaps. The harness doesn't disappear — it shifts to address new frontiers.

## Key Information
- **Co-Evolution**: Every model release ships alongside harness changes — models and harnesses "co-evolve together." The harness fills gaps in the model, then those patterns inform model training, and the harness adapts again
- **The Frontier Moves**: "The frontier doesn't really shrink, it just moves." As one capability becomes baked into model weights, new capabilities become the focus of harness engineering
- **Concrete Example**: Opus 4.5 needed context resetting between sessions, sprint decomposition (one feature at a time), evaluator at every sprint. Opus 4.6: single continuous session with compaction, no forced sprint decomposition, evaluator at end of generation. Same harness pattern, simplified loops
- **Lesson**: "The harness wasn't wrong — it was right for 4.5, the frontier moved, and we ran a simplified version to see how it worked"
- **Hunting for Model Releases**: Key skill is identifying harness components that exist only to compensate for current model weaknesses, then "hunting for the model release" that lets you strip them out
- **Training Feedback Loop**: Anthropic uses harness patterns in post-training and RL — making models more adept at autonomous work. Harness components that prove effective get trained into the model
- **Claude Code Philosophy**: "Give it tools and get out of the way" — don't over-engineer around model flaws today because models will get better. This is the "AGI pill" philosophy
- **Meter Chart Evidence**: Opus 3.7 ran ~1 hour on minimal scaffold. Opus 4.6 reached 12 hours. With better harnesses, runs extend much longer — but the minimal scaffold baseline also improves dramatically
- **Spiky Behaviors**: Each model has "spiky" behaviors — specific strengths and weaknesses. Harness design means identifying these spikes and filling gaps, then watching for the next model to smooth them out
- **What Gets Simplified Over Time**: Context resetting (dropped with 4.6), sprint decomposition (less necessary with 4.6), evaluator cadence (reduced frequency), compacting strategy (continuous vs per-sprint)

## Related
- [[summary-20260518 - Anthropic Workshop： Build Agents That Run for Hours — Ash Prabaker & Andrew Wilson]] — source
- [[GeneratorEvaluator Pattern]] — harness pattern that evolved
- [[Context Anxiety]] — model weakness that was addressed
- [[Agent Harness]] — broader category
- [[Sprint Decomposition]] — harness component that got simplified
- [[Compaction]] — technique that replaced session resetting
- [[RALPH Loop]] — earlier harness pattern
- [[ModelBehavior]] — understanding model-specific behaviors
- [[CoEvolvingLoops]] — related concept
