---
title: "Latent Demand"
type: concept
tags: [product-management, market-analysis, framework]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/04 - What happens after coding is solved ｜ Fiona Fung (Claude Code & Cowork).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/05 - The hidden pattern behind successful products ｜ Mark Pincus (FarmVille, Words with Friends, & more).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny.md"]
last_updated: 2026-07-11
---

## Definition

The idea that unmet or underserved demand can exist even when it isn't directly observable. Two complementary framings surface across episodes: [[Mark Pincus]]'s market-level version — the absence of a category today doesn't mean there's no underlying consumer desire for it, since access/friction/cost has been suppressing observable demand — and [[Fiona Fung]]'s usage-level version — watching for people using a product in unexpected ways as a signal of unmet need, then deliberately building for that use case.

## Key Information

- Founding insight behind [[Zynga]] (Pincus): in 2007, video gaming was a $23B industry, yet Pincus (who didn't play games and knew no one who did) believed there was latent demand for a mass-market, "adults giving themselves permission to play" category — if friction (cost, install effort, time investment) were removed (free, three clicks, 5-15 minutes). Gaming is now a ~$280B industry.
- Applied to social/consumer in the AI era: Pincus argues we don't merely have latent demand for social connection, we already are being social (Snapchat, Instagram, TikTok) — but that experience has "lost the adrenaline," implying latent demand for a *better* version of an already-served need, not an unserved one. See [[Cocktail Party Distribution]].
- Related diagnostic (Pincus): look for a feature or behavior that's "proven" but buried/underserved inside someone else's product (e.g., offline browsing buried in Netscape/IE, leading to [[Freeloader]]; an Arabic-only version of an app, leading to [[Nikita Bier]]'s [[TBH]]) — evidence of latent demand hiding in plain sight.
- Fung's framing at [[Anthropic]]: "when you see people jumping through hoops to make something work, can you actually make that an even smoother and better experience?" — form a hypothesis from observed workaround behavior, then build toward it. Cited as one of the main mechanisms behind Anthropic's ability to spot large new opportunities (e.g., coding as a market, and [[Claude Cowork]] itself) ahead of other AI labs.
- Concrete example inside Anthropic: the Claude Cowork team noticed non-coders were already using [[Claude Code]] for non-coding tasks, which led to investing in and shipping Cowork as a dedicated non-coding-work product.
- Concrete example from Fung's personal life: she found Cowork "magic" for her own travel-expense reporting, then noticed her small-business-owner friends do large amounts of manual invoicing/expensing work — leading directly to the "Claude for Small Business" bundle inside Cowork.
- Fung distinguishes this explicitly from designing for an already-articulated, well-understood need: latent demand is discovered via close observation of real usage/behavior (including unintended behavior), not via traditional requirements-gathering. Connects to [[Dogfooding]] and direct customer visits as observation mechanisms.
- Per [[Boris Cherny]] (episode 25), who calls this "the single most important principle in product": cites two Meta case studies from [[Fiona Fung]]'s time founding the Marketplace team — [[Facebook Marketplace]] originated from noticing 40% of posts in Facebook Groups were people buying/selling ("abusing" a product not designed for that); Facebook Dating originated from noticing 60% of profile views were between non-friends of opposite gender (people using the profile-browsing feature as an informal dating tool).
- Cherny's account of [[Claude Cowork]]'s origin: for months, people were using [[Claude Code]]'s terminal for entirely non-coding tasks (growing tomato plants, analyzing a genome, recovering corrupted wedding photos, analyzing an MRI); Anthropic's own data scientist [[Brendan]] independently figured out how to install and use the terminal/Node.js/Claude Code to do SQL analysis, and the rest of the data science team followed within a week — a strong enough signal that Anthropic built a dedicated non-coding product around it.
- Cherny's "second dimension" of latent demand — a newer, model-side framing distinct from the classic user-side framing: instead of only watching what *people* are trying to do, watch what the *model itself* is trying to do, and make that easier. Internally called being "on distribution" (a research/alignment term). This inverted the earlier LLM-application design pattern of putting a model in a rigid box with narrow tool access — Claude Code instead exposes the model with minimal scaffolding, letting it decide which tools to use and in what order. See [[Don't Box The Model In]].

## Related

- [[summary-04 - What happens after coding is solved ｜ Fiona Fung (Claude Code & Cowork)]] — source summary
- [[summary-05 - The hidden pattern behind successful products ｜ Mark Pincus (FarmVille, Words with Friends, & more)]] — source summary
- [[summary-25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny]] — source summary
- [[Zynga]] — founded on this latent-demand bet about gaming
- [[Cocktail Party Distribution]] — application of this concept to consumer/social
- [[Freeloader]] / [[TBH]] — case studies of spotting latent demand buried in existing products
- [[Fiona Fung]] — describes and applies the usage-observation version of this concept
- [[Anthropic]] — organizational context for Fung's framing
- [[Claude Code]] / [[Claude Cowork]] — product example of latent demand discovered via usage
- [[Dogfooding]] — related observation practice
- [[Boris Cherny]] — calls this the single most important product principle; adds the model-side framing
- [[Facebook Marketplace]] — Meta case study
- [[Brendan]] — data scientist whose terminal use signaled Cowork's opportunity
- [[Don't Box The Model In]] — the model-side design implication of this principle
