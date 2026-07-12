---
title: "Genie Metaphor (AI Prompting)"
type: concept
tags: [AI, prompting, mental-model, metaphor]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/27 - The rise of the professional vibe coder (a new AI-era job).md"]
last_updated: 2026-07-10
---

## Definition

The Genie/Aladdin Metaphor is Lazar's mental model for understanding AI limitations. Like the genie that grants only three wishes, AI has a limited token context window. Vague wishes ("I want to be taller") produce dysfunctional results (13 feet tall). Specificity is required.

## Key Information

- Two layers of the metaphor:
  1. **Three wishes = token limit.** AI can only process so many requests within a single context window. "Not 3,000 wishes, not three million, just three at a time."
  2. **Vague wish = wrong result.** "I want to be taller" → 13 feet tall, can't fit in car or house. AI doesn't know "what you mean" — it takes requests literally.
- Token allocation breakdown: some tokens for reading, some for browsing the web, some for thinking, some for executing code
- You can't control the token limit (machine limitation), but you can 100% control the specificity of your request (human limitation)
- AI tools are obedient and agreeable — they'll try to make you happy rather than tell you your request was unclear
- When AI lacks context, it spends tokens on reading and apologizing instead of problem-solving
- Practical implication: use PRDs, rules files, and documentation to give the AI context without consuming prompt tokens

## Related

- [[summary-27 - The rise of the professional vibe coder (a new AI-era job)]] — source summary
- [[Lazar]] — originator
- [[Clarity in AI Prompting]] — the skill the metaphor teaches
- [[Context Window Management]] — the technical problem
- [[4x4 Debugging Framework]] — what to do when the genie gets it wrong
