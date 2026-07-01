---
title: "Tokens Per Successful Outcome"
type: concept
tags: [agents, metrics, efficiency, agent-interface, token-economics]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google.md"]
last_updated: 2026-06-30
---

## Definition
Tokens Per Successful Outcome is a fuel efficiency metric for agent interfaces that measures token consumption per completed task, not per outcome. It combines effectiveness (did the agent complete the user journey?) with efficiency (token cost, tool calls, duration) to provide a meaningful measure of agent interface quality.

## Key Information
- Introduced by Michael Hablich as the key metric for measuring Chrome DevTools MCP interface quality
- Formula: tokens consumed / successful task completions — not tokens per any outcome
- "Fuel efficiency is relatively worthless if you can't reach your destination" — hence "per successful outcome" not "per outcome"
- Cannot be measured globally — dramatically different between user journeys and task classes (e.g., web scraping is cheap, debugging responsive layout is expensive)
- Compared within the same user journey/task class, not across different ones
- Even imperfect measurement is better than gut-driven decisions — enables data-informed choices
- Used to identify which tools/use cases need improvement: shorter bars (less effective) are the ones to focus on
- Chrome DevTools addresses token burn from three angles: tool categorization, Slim Mode, CLI interface
- Related to [[TokenBudget]] but focuses on outcome efficiency rather than raw budget constraints

## Related
- [[summary-20260605 - Building Agent Interfaces： Lessons from Chrome DevTools (MCP) for Agents — Michael Hablich, Google]] — source
- [[Agent Experience]] — broader framework this metric fits into
- [[TokenBudget]] — related constraint
- [[Slim Mode]] — strategy for reducing tokens per outcome
- [[CLI For Agents]] — strategy for reducing tokens per outcome
- [[Agent Efficiency]] — parent category
