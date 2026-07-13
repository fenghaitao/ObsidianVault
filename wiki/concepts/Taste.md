---
title: "Taste"
type: concept
tags: [product-management, design, judgment, curation]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/03 - Why OpenAI is merging Codex and ChatGPT and the future of knowledge work ｜ Andrew Ambrosino.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/06 - Tony Fadell： How to build real taste (and why AI makes it matter more).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/02 - The rise of taste, human authenticity and judgment in an AI world ｜ Adam Mosseri (Head of IG).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/27 - The rise of the professional vibe coder (a new AI-era job).md"]
last_updated: 2026-07-11
---

## Definition

"Taste," as discussed by [[Andrew Ambrosino]] of [[OpenAI]], is the curatorial judgment needed to decide what to build, what to keep, and how to present it — the skill that becomes the primary bottleneck in product work once implementation (via AI) is nearly free. [[Tony Fadell]] frames the same underlying idea from a hardware/product-leadership angle: "real taste" is the informed, opinion-based judgment a small team of "tastemakers" must exercise to build a genuinely new 1.0 product, since there is no analog data to fall back on. [[Adam Mosseri]] (Head of Instagram) independently converges on the same idea: "in a world where it's easier to build things, it's more important to make sure that your time is spent figuring out what you should be building in the first place" — an instinct for what AI is and isn't (and won't be) good at.

## Key Information

- Ambrosino's core claim: "The implementation is actually not the expensive part anymore. It's dare I say taste... it's the curation process." With unlimited tokens, many people/teams can independently build 90 different explorations of the same feature; the hard work is judging which are good, what to fold together, and how to frame the result.
- Taste is explicitly not just aesthetics: citing a tweet about Paul Graham (who "has great taste" but "wears cargo shorts"), Ambrosino argues taste includes systems thinking (how something fits the broader product), sequencing (where a feature fits in a longer-term arc), and framing/communication — not just visual polish.
- Taste is the primary hiring/promotion signal Ambrosino describes for the Codex org: "command over the discipline" plus the taste to distinguish signal from noise in a world of unlimited AI-generated content ("we can't just be doing slop").
- Discussed as the reason AI/frontier models are still weak at design: judging good design requires a human "taste" feedback signal that's inherently harder to construct a clean training loop for than code correctness (does the code compile) — a practical, not fundamental, limitation.
- Related structural reasons AI lags at design/taste specifically (per Ambrosino): design rewards novelty over pattern-conformity (the opposite of code, where matching known-good patterns is usually desirable), and there's a missing semantic abstraction layer connecting visual/design intent to the underlying code architecture (e.g., knowing that two visually different UI elements should share the same underlying interaction pattern across a rebrand).
- Also framed as the answer to "who is most valuable now": people who can take an idea from concept to finished, polished product ("high agency, high taste") are described as among the most valuable people in this new environment.
- **Tony Fadell's framing — opinion-based vs. data-driven decisions**: for a genuinely new 1.0 product (no analogs exist yet), most decisions can't be data-driven, so a small team of "tastemakers" must make opinion-based ("informed gut") calls. Fadell calls this a "benevolent dictatorship" — e.g., Steve Jobs choosing the iPhone's on-screen keyboard over a physical one despite inconclusive data on both sides.
- Fadell distinguishes this from reckless intuition: opinion-based decisions still require "a lot of informed judgment from all the experts around, asking questions, refining, prototyping" — taste is built on inputs, not just a single person's whim.
- Fadell's real-world formula for deciding *what* is worth building in the first place: start from genuine, often long-habituated customer pain, then ask whether a new technology has just become available to solve that pain in a fundamentally different way (see [[Pain-Driven Innovation]]).
- Fadell notes B2C contexts make opinion-based/taste decisions hardest, because consumers can only judge a product once they experience the full, shipped context (marketing, feature set, usability together) — you can't get that feedback from a 1.0 in pieces.
- Fadell connects taste to good "micromanagement": leaders need to identify the few key details or decisions that truly matter (for the customer, cost, or long-term vision) and go deep on those, while delegating the rest — see [[Micromanagement (Product Leadership)]].
- Fadell's "luxury vs. fast fashion" framing: taste/craft is what separates durable "luxury" software (his example: [[Flighty]]) from cheap, AI-"vibe coded" software that looks similar but doesn't last — see [[Vibe Coding]] and [[Technical Debt]].
- [[Adam Mosseri]]'s framing (Instagram/Meta): with AI, "people who I think are going to make the most of it are the ones who are cleareyed about what AI is good at and what it's not good at and also have an instinct or a nose for what it will be good at and not good at" — taste extended into a forward-looking, predictive instinct about AI's trajectory, not just present-day judgment.
- Mosseri says he is "pretty long on designers" specifically because they tend to have taste, which he considers much harder to automate away than other design-adjacent skills; he cites [[Fiona Fung]]'s independent framing (from a separate episode) that the people worth hiring now split into "builders with great taste that can take an idea from end to end" and deep domain specialists — Mosseri responds "the taste [sic] matters a lot. I really agree with that."
- Mosseri also applies taste at the leadership level: describes the best product leaders as less "idea machines" and more curators — of ideas, people, and technologies — arguing curation itself is a form of taste applied to talent and strategy rather than to a single artifact.
- **[[Lazar]]'s framing (episode 27, professional vibe coding)**: in the old world, "good enough" was already hard to produce, so it was rewarded; now that AI lets everyone produce "good enough" trivially, the gap worth optimizing for has shifted entirely to the space between "good enough" and "world class" — "everybody produces good enough with AI... so now learning and optimizing for how do I produce world class and magic is the key lesson."
- Lazar predicts PMs are the current biggest winners of AI because they bring clarity, and bets designers are next, since design is fundamentally about emotional, human-preference decisions that AI isn't yet trained to make well.
- Lazar's formulation of the ceiling on AI capability: "the ceiling on the AI isn't the model intelligence. It's what the model sees before it acts" — i.e., taste and judgment about what to expose the agent to (references, context, examples) bounds output quality more than raw model capability. See [[Exposure Time]].
- Lazar's concrete taste-building anecdote: after working alongside Lovable's designers (Felix, Nad, Abby) and trying to copy a "simple" gradient background from [[Figma]] into a prompt, he discovered it was actually 50 layered colors at varying opacity levels — a formative moment in realizing the gap between what looks simple and what world-class design craft actually requires.
- Practice Lazar recommends for building taste: "[[Exposure Time]]" — deliberately spending more time exposed to great design/work than spent building, including following excellent designers and watching how they prompt AI tools.

## Related

- [[summary-03 - Why OpenAI is merging Codex and ChatGPT and the future of knowledge work ｜ Andrew Ambrosino]] — source summary
- [[summary-06 - Tony Fadell： How to build real taste (and why AI makes it matter more)]] — source summary
- [[Andrew Ambrosino]] — articulates this concept at length
- [[OpenAI]] — organizational context where this concept is applied
- [[Codex]] — product built around this philosophy
- [[Zone Defense]] — how "taste"-driven product people organize themselves
- [[Role Collapse]] — related shift in what skills matter across roles
- [[Design Process]] — related discussion of how taste applies to design workflow
- [[Tony Fadell]] — articulates the opinion-based-decision framing of taste
- [[Pain-Driven Innovation]] — Fadell's framework for deciding what's worth building
- [[Micromanagement (Product Leadership)]] — related leadership practice
- [[Vibe Coding]] — contrasted "fast fashion" approach lacking taste
- [[Technical Debt]] — risk of building without taste/architecture discipline
- [[summary-02 - The rise of taste, human authenticity and judgment in an AI world ｜ Adam Mosseri (Head of IG)]] — source summary
- [[Adam Mosseri]] — articulates taste as a forward-looking instinct about AI capability and as a curatorial leadership trait
- [[Fiona Fung]] — independently corroborates the "taste + deep specialists" hiring split
- [[Product Staff]] — Instagram's generalist role, explicitly selected in part for taste
- [[Pods]] — the small-team structure taste-driven generalists operate within
- [[summary-27 - The rise of the professional vibe coder (a new AI-era job)]] — source summary
- [[Lazar]] — articulates the "good enough vs. world class" gap and the AI-capability-ceiling framing
- [[Exposure Time]] — Lazar's practice for building taste
- [[Figma]] — source of Lazar's gradient/layers taste anecdote
- [[Professional Vibe Coder]] — role built around exercising this skill
