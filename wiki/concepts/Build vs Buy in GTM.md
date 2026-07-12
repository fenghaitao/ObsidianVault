---
title: "Build vs Buy in GTM"
type: concept
tags: [go-to-market, AI, tooling, strategy]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/42 - What world-class GTM looks like in 2026 ｜ Jeanne DeWitt Grosser (Vercel, Stripe, Google).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/35 - We replaced our sales team with 20 AI agents—here's what happened next ｜ Jason Lemkin (SaaStr).md"]
last_updated: 2026-07-10
---

## Definition

The shifting calculus for go-to-market tooling: whether to build custom AI agents internally or buy off-the-shelf GTM software. The current landscape favors building because internal agents are surprisingly cheap and fast to create, and they capture esoteric company context that generic tools miss.

## Key Information

- Internal AI agents are not that hard to build and not that expensive:
  - Vercel's lead qualification agent: ~6 weeks, one person at 25-30% time.
  - Vercel's Dealbot (initial Lostbot): ~2 days, ~40 hours.
  - Lead agent runtime cost: ~$1,000/year vs. $1M+ in SDR salaries.
- The key advantage of building: "Often your own esoteric context, your content, your workflow is really key to unlocking the power of the agent."
- Risk of buying: Tool proliferation — ending up with 20 different tools for 20 jobs to be done rather than an integrated platform. This is a common pain point for customers deploying AI.
- "ERR" (Experimental Run Rate Revenue): Companies are buying AI tools on a trial basis (blank check AI mandates), leading to procurement bottlenecks.
- Future uncertainty: May end up on better integrated agent platforms, or CIOs may shift from software procurers to software builders with thousands of internal agents.
- Recommendation: Try building yourself first — "you may find that it's meaningfully easier than you think and you get returns pretty quickly."
- For more generalizable workflows, off-the-shelf may be better; for specific/esoteric workflows, build.
- Contrasting view from Jason Lemkin: "Don't build it yourself" for GTM agents — unless you're Vercel with a dedicated GTM engineer. The pace of AI innovation is so fast that internally-built agents become obsolete within months if not constantly maintained.
- Lemkin's rule: "You're not Vercel. You don't have a full-time wicked awesome engineer that wants to build this." Even if you can hire someone to build internally, maintaining pace with vendor innovation is nearly impossible.
- The vendor's willingness to provide forward-deployed engineer support is more important than raw feature comparisons when buying.
- All AI GTM agents are "more similar than different" under the hood — all running on Cloud 4, mashing APIs together. The FDE support is the differentiator.
- SaaStr built many non-GTM tools (valuation calculator, pitch deck reviewer) on Replit but bought all GTM agents (Artisan, Qualified, Agentforce).

## Related

- [[summary-42 - What world-class GTM looks like in 2026 ｜ Jeanne DeWitt Grosser (Vercel, Stripe, Google)]] — source summary
- [[summary-35 - We replaced our sales team with 20 AI agents—here's what happened next ｜ Jason Lemkin (SaaStr)]] — source summary
- [[GTM Engineer]] — role that does the building
- [[Dealbot]] — example of a built agent
- [[Gong]] — example of a bought tool that enables building on top
- [[Forward Deployed Engineer]] — key consideration when buying
- [[AI Sales Agents]] — the build vs buy decision applied to sales
