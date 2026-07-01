---
title: "Viktor： AI Coworker That Lives in Slack — Fryderyk Wiatrowski"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260511 - Viktor： AI Coworker That Lives in Slack — Fryderyk Wiatrowski.md"
date: 2026-05-11
ingested: 2026-06-29
tags: [ai-employee, ai-coworker, company-agent, slack, victor, integrations, personality, proactivity, shared-context]
---

## Core Thesis
Fryderyk Wiatrowski, co-founder of Viktor, presents Viktor as an AI employee/coworker that lives in Slack, has access to 3,000+ integrations, and acts as a company-wide agent with shared context. Unlike personal AI agents (like OpenClaw), Viktor is a "company agent" — one person connects an integration and the whole team benefits. The talk traces Viktor's evolution from web agents (JCAI) to email agents (Jace) to the current Slack-based AI employee, and outlines three pillars for a great AI coworker: (1) helps get work done (connected integrations), (2) knows the company (Slack context), and (3) is friendly (personality matters). The central thesis is that Viktor is "not a tool, it's a hire" — it should be treated like a human employee with appropriate scoping of access and integration.

## Key Topics
- **Viktor Overview**: Launched February 2026 as an experiment with zero growth expectations; achieved immediate product-market fit. Lives in Slack (no web app), has access to 3,000+ integrations, and can build its own connections if an integration is missing. Viktor has "universal PhD level understanding" across all areas of the company — broad horizontal context that no human employee possesses.
- **Evolution from Web Agents**: In 2023, the team believed the right way to build AI employees was through browsers. JCAI was their web agent — state-of-the-art on the WebArena benchmark — that took DOM snapshots, minified them losslessly, and decided on next steps. But it only worked reliably for 3-5 steps at ~60% reliability, making it impractical as a product due to speed and compounding error issues.
- **Jace — The Email Agent**: When Sonnet 3.5 launched, the team built Jace, an email agent that could react to incoming emails with tool calls (not just drafts). For example, if someone requested a refund, Jace could automatically process it (with optional approval gates). Jace achieved product-market fit and is still alive.
- **Company Agent vs Personal Agent**: Viktor is designed as a company agent, not a personal agent like OpenClaw. Key differences: (1) company agents live where you work and have all company context, (2) only one person needs to connect an integration — Viktor inherits permissions and the whole team benefits, (3) no need to connect the same integration 100 times across team members.
- **Slack as Interface — Why and What Breaks**: Two reasons for choosing Slack: (1) it feels like interacting with a human employee (no separate web app), (2) for long-running tasks (10+ minutes), Slack's async nature makes latency feel acceptable — "if you ping someone on Slack and tell them to build an app and get an answer in 10 minutes, you are shocked." What breaks: Slack has multiple interaction modes (DMs, channels, threads, emoji reactions, message edits, deletions) that all serve as agent inputs and must fit into a linear context. Examples: edited messages need updated responses, deleted messages should signal task cancellation, and users often abandon threads and start new DMs — the agent must roll over context from previous conversations.
- **Memory Challenges at Scale**: Personal agents face memory clutter over time; company agents with 100+ users face it 100x faster. Viktor solved this multi-user memory problem.
- **Context Isolation Across Channels**: Viktor may be in growth channels, engineering channels, executive channels, and DMs simultaneously. Context from the growth channel must not leak to engineering or support. Similarly, DM context should not pull from the growth channel unless the user is on the growth team. This requires structured access control beyond simple conversation threading.
- **Personality and Model Selection**: The team tested replacing Opus 4.6 (Viktor's main model) with GPT 5.4, which was actually better at tool calling and code generation and cheaper. Users rejected it — they loved Opus's personality. "There is something beautiful in that model." Opus in Viktor has a slightly sassy tone that users appreciate. Personality directly impacts user adoption and satisfaction.
- **Proactivity**: Viktor can proactively suggest automatable workflows. Example: in a growth team discussing A/B test results, Viktor can check PostHog, verify statistical significance, run calculations, and join the conversation. This drives broader activation in the workspace. Risk: if enabled on day one, security teams react badly — recommend gradual rollout starting with a few users.
- **Shared Context vs Desktop Agents**: Viktor works in the cloud (no computer needed to be open). Unlike Claude Code or desktop agents, Viktor's integrations are shared across the company — one person connects Meta Ads or analytics, and the whole team uses it. In a 100-person team with 20 in growth, asking everyone to connect individually is painful and error-prone (someone connects wrong integrations).
- **Viktor is a Hire, Not a Tool**: Customer story — an admin at a major US e-commerce brand connected Viktor to their personal Gmail as a team integration, and the team started discussing that person's emails. Lesson: treat Viktor like a human employee — don't give it access to personal accounts as shared integrations. Viktor now supports scoped integrations (personal vs shared).
- **Three Pillars for Great AI Coworkers**: (1) Helps get work done — models are capable today, connect integrations (e.g., via Pipedream), (2) Knows the company — utilize Slack context, navigate Slack's approval process, (3) Make it friendly — personality makes a difference; ensure the team likes Viktor and Viktor likes the team.
- **Historical Vision**: Fryderyk ties the AI employee vision to Gottfried Leibniz (17th century), who wanted to build a calculator to free humans from "the labor of calculation." Quotes Leibniz: "It is unworthy of excellent men to lose hours like slaves in the labor of calculation. Let us leave that to machines." The vision of automating cognitive tasks has been with us for centuries.

## Entities
- [[Viktor]] — AI employee/coworker platform, lives in Slack
- [[Fryderyk Wiatrowski]] — co-founder of Viktor, speaker
- [[JCAI]] — predecessor web agent, state-of-the-art on WebArena benchmark
- [[Jace]] — predecessor email agent with tool-calling capabilities
- [[OpenClaw]] — personal agent, contrasted with Viktor's company agent approach
- [[Slack]] — primary interface and living environment for Viktor
- [[Anthropic]] — provider of Opus 4.6, Viktor's main model
- [[PostHog]] — analytics tool Viktor integrates with for proactive insights
- [[Pipedream]] — integration platform suggested for building AI coworker connections
- [[ClaudeCode]] — desktop agent contrasted with Viktor's cloud-based approach
- [[OpenAI]] — provider of GPT 5.4, tested as alternative model
- [[aiDotEngineer]] — conference where talk was presented

## Concepts
- [[AI Employee]] — AI as a hire, not a tool; treated like a human team member
- [[Company Agent]] — agent with shared integrations across the organization, distinct from personal agents
- [[Personal Agent]] — individually-owned agent with personal integrations (contrasted with company agent)
- [[Shared Context]] — integrations connected once and shared across the team
- [[Agent Proactivity]] — agent proactively suggesting workflows and joining conversations
- [[Context Isolation]] — preventing context leakage between channels and teams in a company agent
- [[AgentPersonality]] — model personality as a critical factor in user adoption and satisfaction
- [[Agent Memory]] — multi-user memory management challenges at scale
- [[Web Agent]] — browser-based AI agents (JCAI's original approach)
- [[SlackBased Agent Interface]] — using Slack's multi-modal interaction surface as an agent input layer
- [[Integration Scoping]] — personal vs shared integration access control
- [[AgenticLoop]] — the agent loop pattern underlying Viktor's operation
- [[ToolCalling]] — function calling capability enabling Viktor to use 3,000+ integrations

## Related
- [[summary-20260417 - State of the Claw — Peter Steinberger]] — OpenClaw as personal agent counterpart
- [[summary-20260423 - The End of Apps — Kitze, Sizzy.co]] — personal agents and the end of web apps
- [[summary-20260422 - Agents need more than a chat - Jacob Lauritzen, CTO Legora]] — agent interaction modes beyond chat
- [[summary-20260418 - The Friction is Your Judgment — Armin Ronacher & Cristina Poncela Cubeiro, Earendil]] — agent personality and user experience
- [[summary-20240731 - Emergence Launch： AI Agents and the future enterprise： Dr. Satya Nitta]] — web agents and enterprise AI
