---
title: "Vibe Coding"
type: concept
tags: [ai, software-engineering, product-design]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/02 - The rise of taste, human authenticity and judgment in an AI world ｜ Adam Mosseri (Head of IG).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/06 - Tony Fadell： How to build real taste (and why AI makes it matter more).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/27 - The rise of the professional vibe coder (a new AI-era job).md"]
last_updated: 2026-07-11
---

## Definition

Term for building software primarily by prompting/steering AI coding agents rather than writing code by hand. [[Tony Fadell]] treats it as useful for prototyping but insufficient, on its own, for building durable, well-architected, differentiated products. [[Adam Mosseri]] and [[Lenny Rachitsky]] extend the term to the idea that different AI models/tools produce recognizably distinct "vibes" or styles in the apps they generate.

## Key Information

- Fadell's framing: "today in the AI world, I can just make a prompt and all of a sudden it gets spit out" — but without understanding the underlying functional layers (marketing, engineering, manufacturing, sales, etc.), the result risks being unreviewed and brittle, referencing "you're building on a really crusty foundation."
- Applied to the "SaaS is dead / anyone can vibe code it" narrative: Fadell notes investors are increasingly funding only companies with "atoms in their business plan" alongside software, since pure software differentiation is easy to replicate via AI ("Duh... where have you guys been?").
- His "luxury vs. fast fashion" distinction: an AI agent might now be able to "vibe code" a copycat version-two of an app like Flighty (since the original exists as a reference), but the original version-one product's craft and architecture required human taste and could not have been produced by AI alone.
- Recommended constructive use: AI coding agents are good for producing "incredible prototypes" that help a team reach an "informed gut" decision faster, and for handling well-scoped sub-segments of an already-architected system — not for owning end-to-end product architecture.
- Connected to why hardware-plus-software ("atoms plus software") companies (e.g., Waymo, Snapchat's hardware investments per Evan Spiegel) are seen as more defensible than software-only products in an era where implementation is cheap.
- Mosseri and Rachitsky observe that AI-built apps have a recognizable "vibe" tied to which tool built them (e.g., distinguishing "that's a Codex app" from "that's a Claude app," or products built with Replit vs. Lovable), similar to how a trained eye can spot which design tool produced a given interface.
- Mosseri personally started vibe coding together with his 10-year-old son, building a 19-level 8-bit-style platformer game (with a shop for skins/weapons) over a couple of hours, using [[Claude Code]]. He says an attempt to do this six months earlier "totally didn't work," but newer models made it "amazing."
- Framed by Mosseri as part of a broader claim that coding itself is being "eaten" by AI in stages: from engineers writing all their own code, to AI writing most code with humans steering/reviewing, to a near future where the entire software development life cycle — including idea generation — is increasingly AI-assisted, leaving strategy, vision, and taste as the primary remaining human contributions. See [[Vision Vs Strategy]].
- Per [[Simon Willison]] (episode 17): traces the term to [[Andrej Karpathy]]'s original, narrower definition — not looking at the code at all, playing purely by vibes, appropriate specifically for prototyping/personal projects where only the author is harmed by bugs. Willison argues the term has since been stretched to cover *all* AI-assisted programming, including professional, reviewed, production code — a conflation he considers a devaluation of the original useful distinction, and the reason he coined "[[Agentic Engineering]]" as a separate term for the professional practice.
- Willison's practical dividing line: vibe code freely for yourself; the moment code you haven't reviewed could harm someone else who uses it, you've crossed into territory requiring professional (agentic-engineering) practices, not vibes.
- Per [[Lazar]], [[Lovable]]'s first official full-time "vibe coding engineer" (episode 27): the practice has professionalized into a hireable full-time job — see [[Professional Vibe Coder]] — that goes well beyond casual prototyping, applied to both internal tools and shipped, customer-facing products.
- Lazar's framing of what vibe coding requires to succeed at production quality: roughly 80% of time in planning/chat mode versus 20% executing, treating the AI tool as a "technical co-founder," and religiously reading the agent's natural-language output rather than the generated code ("I don't care about the code... it's what the agent tells me that matters to me").
- Lazar predicts coding itself will become like calligraphy: a rare, artisanal skill rather than a necessary one, as AI increasingly writes the code across skill levels ("Coding is going to be like calligraphy... it's going to be so rare that it's going to become an art").
- Lazar says he began vibe coding in July 2024, about seven months before Andrej Karpathy coined the term in early 2025, and taught it (via YouTube and a paid course) before it had a name.
- Recommended starting technique: begin any new project with four parallel first attempts — a voice brain-dump, a typed prompt, a pulled design reference (from [[Mobbin]]/[[Dribbble]]), and an actual code/component snippet (from a library like [[21st.dev]]) — to reach clarity fast and cheaply before committing to one direction; see [[Token Budgeting]].

## Related

- [[summary-02 - The rise of taste, human authenticity and judgment in an AI world ｜ Adam Mosseri (Head of IG)]] — source summary
- [[summary-06 - Tony Fadell： How to build real taste (and why AI makes it matter more)]] — source summary
- [[summary-17 - An AI state of the union： We’ve passed the inflection point & dark factories are coming]] — source summary
- [[Tony Fadell]] — discusses this trend's limits
- [[Adam Mosseri]] — uses this term and practices it with his son
- [[Lenny Rachitsky]] — discusses this term and its "vibe"-recognition angle
- [[Claude Code]] — the tool Mosseri's son used
- [[Technical Debt]] — the main risk of unreviewed vibe coding
- [[Cognitive Surrender]] — the underlying failure mode
- [[Flighty]] — example of craft that resists pure vibe-coded replication
- [[Waymo]] — example of atoms-plus-software defensibility
- [[Snapchat]] — example of atoms-plus-software defensibility
- [[Taste]] — the human judgment vibe coding alone lacks
- [[Vision Vs Strategy]] — the higher-order human work this trend leaves behind
- [[Andrej Karpathy]] — originated this term
- [[Simon Willison]] — distinguishes this term from professional [[Agentic Engineering]]
- [[Agentic Engineering]] — the professional counterpart term Willison coined
- [[summary-27 - The rise of the professional vibe coder (a new AI-era job)]] — source summary
- [[Lazar]] — first official full-time "vibe coding engineer" at Lovable
- [[Lovable]] — company where Lazar practices this professionally
- [[Professional Vibe Coder]] — the job role built around this practice
- [[Token Budgeting]] — context-window management techniques for doing this well
