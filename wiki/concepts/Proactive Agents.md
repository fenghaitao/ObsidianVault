---
title: "Proactive Agents"
type: concept
tags: [AI, agent, product-design]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/39 - Inside OpenAI： 2026 is the year of agents, AI's biggest bottleneck, and why compute isn't the issue.md", "raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon.md"]
last_updated: 2026-07-10
---

## Definition

Proactive agents are AI systems that anticipate user needs and take helpful action without being explicitly prompted, functioning like a good human teammate who identifies work to be done rather than waiting to be told.

## Key Information

- Alexander Imbiricos describes proactivity as a "major goal" for Codex — evolving from a tool you prompt into a teammate that's "helpful by default"
- Currently, AI products are "actually really hard to use" because you have to be thoughtful about when AI could help; if you're not prompting it, it's not helping
- The average user prompts AI tens of times per day, but could benefit from it thousands of times per day
- A proactive teammate would: read Slack, check DataDog/Sentry, participate in planning and prioritization, validate and deploy code, maintain systems, schedule calendar invites, move standups
- The metaphor: like a new teammate you eventually trust to say "you tell me what you think makes sense to be done"
- The bottleneck to proactivity is validation — agents need to be able to verify their own work before humans can trust them to act autonomously
- The vision of a proactive agent is like a "Tinder meets TikTok meets Codex" app where the agent watches signals, proposes ideas, and you swipe left/right to approve or reject
- John G Donji (CTO of Block) described an engineer at Block who has Goose (their internal agent) watch his screen, listen to meetings, and proactively ship PRs, send emails, and draft Slack messages

- [[Kiti Bottom]] frames proactive agents as "background agents" that understand your workflow and prompt you back — e.g., a coding agent that says "I fixed five of your Linear tickets, here are the patches, just review them at the start of your day"
- ChatGPT Pulse is an early example — a daily update of things you might care about, jogging your brain
- The key enabler for proactivity is [[Context Engineering]] — agents need to be plugged into the right places where actual work is happening to understand context
- Kiti predicts 2026 will be a strong year for proactive/background agents

## Related

- [[Codex]] — the product being built toward proactivity
- [[Super Assistant]] — the broader vision
- [[Human Typing Speed Bottleneck]] — what proactivity solves
- [[Context Engineering]] — the enabler for proactive agents
- [[summary-39 - Inside OpenAI： 2026 is the year of agents, AI's biggest bottleneck, and why compute isn't the issue]] — source summary
- [[summary-33 - Why most AI products fail： Lessons from 50+ AI deployments at OpenAI, Google & Amazon]] — additional source
