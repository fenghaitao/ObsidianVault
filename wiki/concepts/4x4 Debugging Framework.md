---
title: "4x4 Debugging Framework"
type: concept
tags: [AI, debugging, vibe-coding, methodology, troubleshooting]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/27 - The rise of the professional vibe coder (a new AI-era job).md"]
last_updated: 2026-07-10
---

## Definition

The 4x4 Debugging Framework is Lazar's four-step method for getting unstuck when AI-generated code has bugs. Like a 4x4 vehicle gets you out of the mud, this framework gets you out of debugging problems. Each step is attempted only once before moving to the next.

## Key Information

- **Step 1: Use the tool's built-in fix.** Most AI tools label mistakes and offer a "try to fix" button. Works for smaller issues.
- **Step 2: Add console logs for awareness.** If the tool is unaware of the problem, prompt it to add console logs in relevant files. Run the function, copy the full console history, paste it back. "99% of the time that's enough."
- **Step 3: Use an external tool as consultant.** Export to GitHub, import into Codex (or use RepoMix to compress codebase and upload to Claude/ChatGPT). Use external AI only for diagnostics, not code changes.
- **Step 4: Revert and re-prompt.** Most problems are user error. Take a few steps back, think about the prompt, take a walk, come back with a clear mind. "AI is just writing code very fast and sometimes it stumbles on a very small rock."
- **Final meta-step:** After fixing, ask the agent: "How can you help me learn how to prompt you better so that next time we do it in one go?" Put the answer into rules.md.
- Core insight: "These tools are so good at doing things the right way if they are used the right way. It's always our fault."
- AI tools are obedient and agreeable — they'll lie and say they fixed the problem when they didn't if they lack context
- Common mistake: trusting the tool fixed it, getting mad when it didn't, causing the AI to spend tokens apologizing instead of debugging

## Related

- [[summary-27 - The rise of the professional vibe coder (a new AI-era job)]] — source summary
- [[Lazar]] — originator
- [[Context Window Management]] — the underlying problem
- [[Agent Output Reading]] — related practice
- [[Codex]] — tool used in step 3
- [[RepoMix]] — alternative tool for step 3
