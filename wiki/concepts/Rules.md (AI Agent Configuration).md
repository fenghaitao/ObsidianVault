---
title: "Rules.md (AI Agent Configuration)"
type: concept
tags: [AI, vibe-coding, configuration, methodology, documentation]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/27 - The rise of the professional vibe coder (a new AI-era job).md"]
last_updated: 2026-07-10
---

## Definition

Rules.md (also called agent.md in some tools) is a configuration file that tells an AI coding agent how to behave, what to read, and what to focus on. It eliminates the need to repeat instructions in every prompt by providing perpetual context.

## Key Information

- Different tools use different names: rules.md (Cursor, Claude Code), agent.md (Cloud Code), project knowledge (Lovable)
- Purpose: "You're letting the agent know how you want it to behave and what it should focus on in the long run so that you don't have to repeat yourself with every prompt."
- Typical content: "Read all the files before you do anything. Don't do anything before you read all the PRDs. Read tasks.md to see which task is next. Then execute on that next set of tasks. When you're done, tell me what you did and how I should test it."
- This is how Lazar manages 5-6 projects simultaneously: "My prompts have become 'proceed with the next task.' I don't need the context. I outsourced that and delegated that to the agent."
- Also used for recording learnings: when a bug is fixed, ask the agent how to prompt better next time, then put the answer into rules.md
- "Eliminate yourself completely out of the equation. I won't remember to prompt you better two days from now. Put this into rules."
- In Lovable, accessed via project settings → project knowledge

## Related

- [[summary-27 - The rise of the professional vibe coder (a new AI-era job)]] — source summary
- [[Lazar]] — originator of the workflow
- [[Context Window Management]] — the problem this solves
- [[PRD (Project Requirements Document)]] — the documentation read by rules
- [[4x4 Debugging Framework]] — where learnings for rules come from
