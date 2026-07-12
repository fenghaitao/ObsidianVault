---
title: "summary-25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny"
type: source-summary
source: "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny.md"
date: 2026-07-10
---

## Core Thesis

Coding is virtually solved by AI (Claude Code), and the next frontier is AI agents that proactively act on behalf of users for non-coding tasks — from managing projects to handling personal errands. This shift will democratize software creation, blur traditional job roles (engineer, PM, designer), and fundamentally reshape the nature of work, analogous to how the printing press democratized literacy.

## Key Entities

- [[Boris Cherny]] — Head of Claude Code at Anthropic; born in Odessa, Ukraine; self-taught programmer; former Meta/Instagram engineer; wrote 100% of his code via Claude Code since November 2025
- [[Anthropic]] — AI safety lab behind Claude and Claude Code; raised at over $350B valuation; mission-driven around safety; scaling laws paper co-authors among founders
- [[Claude Code]] — Anthropic's AI coding agent, launched ~1 year ago; started as a terminal hack; now available on iOS, Android, desktop, web, Slack, GitHub; ~$2B in revenue; powers 4% of all GitHub commits
- [[Ben Mann]] — Anthropic co-founder; nudged Boris to create DAU chart; suggested topics for this episode
- [[Mike Krieger]] — Anthropic; kicked off Anthropic Labs team; suggested topics for this episode
- [[Jenny Wen]] — Anthropic; part of the Claude Code team; suggested topics for this episode
- [[Cursor]] — AI coding tool; Boris briefly joined then returned to Anthropic after 2 weeks
- [[SemiAnalysis]] — Research firm that reported 4% of all GitHub commits are authored by Claude Code
- [[GitHub]] — 4% of all commits are Claude-authored; SemiAnalysis predicts 20% by end of year
- [[Spotify]] — Reported their best developers haven't written a line of code since December 2025
- [[DX (developer intelligence)]] — Developer intelligence platform; sponsor of the episode
- [[Sentry]] — Error monitoring and AI debugging platform; sponsor; Sear is their AI debugging agent
- [[Sear]] — Sentry's AI debugging agent that finds root causes, suggests fixes, and opens PRs
- [[Metaview]] — AI recruiting platform; sponsor of the episode
- [[Chris Olah]] — Pioneer of mechanistic interpretability at Anthropic
- [[Richard Sutton]] — Author of "The Bitter Lesson" (blog post ~10 years ago)
- [[Cixin Liu]] — Sci-fi author of Three-Body Problem and The Wandering Earth
- [[Charles Stross]] — Sci-fi author of Accelerando
- [[Vernor Vinge]] — Sci-fi author of A Fire Upon the Deep
- [[Instagram]] — Boris's previous employer; he was one of the top few most productive engineers
- [[Meta]] — Boris's previous employer; he was responsible for code quality across Facebook, Instagram, WhatsApp
- [[Facebook]] — Marketplace and Dating examples of latent demand
- [[Google Docs]] — Co-work integrates with Google Docs
- [[Gmail]] — Co-work can send and read emails
- [[Slack]] — Claude Code integrates with Slack; Co-work uses Slack for messaging
- [[Threads]] — Boris previously used Threads exclusively; helped build it at Meta
- [[Twitter X]] — Boris became active on Twitter to engage with Claude Code users
- [[Three Body Problem]] — Netflix series adaptation of Cixin Liu's book; Boris recommends
- [[A Fire Upon the Deep]] — Sci-fi novel by Vernor Vinge; both Lenny and Boris recommend
- [[Acquired (podcast)]] — Business history podcast hosted by Ben and David; Boris recommends starting with Nintendo episode
- [[Functional Programming in Scala]] — Boris's favorite technical book
- [[Accelerando]] — Sci-fi novel by Charles Stross; captures the pace of the current AI moment
- [[The Wandering Earth]] — Short story collection by Cixin Liu; Chinese sci-fi perspective
- [[Opus 4]] — Anthropic's first ASL-3 class model; inflection point for Claude Code adoption
- [[Opus 4.6]] — Current most capable model; runs 10-30 minutes unattended; can run for hours or days
- [[Sonnet 3.5]] — Earlier model; could only run 15-30 seconds before going off the rails
- [[Sonnet 4]] — Later model improvement
- [[MCP (Model Context Protocol)]] — Anthropic's protocol for giving AI the ability to use tools
- [[QuadCode]] — Earlier name for Claude Code before it was renamed
- [[Felix (Anthropic)]] — Anthropic team member who worked on Claude Code
- [[Sam (Anthropic)]] — Anthropic team member who worked on Claude Code
- [[Lena (Anthropic)]] — Anthropic engineer who still writes C++ by hand on weekends
- [[Brendan (Anthropic)]] — Anthropic data scientist; early non-engineer adopter of Claude Code for SQL analysis
- [[Fiona (Anthropic)]] — Facebook Marketplace founding manager; latent demand case study

## Key Concepts

- [[Latent Demand]] — Building products based on what users are already "abusing" existing tools to do; also applies to what the model is trying to do ("being on distribution")
- [[The Bitter Lesson]] — Rich Sutton's principle: more general models always outperform more specific ones; Boris's corollary: always bet on the more general model
- [[Mechanistic Interpretability]] — Understanding what individual neurons and layers in models represent; pioneered by Chris Olah at Anthropic
- [[AI Safety Layers]] — Three layers: alignment/mechanistic interpretability (lowest), evals (laboratory), real-world behavior (highest); releasing early helps study the third layer
- [[Building for Future Models]] — Design products for the model 6 months from now, not today; product-market fit won't be great initially but hits when the model catches up
- [[Plan Mode]] — Claude Code feature: injects "don't write code yet" into the prompt; Boris uses it for ~80% of tasks; leads to one-shot correct implementations
- [[Race to the Top]] — Anthropic's strategy of open-sourcing safety tools (e.g., sandbox) to encourage other labs to adopt safe practices
- [[Token Economics]] — Use the most capable model (Opus 4.6) because it's actually cheaper: less intelligent models use more tokens with more corrections
- [[Generalist Approach]] — Cross-disciplinary skills becoming more valuable; everyone on Claude Code team codes regardless of role (PM, EM, designer, finance, data scientist)
- [[Superposition (Neural Networks)]] — A single neuron can correspond to dozens of concepts; combined activations represent more sophisticated concepts
- [[ASL (AI Safety Level)]] — Anthropic's model safety classification; Opus 4 was first ASL-3 class model
- [[Jevons Paradox]] — As AI makes coding cheaper, demand for coding increases rather than decreases; more experimentation, more volume
- [[Common Sense]] — Boris's life motto: think from first principles; if something smells weird, it's probably not a good idea
- [[Being on Distribution]] — Research term for observing what the model naturally tries to do; product equivalent of latent demand applied to the model
- [[Product as the Model]] — Inverting the traditional approach: the product IS the model, with minimal scaffolding; give the model tools and a goal, let it figure out the rest
- [[Printing Press Analogy]] — Historical parallel for AI democratization: scribes vs. printing press mirrors current coding transition; literacy went from <1% to 70% over 200 years
- [[Claudify Everything]] — Principle: what's better than doing something? Having Claude do it; also known as "Claudify it"
- [[Underfunding as a Principle]] — Deliberately under-resourcing projects forces people to use AI more; leads to better AI utilization
- [[Multi-Claudeing]] — Running multiple Claude Code/Co-work agents in parallel; Boris typically has 5 agents running simultaneously
- [[Don't Box the Model In]] — Give the model tools and a goal instead of rigid workflows; scaffolding gains (10-20%) get wiped out by next model version
- [[Maximum Effort Mode]] — Always enabled for Boris; using the most capable model setting
- [[Co-work (Claude)]] — Anthropic's agentic product for non-coding tasks; can use Chrome, Gmail, Slack, spreadsheets; growing faster than Claude Code did
- [[Psychological Safety]] — Creating space for experimentation where 80% of ideas can fail; key to innovation
- [[Speed as Advantage]] — Early on, speed was Claude Code's only competitive advantage; principle of "if you can do something today, do it today"
- [[Fast Feedback Loops]] — Fixing user-reported bugs within minutes; makes users feel heard and encourages more feedback
- [[Code Review (AI)]] — Claude reviews 100% of pull requests at Anthropic; human review layer still exists on top
- [[Programming History]] — Programming has evolved from pen and paper → hardware → switches → punch cards → software → AI; always changing
- [[Builder (Role)]] — Boris predicts "software engineer" title will be replaced by "builder" as everyone becomes a product manager who codes
- [[Miso Making]] — Boris's post-AGI plan: craft miso (3 months for white, 2-4 years for red); teaches long time scales
- [[Coding Vacation]] — Boris's favorite type of vacation: coding all day in a new city
- [[TI-83 Plus]] — Boris's first programming experience: cheating on math tests by programming answers into a graphing calculator
