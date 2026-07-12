---
title: "Post-Training"
type: concept
tags: [AI, training, LLM, machine-learning, fine-tuning]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/40 - The $1B Al company training ChatGPT, Claude & Gemini on the path to responsible AGI ｜ Edwin Chen.md"]
last_updated: 2026-07-10
---

## Definition

Post-training is the phase of AI model development after initial pre-training, where models are refined using techniques like SFT, RLHF, rubrics, verifiers, and RL environments. Edwin Chen describes it as having "an art to it" — not purely a science.

## Key Information

- Evolution of post-training techniques: SFT → RLHF → Rubrics and Verifiers → RL Environments
- Each new technique complements the previous ones; none become obsolete
- "There's an art to post-training, it's not purely a science" — decisions about what kind of model to build involve taste and sophistication
- Post-training involves countless choices: human data vs. synthetic data, what to ask annotators to create, which benchmarks to prioritize, front-end vs. back-end coding focus, visual design emphasis
- The objective function chosen during post-training fundamentally shapes what the model becomes good at
- Some companies optimize for benchmarks (for PR/marketing) even when they know it makes models worse at real tasks; others take a principled approach focused on real-world performance
- The analogy: humans learn to become great writers not by memorizing grammar rules, but through reading great books, practicing, getting feedback, noticing what works, and developing taste

## Related

- [[Supervised Fine Tuning (SFT)]] — first post-training technique
- [[Reinforcement Learning from Human Feedback (RLHF)]] — second post-training technique
- [[Reinforcement Learning Environments]] — latest post-training technique
- [[Objective Functions in AI]] — what post-training optimizes toward
- [[summary-40 - The $1B Al company training ChatGPT, Claude & Gemini on the path to responsible AGI ｜ Edwin Chen]] — source summary
