---
title: "Taste & Craft： A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @pragmaticengineer"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260421 - Taste & Craft： A Conversation with Tuomas Artman, CTO Linear & Gergely Orosz, @pragmaticengineer.md"
date: 2026-04-21
ingested: 2026-06-26
tags: [talk, quality, taste, linear, ai-agents, product-engineering, software-craft, bug-fixing, claude-code]
---

## Core Thesis
Tuomas Artman (CTO of Linear) and Gergely Orosz (@pragmaticengineer) argue that as AI agents make shipping software trivially easy, the pendulum has swung too far toward shipping everything without thinking. The real competitive advantage shifts to taste, craft, and quality — saying no to 999 things and yes to one. Linear's practices (Quality Wednesdays, Zero Bug Policy, customer proximity) demonstrate how to build tasteful software at scale even as AI accelerates development.

## Key Topics
- **The pendulum swinging too far**: AI agents can now ship every feature request immediately, but shipping without thinking leads to convoluted, confusing software. Steve Jobs' principle of saying no to 999 things to say yes to one is more relevant than ever.
- **Hypergrowth and quality**: Tuomas draws on his Uber experience where winner-takes-all dynamics forced shipping at all costs, sacrificing quality. In an AI world where everyone can ship fast, quality becomes the differentiator — but it degrades gradually, not overnight, making it hard to measure and easy to ignore.
- **Linear's approach to feature requests**: Linear receives tons of feature requests but rarely ships them as-is. Instead they talk to customers, group requests, find root causes, and design a single perfect solution. AI helps summarize and group requests but doesn't replace the thinking.
- **AI for bug fixing at Linear**: 10% of bugs are automatically fixed by single-shot AI — when a bug is reported, an agent creates a PR and lands it without engineer involvement. Tuomas foresees this approaching 100% in the next few years.
- **Claude Code critique**: Tuomas notes that Anthropic's claim of Claude Code being built by Claude is visible in the product — small bugs appear within seconds of use, it's slow, and behaves unexpectedly. This is a side effect of moving too fast in a competitive market.
- **Measuring quality is hard**: At Uber, revenue was the golden metric that everyone optimized for. Quality didn't affect revenue until it did — when Lyft launched a competing product at the same price point, users gradually migrated to the higher-quality app. No A/B test can measure this; it happens slowly over time.
- **Quality Wednesdays**: Every Wednesday, the entire Linear engineering team (remote, ~25 engineers) gathers for 30 minutes. Each engineer shows one quality fix they found themselves — from one-pixel changes to backend efficiency improvements. Started when Tuomas found 35 problems in a single small UI menu. To date, Linear has fixed 2,500-3,000 small quality details. The side effect: engineers are always on the lookout for quality issues because they know they need a fix for Wednesday.
- **Zero Bug Policy**: Every reported bug is assigned immediately and becomes the assignee's highest priority. Bugs are fixed within hours, typically within 2-3 hours. Linear spent three weeks fixing all bugs to get to zero, then enforced immediate fixing. The insight: the rate of bug creation is constant, so fixing immediately costs no more than fixing months later. Users get excited when a bug they reported is fixed two hours later.
- **AI has no taste**: AI doesn't feel time, doesn't know what a good animation feels like, and can't experience user frustration. It can implement all the right technical pieces but produces unnatural-feeling results. Emil (Linear design engineer) demonstrated this: agents built animations correctly but they felt wrong — wrong easing, wrong timing. Human touch made them feel natural.
- **Hiring for taste**: Linear does a full-week paid trial with every candidate, where they implement a greenfield project from start to finish. This self-selects for people who care about quality. Very few hiring misses as a result.
- **Customer proximity**: Linear has Slack channels with all big customers, open to any engineer. Every customer meeting is recorded and tagged. Engineers are exposed to a "fire hose" of customer feedback — they can't escape feeling customer pain or joy.
- **The future: everyone becomes a product engineer**: In four years, if AI growth continues, engineers won't be needed to pipe data around. They'll need to know what customers want, what good UX looks like, and be mini-PMs. Tuomas recommends reading Apple's Human Interface Guidelines and building things for real users.

## Entities
- [[TuomasArtman]] — CTO of Linear, former Uber engineer
- [[GergelyOrosz]] — @pragmaticengineer, interviewer, author of The Pragmatic Engineer
- [[Linear]] — project management tool known for high-quality software
- [[Uber]] — ride-sharing company where Tuomas previously worked
- [[Lyft]] — Uber competitor, example of quality-driven market shift
- [[SteveJobs]] — Apple co-founder, quoted on saying no
- [[ClaudeCode]] — Anthropic's coding agent, critiqued for quality issues
- [[Anthropic]] — creator of Claude Code
- [[aiDotEngineer]] — conference hosting the talk

## Concepts
- [[QualityWednesdays]] — Linear's weekly team practice for finding and fixing quality issues
- [[ZeroBugPolicy]] — fixing every bug immediately rather than backlogging
- [[AIAndTaste]] — AI's fundamental inability to have taste or feel user experience
- [[ProductEngineer]] — the evolving role combining engineering with PM and customer skills
- [[CustomerProximity]] — exposing all engineers directly to customer feedback
- [[CompetitionThroughQuality]] — quality as a slow but inevitable competitive differentiator
- [[SayingNo]] — the discipline of rejecting feature requests to maintain product coherence
- [[Hypergrowth]] — the winner-takes-all shipping dynamic that sacrifices quality
- [[Taste (Software)]] — human ability to distinguish quality from AI-generated output

## Related
- [[summary-20260417 - State of the Claw — Peter Steinberger]] — also discusses taste as key moat
- [[summary-20260418 - The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil]] — also discusses quality and agent limitations
- [[summary-20260416 - Building pi in a World of Slop — Mario Zechner]] — critique of Claude Code
- [[summary-20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary]] — also references Linear
