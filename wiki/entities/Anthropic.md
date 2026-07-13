---
title: "Anthropic"
type: entity
tags: [company, ai, claude, platform]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/04 - What happens after coding is solved ｜ Fiona Fung (Claude Code & Cowork).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/02 - The rise of taste, human authenticity and judgment in an AI world ｜ Adam Mosseri (Head of IG).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/06 - Tony Fadell： How to build real taste (and why AI makes it matter more).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/10 - How Anthropic, Costco, and Patagonia all build incorruptible companies ｜ Eric Ries.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/07 - The most rational take on AI you’ll hear this year.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/13 - How Anthropic’s product team moves faster than anyone else ｜ Cat Wu (Head of Product, Claude Code).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/16 - Head of Growth (Anthropic)： Anthropic is automating its own growth.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/27 - The rise of the professional vibe coder (a new AI-era job).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/40 - The $1B Al company training ChatGPT, Claude & Gemini on the path to responsible AGI ｜ Edwin Chen.md"]
last_updated: 2026-07-12
---

## Definition

Anthropic is the AI company that builds the Claude family of models and products, including [[Claude Code]] and [[Claude Cowork]]. [[Fiona Fung]] leads the engineering teams behind Claude Code and Claude Cowork at Anthropic, overseeing [[Boris Cherny]] and [[Cat Wu]]. [[Tony Fadell]] separately cites Anthropic (via a reported source-code leak) as a cautionary example about AI-generated code quality.

## Key Information

- Anthropic engineers ship, on average, roughly 8x as much code per quarter as they did in 2021-2025 — used internally as evidence that coding is no longer the throughput bottleneck for software teams.
- Internally, Anthropic frames its post-coding-bottleneck challenge as verification: as more roles (engineers, designers, PMs) check in code and throughput rises, the org invests in automated code review, spec-checked-into-repo validation, and quality frameworks like [[Bad Vs Sad Framework|"bad vs. sad"]] rather than manual review alone.
- Claude Code did not have automated Claude-based code review as recently as roughly a year before this conversation (per Fung); it has since become central to how the team scales review without a purely human bottleneck.
- Launched "Claude for Small Business," a bundle inside [[Claude Cowork]] aimed at non-technical small-business owners, which grew directly out of Fung's personal use of Cowork for expense/invoicing work and subsequent visits with small-business friends (an example of following "[[Latent Demand|latent demand]]").
- Launched "routines" (a [[Claude Cowork]] feature, per this source) roughly one to two months before this conversation: scheduled automations that run agents against feedback channels and other sources, generating summaries and draft PRs asynchronously (e.g., overnight) for a human to review.
- Internal team culture on the Claude Code/Cowork org emphasizes [[High Agency High Accountability|high agency paired with high accountability]], a "one team" mentality, explicit permission to kill processes that no longer serve the team, and monthly "[[Just In Time Planning|just-in-time planning]]" instead of long-range roadmaps.
- Tracked an internal (reportedly informal) "swear word dashboard" starting around September of a prior year, monitoring frustration signals as part of broader attention to user/employee experience quality.
- Hiring on the Claude Code/Cowork team indexes on two profiles: creative builders with product sense, and deep systems/distributed-systems experts for areas still requiring "[[Trust But Verify|trust but verify]]."
- Per [[Adam Mosseri]] (Head of Instagram, Meta), Anthropic's current model lineup as of mid-2026 includes [[Fable]] and [[Mythos]]; Mosseri describes spending significant time with Mythos and, for the first time, feeling like he's "talking to a much more technical, much smarter engineer" than himself. He frames the ongoing question for cost-sensitive users as whether to pay for frontier tokens (an "anthropic model 6.0"-tier model) or use a cheaper model like Fable for smaller projects.
- Mosseri singles out Mythos as a model with a distinct "vibe" of being willing to push back and say "I can't do this, let's move on" rather than being a pure pleaser — a trait he says he actively looks for when picking a model to help with strategy work.
- Per Tony Fadell: Dario Amodei reportedly said 90-100% of Anthropic's code is written by Claude, with humans monitoring the output; when Anthropic's/Claude's source code reportedly leaked, experienced software architects who examined it found it brittle and poorly layered despite it being the functioning "main loop" of Claude — Fadell's central illustration of AI "cognitive surrender" risk.
- Fadell notes Anthropic is currently valued more highly and generating more revenue than OpenAI in the current market environment.
- Per [[Eric Ries]] (author of Incorruptible): Anthropic is a governance case study for how to build a durable, "incorruptible" company. [[Dario Amodei]] and [[Daniela Amodei]] left [[OpenAI]] to found Anthropic; Ries — then known as "an eccentric collector of alternative governance ideas" — was brought in by an early investor to advise them before the generative-AI boom (pre-ChatGPT), when Anthropic was not yet a hot company and top venture funds weren't participating in its round.
- Anthropic was incorporated as a [[Public Benefit Corporation]] from inception and wrote into its charter the right to later create an outside mission-oversight body; it did not actually stand up the **[[Long-Term Benefit Trust]]** (LTBT) until its Series C, roughly two years later.
- The Long-Term Benefit Trust gives Anthropic directors on its for-profit board who are appointed by, and accountable to, outside AI-safety-expert trustees who hold no equity in Anthropic — i.e., no financial incentive in its growth, only an incentive to see the mission executed properly. Ries argues this is why Anthropic can refuse to release a model it judges too dangerous, and why it turned down a reported $200 million Pentagon contract (framed by Ries as a case of government overreach putting Anthropic in an impossible position, not simply a values win).
- Ries argues Dario does not have founder-control dual-class shares (unlike Mark Zuckerberg or Larry Page/Sergey Brin); Anthropic's structure is "more institutional" and, in his view, actually more resistant to abuse than founder control alone.
- Ries's causal chain for "why Anthropic is winning": people commonly cite surface traits (lower inference costs, faster product velocity, sharper focus) — but tracing "why" repeatedly leads back to talent wanting to work for "the good guys" pursuing a safety mission, which in turn depends on the mission having been protected structurally (ethos + integrity), not just declared.
- Anthropic was one of several AI labs (alongside OpenAI, Google, Cohere, Palantir) that Ries shared a governance-focused AI panel with at a Vatican-convened AI conference; he notes none of the major AI labs use "standard" (conventional shareholder-primacy) governance.
- Referenced in connection with a reported dispute/tension between Anthropic and Figma around board composition and AI-related governance questions ("can I have an AI person on my board").
- Per [[Benedict Evans]] (episode 07): cited, alongside [[OpenAI]], as a leading example of an AI lab whose headcount is rising rather than falling — including investment in [[Forward Deployed Engineer|forward-deployed engineers]] and professional-services-style capability — which Evans argues reflects how large a custom, consulting-style project it is to reimagine a company's internal workflows around AI, not a sign that "AI ends jobs."
- Evans argues foundation-model labs like Anthropic likely lack durable network effects/differentiation versus competitors, implying long-run commoditization/pricing pressure unless value moves up the stack to applications built on top of its models — a distinction he says people calling races between labs ("anthropic got it this week") tend to miss.
- Per [[Cat Wu]] (episode 13): its core execution advantage comes from putting the company mission above any individual product line — see [[Mission Over Product]] — plus a PM team of ~30-40 across research PM, developer platform, Claude Code/Cowork, enterprise, and growth, organized around "[[AGI Pilled]]" product judgment, small trusted eval sets ([[Evals As Product Definition]]), and a "[[Building Blocks Progression]]" roadmap (single task → multi-task → mass-parallel agents).
- Per [[Amol]] (episode 16): grew from ~$1B to ~$19B ARR in ~14 months (10x YoY for three straight years) despite starting as the least-funded, least-distributed, non-first-mover AI lab — attributed to deep early focus on coding/B2B (reinforced by resource constraints; see [[Freedom Through Constraints]]) and a growth org that skews toward large bets given [[Exponential Thinking]] about AI-native product value. Notably chose not to release an early Claude chatbot before ChatGPT launched, for safety reasons — inadvertently ceding first-mover consumer traction to OpenAI.
- Internal culture practices highlighted by Amol: company-wide "[[Notebook Channels]]" (personal internal-Twitter-style feeds, including one from [[Dario Amodei]], used for transparency and scaling culture as headcount grows) and a "[[Two-Week PM Rule]]" delegating PM responsibilities to engineers for smaller projects.
- Talent density is repeatedly cited (by Amol) as the company's least replicable advantage — examples include [[Mike Krieger]] (Instagram co-founder, now CPO), [[Amie Vora]], and [[Alexey Komissarouk]] (who leads the "[[CASE (Claude Accelerates Sustainable Hypergrowth)|CASE]]" growth-automation initiative).
- Per [[Lenny Rachitsky]] (episode 27, in an aside during the professional-vibe-coding episode): recounts that one of the founders of a data-labeling company (name uncertain — "Merkore or maybe Serge" in the transcript) said Anthropic hired a number of National Lampoon-style comedy writers to help train its models, in the context of a discussion about whether AI will ever be able to write genuinely funny jokes.

## Related

- [[summary-04 - What happens after coding is solved ｜ Fiona Fung (Claude Code & Cowork)]] — source summary
- [[summary-02 - The rise of taste, human authenticity and judgment in an AI world ｜ Adam Mosseri (Head of IG)]] — source summary (Adam Mosseri episode)
- [[summary-06 - Tony Fadell： How to build real taste (and why AI makes it matter more)]] — source summary (Tony Fadell episode)
- [[Tony Fadell]] — cites Anthropic's leaked code as a cautionary example
- [[Dario Amodei]] — Anthropic figure quoted regarding Claude's code authorship
- [[Cognitive Surrender]] — concept illustrated by the leaked-code anecdote
- [[Technical Debt]] — risk raised in connection with the leaked code
- [[OpenAI]] — contrasted competitor per Fadell
- [[Fable]] — Anthropic model referenced by Adam Mosseri
- [[Mythos]] — Anthropic model referenced by Adam Mosseri
- [[Adam Mosseri]] — Head of Instagram, discusses using Anthropic's models
- [[Fiona Fung]] — leader of the Claude Code and Claude Cowork teams
- [[Claude Code]] — Anthropic's coding agent product
- [[Claude Cowork]] — Anthropic's knowledge-work agent product
- [[Boris Cherny]] — engineer on the Claude Code team, overseen by Fung
- [[Cat Wu]] — Head of Product for Claude Code, overseen by Fung
- [[High Agency High Accountability]] — core internal team value
- [[Bad Vs Sad Framework]] — internal quality framework
- [[Just In Time Planning]] — internal planning methodology
- [[Latent Demand]] — concept behind the Claude for Small Business bundle
- [[summary-10 - How Anthropic, Costco, and Patagonia all build incorruptible companies ｜ Eric Ries]] — source summary
- [[Eric Ries]] — author/advisor discussing Anthropic's governance structure
- [[Public Benefit Corporation]] — Anthropic's corporate structure since inception
- [[Long-Term Benefit Trust]] — Anthropic's mission-guardian mechanism
- [[Daniela Amodei]] — co-founder, left OpenAI with Dario to found Anthropic
- [[Financial Gravity]] — force Anthropic's structure is designed to resist
- [[Mission Guardian]] — concept Anthropic's LTBT exemplifies
- [[Costco]] — parallel governance-fortress case study
- [[Patagonia]] — parallel perpetual-purpose-trust case study
- [[summary-07 - The most rational take on AI you’ll hear this year]] — source summary (Benedict Evans episode)
- [[Benedict Evans]] — analyst discussing Anthropic's hiring strategy and market position
- [[Forward Deployed Engineer]] — hiring trend discussed regarding Anthropic
- [[Jevons Paradox]] — economic concept invoked to explain lab hiring growth
- [[summary-13 - How Anthropic’s product team moves faster than anyone else ｜ Cat Wu (Head of Product, Claude Code)]] — source summary
- [[summary-16 - Head of Growth (Anthropic)： Anthropic is automating its own growth]] — source summary
- [[Mission Over Product]] / [[AGI Pilled]] / [[Building Blocks Progression]] — Cat Wu's core product frameworks
- [[Amol]] — head of growth, describes the company's growth trajectory
- [[Freedom Through Constraints]] / [[Exponential Thinking]] — Amol's strategic frameworks
- [[Notebook Channels]] / [[Two-Week PM Rule]] — internal culture and process practices
- [[Mike Krieger]] / [[Amie Vora]] / [[Alexey Komissarouk]] — cited examples of talent density
- [[summary-27 - The rise of the professional vibe coder (a new AI-era job)]] — source summary
- [[Lenny Rachitsky]] — recounts the comedy-writers-hired-for-training anecdote
- Per [[Edwin Chen]] (episode 40, CEO of [[Surge AI]], which supplies training data to every frontier lab): singled out as unusually principled among frontier labs about what it does and doesn't optimize its models for, in contrast to labs more willing to chase gameable benchmarks like LM Arena or engagement-maximizing model behavior. See [[LM Arena Gaming]].
- [[summary-40 - The $1B Al company training ChatGPT, Claude & Gemini on the path to responsible AGI ｜ Edwin Chen]] — source summary
- [[Edwin Chen]] — praises Anthropic's principled approach
- [[LM Arena Gaming]] — industry problem Chen says Anthropic resists better than most
