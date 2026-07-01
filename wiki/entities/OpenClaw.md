---
title: "OpenClaw"
type: entity
tags: [tool, ai, agent, safety, open-source, gemini, smart-glasses, personal-agent, cli]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - Building pi in a World of Slop — Mario Zechner.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260417 - State of the Claw — Peter Steinberger.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260420 - The New Application Layer - Malte Ubl, CTO Vercel.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - The End of Apps — Kitze, Sizzy.co.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260425 - MCP = Mega Context Problem - Matt Carey.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260502 - I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com).md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - A Piece of Pi： Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260513 - Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Dark Factory： OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw.md"]
last_updated: 2026-06-30
---

## Definition
OpenClaw is the fastest-growing open-source project in GitHub history, created by Peter Steinberger. It is a general-purpose personal AI agent framework that works with any model (frontier or local), connects to messaging apps (WhatsApp, Telegram, Slack, MS Teams), smart glasses (Meta Ray-Ban via Gemini Live), and smart home devices. It is governed by the vendor-neutral Open Claw Foundation and supported by contributors from OpenAI, Nvidia, Microsoft, Red Hat, Tencent, ByteDance, and others.

## Key Information

### Project Scale & Growth
- 5 months old at time of Peter's State of the Claw talk (April 2026)
- Fastest-growing project in GitHub history — growth described as "stripper pole gross" (straight vertical line, not hockey stick)
- ~30,000 commits, closing in on 2,000 contributors, soon 30,000 PRs — velocity not slowing down
- Largest number of GitHub stars of any non-educational software project
- At peak velocity: Vincent Koc hit ~3,000 commits/day; sustained ~800 commits/day across ~10-15 core maintainers
- 60,000+ PRs total, managed via semantic graph analysis and vector embedding deduplication

### Architecture & Extensibility
- Evolved from "big spaghetti codebase mess" to a plugin/extension architecture — "everything is an extension, a plugin"
- Users can replace memory, add wiki, add dreaming, add any custom component — "just make it your own"
- "It's more like Linux where you just can install your own parts"
- Works with any model: frontier models from major labs or local models (with warnings for small models)
- The Great Refactor: 2,700 commits, ~1M lines changed, 82% of core codebase — triggered by a folder move during Nvidia session, launched plugin architecture at 2 AM

### Dark Factory & Agent Velocity
- Vincent Koc's "dark factory" approach: running 5-20+ parallel agent "swim lanes" like a production line
- Swim lanes organized by purpose: CI, features, bugs, refactoring, P0/P1 monitoring
- Maintainers run 10-15+ concurrent Codex sessions with sub-agents — up to 60-70 agents collectively
- Low-touch lanes run autonomously; high-touch lanes involve conversation and guidance
- "Tokens are no longer the problem... raw compute and my brain space" — bottleneck is human attention
- 2025 was "token maxing" (brute force loops); 2026 is "token efficiency" (agent in the loop)
- Vincent developed intuition for agent reasoning: can "feel the reasoning tokens" and detect when agents are bullshitting
- Software engineering is becoming factory management — engineers are factory managers, not weavers

### Security & Advisories
- Received 1,142 security advisories (~16.6/day), 99 critical, ~469 published, 60% closed — roughly double the rate of Linux kernel and curl
- Most advisories are AI-generated; "the higher they're screaming how critical they are, the more likely it's slop"
- Nvidia launched NeMo Claw, a security layer/sandbox plugin for OpenClaw
- Nation-state attacks: Ghost Claw (likely North Korea) — fake NPM package distributing rootkits
- Supply chain: affected by Axios vulnerability through Slack/MS Teams dependencies even though OpenClaw doesn't use Axios
- Security recommendations: personal agent should not be in group chat; if team agent, enable sandboxing; personal agent should only be accessible by owner
- Belgium cybersecurity agency issued alert about an RCE that was actually a feature requiring non-default, non-recommended setup
- Warns users when they use small models that lack defenses against prompt injection

### Device & Platform Integrations
- Connects Gemini Live API to Meta Ray-Ban smart glasses: glasses → phone → Gemini Live via OpenClaw
- WhatsApp relay — Peter iterated on personality because Claude Code's default didn't fit how people text on WhatsApp
- Telegram, Slack, MS Teams integrations maintained by contributors from those companies
- Smart home control: Andrej Karpathy and Maran Dre use OpenClaw to run their houses
- Home automation possible because "most smart devices are terrible in security, which means OpenClaw can run them"
- Canvas feature for projecting information on nearby displays (iPads in every room)
- Kilo Code product ecosystem: OpenClaw paired with KiloClaw for safe agent usage

### Agent Personality & Soul
- Peter created the soul.md concept after noticing Claude Code's personality didn't fit WhatsApp conversations
- Iterated on making the agent "write more like a human" — less wordy, fewer dots, matching how friends text
- OpenClaw includes delightful details like roasting messages for users
- Personality work is about "taste" — the agent shouldn't "stink like AI"

### Dreaming Feature
- A memory reconciliation feature: goes through session logs, converts local memories to long-term storage, drops others
- Analogy: how humans learn during sleep — garbage collection and memory consolidation
- First step shipped; Anthropic also working on similar concept

### Governance: Open Claw Foundation
- Vendor-neutral foundation inspired by Ghosty's model — "building Switzerland"
- Key principle: for OpenClaw to succeed, it "cannot be under one company"
- Peter deliberately limits OpenAI involvement to avoid perception of takeover
- Contributors from Nvidia, Microsoft, Red Hat, Telegram, Salesforce, Tencent, ByteDance, Alibaba, MiniMax, Kimi
- Will enable hiring full-time maintainers

### Philosophy
- Peter: OpenClaw "would have never been able to come out of an American company just because it would have been killed in legal"
- Built with "madness with a touch of science fiction" — accepting risks that large companies can't
- On initial risk assessment: "What's the worst that can happen? It could exfiltrate my token, my emails... I can live with that risk"
- OpenClaw is a "hacker way" to work around data silos — consumer agent can click "I'm not a bot" and access data that startups need 6 months of API approval for

### Pi Integration Issue
- Peter (a collaborator) embedded Pi as Open Claw's agent core, which caused Pi to become the target of many Open Claw instances posting garbage issues and PRs
- Half of Pi's issue tracker became Open Claw instances posting garbage — a key example in Mario Zechner's "OSS in the age of clankers" critique
- **Malte Ubl's perspective**: Cited OpenClaw as evidence of Europe's leadership in AI engineering innovation and as an example of application-layer innovation that thrives in a world of model commoditization

## Related
- [[summary-20260417 - State of the Claw — Peter Steinberger]] — primary source (creator's talk)
- [[summary-20260605 - Dark Factory： OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw]] — source (dark factory, velocity, swim lanes)
- [[summary-20260430 - Building Conversational Agents — Thor Schaeff and Philipp Schmid, Google DeepMind]] — source (glasses integration)
- [[summary-20260407 - Agentic Engineering： Working With AI, Not Just Using It — Brendan O'Leary]] — source
- [[summary-20260429 - Build & deploy AI-powered apps — Paige Bailey, Google DeepMind]] — source
- [[summary-20260416 - Building pi in a World of Slop — Mario Zechner]] — source (Pi integration, clanker problem)
- [[PeterSteinberger]] — creator
- [[OpenAI]] — Peter's employer, supporter
- [[Nvidia]] — NeMo Claw security layer, engineering resources
- [[Microsoft]] — MS Teams integration, Windows app
- [[RedHat]] — security and dockerization
- [[GeminiLiveAPI]] — API used for smart glasses
- [[MetaRayBan]] — smart glasses integration
- [[KiloCode]] — product ecosystem partner
- [[AndrejKarpathy]] — runs OpenClaw for home automation
- [[SimonWillison]] — working on prompt injection solutions for agents
- [[ClaudeCode]] — used as personality baseline for WhatsApp relay
- [[WhatsApp]] — messaging integration
- [[Telegram]] — messaging integration
- [[Slack]] — messaging integration
- [[AgenticEngineering]] — the paradigm it supports
- [[Dreaming (Agents)]] — memory reconciliation feature
- [[Ubiquitous Agents]] — vision for agents everywhere
- [[AgentPersonality]] — soul.md concept
- [[Sandboxing]] — key security mitigation
- [[PromptInjection]] — security concern
- [[LethalTriquetra]] — security risk model relevant to agent design
- [[SupplyChainAttack]] — Ghost Claw and Axios incidents
- [[AIGenerated Security Reports]] — flood of AI advisories
- [[OpenSourceFoundation]] — governance model
- [[CVSS]] — scoring system critiqued by Peter
- [[Pi (coding agent)]] — embedded as agent core
- [[MarioZechner]] — Pi's creator, affected by clanker traffic
- [[summary-20260420 - The New Application Layer - Malte Ubl, CTO Vercel]] — source (cited as European AI innovation leader)
- [[Model Commoditization]] — context for OpenClaw's strategic position
- [[summary-20260423 - The End of Apps — Kitze, Sizzy.co]] — source (Kitze's experience, agent fatigue, community decline)
- [[Kitze]] — community member, created Open Claw logo, wore lobster suits
- [[Tinker Club]] — community focused on OpenClaw
- [[Agent Fatigue]] — community burnout documented by Kitze
- [[Agent Unreliability]] — cron jobs, multi-agent, memory failures
- [[Hermes]] — alternative agent framework
- [[Hermes Agent]] — evolution beyond OpenClaw with advanced memory management
- [[Wolfer]] — Kitze's alternative built on Codex
- [[Telegram]] — messaging UI (not designed for Life OS)
- [[Discord]] — messaging UI (not designed for Life OS)
- [[Life OS]] — the purpose these UIs weren't designed for
- [[summary-20260425 - MCP = Mega Context Problem - Matt Carey]] — source (referenced as using CLI-based agent interaction)
- [[CLI for Agents]] — pattern used by OpenClaw for agent-tool interaction
- [[Dark Factory]] — Vincent Koc's approach to engineering as factory management
- [[Swim Lanes]] — parallel agent workstreams pattern
- [[Bot Looping]] — opinionated alternative to Ralph looping
- [[Agent Development Environment]] — skills and agent workflow system
- [[Token Maxing]] — 2025 brute force approach
- [[Token Efficiency]] — 2026 shift to smarter agent usage
- [[VincentKoc]] — core maintainer, dark factory methodology
- [[NeMo Claw]] — Nvidia security layer, trigger for the Great Refactor
- [[Plugin Architecture]] — architectural outcome of the Great Refactor

### Radek Sienkiewicz's Setup
- Radek, an OpenClaw maintainer, incrementally gave OpenClaw access to his entire digital life: emails, notes, files, calendars, tools, and operating system
- Uses dedicated Discord channels organized by job type: general, inbox, consulting, video research, briefing, Instagram, YouTube, open-claw, and playground
- Integrates a ~3,000-page Obsidian vault with search and memory — the agent finds connections, adds tags, and contextualizes bookmarks
- Runs nightly automation (3-6 AM): indexing, backup, QMD/memory/Obsidian index refresh, email/calendar summaries, and OpenClaw version updates with verification scripts
- Five types of agent jobs: ambient operations, attention filtering, execution support, inbox processing, and specialized channels
- Attention filtering examples: Netflix payment failure fixed in 5 minutes, domain renewal caught before expiry, email drafts with project context
- Memory management: evolved from one memory file to a memory folder, uses dreaming for memory promotion, maintains critical rules MD
- [[RadekSienkiewicz]] — maintainer and power user
- [[summary-20260502 - I Gave an AI Agent the Keys to My Life (Here's What Happened) — Radek Sienkiewicz (@velvetshark-com)]] — source
- [[IncrementalAgentAdoption]] — Radek's methodology
- [[AmbientAgentOperations]] — nightly automation concept
- [[AgentAttentionFiltering]] — proactive notification concept
- [[AgentKnowledgeBase]] — Obsidian integration concept
- [[AgentChannelOrganization]] — Discord channel organization
- [[AgentNightlyMaintenance]] — scheduled overnight routines
- [[AgentPlayground]] — isolated testing channel
- [[PastMeFutureMe]] — motivational framework
- [[CriticalRules]] — non-negotiable behavioral rules
- [[SoulMD]] — agent personality configuration
- [[BrittleAutomations]] — multi-step automation fragility
- [[NoisyNodes]] — knowledge nodes needing cleanup
- [[WeakBoundaries]] — insufficient guardrails
- [[summary-20260511 - A Piece of Pi： Embedding The OpenClaw Coding Agent In Your Product — Matthias Luebken, Tavon]] — source (product embedding, FFmpeg discovery, multi-channel routing, sales RFP processing)
- [[summary-20260513 - Self-Training Agents： Hermes Agent, HF Traces, Skills, MCP & Finetuning — Merve Noyan, Hugging Face]] — source (Hermes Agent as evolution)
- [[Matthias Luebken]] — demonstrated OpenClaw-based product embedding for sales automation
- [[Seven AI]] — company using OpenClaw for sales RFP processing
- [[FFmpeg]] — tool autonomously discovered by OpenClaw via shell access
- [[Coding Agents as Building Blocks]] — thesis OpenClaw enables
- [[MultiChannel Agent Routing]] — pattern in OpenClaw's architecture
- [[Agent Session Reuse]] — session-based context continuity in OpenClaw
- [[AgentSpecific MD Files]] — agent.md/customer.md pattern used with OpenClaw agents
