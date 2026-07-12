---
title: "Anthropic"
type: entity
tags: [company, AI, AI-lab, Claude]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/40 - The $1B Al company training ChatGPT, Claude & Gemini on the path to responsible AGI ｜ Edwin Chen.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/39 - Inside OpenAI： 2026 is the year of agents, AI's biggest bottleneck, and why compute isn't the issue.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/23 - The design process is dead. Here's what's replacing it. ｜ Jenny Wen (head of design at Claude).md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/16 - Head of Growth (Anthropic)： Anthropic is automating its own growth.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/18 - From skeptic to true believer： How OpenClaw changed my life ｜ Claire Vo.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/17 - An AI state of the union： We've passed the inflection point & dark factories are coming.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/13 - How Anthropic's product team moves faster than anyone else ｜ Cat Wu (Head of Product, Claude Code).md"]
last_updated: 2026-07-11
---

## Definition

Anthropic is an AI safety and research company that builds Claude, a frontier AI model. Edwin Chen considers Anthropic to be the most principled AI lab, taking a thoughtful approach to model behavior and values.

## Key Information

- Claude (Anthropic's model) was significantly better at coding and writing than any other model for a long time, and Edwin attributes much of this to superior data quality and taste in post-training
- Edwin says Anthropic takes a "very principled view about what they do and don't care about and how they want their models to behave"
- Anthropic's Claude demonstrates an interesting model behavior tension: it will happily iterate through 30+ versions of an email to make it perfect, which raises questions about whether models should optimize for your time or for perfection
- Anthropic introduced "Artifacts" — mini-apps/UI components generated within the chat interface — which Edwin considers underhyped
- Anthropic is a customer of Finn (AI agent for customer service), alongside Shutterstock, Synthesia, Clay, Vanta, and monday.com
- Anthropic's constitutional classifiers have made it significantly harder to elicit SEAB burn (chemical, biological, radiological, nuclear, explosives) information from Claude models compared to earlier versions
- Anthropic co-authored a major research paper with HackAPrompt, OpenAI, and Google DeepMind on adaptive attacks against state-of-the-art defenses
- Anthropic is considered by Sander Schulhoff to have the best AI security among frontier labs, though humans can still jailbreak Claude models in under an hour
- Claude Code (Anthropic's coding agent) was recently hijacked by attackers who split malicious requests across separate instances to bypass defenses
- Anthropic developed MCP (Model Context Protocol), which gives AI the ability to use tools — Zevi Arnovitz uses it to connect Claude Code to Linear for automatic issue creation
- Anthropic acquired Bun, a JavaScript runtime
- Anthropic raised at over $350 billion valuation; Claude Code alone makes ~$2B in revenue, with Anthropic overall at ~$15B in revenue
- The company's trajectory is: coding → tool use → computer use, driven by a safety-first mission
- Anthropic's co-founders include three of the first four authors on the scaling laws paper; the company thinks in exponentials
- Everyone at Anthropic, if asked why they're there, "the answer is always going to be safety"
- Anthropic has economists, policy folks, and social impact folks to address the societal implications of AI
- Claude reviews 100% of pull requests at Anthropic internally; human review layer still exists on top
- Productivity per engineer at Anthropic has increased 200% in terms of pull requests over the past year
- The Claude Code team is hiring; everyone on the team codes regardless of role (PM, EM, designer, finance, data scientist)
- Anthropic's "race to the top" strategy: open-sourcing safety tools (e.g., Claude Code sandbox) to encourage other labs to adopt safe practices
- Released Claude Code early internally (4-5 months before external) to study safety of the first broadly used coding agent

- The internal Slack at Anthropic is described by Jenny Wen as a "gold mine" of AI news and insights
- Anthropic's design team is described as humble, resilient, and spanning the spectrum from highly technical prototypers to high-craft designers
- Anthropic has a culture of rapid prototyping — many teams are constantly trying different ideas with code names; keeping up with internal projects is a significant part of the job
- At Anthropic, there are internal prototypes and products that employees can use; Jenny describes being excited to try them out
- Many folks internally have deep insights and opinions on where the industry is going, with philosophical debates and direction discussions

### Growth and Revenue
- Grew from 1B ARR (start of 2025) to 19B+ ARR (Feb 2026) — 1 to 19 billion dollars in 14 months
- 10x year-on-year revenue growth trend since 2023: 0 to 100M (2023), 100M to 1B (2024), 1B to ~10B (2025)
- Growth team is roughly 40 people: engineers, designers, PMs, data — structured with horizontals (growth platform, monetization) and audience-focused pods (B2B, Claude Code, knowledge worker, API)
- Growth team indexes toward larger bets (70/30 or 50/50) vs. traditional small-to-medium optimizations — driven by exponential thinking about product value
- CACHE initiative (Claude Accelerates Sustainable Hypergrowth): using Claude to automate growth experimentation — identifying opportunities, building, testing, analyzing results
- Growth team built the Chrome extension that underpins Claude Code and Co-work use cases
- Head of Growth is Amol Avaisary, who cold-emailed Mike Krieger to get the job

### Culture
- Structured as a Public Benefit Corporation (PBC), not a Delaware C-corp — legally allows optimizing for public benefit over shareholder value
- Mission: "Make sure the transition to powerful AI goes well and is net beneficial for humanity"
- "Notebook channels": everyone has a Slack channel where they share internal thoughts, provocative ideas, and leaders scale their beliefs — also serves as training data for Claude
- Extreme openness: employees are encouraged to publicly disagree with Dario; debates happen in notebook channels
- Amol: "I have not met a single person who's checked out. Everyone is putting everything they have on the table."
- Talent density compared to "playing for Real Madrid"
- Anthropic had Claude before ChatGPT launched but chose not to release it for safety reasons — didn't want to kick off an AI arms race
- Leadership team is considered the strongest across any of the major AI labs by people who've worked at multiple

### Focus and Strategy
- Extreme focus on B2B and coding from the very beginning — Dan Mad wrote a doc in 2021 arguing for AI coding focus
- Coding focus serves dual purpose: huge TAM + accelerates the research loop (better coding → better models)
- Historically the smallest, least well-funded player — constraints forced extreme focus; "freedom through constraints"
- Uses Workday, Figma, Slack, and other SaaS tools heavily — doesn't see that changing in the immediate future
- 60-80% of what the growth team ships has no PRD — just Slack messages; Amol is averse to PRDs

### PM Team Structure (~30-40 PMs)
- **Research PM team** (led by Diane): understands customer feedback for models, feeds to research, shepherds model launches
- **Claude Developer Platform team**: maintains the APIs Claude Code is built on, releases managed agents
- **Claude Code team**: works on Claude Code and Co-work core products (led by Cat Wu)
- **Enterprise team**: cost controls, RBAC, security controls for enterprise adoption
- **Growth team**: growing across entire product suite (led by Amol Avaisary)
- **Applied AI team**: technical go-to-market, helps customers adopt API, builds prototypes

### Shipping Velocity and Process
- Feature timelines have gone from 6 months to 1 month, 1 week, or even 1 day
- Almost all features ship as "research previews" — reducing commitment, enabling 1-2 week turnaround
- "Evergreen launch room": tight process where engineers post ready features, and PMM, docs, DevRel turn around marketing the next day
- "We want to remove every single barrier to shipping things"
- Weekly metrics readouts with entire team; team principles enable independent decision-making
- PRDs used occasionally for ambiguous features or heavy infrastructure projects

### Models
- Built Mythos: an incredibly powerful model still in preview — "people are a little afraid of what it can do"
- Opus 4.5, Opus 4.6, and Sonnet 4.6 enabled reliable AI code review for the first time
- Anthropic uses frontier models internally, creating an AI flywheel effect

### Claude Code Source Code Leak
- Human error: a human working with Claude on a PR, which went through two layers of human review
- Process failure, not individual — the person is still at Anthropic
- Processes have been hardened to prevent recurrence

### OpenClaw Decision
- Prioritized first-party products and API over third-party OpenClaw usage
- OpenClaw users got credits alongside their subscription
- "Hard decision" driven by massive demand and different usage patterns

### Culture
- "Just do things" mentality — roles are blurry, people are empowered to operate across boundaries
- Team leans into chaos, faces challenges with a smile
- "If Claude Code failed but Anthropic succeeded, I would be extremely happy" — teams sacrifice own OKRs for Anthropic's mission
- Slack is "the core OS of the company"
- Claude Code has lowered the barrier to building custom internal apps ("crystallized work software")
- Claude's character is a key differentiator — molded by Amanda, described as light-hearted, fun, low ego, positive

## Related

- [[Claude]] — Anthropic's AI model
- [[summary-40 - The $1B Al company training ChatGPT, Claude & Gemini on the path to responsible AGI ｜ Edwin Chen]] — source summary
- [[summary-31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz]] — source summary
- [[Model Differentiation]] — how values shape model behavior
- [[Objective Functions in AI]] — what models optimize for
- [[summary-37 - Why securing AI is harder than anyone expected and guardrails are failing ｜ HackAPrompt CEO]] — source summary
- [[Constitutional Classifiers]] — Anthropic's defense mechanism
- [[Claude Code]] — Anthropic's AI coding agent
- [[Bun JavaScript]] — acquired by Anthropic
- [[Zevi Arnovitz]] — uses Anthropic's tools extensively
- [[Boris Cherny]] — Head of Claude Code
- [[Ben Mann]] — co-founder
- [[Mike Krieger]] — kicked off Anthropic Labs team
- [[Chris Olah]] — mechanistic interpretability pioneer
- [[Jenny Wen]] — head of design for Claude, now leading design for Claude Co-work
- [[summary-25 - Head of Claude Code： What happens after coding is solved ｜ Boris Cherny]] — source summary
- [[summary-23 - The design process is dead. Here's what's replacing it. ｜ Jenny Wen (head of design at Claude)]] — source summary
- [[Mechanistic Interpretability]] — pioneered at Anthropic
- [[AI Safety Layers]] — Anthropic's three-layer safety framework
- [[Race to the Top]] — Anthropic's safety strategy
- [[Co-work (Claude)]] — Anthropic's agentic product for non-coding tasks
- [[Claude Co-work]] — Anthropic's agentic product
- [[OpenClaw]] — Opus 4.6 and Sonnet 4.6 are recommended models for OpenClaw agents due to their security hardening against prompt injection
- [[summary-18 - From skeptic to true believer： How OpenClaw changed my life ｜ Claire Vo]] — source summary
- [[Amol Avaisary]] — Head of Growth
- [[Alexey Komissarouk]] — growth engineer, leads CACHE
- [[Amie Vora]] — product leader
- [[Dan Mad]] — co-founder
- [[Nick Lin]] — runs financial services product
- [[Dario Amodei]] — CEO
- [[Daniela Amodei]] — co-founder
- [[CACHE (Claude Accelerates Sustainable Hypergrowth)]] — automated growth initiative
- [[Success Disasters]] — growth team concept
- [[Notebook Channels]] — internal culture practice
- [[Public Benefit Corporation (PBC)]] — corporate structure
- [[summary-16 - Head of Growth (Anthropic)： Anthropic is automating its own growth]] — source summary
- [[Cat Wu]] — Head of Product, Claude Code
- [[Mythos]] — frontier model in preview
- [[Sonnet 4.6]] — model enabling code review
- [[Amanda (Anthropic)]] — molds Claude's character
- [[Diane (Anthropic)]] — leads Research PM team
- [[Sid (Anthropic)]] — engineer, created to-do list tool
- [[summary-13 - How Anthropic's product team moves faster than anyone else ｜ Cat Wu (Head of Product, Claude Code)]] — source summary
- [[Evergreen Launch Room]] — shipping process
- [[Crystallized Work Software]] — custom internal apps
- [[OpenClaw Decision]] — prioritization of first-party products
- [[Claude Code Source Code Leak]] — security incident
- [[Applied AI Team]] — technical go-to-market team
- [[Claude's Character]] — personality as differentiator
