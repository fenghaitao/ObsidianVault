---
title: "Jason Lemkin"
type: entity
tags: [person, founder, sales, saastr, ai]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/35 - We replaced our sales team with 20 AI agents—here’s what happened next ｜ Jason Lemkin (SaaStr).md"]
last_updated: 2026-07-11
---

## Definition

Jason Lemkin is a two-time founder and the founder/CEO of [[SaaStr]] (rendered "Zaster"/"Saster" in transcript ASR), the largest B2B founder community. He is a featured guest on [[Lenny's Podcast]] (episode 35) discussing how he replaced SaaStr's ~10-person sales team with 1.2 humans and 20 AI agents, and was previously referenced (episode 33) as a case study by other guests before appearing himself.

## Key Information

### Background
- Sold his prior startup to Adobe; started a blog in 2012 documenting mistakes made after that sale, which grew into SaaStr — meetups starting 2015, SaaStr Annual (~10,000 attendees/year) since 2016, plus seven events in Europe (12 years/roughly 20 major events total).
- Has personally invested ~$200 million lifetime (~10x return) into founders from the SaaStr community, alongside running the media/events business (eight figures of annual revenue).
- Previously appeared on Lenny's Podcast about a year and a half before episode 35, in a widely shared episode about building a sales org — Lenny calls it "legendary."

### The AI go-to-market transition (episode 35)
- Trigger: at SaaStr Annual, two well-paid, long-tenured salespeople quit on site — "the third time I've done this, the eighth team I've built." Having already seen a general-purpose digital-clone agent ([[Delphi]], "Deli" in the transcript) autonomously close a $70,000 sponsorship, Lemkin told [[Amelia]] (SaaStr's Chief AI Officer), "We're done with hiring humans in sales. We're done."
- Result: SaaStr went from ~10 GTM staff (2-3 SDRs, up to 5 AEs) to 1.2 humans (one full-time AE plus Amelia at 20% time) plus 20 AI agents, each with a desk labeled with its agent nickname (Reply/[[Replit]], Quali/[[Qualified]], Arty/[[Artisan]]). Net productivity is "about the same" as the human team but far more efficient — "it scales because software scales."
- Explicitly says he'd still hire two more great humans tomorrow if available, but wouldn't hire another junior rep who, three months in, "doesn't know what SaaStr does" — his framing: "AI is replacing the jobs people don't want to do today, and it is displacing the midpack and the mediocre."
- Deployment sequence: general-purpose agent for support/inbound ([[Delphi]]) → outbound to lapsed high-value contacts ([[Artisan]]) → inbound qualification ([[Qualified]]) → [[Salesforce]] Agent Force for reactivating leads sales had deprioritized (70% response rate after training on a single distilled prompt).
- Vendor-selection philosophy: weight a vendor's willingness to provide hands-on [[Forward Deployed Engineer]] support as heavily as feature comparisons. Artisan and Qualified won SaaStr's business by "offering to help the most"; one rival vendor demanded $100K upfront, another declined to be SaaStr's first customer for fear of bad PR if the deployment failed.
- Describes the [[Agent Training Loop]] in detail: ingest a website/wiki/docs, train by answering the agent's clarifying questions, then correct its daily mistakes for ~30 days (roughly an hour or two a day) until it performs like a clone of your best salesperson's script.
- Scale claim: companies with as few as ~30,000 historical website visitors or leads already have enough volume to make agentic GTM worthwhile — the binding constraint is willingness to do the training work, not data volume. Illustrates with a call to a public B2B company "worth well over $10 billion" whose team had never actually trained an agent themselves and, unsurprisingly, had no working deployment.
- Coins/uses two central frameworks: "[[Plays Vs Playbooks]]" (the tactics still work, the blanket playbooks for applying them don't) and "[[Everyone In Market At Once]]" (in-market prospect share in hot AI categories has jumped from a historical 3-5%/year to 50%+).
- On the future of sales roles: predicts the classic email-cadence SDR and inbound-lead-qualifier roles will be "mostly extinct" within 12 months; AE roles are ~70% safe today but could fall to 40-50% within a year; field/in-person sales and complex enterprise negotiation remain largely AI-resistant. Floats a future where $250,000/year SDRs manage ~10 agents instead of 10 people.
- Practical advice for anyone worried about their job: personally pick one agentic tool, deploy and train it yourself for about a month (50-60 hours) — "if you can go do this and get it live into production, you're hyper employable."
- On outbound email quality: argues untrained AI is compared unfairly to an idealized human standard when most human sales emails are actually mediocre; trained on a company's single best template, AI email performs at or above the human median. Cites hundreds of thousands of sent AI emails where recipients "don't really care" that it's AI as long as it adds value and responds instantly.
- On managing a large agent fleet: describes it as a new, exhausting full-time role — Amelia spends 10-15 hours/week reviewing outputs because "agents work all night and they work weekends and they work on Christmas." Distinguishes this internal "[[Chief Orchestration Officer]]" role from the vendor-side Forward Deployed Engineer role, and is skeptical that "GTM engineer" is yet a well-formed hireable profession.
- Long-term vision: agents today are siloed per customer/segment; the future ("[[Hive Mind]]," explicitly borrowing from the TV show *Pluribus*) is agents sharing data and learnings across a company's entire customer base simultaneously — and frames [[Salesforce]]'s emergence as the shared data hub most competing AI GTM vendors plug into as an early instance of this pattern.
- Net effect on the sales profession: argues AI won't shrink total GTM headcount economy-wide because winning companies are growing so fast they'll need more humans even while being individually more efficient — cites [[Owner.Com]] CEO Kyle's target of $3-5M revenue per rep (up from an estimated $300-500K a few years ago) as one example, and cites an unnamed OpenAI leadership contact ("Maggie") saying OpenAI "can't hire enough enterprise reps."
- On layoffs: argues AI is mostly used as a cover story for unrelated headcount decisions ("it's probably not because you brought in 20 agents... it's probably because you just want to downsize anyway"), and that the bigger dynamic is roles simply not being backfilled with humans rather than active firing — he says he has never fired anyone in his career except for inappropriate conduct.
- Personal habits/asides: built 12+ apps on [[Replit]] over ~150 days (despite being unable to code), describing himself as a "top 1% user"; recommends the imaging tool Reve (app.reve.com) for marketing images; names *Pluribus* as his favorite recent show; recommends the SaaStr talk "Everything That Breaks on the Way to One Billion" (with Ben Chestnut, post-Mailchimp-acquisition) and Matt Plank/Sam Blonde's "Rippling's Secrets to Hyperrowth" talk as GTM-episode picks; advises founders not to abandon an already-successful startup to chase a "hotter" AI idea.

### Per episode 33 (referenced, not yet a guest)
- Per Lenny: Lemkin had 10 salespeople and replaced them with 1.2 humans plus 20 agents.
- One of the agents automatically tracked sales calls and updated Salesforce records on the team's behalf; a salesperson who turned out to have been doing little real work beyond that task realized the automation would expose it and quit before being confronted ("this will catch me, I got to get out of here"). (Episode 35 corroborates and expands this: the tracking tools are named Momentum and Attention, and Lemkin confirms the rep "hadn't done anything in 30 days.")
- Cited by Lenny as illustrating a broader theme from the episode: as agents take over busy-work, it becomes harder for underperforming employees to hide.

## Related

- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]] — source summary
- [[summary-35 - We replaced our sales team with 20 AI agents—here’s what happened next ｜ Jason Lemkin (SaaStr)]] — source summary
- [[Lenny Rachitsky]] — host; recounts this anecdote in episode 33, interviews him directly in episode 35
- [[Aishwarya Naresh Reganti]] — reacts to the episode-33 anecdote
- [[Kiriti Badam]] — reacts to the episode-33 anecdote
- [[SaaStr]] — company he founded and leads
- [[Amelia]] — SaaStr's Chief AI Officer, who orchestrates the 20 agents
- [[Delphi]] — platform behind SaaStr's general-purpose "Deli"/Digital Jason agent
- [[Artisan]] / [[Qualified]] — the two AI GTM vendors credited with SaaStr's early wins
- [[Salesforce]] / [[Marc Benioff]] — CRM and CEO discussed at length re: Agent Force and forward-deployed support
- [[Palantir]] — cited as originator of the "forward deployed engineer" model
- [[Owner.Com]] — cited example of AI-driven per-rep revenue efficiency
- [[Brian Halligan]] — inspiration for SaaStr's digital-clone agent
- [[Replit]] — platform he personally builds tools on as a "top 1% user"
- [[Forward Deployed Engineer]] — vendor-side implementation role central to his vendor-selection advice
- [[Agent Training Loop]] — the ingest/train/QA methodology he describes in detail
- [[Plays Vs Playbooks]] / [[Everyone In Market At Once]] — his two central 2026 GTM frameworks
- [[Chief Orchestration Officer]] — the internal agent-fleet-management role he describes
- [[Hive Mind]] — his long-term vision for cross-customer agent data sharing
