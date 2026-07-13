---
title: "Go-To-Market Engineer"
type: concept
tags: [gtm, sales, ai-agent, role]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/42 - What world-class GTM looks like in 2026 ｜ Jeanne DeWitt Grosser (Vercel, Stripe, Google).md"]
last_updated: 2026-07-12
---

## Definition

An emerging technical role, championed by [[Jeanne DeWitt Grosser]] (COO, [[Vercel]]): a GTM (go-to-market) engineer breaks down sales/marketing/customer-success workflows into discrete steps and turns the ones AI can do well into custom internal agents, starting with the most "legible" (documentable, largely deterministic) workflows first.

## Key Information

- Ideal profile: someone with real GTM experience (e.g., a former sales engineer or salesperson who also codes), not a pure engineer — because you need to know what *good* sales practice looks like to encode it correctly. Vercel's first three GTM engineers were all former front-end developers who had become sales engineers.
- Process: shadow the highest-performing person in a given function (e.g., an SDR with many browser tabs open doing manual research), use that to define the initial agent workflow, then let the agent make judgment calls (e.g., is this lead qualified? what should we say?) with a human reviewing/approving output before anything is sent — gradually reducing human review as trust builds.
- Sequencing: start with the most legible workflows (Vercel began with inbound lead qualification, then moved to outbound prospecting, starting with lower-market segments that have simpler single-decision-maker buying); large-enterprise, multi-stakeholder prospecting will remain human-heavy the longest.
- Concrete Vercel results: a "lead agent" took ~6 weeks and ~30% of one GTM engineer's time to build, letting the team shift 9 of 10 inbound SDRs to outbound work while holding lead-to-opportunity conversion flat and cutting time-to-convert (since the agent responds instantly rather than letting leads sit in a queue). A follow-on "dealbot" (built from Gong call transcripts) took 2 days to build as a lost-deal post-mortem tool, then evolved into a real-time in-Slack deal-coaching agent.
- Cost comparison: the lead agent costs roughly $1,000/year to run on Vercel's own platform, versus well over $1M in prior SDR salary costs for the 9 people it displaced — framed as a >90% cost reduction for equivalent output.
- Build vs. buy: Grosser argues these agents are easier and cheaper to build in-house than most companies assume, since a company's own proprietary context/workflow data (not generic access to "everything on the drive") is what actually makes an agent effective — feeding an agent unrestricted access to a full knowledge corpus performs poorly.
- Prerequisite for adoption: a company needs an existing, at least somewhat repeatable/documented sales process before GTM engineering can be applied — you can't automate a workflow that was never made explicit in the first place. Grosser suggests ~10 people as a reasonable team size to start investing in a GTM engineer.
- Broader implication: GTM functions are expected to consolidate from today's ~17 hyper-specialized roles back into a more integrated life cycle as agents absorb the more legible sub-tasks, freeing human sellers to spend more time actually talking with customers (historically only ~30-40% of a salesperson's time, per industry benchmark reports Grosser cites).

## Related

- [[summary-42 - What world-class GTM looks like in 2026 ｜ Jeanne DeWitt Grosser (Vercel, Stripe, Google)]] — source summary
- [[Jeanne DeWitt Grosser]] — champion of this role
- [[Vercel]] — where this role was built out
- [[GTM As Product]] — companion strategic framework
