---
title: "Agent Training Loop"
type: concept
tags: [ai, agents, sales, go-to-market, methodology]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/35 - We replaced our sales team with 20 AI agents—here’s what happened next ｜ Jason Lemkin (SaaStr).md"]
last_updated: 2026-07-11
---

## Definition

The Agent Training Loop is [[Jason Lemkin]]'s repeatable, hands-on process for making an AI go-to-market agent actually work: ingest your best material, train the agent by answering its clarifying questions, then spend roughly an hour or two a day for about 30 days correcting its live mistakes until it performs like a cloned version of your best salesperson.

## Key Information

- Step 1 — ingestion: give the agent a URL to your website, wiki, and training docs, and upload key documents (e.g., a prospectus). "Ingestion" just means uploading and processing this data (Lemkin waves off the underlying jargon — "some ragging, some vectoring, it really doesn't matter").
- Step 2 — training: the agent turns ingested material into clarifying questions; you answer them, and it improves the more you answer — "training is just answering questions and getting better and better."
- Step 3 — QA/correction: once live (e.g., sending practice outbound emails), the agent will make mistakes ("maybe it's hallucinations... it really doesn't matter what the technical term is") that you must catch and correct daily; doing this consistently for about 30 days, at roughly an hour or two a day, produces a well-trained agent.
- Best-input principle: take your single best salesperson's or marketer's actual email copy/script and use it as the training template — agents are "really good at AB testing" and creating variants once seeded with a genuinely strong example, comparable to asking Claude or ChatGPT to "give me three versions of my best email."
- Personalization layer: once trained, agents can pull lightweight personalization data from sources as simple as Salesforce, or from website-visitor tracking, to tailor otherwise-templated messages.
- Anti-pattern this loop corrects: Lemkin says the industry's 2024 failure mode was vendors claiming a product could be "turned on" with zero training and immediately generate revenue — "it's not the way it works." He cites a call with a public B2B company worth over $10 billion whose team had never done this training loop themselves and, as a result, couldn't get any of their deployed agents to work.
- Compounding claim: once the loop is done for one agent, subsequent agents get progressively easier to train — Lemkin describes becoming "the master of the universe" after doing it repeatedly, and says SaaStr is "only experts because we did it 20 times."
- Scale threshold is lower than people assume: Lemkin argues most companies dismissing this approach because they "don't have Lenny's/SaaStr's scale" actually already have enough historical leads/website traffic (often tens of thousands) sitting untouched in their CRM to make the loop worthwhile — the binding constraint is willingness to do the work, not data volume.

## Related

- [[summary-35 - We replaced our sales team with 20 AI agents—here’s what happened next ｜ Jason Lemkin (SaaStr)]] — source summary
- [[Jason Lemkin]] — originates and describes this methodology in detail
- [[SaaStr]] — company where this loop was applied across 20 agents
- [[Delphi]] — first agent this loop was applied to (SaaStr's general-purpose "Deli" clone)
- [[Artisan]] / [[Qualified]] — vendors whose agents were trained via this loop
- [[Forward Deployed Engineer]] — the vendor-side role that often assists with this loop
- [[Chief Orchestration Officer]] — the internal role responsible for running this loop across many agents
