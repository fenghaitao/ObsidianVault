---
title: "summary-20260330 - Coding Agent Reliability EXPLODES When They Argue (New Adversarial Dev Technique)"
type: source
tags: [source, transcript, adversarial-dev, harness, gan, sycophancy, anthropic]
sources: ["raw/03-transcripts/Cole Medin/Channel Only/20260330 - Coding Agent Reliability EXPLODES When They Argue (New Adversarial Dev Technique).md"]
last_updated: 2026-06-20
---

## Core Summary

[[ColeMedin]] introduces **[[AdversarialDev]]** — a GAN-inspired [[AgentHarness]] where a *generator* coding agent implements and a separate *evaluator* coding agent (its own context session) rips the implementation apart. Solves [[Sycophancy]]: an agent grading its own work is "a student grading their own homework." Inspired by an [[Anthropic]] blog post (not open-sourced), Cole built both Claude Code and Codex versions. Built an elaborate RAG app in ~4 hours, one-shot, using Sonnet 4.6 — which he says Opus 4.6 couldn't one-shot *without* the harness.

## Key Points

- **The problem: [[Sycophancy]].** LLMs are biased toward agreeing with the user and with their own prior work. Worst in AI coding: an agent reviewing code it just wrote, in a session full of the user's injected opinions, gives itself a gold star. Cole claims sycophancy is getting *worse* as models get more powerful.
- **The solution: a sparring partner.** A totally separate coding agent, own context session, whose sole job is to be nitpicky, play devil's advocate, question deep decisions. "Adversarial dev."
- **GAN analogy.** Generative Adversarial Networks: a generator makes images, a discriminator judges real-vs-fake; the generator improves by trying to fool the discriminator. Mapped to coding: generator implements, evaluator judges against criteria. As long as the evaluator judges correctly, the generator "fooling" it = the code actually being good.
- **Three agents** (from Anthropic's architecture):
  1. **Planner** — expands the user prompt into a full spec.
  2. **Generator** — implements (the "software engineer").
  3. **Evaluator** — judges (the "skeptical QA engineer").
- **The contract negotiation** — the most fascinating part. Before any code is written, generator and evaluator *negotiate a contract*: how to split the spec into sprints, and what criteria each sprint will be judged against (1-10 scores with thresholds). "Adversarial but ethical — they agree on what the battle looks like up front."
- **Sprint cycle**: per sprint, generator implements → evaluator scores against negotiated criteria → if below threshold, generator retries (max 3×) → if all pass, next sprint.
- **Cross-model mixing**: Cole built Claude and Codex versions with identical structure to prove the pattern isn't Anthropic-specific. You can even mix — Claude as implementer, Codex as evaluator.
- **The economic argument**: harnesses let you use *cheaper/faster* models and still get great results. Cole built the whole RAG app with **Sonnet 4.6** + the harness; argues **Opus 4.6** alone (no harness) couldn't have one-shotted it. The harness substitutes engineering for raw model power.
- **Subscription vs API note**: Cole clarifies (via Anthropic team member "Threek") you can use a Claude/Codex subscription with the Agent SDK / headless mode for *local development and experimentation*. Building a business where others use your script → use an API key (ToS).

## Related

- [[AdversarialDev]] — central concept
- [[Sycophancy]] — the problem
- [[AgentHarness]] — the architectural family
- [[Anthropic]] — source of the GAN-inspired architecture
- [[Codex]] — OpenAI coding agent; Cole built a parallel version
- [[ClaudeCode]] — primary harness substrate
- [[ValidationGates]] — the evaluator's scoring is a sophisticated validation gate
- [[ColeMedin]] — author
