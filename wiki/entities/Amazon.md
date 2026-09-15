---
title: "Amazon"
type: entity
tags: [company, FAANG, tech, e-commerce, cloud]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20240708 - Getting To Staff (IC6) at FAANG Panel (Full, Feb 2024).md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20240708 - Getting To Staff (IC6) at FAANG Panel (Full, Sept 2023).md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20250301 - Amazon Principal Engineer (L7)： Layoffs, Interviewing & Career Growth ｜ Steve Huynh.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story).md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20250421 - Meta Staff Eng (IC6) Promotion by 28 ｜ Rahul Pandey.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20250501 - Industry Secrets We Wish We Knew Before Graduating (Staff Engs Talk at UCLA).md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20251229 - Best Software Engineering Career Advice of 2025.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260302 - Distinguished Eng： Stack Ranking, Competing with Bezos, Regrets ｜ Bryan Cantrill.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260330 - Retired Amazon VP： How Corporate Politics Work And How To Win ｜ Ethan Evans.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker.md"]
last_updated: 2026-09-14
---

## Definition

Amazon is a multinational technology company focused on e-commerce, cloud computing (AWS), and digital streaming. It is one of the FAANG companies.

## Key Information

- Zach Wilson worked at Amazon from 2012 to 2021 and benefited from significant stock price appreciation during that period
- Lee worked at Amazon as an SDE2, moved into people management, and was promoted to L6 (Senior Engineer equivalent) as a manager
- Lee's first three promotion attempts to Senior SDE3 all failed; the first try to get to L6 as a manager also failed
- Lee's most technically complex IC work at Amazon involved writing a custom class loader to solve Android's method limit problem, allowing multiple DEX files in an app before Google officially supported it
- This work was for Amazon Video (now Prime Video) and the combination of Shopping, App Store, and Video apps that exceeded the Android method limit
- Amazon's promotion process for L6 did not use formal committees — decisions were made by skip-level managers (senior manager through senior, director for principal)
- Amazon's leveling: SDE3 is Senior, there is no "Staff" vocabulary — the level after Senior at Amazon is Principal
- Lee emphasized that even at Amazon where there weren't promotion panels, the manager still couldn't unilaterally promote someone — higher levels required higher management approval
- Ryan Peterman accepted Amazon's offer after failing all other onsites, receiving it through an unusual SAT-like logic puzzle interview process where Amazon came to UCLA and booked a room for hundreds of applicants
- Steve Huynh spent 18 years at Amazon, progressing from green badge (contractor) Support Engineer to Principal Engineer (L7)
- Amazon uses color-coded badges: blue badge (full-time employee), green badge (contractor/temp), yellow badge (vendor)
- Amazon's performance management has historically targeted ~5-6% of employees managed out per year, shifting from soft guidance to harder mandate in recent years
- Amazon has a strong operational culture with on-call rotations and emphasis on operational excellence
- The writing culture is a core part of Amazon: meetings start with 30 minutes of silent reading of a six-page document before discussion
- Customer Obsession was the highest priority under Jeff Bezos, from interns to VPs
- Amazon is known for frugality (one of the Leadership Principles), sometimes taken to extremes (e.g., difficulty getting adequate hardware)
- The SDE1 to SDE2 promotion is about independence; SDE2 to SDE3 is about ownership; SDE3 to Principal is about cross-team influence
- Amazon effectively skips a staff level — the gap from SDE3 (Senior) to L7 (Principal) is like jumping two levels, making it notoriously difficult
- The promotion process for Principal changed three times during Steve Huynh's 4-year attempt (2016-2020)
- Amazon promotions and performance reviews are decoupled processes; an engineer can be high-performing at principal-level work but flagged as low-performing at SDE3
- People who couldn't make the SDE3 to Principal jump at Amazon have gone to Meta and Google and thrived as Staff/Senior Staff/Principal
- SDE1 is not a terminal level — there is an "up or out" expectation within ~2 years; SDE2 is debated as a terminal level
- Ryan Peterman described Amazon as "the lowest tier of the FAANG ones" at the time, though his LinkedIn was "blowing up" with recruiter interest after joining
- Ryan floundered at Amazon for the first 8 months, realizing he wasn't learning and didn't know what growth to the next level looked like, which motivated him to apply broadly and end up at Meta
- In the 2025 advice compilation, a guest who "always preferred high growth" recalled Amazon growing ~100-fold (from roughly 10,000 people to a million) with revenue up ~80x while he was there, calling his career ladder "an escalator" that moved up beneath him

### Bryan Cantrill on AWS / Amazon
- Amazon "hit the mother lode" by letting S3 and EC2 be developed and realizing it was cloud-first before anyone else; there was luck involved, but the execution was relentless.
- During the ~2015 re:Invent era every event brought a price cut and new services, which made the cloud look like a terrible business to would-be competitors.
- Amazon did not break out AWS revenue — "we're not talking about that" — obscuring how good the margins actually were; having competed with it at Joyent, Cantrill says "the margins on this thing are great."
- Cantrill calls Jeff Bezos "an apex predator in capitalism" for pressing Amazon's advantage rather than milking it: "I'm going to make it so no one can compete with me... I'm going to do it by giving a great product at a reasonable price." He notes re:Invent no longer offers the same "can't live without" new services and price cuts ([[summary-20260302 - Distinguished Eng： Stack Ranking, Competing with Bezos, Regrets ｜ Bryan Cantrill]]).

### Ethan Evans on Amazon Politics
- Post-era Amazon reportedly wrote down a director threshold of ~90 people in some orgs, despite the leadership principle "there's no bonus for additional head count."
- Amazon grew from ~14,000 people when Ethan joined to 1.4 million when he left (a hundredfold), which opened doors that a 5–10%-a-year company never would.
- Andy Jassy, running AWS then the company, would "absolve" a few principal engineers of mentoring/architecture duties so they could solve the hardest problems — leverage over politics.
- Amazon Cloud Drive began as an idea from an entry-level new-grad engineer who pitched it to Jeff Bezos at a poster session; Amazon Fire TV similarly came from a not-super-senior person's legwork.

### Marc Brooker and Mike Stonebraker on Amazon
- Marc Brooker notes that "writing forces a level of mental clarity that speaking, making slide decks, etc. doesn't" is a core belief held culturally at Amazon; Al Vermeulen (an early AWS engineer) was CTO of Amazon for a period.
- Mike Stonebraker gave a talk at Amazon (~3 years prior) telling them they support ~15 database systems — about 12 too many; he argues most are outperformed by another of their own systems, and any database that isn't performant in a big-enough market should be retired.

## Related

- [[summary-20260330 - Retired Amazon VP： How Corporate Politics Work And How To Win ｜ Ethan Evans]] — source summary
- [[Ethan Evans]] — the VP describing these mechanics
- [[Corporate Politics]] — the theme
- [[Empire Building]] — the headcount threshold
- [[summary-20240708 - Getting To Staff (IC6) at FAANG Panel (Full, Feb 2024)]] — source summary
- [[summary-20240708 - Getting To Staff (IC6) at FAANG Panel (Full, Sept 2023)]] — source summary
- [[Steve Huynh]] — Principal Engineer who spent 18 years at Amazon
- [[Zach Wilson]] — engineer who worked at Amazon 2012-2021
- [[Lee]] — engineer and manager who worked at Amazon
- [[Ryan L. Peterman]] — worked at Amazon for 8 months
- [[Prime Video]] — product Lee and Steve worked on
- [[Kindle]] — product Steve worked on
- [[Staff Engineer]] — the L6 level at Amazon (though Amazon uses different vocabulary)
- [[Amazon Leadership Principles]] — the cultural framework
- [[Amazon Bar Raiser]] — interviewer training program
- [[Amazon Performance Improvement Plan]] — Amazon's PIP process
- [[Amazon Writing Culture]] — six-page document and reading culture
- [[Amazon Promotion Process]] — the promotion gauntlet
- [[Amazon Leveling]] — SDE1 through Principal
- [[Stack Ranking]] — performance management approach
- [[Customer Obsession]] — core leadership principle
- [[Frugality]] — leadership principle
- [[Promotion By Committee]] — how Amazon handled promotions differently
- [[Feedback Reception]] — how Lee handled promotion rejection
- [[summary-20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story)]] — source summary
- [[summary-20250421 - Meta Staff Eng (IC6) Promotion by 28 ｜ Rahul Pandey]] — source summary
- [[summary-20251229 - Best Software Engineering Career Advice of 2025]] — source summary (high-growth escalator)
- [[summary-20260302 - Distinguished Eng： Stack Ranking, Competing with Bezos, Regrets ｜ Bryan Cantrill]] — source summary (AWS economics)
- [[Bryan Cantrill]] — the apex-predator framing
- [[summary-20260413 - AWS Distinguished Eng： Learning From 3000 Incidents And How Engineering Is Changing ｜ Marc Brooker]] — source summary
- [[Marc Brooker]] — on writing culture and Al Vermeulen
- [[summary-20260420 - Turing Award Winner： Disagreeing with Google, Postgres, Future Problems ｜ Mike Stonebraker]] — source summary
- [[Michael Stonebraker]] — on Amazon's 15 database systems
- [[Al Vermeulen]] — former CTO of Amazon
