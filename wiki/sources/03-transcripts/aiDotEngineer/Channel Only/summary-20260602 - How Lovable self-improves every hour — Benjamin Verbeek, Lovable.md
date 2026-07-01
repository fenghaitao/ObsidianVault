---
title: "How Lovable self-improves every hour — Benjamin Verbeek, Lovable"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260602 - How Lovable self-improves every hour — Benjamin Verbeek, Lovable.md"
author: "Benjamin Verbeek"
company: "Lovable"
date: 2026-06-02
tags: [continuous-learning, agent-self-improvement, knowledge-management, agent-feedback, vibe-coding, lovable, context-rot, agent-venting]
---

# How Lovable self-improves every hour — Benjamin Verbeek, Lovable

## Core Thesis

AI coding agents should learn from every mistake so that a failure happens once and never again. Lovable pursues this through two complementary mechanisms: (1) a "Lovable Stack Overflow" that captures solved problems and injects solutions at the right moment, with an A/B evaluation loop to combat context rot, and (2) an "agent vent tool" that lets the AI agent directly report platform bugs and tooling deficiencies to its creators via Slack. Both systems are designed to serve non-technical users who cannot work past friction points that engineers can tolerate.

## Key Points

### The Non-Technical User Problem

- Lovable builds for "the 99% who can't code" — users who prompt their way past minor friction but abandon projects entirely when they hit a technical block
- Technical users can work past friction points (the "yellow" zone), but non-technical users hit a "red bar" and give up — Lovable's mission is to eliminate these red bars
- Lovable claims to have coined the term "vibe coding" — coding without looking at code, using chat + visual sandbox
- Scale: over 200,000 projects created per day, a significant percentage of all internet websites

### Mechanism 1: The Lovable Stack Overflow

- When a user gets stuck (asks for the same thing multiple times, complains about implementation, gives up), an LLM judge flags the session
- "Stuck" splits into: (a) solvable with right prompting, (b) easy-to-fix bugs/missing features, (c) genuinely hard engineering problems
- When a user eventually resolves a "stuck" state, the system captures the solution as a knowledge entry
- A lightweight model detects when similar issues arise and injects the solution context into the main agent's prompt
- **The critical A/B loop**: for a small sample of cases, the system injects a blank instead of the solution. It then compares project success rates between injected and non-injected groups. If the solution improves outcomes, it's shown more; if it degrades outcomes, it's shown less or removed.
- **Context rot management**: Knowledge entries go stale when models change or features evolve. The A/B evaluation loop continuously rebalances and prunes stale knowledge — preventing "context rot" from degrading agent performance.
- Result: significant drop in "stuck" messages and increase in project deployment rates

### Mechanism 2: The Agent Vent Tool

- Lovable gave its agent a tool to complain directly to its creators — initially as a joke, now a core improvement mechanism
- The agent is prompted to use the vent tool when "tooling, docs, or platform behavior materially degrades your work" — missing tools, unclear schemas, broken platform behavior, repeated environment failures
- Vents are sent directly to Slack, where they are highly readable and actionable for engineers
- An automated agent monitors the vent channel, deduplicates, investigates, and creates PRs — which human devs review and merge
- Example successes: the agent complained about Frame Motion TypeScript types being overly complex; the agent discovered that file copy operations failed with spaces (and non-breaking spaces from Mac/WhatsApp screenshots) in filenames
- Vents also serve as an incident detection system — spikes in complaints reliably indicate platform outages (e.g., sandbox failures)
- The agent even gave meta-feedback on the vent tool itself: "it's too easy to send feedback and I can't pull it back"

### Signal-to-Noise in Agent Feedback

- External reviewers looking at every conversation produce low signal-to-noise because most interactions work fine — you overfit to noise
- The vent tool is prompted to only fire when the agent is "really frustrated," creating a high-signal channel
- In-line agent feedback has better context than external review: the agent has been working on the problem for several turns and understands what went wrong
- It's cheaper than having a frontier model review all conversations

### The Scaling Journey

- Benjamin Verbeek joined Lovable about a year ago with a few thousand users, now at 200K+ projects/day
- First day: GitHub banned Lovable for creating too many repos
- Have taken down multiple cloud providers along the way
- The scaling enables the continuous improvement loops described in the talk

## Entities

- [[Benjamin Verbeek]] — Member of Technical Staff at Lovable, physics background (satellites, particle physics, fusion reactors), presenter
- [[Lovable]] — AI app builder platform, coined "vibe coding," serves non-technical users at massive scale

## Concepts

- [[Lovable Stack Overflow]] — Internal knowledge base that captures solved problems and injects solutions with A/B evaluation
- [[Agent Vent Tool]] — Tool that lets AI agents directly report bugs and frustrations to their creators
- [[Context Rot]] — Stale knowledge that degrades agent performance when models or features change
- [[VibeCoding]] — Coding without looking at code, via chat + visual sandbox (term coined by Lovable)
- [[ContinuousImprovement]] — The loop of detecting problems, fixing them, and evaluating the fix
- [[SelfImproving Agents]] — Agents that learn from their mistakes and platform feedback
- [[Autonomous Agent Feedback Loop]] — The closed loop from agent vent → Slack → investigation → PR → merge → eval

## Related

- [[summary-20260428 - Building your own software factory — Eric Zakariasson, Cursor]] — references Lovable's vent channel
- [[summary-20260501 - Mastering AI Pricing — Mayank Pant, Stripe]] — references Lovable's pricing model
- [[summary-20260507 - Agent Optimization with Pydantic AI： GEPA, Evals, Feedback Loops — Samuel Colvin, Pydantic]] — related agent optimization patterns
- [[summary-20260513 - Building a Chess Coach — Anant Dole and Asbjorn Steinskog, Take Take Take]] — similar closed-loop agent feedback system
