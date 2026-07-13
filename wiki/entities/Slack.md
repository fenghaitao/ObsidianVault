---
title: "Slack"
type: entity
tags: [product, company, workplace-communication]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/05 - The hidden pattern behind successful products ｜ Mark Pincus (FarmVille, Words with Friends, & more).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/44 - Mental models for building products people love ft. Stewart Butterfield.md"]
last_updated: 2026-07-12
---

## Definition

Workplace messaging product founded by [[Stewart Butterfield]] (with longtime CTO [[Cal Henderson]]), sold to Salesforce in one of the largest acquisitions in tech history at the time. Cited by [[Mark Pincus]] as a rare example of a hit that may have succeeded on "proven and better" alone, with little "new."

## Key Information

- Pincus: "Slack might have just been proven and better and no new — and that's even better if you can [pull it off]," arguing that taking a behavior people already like and making it much more accessible/fun (without needing genuine novelty) can be enough, since people generally resist change.
- Slack emerged, like [[Discord]], from a company originally pursuing a game (Stewart Butterfield's team was building an MMO called Glitch); the internal tool the team built for itself became the real product — an example of being "humbled" out of an overly ambitious original idea into a more focused one.

### Per episode 44 (Stewart Butterfield's dedicated interview)

- Officially launched February 2014; by year-end, Butterfield told MIT Technology Review "what we have right now is just a giant piece of [expletive]... we should be humiliated that we offer this to the public" — employees printed and posted the quote around the office; he intended it as a standing challenge to keep improving, not as workplace negativity. See [[Divine Discontent]].
- Growth was substantially driven by cross-company word of mouth (an employee who loved Slack at one company would advocate for it at the next) — Butterfield attributes much of this emotional loyalty to small, deliberate craft details rather than core functionality alone (see the "tilting your umbrella" story on [[Stewart Butterfield]]'s page).
- Product craft decisions: the "email + magic link" login flow (avoiding password entry on mobile); deliberately noisy default notifications for brand-new accounts (switched to sane defaults after ~10 messages received, since early testers without notifications thought the product "didn't work"); the "shouty rooster" animated warning shown before an @channel/@everyone broadcast, curbing notification-abuse; a deliberately elaborate, cascading-override rollout design for Do Not Disturb (org default → admin override → individual override → admin re-override) built to avoid conflict across millions of already-configured users, including on-call engineering teams routing critical ops alerts through Slack.
- Threads feature anecdote (see [[Hyperrealistic Work-Like Activities]]): Butterfield removed an auto-populated "@[previous poster]" from the thread-reply input box at launch, arguing it taught people the wrong mental model; ~6 months later it was quietly reintroduced based on an A/B test showing threads were marginally longer (2.17 vs. 2.14 messages) with it — which Butterfield considered a "guaranteed loser" once weighed against the actual organizational cost of running that analysis.
- Butterfield's SLA policy credited customers 100x their money back for any downtime, automatically and without customers needing to request it — an intentionally generous policy that cost the company roughly $8M in forward credits after a major outage shortly following its IPO, prompting a subsequent ToS change specific to being a public company.
- Gave free credits/billing relief to struggling customers during COVID and introduced "fair billing" (not charging for unused seats) even where existing contracts would have permitted charging for them.
- Butterfield made "in the long run, the measure of our success will be the amount of value that we create for customers" a company-wide chanted mantra at multiple all-hands meetings.
- Butterfield's internal positioning memo, "[[We Don't Sell Saddles Here]]," was written and circulated when the company was ~8 people, before public launch.
- [[Noah Weiss]] worked at Slack since its early days and later became CPO, succeeding [[Tamar Yehoshua]].

## Related

- [[summary-05 - The hidden pattern behind successful products ｜ Mark Pincus (FarmVille, Words with Friends, & more)]] — source summary
- [[Stewart Butterfield]] — founder
- [[Proven Better New]] — framework Slack is cited as exemplifying (proven + better, minimal new)
- [[Discord]] — parallel case of a game-company pivot into a communication tool
- [[summary-44 - Mental models for building products people love ft. Stewart Butterfield]] — source summary
- [[Cal Henderson]] — co-founder/CTO
- [[Divine Discontent]] / [[Hyperrealistic Work-Like Activities]] / [[We Don't Sell Saddles Here]] — frameworks illustrated by Slack's own history
- [[Noah Weiss]] — later CPO of Slack
