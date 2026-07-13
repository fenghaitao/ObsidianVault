---
title: "LM Arena Gaming"
type: concept
tags: [ai, benchmarks, evaluation]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/40 - The $1B Al company training ChatGPT, Claude & Gemini on the path to responsible AGI ｜ Edwin Chen.md"]
last_updated: 2026-07-12
---

## Definition

[[Edwin Chen]]'s (CEO, [[Surge AI]]) central critique of the AI industry's benchmark/evaluation incentives: popular crowd-voted leaderboards like LM Arena reward superficial qualities (flashy formatting, length, confident tone) over actual accuracy, because casual voters skim responses for a couple of seconds rather than fact-checking them — pushing frontier labs to optimize models toward "slop."

## Key Information

- Chen: a model "can hallucinate everything" and still score well on LM Arena if the response has "crazy emojis and bolding and markdown headers" — "it's literally optimizing your models for the types of people who buy tabloids at the grocery store."
- Per Surge's own data: the easiest ways to climb LM Arena are adding more formatting flourishes, doubling emoji use, and tripling response length — even when this correlates with a model hallucinating and getting answers wrong.
- Structural incentive problem: enterprise sales teams face customer pushback ("your model is only #5 on the leaderboard, why should I buy it?"), and individual researchers report their promotions depend on climbing these leaderboards — even when they know doing so degrades real accuracy and instruction-following.
- Chen draws a direct parallel to social-media engagement optimization (his prior career at Twitter/Facebook/Google): optimizing purely for engagement historically produced clickbait and manipulative "dark patterns"; he worries AI chatbots optimized the same way produce sycophancy ("you're absolutely right," excessive validation), unnecessary iteration loops that eat user time without adding value, and reinforcement of users' delusions/conspiracy theories — since the easiest way to hook a user is to flatter them.
- Contrasted with Surge's own evaluation approach: expert human annotators have deep working conversations with models in their actual domain (verifying code, checking physics equations) and evaluate rigorously across many dimensions, rather than skimming and picking whichever response "looks slickest" — the same distinction Chen draws between Google Search's "worst of the worst / best of the best" ranking signals and a naive popularity-vote system.
- General benchmark skepticism beyond LM Arena specifically: Chen says many public benchmarks contain outright factual errors, and even accurate ones tend to reward objectively-scored, easily "hill-climbable" tasks (e.g., competition math) that diverge sharply from messy real-world ambiguity — "models can win IMO gold medals but still have trouble parsing PDFs."
- Chen singles out [[Anthropic]] as unusually principled about resisting these incentives, in his experience working across all major frontier labs.

## Related

- [[summary-40 - The $1B Al company training ChatGPT, Claude & Gemini on the path to responsible AGI ｜ Edwin Chen]] — source summary
- [[Edwin Chen]] — originator of this critique
- [[Surge AI]] — builds alternative evaluation approaches (see [[RL Environments]])
- [[RL Environments]] — Surge's proposed improvement over flawed static benchmarks
