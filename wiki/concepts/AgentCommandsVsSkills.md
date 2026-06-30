---
title: "AgentCommandsVsSkills"
type: concept
tags: [agents, cursor, prompt-engineering, product-design]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor.md"]
last_updated: 2026-06-29
---

## Definition

Agent Commands vs Skills is a distinction in Cursor's architecture: commands are server-controlled prompts that load into context only when the user chooses to invoke them (via slash commands), while skills are locally-defined markdown instructions. Commands allow Cursor to iterate prompts on the backend without requiring users to update their client.

## Key Information

- In Cursor, /worktree and /bestofn are implemented as commands, not skills
- Commands work extremely similarly to skills: prompts only get loaded into context if the user chooses to load them
- The key difference: command prompts are controlled on Cursor's servers/backend, enabling iteration without client updates
- This means David Gomes can improve the work tree prompts and users get the latest version on next use
- The distinction is primarily about deployment and iteration speed, not functional capability

## Related

- [[summary-20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor]] — source
- [[Skills]] — the locally-defined equivalent
- [[Cursor]] — the product
- [[FeatureDiscoverability]] — affected by the command vs UI trade-off
