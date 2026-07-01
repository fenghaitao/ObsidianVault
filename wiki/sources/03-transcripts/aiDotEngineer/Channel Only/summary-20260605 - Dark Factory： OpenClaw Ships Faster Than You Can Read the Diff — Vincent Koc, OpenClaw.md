---
title: "summary-20260605 - Dark Factory： OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw"
type: source
tags: [source, transcript, ai, open-claw, agents, dark-factory, swim-lanes, token-efficiency, engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Dark Factory： OpenClaw Ships Faster Than You Can Read the Diff — Vincent Koc, OpenClaw.md"]
last_updated: 2026-06-30
---

## Core Summary
Vincent Koc, core maintainer at OpenClaw, presents his "dark factory" approach to AI-assisted software engineering. He describes how OpenClaw achieves astronomical velocity (3,000+ commits/day at peak, 800 commits/day sustained, 60K+ PRs total) through parallel agent swim lanes managed like a production line. The talk frames engineering as shifting from writing code to managing agents — the bottleneck is no longer code production but human taste and soft skills in steering autonomous agents. Vincent contrasts 2025's "token maxing" approach (burning massive tokens in Ralph-style loops) with 2026's shift toward token efficiency and agent-in-the-loop engineering.

## Key Points

### The Dark Factory Vision
- OpenClaw's velocity is not luck — "there's actual engineering work here"
- Analogy: the Industrial Revolution moved from handlooms in cottages to centralized mills; software engineering is undergoing the same transformation
- Engineers become factory managers; the bottleneck shifts from writing code to taste and judgment
- "The ways we used to work before just don't work anymore"

### Scale & Velocity
- At peak: Vincent hit close to 3,000 commits/day (March 15)
- Sustained: ~800 commits/day across ~10-15 core maintainers, all with day jobs
- 60,000+ PRs total in the project
- Vincent's commit history literally shows when he sleeps — commits stop when he goes to bed
- This scale is "going to become the norm everywhere else"

### The Great Refactor (Nvidia Session)
- While at Nvidia working on NeMo Claw, another maintainer moved entire channel folders (Slack, MS Teams) — forcing a refactor
- "It was 2:00 in the morning. We're tired. We thought, 'Why not refactor the entire code base?'"
- Result: 2,700 commits, close to 1M lines changed, 82% of core codebase touched
- Launched plugin architecture — each provider (OpenAI, Mistral, Anthropic) owns their piece of the code
- Vision: cut the codebase down, not bloat it — saying no, not yes
- Saving grace: over-fitted AI-generated unit tests that still passed after the refactor, proving the system was intact

### Swim Lanes: The Factory Pattern
- Vincent runs multiple parallel agent sessions (5-20+) organized into swim lanes
- Each swim lane has a different purpose: CI, features, bugs, refactoring, P0/P1 monitoring
- Low-touch lanes (refactoring tests): "Take your time. Make sure tests pass. Just push them through."
- High-touch lanes (features, Docker, messaging channels): conversational, investigating, coming back
- Monitor lanes: agents in Discord channel reporting on releases — "What happened in the last 2 hours?"
- Bottleneck: "tokens are no longer the problem... raw compute and my brain space"

### Bot Looping vs. Ralph Looping
- Ralph looping: burning tokens for 8-9 hours, hoping something happens — "this reminds me of Ralph looping"
- Bot looping: a more opinionated approach — run loops but be smarter about it
- Question: "Do we need more than just tokens? What does that reward mechanism look like?"

### Token Maxing (2025) → Token Efficiency (2026)
- 2025 was about "token maxing" — burning as many tokens as possible in agent loops
- 2026 is about "not wasting them" — token efficiency, agent in the loop
- The shift from brute force to smart engineering

### Intuition & Reasoning Tokens
- Vincent describes developing an intuitive feel for agent reasoning: "You start to have this relationship where you can feel the reasoning tokens"
- He knows something is off not by what the agent does, but by how it explains itself — "It's waffling. It's not making sense."
- This feels like managing people: "If I had someone working for me and they started downright bullshitting, I'd be like, 'Wait a minute.'"
- When agents go off-track, Vincent may nuke the session and either delegate to another maintainer or revisit days later
- This intuition was built through "sheer volume of token maxing" over the previous year

### Soft Skills for Agent Management
- "How do you manage 10 plus agents?" → "How do you manage 10 plus staff?"
- Vincent's experience managing 30-40+ people in large organizations (airlines, etc.) directly transfers to managing agents
- For engineers new to this: "it's the soft skills that matter"
- Key skills: asking agents "What's going on?", knowing when they're bullshitting, running the factory

### Agent Development Environment
- Vincent uses a system of ".skills" (similar to dotfiles), available open source on GitHub
- Skills cover technical documentation, agent workflows, and other engineering practices
- Process: use a skill, read Codex session logs, make improvements to the skill, deploy
- Uses vercel.skills.sh as a distribution mechanism
- Some skills are private; public ones available on GitHub

### Git Worktrees & Infrastructure
- Vincent adopted Git worktrees — regrets it due to heavy test harness overhead
- Each PR creates a new worktree; can have 70-80 active worktrees on any given day
- Had to build custom "magic sauce" around his Codex session to manage worktrees
- Alternative approach (used by Peter Steinberger): clone the repo 10 times, point 10 different Codex sessions to each one
- "I don't use plan mode or spec mode. I have a conversation with the agent and we work through it."

### PR Management & Deduplication
- 60,000+ PRs — every new maintainer tries to solve the PR problem
- Vincent's approach: semantic graphing and vector embedding on the entire GitHub repo
- One PR had 73-106 edges in the graph
- Signal detection: "If there's enough pressure coming on one issue, it must be big enough that all these other clankers decided it's a big problem"

### Evals at OpenClaw
- After the refactor, the team built a "fake Slack" with synthetic and real models
- Used for evaluation loops to check that each provider and channel works
- Vincent's day job is in structured evals with telemetry; OpenClaw is "blind faith in the harness"
- These two worlds are "starting to come together"

### Engineering in the Agent Era
- There IS engineering work — it's not just luck or Ralph looping
- The process matters more than the model or agent
- 2026's focus: agent in the loop, token efficiency
- Taste remains the moat — knowing what to say no to, not what to say yes to

## Related
- [[VincentKoc]] — speaker, core maintainer at OpenClaw
- [[OpenClaw]] — the project
- [[PeterSteinberger]] — OpenClaw creator, worked alongside Vincent at Nvidia
- [[Nvidia]] — NeMo Claw collaboration, hosted the great refactor session
- [[NeMo Claw]] — security layer they were building at Nvidia
- [[Codex]] — agent coding tool used by Vincent
- [[SteveYegge]] — referenced as "vibe maintainer" pushing 50 PRs/day
- [[Spotify]] — cited as company "no longer writing code by hand"
- [[Anthropic]] — cited for C compiler work with autonomous agents
- [[Dark Factory]] — the core concept of engineering as factory management
- [[Swim Lanes]] — parallel agent workstreams pattern
- [[Bot Looping]] — opinionated alternative to Ralph looping
- [[Ralph Loop]] — the "burn tokens for 8-9 hours and hope" approach
- [[Agent Development Environment]] — skills management and agent workflow system
- [[Token Maxing]] — 2025's brute force approach
- [[Token Efficiency]] — 2026's shift toward smarter agent usage
- [[GitWorktrees]] — infrastructure pattern Vincent adopted (and regrets)
- [[Plugin Architecture]] — the great refactor's architectural outcome
- [[SayingNo]] — key taste skill in an era of cheap tokens
- [[Agent Parallelism]] — running multiple agents simultaneously
- [[AgentHarness]] — the infrastructure running agent sessions
- [[Vibe Maintainer]] — Steve Yegge's self-description, role Vincent relates to
- [[Slack]] — messaging channel used for agent monitoring and evals
- [[Discord]] — used for agent monitoring channels
- [[Docker]] — one of Vincent's swim lane focus areas
- [[GitHub]] — source of PRs and issues for semantic graph analysis
