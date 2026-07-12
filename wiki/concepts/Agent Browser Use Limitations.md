---
title: "Agent Browser Use Limitations"
type: concept
tags: [AI, agent, browser, web, limitation]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/18 - From skeptic to true believer： How OpenClaw changed my life ｜ Claire Vo.md"]
last_updated: 2026-07-11
---

## Definition

Agent browser use is the capability for AI agents to navigate websites through a browser. It is currently unreliable across all AI products (not just OpenClaw) because the web has been hardened against bots, with anti-bot mechanisms, CAPTCHAs, and site architectures that are actively hostile to automated agents.

## Key Information

- Browser use is a universal problem, not specific to OpenClaw: "I don't think anybody has really unlocked browser use"
- The web is "hostile to agents" — anti-bot mechanisms, bot-identifying systems, and punishments for detected bot activity
- "The number one user of websites in a couple years are going to be people's agents" — the web will need to adapt
- OpenClaw implementation: each agent gets a dedicated Chrome profile with a color (pink for Polly, green for Sage)
- Inconsistency: some sites work (YouTube Studio for comments), others don't (Buffer for social media posting)
- Claire Vo's workaround hierarchy:
  1. **API first:** Does the service have an API key? Use that instead of the browser
  2. **Browser attempt:** Try the browser if no API exists
  3. **Walk away:** If the browser doesn't work, find another way to solve the underlying problem
- Alternative: web search APIs (Brave, Exa, Perplexity) for search-based tasks
- Browser disconnects from Chrome frequently — an ongoing fix area

## Why It Matters

- Browser use is often the first thing users try and the first thing that fails, leading to frustration
- Understanding the limitations helps set realistic expectations
- The "problem behind the problem" approach is more productive: "If it can't order DoorDash, maybe it can meal plan for you and remind you of lunches you like at 10:30"

## Related

- [[OpenClaw]] — the platform
- [[Web Search APIs for Agents]] — alternative approach
- [[Exa]] — web search API
- [[Brave (search API)]] — web search API
- [[Perplexity]] — web search API
- [[summary-18 - From skeptic to true believer： How OpenClaw changed my life ｜ Claire Vo]] — source summary
