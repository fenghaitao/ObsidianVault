---
title: "summary-20260417 - State of the Claw — Peter Steinberger"
type: source
tags: [source, transcript, ai, open-claw, open-source, security, agents, foundation]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - State of the Claw — Peter Steinberger.md"]
last_updated: 2026-06-26
---

## Core Summary
Peter Steinberger, creator of OpenClaw (the fastest-growing open-source project in GitHub history), delivers a "State of the Claw" talk followed by an AMA with swyx. He covers the project's explosive growth (~30K commits, ~2K contributors, ~30K PRs in 5 months), the overwhelming flood of AI-generated security advisories (1,142 advisories, ~16.6/day, 99 critical), the creation of the Open Claw Foundation as a vendor-neutral home, and his vision for ubiquitous personal agents. The talk is a candid look at the challenges of maintaining the world's most attacked open-source AI project while balancing roles at OpenAI and the Foundation.

## Key Points

### Project Growth & Challenges
- OpenClaw is 5 months old, the fastest-growing project in GitHub history — growth described as "stripper pole gross" (straight vertical line, not a hockey stick)
- ~30,000 commits, closing in on 2,000 contributors, soon 30,000 PRs — velocity not slowing down
- Peter joined OpenAI but also created the Open Claw Foundation — "now I kind of have two jobs"
- Running the foundation is "like running a company on hard mode" — all the responsibilities but with volunteers you can't directly direct
- Bus factor is slowly improving; Vincent (a maintainer) spoke after Peter at the event

### Security Advisory Flood
- 1,142 security advisories received (~16.6/day), 99 critical, ~469 published, 60% closed
- Compare: Linux kernel gets ~8-9/day, curl has ~600 total reports — OpenClaw gets roughly double
- "The higher they're screaming how critical they are, the more likely it's slop" — most advisories are AI-generated
- AI tools are getting so good at identifying multi-chained exploits that "we're going to break all the software that exists"
- Example: NeMo Claw (Nvidia's security layer/sandbox for OpenClaw) — Peter hooked it to Codex security, found 5 sandbox breakout methods in 30 minutes using Nvidia's internal model which is "quite a bit smarter in terms of cyber than what the public has access to"
- Typical attack surface: remote code execution, bypass approval, code injection, path traversal
- Concrete example: CVSS 10 issue (GSHJP) — iPhone app with read-only permission could break system to get write permission, but "in all practical ways it is not even an incident" because the permissive model it exploits isn't used by anyone
- Nation-state attacks: Ghost Claw (likely North Korea) — confusing people with a different NPM package name, installing rootkits
- Supply chain: Axios vulnerability affected OpenClaw even though OpenClaw doesn't use Axios — Slack/MS Teams dependencies use it and didn't pin versions
- "Fear-mongering" from companies and universities: "Agents of Chaos" paper detailed OpenClaw architecture but ignored the security page recommendations
- Security recommendations: don't put personal agent in group chat; if team agent, turn on sandboxing; personal agent should only be accessible by you
- Researchers admitted running OpenClaw in sudo mode "to make the agent maximum powerful" — which requires changing code — but didn't mention it in their report
- Belgium cybersecurity agency issued an alert about an RCE that was actually a feature requiring a non-default, non-recommended setup

### The Lethal Trifecta for Agents
- "Any agentic system that has access to your data, has access to untrusted content, and the ability to communicate is something that's potentially at risk"
- This is not special to OpenClaw — any powerful agent system has this problem
- "The more powerful you make it, the more it can do for you, but the more you also have to understand what it does"

### AI-Generated Security Reports Problem
- Most advisories are created with AI agents, but humans still need to read them — "we're not at the point where you can fully trust that the agent will figure it out"
- Signs of AI-generated reports: "anytime the report is too nice or someone apologizes, that's very likely AI because usually people in security don't apologize"
- Reports rarely come with fixes; if they do, "it's usually a very bad fix"
- Rushing fixes when overloaded "will very certainly break your product"
- Other open-source projects (like FFmpeg) are also publicly complaining about this

### Open Claw Foundation
- Building "Switzerland" — a vendor-neutral foundation inspired by what Ghosty did
- Almost complete; delayed by American banking system ("a little bit slow and very confused when you're not American")
- Will enable hiring full-time people to keep up pace, improve quality, and free Peter's time for "cool stuff"
- Key principle: for OpenClaw to be successful, it "cannot be under one company"
- Peter deliberately limits OpenAI involvement to avoid perception of takeover — brought in Nvidia, Microsoft, Telegram, Salesforce, Tencent, ByteDance, Alibaba, MiniMax, Kimi
- "Nvidia has been immensely helpful... one of the coolest companies in terms of here's some engineers who actually just hire agency and just do things"

### OpenAI & Open Source
- "OpenAI bought OpenClaw — that's not the truth. They might have bought my soul.md"
- OpenAI understands that supporting OpenClaw is useful: people who use OpenClaw at home will come to work asking "why don't we have AI at work?"
- OpenAI is "moving more into the open direction" — Codex is open source, released Symphony orchestration layer
- Compared to "some other top tier labs that start with an A" that "very much will sue you if you leak any of their source or block you if you are too successful"

### Peter's Coding Workflow
- At peak: running almost 10 sessions simultaneously, especially when Codex with 5.1 was slow
- Now: ~5-6 windows, each loop is faster with improvements and fast mode
- "We're going to move into a future where tokens will be faster and faster"
- Working on multiple things at once is "basically a workaround until faster"
- On dark factory (fully automated coding): "I don't see how you could fully automate that" — software development is iterative, not waterfall
- "The way to the mountain is usually never a straight line"
- Bottleneck is still "thinking and having taste"

### Taste
- "Taste is very important" — the moat in AI-assisted development
- Lowest level: "if it doesn't stink like AI" — writing style, personality, UI that immediately signals AI generation
- Higher level: now that so much is automatable, more time for "the little details" — delightful touches like OpenClaw's roasting messages
- Taste can't be achieved by high-level prompting alone

### Agent Personality & Soul
- Started with WhatsApp relay: noticed Claude Code's personality "didn't really fit how people would write to you on WhatsApp"
- Iterated on making the agent write "more like a human" — less wordy, fewer dots, matching how friends text
- This led to the soul.md concept and the personality work OpenClaw is known for

### Ubiquitous Agents Vision
- "I want to be in any room... like Star Trek when you can say 'computer'"
- Has iPads in every room; agent can use canvas feature to project information on nearest display
- "The phone is just a very convenient input point but I kind of want to talk to it from anywhere"
- Future: glasses, earbuds — "if I'm around and I have glasses I should just be able to listen in and project something on me"
- Multi-agent future: personal agent at home, work agent, and they should be able to talk to each other "in a way that both your company and you are comfortable with"

### Prompt Injection
- "Probably not enough yet" — but front-end models are "really quite good at detecting" random injection from websites/email
- Marking content as untrusted makes exfiltration "very hard"
- If attacker has unlimited access and can bombard the agent, "there's still a chance"
- Concern about people running small models (e.g., 20B parameter) that "just does whatever you tell it" without defenses
- OpenClaw warns users when they use small models — "you have to steer the regular user a little bit into a direction to make it harder for them to shoot themselves in the foot"
- Simon Willison has been working on prompt injection; dual LLM approach "seems smart"
- Trust system (reputation over time, more trust = more privileged access) is "part of the story"

### Dreaming
- A feature Peter wanted to work on but his maintainers worked on it while he was busy
- "A way to reconcile memories and create a dream log going through session logs"
- Analogy: how humans learn — experience during the day, sleep does garbage collection, converts local memories to long-term storage, drops others
- First step shipped; Anthropic also working on similar concept (per source code leak)

### Home Automation with OpenClaw
- Andrej Karpathy and Maran Dre both run OpenClaw to run their houses
- "OpenClaw for homes is like a kind of underrated" use case
- "It's only possible because the internet of things means that most smart devices are terrible in security, which means OpenClaw can run them"

### Skills for Engineers in the Age of AI
- Taste — the ability to distinguish good from AI-generated slop
- System design — "if you don't think about that, you will eventually swipe yourself into a corner"
- Saying no — "even the wildest idea is just a prompt away... this idea and this idea and this idea and then how all of that fits together, that's the problem"
- Big picture thinking — agents thrown into a codebase "basically don't know what DF this is"; it's our job to provide hints and context so the agent does its best work

### Madness with a Touch of Science Fiction
- OpenClaw "would have never been able to come out of an American company just because it would have been killed in legal long before it would have been released"
- "It just has some problems that we haven't really solved as an industry yet"
- Built it thinking: "What's the worst that can happen? It could exfiltrate my token, my emails... I can live with that risk"
- "If your company is different, it requires a little different approach"

## Related
- [[PeterSteinberger]] — speaker, creator of OpenClaw
- [[OpenClaw]] — the project
- [[swyx]] — AMA moderator
- [[OpenAI]] — Peter's employer, supporter of OpenClaw
- [[Nvidia]] — NeMo Claw, security help, engineering resources
- [[Codex]] — used by Peter for security analysis and coding
- [[SimonWillison]] — working on prompt injection solutions
- [[AndrejKarpathy]] — runs OpenClaw for home automation
- [[Microsoft]] — contributing to OpenClaw (MS Teams, Windows app)
- [[RedHat]] — contributing security and dockerization
- [[Ghosty]] — inspiration for Open Claw Foundation structure
- [[MiniMax]] — model provider collaborating with OpenClaw
- [[LethalTriquetra]] — security risk model (data + untrusted content + communication)
- [[PromptInjection]] — security concern discussed
- [[Sandboxing]] — key security mitigation
- [[SupplyChainAttack]] — Axios/Ghost Claw incidents
- [[AI-Generated Security Reports]] — the flood of AI-created advisories
- [[Dreaming (Agents)]] — memory reconciliation feature
- [[Ubiquitous Agents]] — vision for agents everywhere
- [[Taste (Software)]] — the moat in AI-assisted development
- [[OpenSourceFoundation]] — governance model for OpenClaw
- [[CVSS]] — scoring system critiqued for not reflecting practical risk
- [[AgentPersonality]] — soul.md and making agents feel human
- [[Slop]] — what taste fights against
- [[ClaudeCode]] — used by Peter, personality didn't fit WhatsApp
- [[SystemDesign]] — critical skill for engineers
