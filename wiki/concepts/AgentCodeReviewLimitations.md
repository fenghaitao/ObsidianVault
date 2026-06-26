---
title: "AgentCodeReviewLimitations"
type: concept
tags: [agents, code-review, quality, ouroboros]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260416 - Building pi in a World of Slop — Mario Zechner.md"]
last_updated: 2026-06-26
---

## Definition
Agent code review limitations refer to the "ouroboros" problem: using AI agents to review code written by AI agents creates a self-referential loop that doesn't reliably catch errors. Mario Zechner argues that review agents catch some issues but fundamentally cannot replace human code review for critical code.

## Key Information
- Mario Zechner: "Then you say, 'Oh, I have a review agent.' Let me introduce you to the wonderful world of the ouroboros. Doesn't work. It catches some issues."
- The problem is compounded by the fact that agents learn complexity from internet garbage
- Agent-written tests reviewed by agents create a closed loop with no ground truth
- "You cannot trust your code base anymore and also not your tests because your agent wrote your tests. So, good game."
- Mario's prescription: critical code must be read line by line by humans; non-critical code can have more relaxed review
- "If you do anything important, write it by hand. You can use a clanker to help you with that, but don't let it make the decisions for you."

## Related
- [[summary-20260416 - Building pi in a World of Slop — Mario Zechner]] — source transcript
- [[CompoundingBooboos]] — the errors that review agents miss
- [[SlowingDownWithAgents]] — the prescription for dealing with this
- [[GoodAgentTasks]] — tasks where agents are appropriate
- [[MarioZechner]] — originator
- [[Verification in Agentic Loops]] — related concept
