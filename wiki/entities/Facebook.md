---
title: "Facebook"
type: entity
tags: [company, social-media, big-tech, Meta]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20251130 - Robinhood SWE Turned $1B+ Founder： Non-Linear Careers, Being Jaded About Promos, Startup Learnings.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20251215 - Boris Cherny (Creator of Claude Code) On What Grew His Career And Building at Anthropic.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20251222 - Frontline Manager at Meta to Senior Director at Snapchat in 3 Years (Career Story).md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260104 - Anthropic Eng Leader： Mentorship Advice, Microsoft vs Facebook, Career Learnings ｜ Fiona Fung.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260202 - Instagram iOS Principal Eng (IC8)： Building IG Stories, 1 Promo Per Half, Small Teams.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260209 - Meta Distinguished Eng (IC9)： Influencing Engs, Failures, and Learnings ｜ Adam Ernst.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260309 - OpenAI Codex Tech Lead： How His Career Grew And How He Uses Codex ｜ Michael Bolin.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260323 - The Co-Creator of Kubernetes： Engineering-Led Direction and Convincing Management ｜ Brendan Burns.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260504 - Meta Superintelligence Labs (MSL) Eng Director： Promo Hacking, Industry Shifts, Regrets ｜ John White.md"]
last_updated: 2026-09-14
---

## Definition

Facebook is the social network (now part of Meta) where Jay Jo interned and where Boris Cherny spent much of his Meta career.

## Key Information

- Jay's "cream of the crop" internship target during college (alongside Google), though the internship itself felt impersonal
- A lucky "number of islands" LeetCode problem secured Jay's Facebook internship and, downstream, much of his later career
- Boris Cherny later built "chats and groups" (bridging Messenger and Facebook) there, volunteered Facebook Groups for the Comet rewrite, and led the "public groups" project that earned him IC7
- Facebook Groups was the single biggest product surface in all of Facebook
- Culture rewarded generalists (engineers doing UXR, design, and product work) and hid titles behind a uniform "software engineer"
- The Snapchat-director guest joined Facebook around 2009 as a frontline manager in its fast-growth years; a critical cultural philosophy he learned there is that everyone who works in engineering must stay technical — even VP-level hires went through the six-week boot camp writing and reviewing code (a contrast with IBM, where VPs no longer coded)
- Fiona Fung joined Facebook in 2015 to build Facebook Marketplace; the early Marketplace ran weekly sprints with the first version on www.fas.com, and the office culture was captured by a poster, "nothing at Facebook is somebody else's problem" — everyone leans in to help regardless of role
- Fiona found Facebook felt much smaller than Microsoft and far faster (weekly vs ~4-week sprints); over time its culture changed as it grew

- Facebook's early (~2011-12) "data science" team of ~20 statisticians and early-ML researchers built the A/B testing and data-measurement infrastructure; the "data scientist" title was later reused for product analytics around 2014.
- Early Facebook culture was bottoms-up with a heavy hackathon culture — Adrien Friggeri did about six hackathons in his first six months ([[summary-20260112 - New Grad to Principal Engineer (IC8) at Meta (Career Story) ｜ Adrien Friggeri]]).

- Ryan Olson failed his 2011 Facebook interview from nerves (the question was later banned), but later joined Instagram (a Facebook company) at IC4 and grew to IC8; he used beta blockers to manage interview anxiety
- Via later antitrust litigation, internal communications revealed tension between Facebook and Instagram leadership — Facebook feared Instagram cannibalizing its users, and Mark Zuckerberg's internal memo surfaced on keeping the Instagram founders

### John Myles White's Facebook Chapter
- Joined a "data science" team that was split into core data science and data science infrastructure around when he arrived; he wanted core data science but loved collaborating with the infrastructure side that owned the experimentation tools.
- Was affiliated with the researchy division whose "Emotional Contagion in Social Networks" PNAS paper became "the absolute singular worst piece of PR for Meta" that year; the paper's author held a company-wide apologetic Q&A.

### Adam Ernst's Facebook Chapter

- Joined Facebook in 2012 as an E5, "literally weeks before the IPO," during the cultural shift from the HTML5 "Faceweb" app to native code.
- All the iOS engineers could meet in one conference room; the native-code rewrite created big opportunities and many scaling problems.
- His first major project replaced Apple's Core Data, on which the native rewrite had just launched.

### Michael Bolin's Facebook Chapter
- Joined Facebook expecting it to build a phone with HTC — forking Android with a hard deadline (shipped to HTC on ~March 1st) after the HTML5 "Faceweb" app clearly wasn't working and mobile became make-or-break.
- Built Buck during a hackathon because the inherited contractor Android code's build (Ant-based, no modularization) was too slow and painful to iterate on; he framed it as "an Android build system" rather than a company-wide takeover to reduce friction.
- Found Facebook's bottoms-up, hackathon-heavy culture meant almost nobody said "no" to his side project, in contrast with Google.
- Later championed Nuclide, the React-based desktop IDE for iOS, because Facebook was "the React company" and Xcode couldn't scale to Facebook's giant app.
- Facebook paid attention to the biggest scaling problems in mobile dev tools before anyone else had them (Buck, Nuclide, the Eden/Miles monorepo work) — "real business value," not science projects.

### In the Kubernetes Origin Story
- Brendan Burns says Google "talked to people at Facebook" about scale-out infrastructure and found "they were all building this stuff" — evidence that Google's orchestrator approach wasn't a secret.

## Related
- [[summary-20260323 - The Co-Creator of Kubernetes： Engineering-Led Direction and Convincing Management ｜ Brendan Burns]] — source summary
- [[Kubernetes]] — the project Facebook was independently building toward
- [[summary-20260209 - Meta Distinguished Eng (IC9)： Influencing Engs, Failures, and Learnings ｜ Adam Ernst]] — source summary
- [[Adam Ernst]] — joined weeks before the IPO
- [[ComponentKit]] — his later iOS framework
- [[Core Data]] — the framework his early project replaced

- [[Rome]] — joined Facebook ~2009 as a frontline manager
- [[Fiona Fung]] — joined Facebook in 2015 for Marketplace
- [[Facebook Marketplace]] — the commerce product she helped build
- [[Snapchat]] — company whose culture she compared to Facebook
- [[summary-20251222 - Frontline Manager at Meta to Senior Director at Snapchat in 3 Years (Career Story)]] — source summary
- [[summary-20260104 - Anthropic Eng Leader： Mentorship Advice, Microsoft vs Facebook, Career Learnings ｜ Fiona Fung]] — source summary
- [[summary-20251130 - Robinhood SWE Turned $1B+ Founder： Non-Linear Careers, Being Jaded About Promos, Startup Learnings]] — source summary
- [[summary-20251215 - Boris Cherny (Creator of Claude Code) On What Grew His Career And Building at Anthropic]] — Boris Cherny's Facebook chapter
- [[Jay Jo]] — interned at Facebook
- [[Boris Cherny]] — principal-engineer career at Meta
- [[Comet]] — the facebook.com rewrite
- [[Messenger]] — the org Facebook clashed with
- [[Instagram]] — sibling Meta app
- [[Pinterest]] — Jay's contrasting internship
- [[Ryan Olson]] — failed a Facebook interview, then rose at Instagram
- [[Mark Zuckerberg]] — internal memo on Facebook–Instagram tension
- [[Instagram]] — the sibling that created friction
- [[summary-20260202 - Instagram iOS Principal Eng (IC8)： Building IG Stories, 1 Promo Per Half, Small Teams]] — source summary
- [[summary-20260309 - OpenAI Codex Tech Lead： How His Career Grew And How He Uses Codex ｜ Michael Bolin]] — source summary
- [[Michael Bolin]] — the Facebook phone, Buck, and Nuclide
- [[Buck]] — the hackathon-born build system
- [[Nuclide]] — the React-based IDE
- [[HTC]] — the phone partner
- [[summary-20260504 - Meta Superintelligence Labs (MSL) Eng Director： Promo Hacking, Industry Shifts, Regrets ｜ John White]] — source summary (John Myles White)
- [[John Myles White]] — joined the data science team
- [[Deltoid]] — the A/B testing framework he built
