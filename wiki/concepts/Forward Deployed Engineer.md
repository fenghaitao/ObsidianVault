---
title: "Forward Deployed Engineer"
type: concept
tags: [job-role, ai, future-of-work, agents]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/08 - AI predictions： Job markets, Codex beats Claude, and the death of org charts ｜ Dan Shipper.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/07 - The most rational take on AI you’ll hear this year.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/27 - The rise of the professional vibe coder (a new AI-era job).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/35 - We replaced our sales team with 20 AI agents—here’s what happened next ｜ Jason Lemkin (SaaStr).md"]
last_updated: 2026-07-11
---

## Definition

A "forward deployed engineer" is a person (or small team) whose job is to set up and continuously maintain a company's shared AI agent — the new job role [[Dan Shipper]] says has emerged directly from the principle that "[[Automation Is A Lie|every agent needs a human]]."

## Key Information

- Dan Shipper argues this role is durable, not transitional: as models get more capable and the number of agents grows, someone still has to manage them — "automation was supposed to take away jobs, but it looks like it just created one or many."
- At [[Every]], [[Nitesh]] fills this role, spending much of his time in Slack correcting and directing the internal agent [[Claudie]], which runs Every's consulting practice.
- Dan Shipper says even the large model companies themselves run internal teams of people managing their own internal agents, and does not expect those teams to go away.
- Distinguished from "babysitting": Dan Shipper reframes it as "building a whole system that makes it so that people who have less knowledge can use that system without doing something dumb" — an engineering challenge, not passive supervision. Example: a data-science bot hooked up to a company's data warehouse (with proper permissioning) that a forward-deployed team builds and maintains so the core data science team isn't swamped with basic questions.
- Every also offers this as a consulting service to other companies.
- Per [[Benedict Evans]] (episode 07): offers a complementary, earlier-stage framing — he explains the rise of forward-deployed-engineer hiring at [[Anthropic]] and [[OpenAI]] as essentially professional-services/consulting labor by another name ("a forward deployed engineer is like an Accenture outsourced software developer who lives in San Francisco"). Evans's point: reimagining a client company's internal workflows around AI (deciding what to automate, how to plug new AI systems into existing vertical/horizontal systems, retraining staff) is a large custom project needing dedicated people — comparable to why companies hire Bain, McKinsey, or Accenture rather than keeping that expertise permanently in-house. This is offered as the underlying economic reason AI labs are *increasing* headcount rather than shrinking, even as their models get more capable.

## Related

- [[summary-08 - AI predictions： Job markets, Codex beats Claude, and the death of org charts ｜ Dan Shipper]] — source summary
- [[Dan Shipper]] — articulates this role and its durability
- [[Every]] — company where this role is staffed
- [[Nitesh]] — engineer who fills this role at Every
- [[Claudie]] — agent this role is responsible for maintaining
- [[Automation Is A Lie]] — the underlying thesis behind this role's necessity
- [[AI Job Apocalypse]] — myth this role is cited as evidence against
- [[summary-07 - The most rational take on AI you’ll hear this year]] — source summary (Benedict Evans episode)
- [[Benedict Evans]] — offers the professional-services framing of this role
- [[Anthropic]] — AI lab hiring forward-deployed-engineer-style talent
- [[OpenAI]] — AI lab hiring forward-deployed-engineer-style talent

## Key Information (episode 27 — Lazar)

- [[Lazar]], describing the general convergence of engineer/PM/designer roles under AI, lists "forward deployed engineer" as one of several near-synonymous emerging titles (alongside "AI assistant engineer," "LLM engineer," "rapid engineer," and "vibe coder") for people whose core job is directing AI tools for raw output — arguing the specific label matters less than the underlying judgment applied. See [[Role Collapse]] and [[Professional Vibe Coder]].

## Related (episode 27 additions)

- [[summary-27 - The rise of the professional vibe coder (a new AI-era job)]] — source summary
- [[Lazar]] — cites this term as one of several converging AI-era job labels
- [[Professional Vibe Coder]] — closely related emerging job-role concept
- [[Role Collapse]] — the broader convergence this term is cited as an example of

## Key Information (episode 35 — Jason Lemkin)

- [[Jason Lemkin]] treats the FDE as the single most important vendor-selection criterion for AI go-to-market tools: "you got to do another column which is your forward deployed engineer... before you write a check, get on the phone with [them] and see if [they're] really going to do deployment." A best-in-class product with no implementation help is, in his view, not what "99% of people should buy," because agents require ~30 days of hands-on training to work at all (see [[Agent Training Loop]]).
- Concrete evidence: [[SaaStr]] chose [[Artisan]] and [[Qualified]] specifically because they offered hands-on FDE-style help, while a rival vendor wanted $100K upfront and another refused to be SaaStr's first customer.
- Traces the term's modern usage to [[Palantir]], where FDEs work in "an army" on-site for months at a time on nine-figure deals — Lemkin says most companies (including SaaStr) need a smaller-scale version of this same idea, not Palantir's exact model.
- Draws an explicit structural contrast with the classic SaaS sales-engineer (SE) model: historically, SEs were a scarce shared resource (e.g., one SE supporting eight reps, who had to compete for that SE's time). The FDE model inverts this — the FDE's number-one job is making the *customer* successful, not supporting the sales rep; sales' job becomes managing procurement around an FDE-led, already-successful deployment.
- Illustrates with an AI vendor that closed a $3 million deal where the FDE handled the entire on-site deployment and tuning while sales only managed procurement — "that's pretty different than a guy answering some questions for the humans."
- Notes the ideal FDE profile: doesn't need to be a professional engineer, but needs real product chops — Lemkin's favorite type is "kind of like mediocre engineers that are ... in love with the product" rather than people who still primarily want to write code.
- Frames FDE quality as the actual explanation for the difference between the ~5% success rate of AI agent deployments in 2024 and the near-100% success rate SaaStr now targets: "when you go live, it works. That's the difference."
- Cites [[Marc Benioff]]'s statement that Salesforce now runs roughly 2,000 people in this function, framing it as Salesforce reverting to the hands-on, high-touch customer relationship it had ~20 years ago before that model faded.

## Related (episode 35 additions)

- [[summary-35 - We replaced our sales team with 20 AI agents—here’s what happened next ｜ Jason Lemkin (SaaStr)]] — source summary
- [[Jason Lemkin]] — frames FDE quality as the top vendor-selection criterion for AI GTM tools
- [[SaaStr]] — company whose vendor choices were driven by FDE availability
- [[Artisan]] / [[Qualified]] — vendors chosen partly for their FDE-style support
- [[Palantir]] — originator of the modern large-scale FDE model
- [[Marc Benioff]] / [[Salesforce]] — cited running ~2,000 people in this function
- [[Agent Training Loop]] — the training process FDEs are often hired to help execute
- [[Chief Orchestration Officer]] — the customer-side counterpart role to the vendor-side FDE
