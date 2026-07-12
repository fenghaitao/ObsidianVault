---
title: "Dealbot"
type: concept
tags: [AI, agent, sales, go-to-market, automation]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/42 - What world-class GTM looks like in 2026 ｜ Jeanne DeWitt Grosser (Vercel, Stripe, Google).md"]
last_updated: 2026-07-10
---

## Definition

Dealbot is an AI agent built by Vercel's GTM engineering team that analyzes Gong transcripts, Slack interactions, and emails to provide real-time insights and coaching on active sales deals. It evolved from an earlier "Lostbot" that performed post-mortem analysis on lost opportunities.

## Key Information

- **Origin:** Started as "Lostbot" — ran against Q2 lost opportunities, sorted by deal size, to identify true reasons for loss.
  - Key finding: A top loss attributed to "price" by the AE was actually lost due to failure to connect with the economic buyer and inability to demonstrate ROI/value.
  - This insight led to building out value quantification for Vercel's GTM team.
- **Dealbot (real-time):** Runs continuously, feeding insights into per-customer Slack channels.
  - Alerts: "You're this far into the sales process and haven't talked to an economic buyer."
  - Call quality: "That call with the economic buyer didn't seem to go well — here are follow-up suggestions."
- **Enablement use case:** After product launches, the agent analyzes calls to find objection handling gaps and stuck points. Weekly "bug fix" sprints address GTM process issues.
- Built in approximately 2 days (initial Lostbot version), refined over time.
- Runs on Vercel's AI cloud infrastructure (Workflow SDK, AI Gateway, Fluid Compute).
- Embodies the principle that GTM problems can be treated like engineering bugs — identified, fixed, and verified.

## Related

- [[summary-42 - What world-class GTM looks like in 2026 ｜ Jeanne DeWitt Grosser (Vercel, Stripe, Google)]] — source summary
- [[Gong]] — data source for Dealbot
- [[GTM Engineer]] — role that built Dealbot
- [[Vercel]] — platform Dealbot runs on
