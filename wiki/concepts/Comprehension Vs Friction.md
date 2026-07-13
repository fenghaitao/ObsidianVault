---
title: "Comprehension Vs Friction"
type: concept
tags: [product-design, ux, cognitive-load]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/44 - Mental models for building products people love ft. Stewart Butterfield.md"]
last_updated: 2026-07-12
---

## Definition

[[Stewart Butterfield]]'s central critique of the "always reduce friction" and "minimize clicks/taps" product-design orthodoxy: for most product surfaces, the real barrier to adoption is comprehension (does the user understand what this is and what to do next), not raw click-count — and treating friction-reduction as the universal goal actively produces worse products.

## Key Information

- **When friction reduction genuinely matters**: only when a user's intent is already both high and specific — e.g., buying a known Taylor Swift concert ticket on Ticketmaster, or any e-commerce checkout/account-registration flow. In these cases people will push through friction because they already know exactly what they want.
- **When it's the wrong lens**: for most first-time or unfamiliar product surfaces, users arrive with low, unspecific intent (e.g., someone finally checking out slack.com after hearing about it from several sources) — their real blocker isn't the number of steps but not understanding what the product is, what a given screen/decision means, or what happens after they act.
- **"Don't make me think"** (the mantra Butterfield adopted, from Steve Krug's book of the same name): forcing a user to make a decision they don't understand has a real biological/metabolic cost (glucose/ATP used in decision-making) and an emotional cost — people who don't understand a piece of software tend to blame themselves, feel "stupid," and associate that bad feeling with the product going forward.
- **Concrete failure examples**: Google Calendar's alphabetically-sorted (not relevance-sorted) time-zone picker; Gmail's action menu for individual emails, split inconsistently across two different menus (with "mark as unread" hidden behind an unlabeled icon in neither); Apple's iPhone Clock app labeling a complex feature simply "Sleep," with no indication of what turning it on does, so an estimated 90%+ of users never engage with it at all.
- **The "reduce clicks" fallacy**: Butterfield argues you could technically make anything one click by exposing every possible option on a single, endlessly scrolling screen — obviously bad. The real design skill is chunking/grouping options (e.g., a menu with dividers, showing only the 2-3 most common actions plus an "other" submenu) so that comparing options stays cognitively cheap, since comparing N options gets "geometrically more expensive" as N grows.
- **Counter-example proving clicks aren't inherently bad**: Butterfield observed a teenager rapidly tapping through Snapchat stories 4-7 times per second for minutes at a stretch — extremely high raw friction/click count, but each tap required zero real cognitive load, making it a genuinely great experience. The goal was never to make her tap less.
- Directly related to "[[Owner's Delusion]]" (why builders fail to see their own comprehension gaps) and to Slack's own product decisions (see [[Slack]]) like deliberately noisy default notifications for new users, which existed specifically to solve a comprehension problem (new testers assumed the product was broken without them) at the cost of some friction.

## Related

- [[summary-44 - Mental models for building products people love ft. Stewart Butterfield]] — source summary
- [[Stewart Butterfield]] — originator of this framing
- [[Owner's Delusion]] — related concept on why builders miss comprehension gaps
- [[Slack]] — product decisions illustrating this principle
