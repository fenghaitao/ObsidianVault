---
title: "summary-20260423 - The End of Apps — Kitze, Sizzy.co"
type: source
tags: [source, transcript, ai, personal-agents, productivity, life-os, open-claw, agent-fatigue, end-of-apps]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - The End of Apps — Kitze, Sizzy.co.md"]
last_updated: 2026-06-26
---

## Core Summary
Kitze (creator of Sizzy.co, Benji, and Wolfer) delivers a talk tracing his lifelong obsession with productivity tools — from a 10-year-old's checkbox notebook to building his own personal agent framework. He argues that the future inverts the current human-prompts-AI paradigm: AI will prompt humans with decisions while working autonomously in the background. Consumer apps will largely disappear, replaced by generative UI and local agents. He also candidly documents the "agent fatigue" hitting the OpenClaw community and his own struggles with agent unreliability.

## Key Points

### Kitze's Productivity Journey
- Started at age 10 with a checkbox notebook — "I need to eat my string cheese today"
- Used text files and Android Tasker for contextual reminders (Wi-Fi connect, location arrival) 15 years ago
- Used Google Home + IFTTT to voice-log todos: "tell my assistant to..." would split the command and store it
- Realized he never wanted a to-do app — he wanted a "life OS"
- **TodoDoIt** (2016): priority-based to-do system where items tagged "health" or "crisis" accumulated points and rose to the top
- **Better** (later): expanded to habits, planner, events — realized todos/habits/calendar must be together for a mini-OS. Terrible SEO ("Better app")
- **Benji** (2022–present): "an app to rule them all" — 60+ features including food tracking, calendar, todos, habits, routines. Named after his dog. Still not properly shipped after 3-4 years due to ADHD-driven feature creep: "Maybe one more feature. Maybe one more feature."
- Vision: "Benji phone and a Benji OS" — joked about on a podcast: "Very ambitious for someone who doesn't have a landing page for Benji"

### The Friction Problem
- Oscillates between two states: locked into Benji logging everything for a month, or completely ignoring it for months
- "There's a lot of friction in using all these tools" — forms to input data are the bottleneck
- ChatGPT plugins moment: called his wife saying "it's over for all the apps, for all SaaS" — she now ignores these calls

### Benji AI Assistant (Unshipped)
- 2023: added voice-to-agent feature before models reliably returned JSON — had to "bully the models to return JSON"
- Press a key, record with microphone, periodically cut speech and call Benji APIs
- Calendar would move live, todos would update — "mind-blowing" to people on Twitter
- Went viral but ADHD kicked in: "People like it. It went viral, which means we never have to talk about this again."
- Still hasn't shipped. Meanwhile, others took one feature (food tracking via photo → calorie analysis) and "made multi-millions"
- "But I have 60 features. There's a lesson in there."

### Claude Code & Personal Skills
- October 2025: realized Claude Code with tool calls and functions could do more than coding
- Started loading Claude Code with personal skills — but coding skills and personal skills got confused
- Wanted a "proper assistant that lives on top of Claude Code" with tools for non-coding tasks
- ADHD intervened again: "Let Pete come up with the Claude bot and everything else"

### OpenClaw & The Lobster Cult
- When Peter Steinberger made Claude bot (OpenClaw predecessor), Kitze saw the WhatsApp/Telegram interface as the missing piece
- "My brain caught on fire. I think we got like mass psychosis. It turned into a cult."
- Joined Discord when it had <100 people with Claude bot setups
- Made the Open Claw logo at 2am, wore lobster suits, did tutorials, podcasts, talked use cases
- "I don't know how the internals of my setup work. I just ask either Codex or Claude Code to fix it... I have no freaking idea."
- People ask about his JSON config — "I haven't seen a JSON file since 4 years ago. Just ask my bots."

### Self-Hosting Everything for Agents
- Went "full hipster mode" — no more Gemini, ChatGPT, Claude directly
- "I got the power of finally owning the assistant, owning the files, owning the memory, deleting the sessions if you wanted to"
- Moved everything off cloud: Nextcloud for images, local markdown for everything requiring API calls
- Went back to Android: agent can read notifications, clear notifications, install/uninstall apps
- On iOS: "it can maybe send you a push notification and if Tim Cook allows"

### The Value Question: OpenClaw vs Claude Code/Codex
- Weekly Tinker Club meetups: asks people about their use cases, then "which ones of them you cannot do with Claude Code and Codex?"
- "Immediately, it just reduces by 90%"
- One-on-one chat with one agent "sucks" — like having one employee loaded with all your life information
- People moved to Telegram topics, Discord, Slack to get organized
- Likes specialized agents in OpenClaw (provider model, system prompt/soul, tools/MCPs, permissions)
- Created many bots, each with a purpose — work, personal, fitness, etc.
- Ended up with five Discords, each with many channels, threads, forum posts

### Agent Fatigue & Community Decline
- "My life is far from solved. It's never been more chaotic. I've never been late on rent, on mortgage, on customer emails. It's a mess. But it's a performative mess."
- Tinker Club: initial explosion of sign-ups → now ~5 people per meetup, "slowly turning into Open Claw Anonymous"
- "Yeah, mine didn't do it like the fucking cron job just managed to drive me fucking nuts"
- Problems: unreliable where it matters most — cron jobs, multi-agents, agents talking to each other, agents forgetting in the next message
- "The message is above you. Just go one message above you."
- Discord and Telegram "were not meant for Life OS" — "just molding them into something, but they'll never be the right UI"
- Model personality degradation: "talking to GPT-5... feels like talking to a box of oats. Seriously, it has the personality of this."
- Every conversation: "Did you do that?" No. "But I told you to do that." Okay, I'll do it. "Did you do it?" No.

### Two Futures: Custom Agents vs Cloud Agents
- **Custom agents** (OpenClaw, Hermes): for tinkerers, but "never going to work" for mainstream — Tinker Club members who build pinball machines are "freaking tired of trying to make this thing work"
- **Cloud agents** (Cohere, OpenAI, Perplexity): "too nerfed" — Cohere "cannot do like even 5% of the things that OpenClaw can do"
- Neither wins: cloud for masses, custom for tinkerers who want to self-host and own models

### Wolfer: Kitze's Personal Agent Framework
- A personal experiment, "never going to see the light of day," "not for people"
- Built on Codex only (afraid to use Claude Code: "I might get arrested")
- **Cons**: forced to use app's UI chat (no Telegram/iMessage), opposite of OpenClaw/Hermes extensibility, no memory system, not modular, "made by an ADHD squirrel brain," no OpenAI funding, no lobster logo
- **Pros**:
  - **Nested topics**: hierarchical topic tree (work → projects → Benji → Benji customer support). When chatting in a child topic, the first prompt injects descriptions of all parent topics — no need for memory retrieval
  - **Predictable UI**: built for multi-agent orchestration with multiple topics/conversations, not molding Discord to a purpose
  - **Tool call visibility**: can see, collapse, uncollapse tool calls with loading spinners; stop button without slash commands
  - **Predictable cron jobs**: cron messages read from entire conversation and are labeled as cron
  - **Agent management UI**: right-side panel shows agent name, model, capabilities — can toggle capabilities on/off
  - **Knowledge base & mentions**: write markdown documents, mention them in conversations; combine multiple @-mentions (knowledge base, password, skill) to give exact context
  - **Workspaces**: switch between different contexts

### The End of Apps Prediction
- "The way we use computers right now is absolutely insane" — greeted by 17 updates for unused apps, tabs from yesterday
- Future: computer ingests all life information (notifications, emails, todos) and greets user with the next task, then the next, with breaks
- **AI prompts human** (inverse prompting): "fully productive people will be the one who delegate 99% of the stuff to the AI and then the AI prompts you"
- AI asks: "Hey, you didn't send me a picture of your passport" or "Hey, what do you want to do?"
- Humans do decisions, click forms, answer questionnaires — background agent constantly working
- **End of consumer apps**: "we're actually not going to need most consumer apps"
- Normies won't vibe code but will do any task in a futuristic OS — UI generates on the fly
- Small set of specialist apps survive (color grading, movie making, music making)
- **Apple may win**: local models getting "insanely good" — most people fine with local Siri agent with tool capabilities from installed apps, no credits, data stays local
- Google Pixel already launches apps in background, orders coffee

## Related
- [[Kitze]] — speaker
- [[Benji]] — Kitze's life OS app (60+ features, unshipped)
- [[Wolfer]] — Kitze's personal agent framework
- [[Tinker Club]] — community Kitze founded
- [[OpenClaw]] — the agent framework that sparked the "lobster cult"
- [[ClaudeCode]] — used for personal skills, WhatsApp relay
- [[Codex]] — used for Wolfer, security analysis
- [[Hermes]] — custom agent framework alternative
- [[Paperclip]] — agent orchestrator Kitze juggles
- [[Discord]] — used as agent UI (not designed for it)
- [[Telegram]] — used as agent UI (not designed for it)
- [[Cohere]] — cloud agent (too nerfed)
- [[OpenAI]] — cloud agent direction
- [[Perplexity]] — cloud agent direction
- [[Anthropic]] — model personality degradation critique
- [[Apple]] — may win with local models + Siri
- [[Siri]] — future local agent with tool capabilities
- [[Google Pixel]] — already launches apps in background
- [[Android]] — Kitze switched back for agent control
- [[iOS]] — limited agent capabilities
- [[Google Assistant]] — used for voice-logging todos
- [[Google Home]] — used with IFTTT for voice commands
- [[IFTTT]] — used to split voice commands
- [[Tasker]] — Android automation app used for contextual reminders
- [[Notion]] — mentioned as life OS platform
- [[AgentPersonality]] — "box of oatmeal" degradation
- [[MultiAgentArchitecture]] — specialized agents pattern
- [[AgentToAgentCommunication]] — agents talking to each other (unreliable)
- [[Ubiquitous Agents]] — AI prompts human, ambient computing
- [[OnDeviceAI]] — local models on phones
- [[GenerativeUI]] — UI generated on the fly
- [[Life OS]] — the vision Kitze has pursued since childhood
- [[End of Apps]] — prediction that consumer apps disappear
- [[AI Inverse Prompting]] — AI prompts human instead of human prompting AI
- [[Agent Unreliability]] — cron jobs, memory, multi-agent failures
- [[Nested Context]] — Wolfer's hierarchical topic context injection
- [[Personal Agent]] — owning your assistant, files, memory
- [[Agent Specialization]] — one agent per purpose vs one general agent
- [[Self-Hosting for Agents]] — moving data off cloud for agent access
- [[Agent Fatigue]] — community burnout from unreliable agents
- [[Cloud Agents vs Custom Agents]] — two diverging futures
- [[Local Models for Agents]] — local models winning for normies
