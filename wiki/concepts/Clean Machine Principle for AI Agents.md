---
title: "Clean Machine Principle for AI Agents"
type: concept
tags: [AI, agent, security, setup, OpenClaw]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/18 - From skeptic to true believer： How OpenClaw changed my life ｜ Claire Vo.md"]
last_updated: 2026-07-11
---

## Definition

The clean machine principle is the practice of running AI agents on a dedicated, separate computer (not your daily work or personal machine) to create physical separation between the agent's workspace and your workspace. This is a foundational security and practical practice for AI agents that have the power to manipulate files, configurations, and systems.

## Key Information

- **Why not your daily computer:** "Would you leave your laptop open and let your assistant run wild on it 24 hours a day? Probably not."
- The agent has the power to do "anything a human could do with your machine" — delete files, change configurations, accidentally send files to the wrong place
- **Options for a clean machine:**
  - Old MacBook Air from a closet (fresh install)
  - Mac Mini (recommended: "they sure are cute stacked up on your computer")
  - Cloud VM
- Clean machine = fresh OS install, dedicated to the agent(s)
- The machine still needs its own local admin account, Gmail account, and Chrome install
- Mac Mini as "accountability cost": "You order it, it arrives, and then you're like 'Okay, I actually have to do this. I spent like 500 bucks on this thing.'"
- Multiple agents can share a machine if you're comfortable with them occasionally crossing boundaries
- Physically separate machines for agents that should never share context (e.g., work vs. family)

## Why It Matters

- Most important security practice for AI agents
- Prevents accidental damage to your important files and configurations
- Makes the "employee mental model" concrete: the agent has its own workspace, just like an employee has their own desk/computer
- Encourages actual adoption: "the safest and cleanest way to start"

## Related

- [[OpenClaw]] — the platform
- [[Progressive Trust with AI]] — the complementary trust practice
- [[Screen Sharing for Headless Machines]] — how to manage headless machines
- [[Apple]] — Mac Mini hardware
- [[summary-18 - From skeptic to true believer： How OpenClaw changed my life ｜ Claire Vo]] — source summary
