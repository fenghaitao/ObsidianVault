---
title: "Boris Cherny"
type: entity
tags: [person, claude-code, anthropic]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/04 - What happens after coding is solved ｜ Fiona Fung (Claude Code & Cowork).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/02 - The rise of taste, human authenticity and judgment in an AI world ｜ Adam Mosseri (Head of IG).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/23 - The design process is dead. Here’s what’s replacing it. ｜ Jenny Wen (head of design at Claude).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny.md"]
last_updated: 2026-07-11
---

## Definition

Head of [[Claude Code]] at [[Anthropic]], overseen by [[Fiona Fung]]; created Claude Code roughly a year before his own episode, starting as a personal side project ("Claude CLI") that became Anthropic's (and one of the industry's) fastest-growing products. Born in Odessa, Ukraine; grew up self-taught in programming; briefly left Anthropic for [[Cursor]] before returning after two weeks.

## Key Information

- Left Anthropic for Cursor (impressed by the team and product), but realized within about two weeks that he missed Anthropic's safety mission specifically — the thing that drew him to Anthropic originally and something he says he personally needs to be happy at work, no matter how exciting the alternative work is.
- Built the first version of Claude Code solo over roughly two months of prototyping (one month exploring model capabilities, one month doing post-training work to understand the research side) before starting to prototype what became Claude Code; the earliest demo showed the model correctly using a bash tool to answer "what music am I listening to" with no explicit instruction on how.
- Deliberately built it in a terminal — originally just the fastest way for a solo builder to prototype, later kept because the model was improving so fast no other form factor could be justified as durable; an early internal announcement post got only two "likes."
- Claude Code was not an immediate hit even after external launch in February 2025 — adoption took months to build, growing from writing ~20% of Boris's code in February to ~30% by May, before crossing 100% in November (when he stopped hand-editing code entirely).
- Cites Anthropic's engineering-wide productivity gains as roughly 4x team size with a 200% increase in pull requests per engineer — numbers he calls unprecedented compared to his prior experience owning code-quality/productivity at Meta (Facebook, Instagram, WhatsApp), where a few percentage points of annual gain was typical.
- Claude reviews 100% of pull requests at Anthropic automatically, with a human review layer still on top for anything beyond throwaway prototype code.
- Describes the next frontier beyond coding (which he considers "virtually solved") as Claude generating its own ideas from feedback/bug reports/telemetry, and expansion into non-coding agentic work via [[Claude Cowork]] (used personally for project management, paying a parking ticket, syncing spreadsheets and Slack messages).
- Cites [[Latent Demand]] as "the single most important principle in product," in two forms: the traditional form (watching what people hack a product into doing, e.g. [[Facebook Marketplace]] and Facebook Dating, both originated at Meta under [[Fiona Fung]]) and a newer, model-side form — "look at what the model is trying to do and make that a little bit easier" (internally called being "on distribution") — which is how [[Claude Cowork]] originated, after noticing non-engineers ([[Brendan]], a data scientist, and many public examples: growing tomato plants, analyzing a genome, MRI analysis, recovering wedding photos) jamming Claude Code's terminal into non-coding use cases.
- States a core design philosophy: don't box the model into rigid workflows/orchestration — give it tools and a goal and let it decide how to use them. See [[Don't Box The Model In]] and [[Bitter Lesson]].
- Advises building for the model 6 months in the future, not the model of today — see [[Build For The Model 6 Months Out]] — citing this as the deliberate bet behind Claude Code's early low code-quality trust that paid off once Opus 4/Sonnet 4 arrived.
- Advocates giving engineers as many tokens as possible without early cost-optimization (only optimize once an idea has proven itself at scale) and deliberately under-resourcing early projects to force creative use of Claude — see [[Under-Resourcing Principle]].
- Describes three layers of AI safety work at Anthropic: alignment/mechanistic interpretability (studying neurons directly, crediting [[Chris Olah]] as the field's inventor), evals (synthetic "petri dish" testing), and real-world deployment feedback — the reason Claude Code and Cowork were both released as early, clearly-labeled "research previews." See [[AI Safety Three Layers]].
- Describes Anthropic's practice of open-sourcing safety-relevant tooling (e.g., an open-source sandbox usable by any agent, not just Claude Code) as "[[Race To The Top]]" — designed to lift safety practices industry-wide, not just at Anthropic.
- Uses the printing press (not just AI-specific analogies) as his preferred historical analogue for the current moment — see [[Printing Press Analogy]].
- Personal practices: always has ~5 Claude agents running in parallel ("multi-clauding" — see [[Multi-Clauding]]); starts ~80% of tasks in "[[Plan Mode]]"; uses the most capable model available (currently Opus 4.6) rather than a cheaper one, since a less capable model often costs more tokens overall due to more correction cycles.
- Personal/lightning-round notes: recommends [[Functional Programming in Scala]], *Accelerando* by [[Charles Stross]], and *The Wandering Earth* by [[Cixin Liu]]; enjoyed Netflix's *3 Body Problem*; loves the *Acquired* podcast (recommends the Nintendo episode); life motto "use common sense"; makes his own miso (a hobby from living in rural Japan before Anthropic, prized for teaching him to think on long multi-year timescales) and jokes he'd return to full-time miso-making post-AGI.
- Coincidentally born in Odessa, Ukraine, like [[Lenny Rachitsky]] (discovered during the recording); his grandfather was an early Soviet programmer who worked with punch cards and never saw the transition to software.
- Team hiring philosophy: values generalists who cross disciplines (engineers with product/design/business sense) over narrow specialists; predicts the "software engineer" job title will start being replaced by "builder" as PM/design/engineering roles increasingly overlap (~50% overlap already, in his estimate).

## Related

- [[summary-04 - What happens after coding is solved ｜ Fiona Fung (Claude Code & Cowork)]] — source summary
- [[summary-02 - The rise of taste, human authenticity and judgment in an AI world ｜ Adam Mosseri (Head of IG)]] — source summary (Adam Mosseri episode)
- [[summary-17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming]] — source summary
- [[summary-23 - The design process is dead. Here’s what’s replacing it. ｜ Jenny Wen (head of design at Claude)]] — source summary
- [[summary-25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny]] — source summary (his own episode)
- [[Fiona Fung]] — manager who oversees him
- [[Claude Code]] / [[Claude Cowork]] — products/team he leads
- [[Anthropic]] — employer
- [[Cursor]] — brief (2-week) employer between Anthropic stints
- [[Latent Demand]] — principle he calls the most important in product
- [[Don't Box The Model In]] / [[Bitter Lesson]] — his model-design philosophy
- [[Build For The Model 6 Months Out]] — his product-timing philosophy
- [[Under-Resourcing Principle]] — his team-resourcing philosophy
- [[AI Safety Three Layers]] / [[Race To The Top]] — his framing of Anthropic's safety practices
- [[Printing Press Analogy]] — his preferred historical analogy for this moment
- [[Multi-Clauding]] / [[Plan Mode]] — his personal Claude Code usage patterns
- [[Chris Olah]] — credited with inventing mechanistic interpretability
- [[Brendan]] — data scientist whose terminal use inspired Claude Cowork
- [[Instagram]] — former colleague of Adam Mosseri and Boris's prior employer
- [[Adam Mosseri]] — former colleague, Head of Instagram
- [[Simon Willison]] — cited alongside him for coding-from-phone habits
- [[Jenny Wen]] — cites his comment about Claude Code generating product ideas
