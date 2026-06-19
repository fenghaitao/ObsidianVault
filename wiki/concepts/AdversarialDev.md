---
title: "AdversarialDev"
type: concept
tags: [concept, harness, gan, sycophancy, multi-agent, code-review, anthropic]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260330 - Coding Agent Reliability EXPLODES When They Argue (New Adversarial Dev Technique).md"
last_updated: 2026-06-20
---

## Definition

Adversarial Dev is an [[AgentHarness]] pattern where a **generator** coding agent implements and a separate **evaluator** coding agent — in its own context session — adversarially critiques the implementation against negotiated criteria. Inspired by Generative Adversarial Networks (GANs). Solves [[Sycophancy]]: an agent reviewing its own work in its own biased context is "a student grading their own homework."

## Key Information

### The problem it solves: [[Sycophancy]]

LLMs are biased toward agreeing — with the user and with their own prior output. In AI coding this is acute: an agent reviewing code it just wrote, in a session full of the user's injected opinions, gives itself a gold star (maybe flags a few token flaws for legitimacy, stuffs the real problems under the rug). [[ColeMedin]] claims sycophancy is getting *worse* as models get more powerful.

### The GAN analogy

Generative Adversarial Networks: a **generator** makes images, a **discriminator** judges real-vs-generated. The generator improves by learning to fool the discriminator → more realistic images over time.

Mapped to coding:
- **Generator** = implementer agent ("software engineer").
- **Evaluator** = critic agent ("skeptical QA engineer").
- As long as the evaluator judges *correctly*, the generator "fooling" it ≡ the code actually being good.

### The three agents (from [[Anthropic]]'s architecture)

1. **Planner** — expands the user prompt into a full spec.
2. **Generator** — implements.
3. **Evaluator** — critiques against criteria.

### The contract negotiation (the clever part)

Before any code is written, generator and evaluator **negotiate a contract**:
- How to split the spec into sprints.
- The criteria each sprint is judged against (1-10 scores with thresholds).

"Adversarial but ethical — they agree on what the battle looks like up front." This makes the adversarial relationship structured rather than chaotic.

### The sprint cycle

```
For each sprint:
  Generator implements the sprint's features
  Evaluator scores against negotiated criteria (1-10 each)
  If any score < threshold:
     Generator retries (max 3×) to appease the evaluator
  If all pass:
     Move to next sprint
```

The generator's job becomes "appease/trick the evaluator" — and because the criteria point at the app actually working, appeasing the evaluator ≡ building working software.

### Why it works — the economic argument

The killer insight Cole emphasizes: **harnesses let you substitute engineering for raw model power.** He built an elaborate RAG app (full UI, token streaming, RAG pipeline) one-shot in ~4 hours using **Sonnet 4.6** + the adversarial harness — and argues **Opus 4.6** alone (no harness) could *not* have one-shotted it. The harness made a cheaper/faster model outperform a more powerful one used naively.

### Cross-model flexibility

Cole built parallel [[ClaudeCode]] and [[Codex]] versions with identical structure (to prove the pattern isn't Anthropic-specific). You can even mix: Claude as generator, Codex as evaluator. The adversarial value may *increase* with cross-model setups — different models have different blind spots.

### Relationship to other patterns

- It's a specific [[AgentHarness]] — multi-session, with handoffs and validation.
- The evaluator is a sophisticated [[ValidationGates]] — instead of running fixed tests, it reasons about quality against negotiated criteria.
- It's the antidote to letting a single agent self-review (the [[Sycophancy]] trap).
- Connects to [[HumanInTheLoop]]: the harness automates the critique that a human reviewer would otherwise have to provide.

### Caveat

Like all harnesses: token-expensive (long-running, multi-agent), and not for immediately-production-ready output — best for rapid POCs and getting projects to a strong starting point. The reliability gain is worth the overhead for Cole.

## Related

- [[Sycophancy]] — the problem
- [[AgentHarness]] — the family this belongs to
- [[HarnessEngineering]] — the discipline
- [[ValidationGates]] — the evaluator is a reasoning-based gate
- [[Anthropic]] — source of the GAN-inspired architecture
- [[ClaudeCode]], [[Codex]] — the two implementations Cole built
- [[HumanInTheLoop]] — what the evaluator automates
- [[ColeMedin]] — author
- [[summary-adversarial-dev-technique]] — primary source
