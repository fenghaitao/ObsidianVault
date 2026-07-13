---
title: "summary-04 - What happens after coding is solved ｜ Fiona Fung (Claude Code & Cowork)"
type: source
tags: [source, original-material, podcast, engineering-management, agentic-coding]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/04 - What happens after coding is solved ｜ Fiona Fung (Claude Code & Cowork).md"]
last_updated: 2026-07-10
---

## Core Summary

Lenny Rachitsky interviews [[Fiona Fung]], who leads the engineering teams behind [[Claude Code]] and [[Claude Cowork]] at [[Anthropic]] (and previously ran Visual Studio and TypeScript at [[Microsoft]], founded [[Facebook Marketplace]], and worked on AR/VR and Instagram infrastructure at [[Meta]]). The conversation argues that coding is no longer the bottleneck for software teams — Anthropic engineers now ship roughly 8x as much code per quarter as in 2021-2025 — so the real management challenge has shifted from writing code to verifying it, staying on top of a much higher throughput of shipped work, and preserving human connection and judgment as agents absorb more of the day-to-day. Fung describes concrete practices her org uses to manage this shift: giving Claude a standing "remote session" across all repos and Slack channels to summarize what shipped and surface PRs for review; automated "[[Routines|routines]]" that run async agents overnight against feedback channels; a [[Bad Vs Sad Framework|bad-vs-sad]] quality framework that lets each team define its own thresholds for irrecoverable versus recoverable failures; checking specs/frameworks into the repo so Claude Code review can validate against "what good looks like"; monthly "[[Just In Time Planning|just-in-time planning]]" instead of six-month roadmaps; requiring managers to start as ICs and stay part-time hands-on ("player-coach") to keep product feel; and instituting pair-programming lunches and hackathons to counter the loneliness of working mostly with an agent. She frames hiring around two profiles — creative builders with product sense, and deep systems experts for the areas that still need "[[Trust But Verify|trust but verify]]" — and around the paired values of high agency and high accountability. She also emphasizes watching for "[[Latent Demand|latent demand]]" (non-coders using Claude Code, small-business owners struggling with expensing) as a source of new product opportunities, and stresses [[Dogfooding|dogfooding]] and direct customer visits over dashboards as the best way for leaders to stay grounded in the product. Open questions she is still wrestling with: whether coding-adjacent orgs (iOS/Android) still need to be split, how far to push fully automated code review, how to measure engineer productivity/ROI without falling into "token maxing" (optimizing activity instead of outcomes), how to manage rising context-switching load from many async agents running in parallel, and how to train the next generation of engineers who may never need to write code by hand.

## Key Points

- Anthropic engineers ship ~8x more code per quarter than 2021-2025 levels; coding throughput is no longer the constraint, so verification and quality assurance become the new bottleneck.
- Fung keeps a standing Claude Code remote session with access to all repos, Slack channels, and metrics, which she uses monthly to review what shipped and turn it into a coaching conversation with reports rather than just generating PRs/bug fixes.
- "Routines" (a Claude Cowork feature) automate her old daily ritual of scanning feedback channels each morning — an agent now summarizes themes and drafts PRs overnight for her to review on waking.
- The "bad vs. sad" framework: "bad" = a serious, irrecoverable error (e.g., a CLI crash that loses work); "sad" = a recoverable pain point (e.g., UI flicker) that can compound into "bad" if it stacks up. Each team sets its own thresholds for its own surface area.
- Checking specs/frameworks ("what good looks like") into the repo lets Claude Code review validate against them automatically — described as an evolution of test-driven development, since Claude can now write the failing test first.
- Two hiring profiles: creative builders with strong product sense ("dreamers" who own a product end-to-end and iterate on feedback), and deep systems/distributed-systems experts for areas that still need "trust but verify."
- Core team value: high agency paired with high accountability — freedom to act on a problem, balanced by ownership of a clear hypothesis and its outcome.
- Managers at Anthropic's Claude Code org start as individual contributors first (no direct reports) before taking on management, and continue shipping small PRs part-time afterward to stay "in the flow" of the product and keep rapport with the team.
- "Latent demand" — watching for people using a product in unexpected ways (non-coders using Claude Code, small-business owners doing expense/invoicing work in Cowork) — led directly to the "Claude for Small Business" bundle.
- Growth mindset and "what is within my control?" are Fung's core advice for navigating fear/frustration during rapid AI-driven role change; she illustrates this with her own path from a Hong Kong immigrant childhood in Ontario to a bank-teller job that funded her engineering degree.
- Team culture risk ("what keeps me up at night"): maintaining "one team" mentality and open, honest reporting ("what's not going well") as the org scales rapidly; she explicitly asks managers to surface problems rather than claim everything is fine.
- Loneliness is an emerging downside of agent-heavy workflows — the team introduced pair-programming lunches and hackathons because engineers increasingly work solo with their own agent instead of with each other.
- Planning shifted from 6-month roadmaps to monthly "just-in-time" (JIT) planning on a lightweight spreadsheet, revisited weekly, because the AI landscape changes too fast for longer-range plans to stay relevant.
- Unsolved problems as of this recording: whether to keep separate iOS/Android orgs now that engineers "flex" across platforms with AI help; how far to push fully automated code review; how to measure engineer productivity/ROI without over-indexing on activity metrics like lines-of-code or "token maxing"; rising context-switching load from managing many parallel async agents; and how to train the next generation of engineers who may never write code by hand the way senior engineers did.
- Dogfooding and direct customer visits (e.g., discovering a Facebook Marketplace LTE-performance blocker in Chile, or a scam vector after selling on Marketplace herself) are held up as more reliable signal than dashboards alone — "trust the anecdote."

## Related

- [[Fiona Fung]] — the guest; leader of the Claude Code and Claude Cowork engineering teams at Anthropic
- [[Lenny Rachitsky]] — podcast host and interviewer
- [[Anthropic]] — company where Fung now works
- [[Claude Code]] — Anthropic's coding agent product, central subject of the conversation
- [[Claude Cowork]] — Anthropic's knowledge-work agent product, also led by Fung
- [[Boris Cherny]] — engineer Fung oversees; early builder of Claude Code, prior podcast guest
- [[Cat Wu]] — Head of Product for Claude Code, whom Fung oversees; prior podcast guest
- [[Meta]] — Fung's prior employer (Facebook Marketplace, Instagram, AR/VR)
- [[Microsoft]] — Fung's prior employer (Visual Studio, TypeScript)
- [[Facebook Marketplace]] — product Fung took from idea to launch, now >$100B GMV/year
- [[High Agency High Accountability]] — core team value described
- [[Bad Vs Sad Framework]] — quality-classification framework described
- [[Just In Time Planning]] — monthly lightweight planning methodology described
- [[Latent Demand]] — concept for spotting unexpected product usage
- [[Dogfooding]] — practice of leaders using their own product
- [[Trust But Verify]] — verification philosophy for AI-generated work
- [[Growth Mindset]] — mindset Fung credits for adapting well to change
