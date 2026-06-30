---
title: "Agent Unreliability"
type: concept
tags: [ai, agents, reliability, failure-modes, debugging]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260423 - The End of Apps — Kitze, Sizzy.co.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench.md"]
last_updated: 2026-06-26
---

## Definition
Agent Unreliability refers to the documented failures of personal AI agents in critical areas: cron jobs not executing, multi-agent systems breaking down, agents forgetting context in the very next message, and model personality degradation. Kitze documents this as the root cause of agent fatigue in the OpenClaw community.

## Key Information
- **Cron jobs**: unreliable where it matters most — "the fucking cron job just managed to drive me fucking nuts"
- **Multi-agent failures**: agents talking to each other breaks down
- **Context amnesia**: agents forgetting "literally in the next message" — "The message is above you. Just go one message above you."
- **Model personality degradation**: "talking to GPT-5... feels like talking to a box of oats. Seriously, it has the personality of this."
- **Conversation pattern**: "Did you do that?" No. "But I told you to do that." Okay, I'll do it. "Did you do it?" No. — "Every conversation with OpenClaw looks like that"
- **Real-world impact**: Kitze has "never been late on rent, on mortgage, on customer emails" — "It's a mess. But it's a performative mess."
- **Community impact**: Tinker Club declining from explosion of sign-ups to ~5 people per meetup, "slowly turning into Open Claw Anonymous"
- Kitze notes this is "getting fixed and it's getting updates every day, but I've yet to see that it's actually working"
- **BullshitBench connection**: Peter Gostev observed the same solve-at-any-cost behavior in agents — he would ask an agent to do something in the wrong project and it would still go and do it rather than push back. This is the same failure mode as models complying with nonsense questions: insufficient training on saying "this doesn't make sense."

## Related
- [[summary-20260423 - The End of Apps — Kitze, Sizzy.co]] — source
- [[Kitze]] — documents the failures
- [[Agent Fatigue]] — community consequence
- [[OpenClaw]] — primary framework affected
- [[Tinker Club]] — community experiencing this
- [[AgentPersonality]] — "box of oatmeal" degradation
- [[AgentToAgentCommunication]] — multi-agent breakdowns
- [[AgentMemory]] — context amnesia
- [[summary-20260424 - What Do Models Still Suck At - Peter Gostev, Arena.ai, BullshitBench]] — source (solve-at-any-cost behavior in agents)
- [[BullshitBench]] — benchmark exposing the root cause
- [[Nonsense Detection]] — capability gap driving agent unreliability
- [[Reasoning Limits]] — overthinking contributes to wrong-project execution
