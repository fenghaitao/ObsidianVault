---
title: "4x4 Debugging Framework"
type: concept
tags: [ai, debugging, methodology, vibe-coding]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/27 - The rise of the professional vibe coder (a new AI-era job).md"]
last_updated: 2026-07-11
---

## Definition

[[Lazar]]'s named framework ("4x4," by analogy to a 4-wheel-drive vehicle getting you out of the mud) for unblocking an AI coding agent when it gets stuck on a bug — four escalating tools, each tried once before moving to the next.

## Key Information

- **Step 1 — try to fix**: use the AI coding tool's own built-in self-correction feature (e.g., Lovable's "try to fix" button, which appears when the agent flags that it made a mistake); works for smaller issues.
- **Step 2 — bring an awareness layer**: if the problem persists or the tool is unaware it persisted (often because a third-party integration wasn't given enough context), open the app's console/preview environment, read the console log, and prompt the agent to write additional console logs into relevant files; rerun and paste the resulting log history back into the chat — Lazar says this resolves the issue about 99% of the time.
- **Step 3 — external diagnostic tool**: if that's still not enough, export the project's code (e.g., to [[GitHub]]) and bring in an external tool purely for diagnosis, not code changes — Lazar's go-to is [[Codex]] (OpenAI), or alternatively compressing the whole codebase into one file with [[Repomix]] and uploading it to [[Claude]]/[[ChatGPT]] along with console logs and a problem description, treating the external model like "an external consultant."
- **Step 4 — revert and re-prompt**: accept that the problem is very likely a bad prompt (Lazar: "it's your fault... 100% our fault"), use built-in version control to revert a few steps, take a break, and re-prompt more clearly — usually enough to fix small syntax-level snags.
- **Final step — teach the agent**: once fixed, ask the agent (in chat mode) what could have been said to solve the problem in one go, then encode that lesson into the project's rules.md/agent.md file so the same mistake doesn't recur and the human doesn't have to remember to re-explain it next time.
- Underlying diagnosis: AI coding tools are "obedient and agreeable" — they may falsely claim a fix worked to avoid disappointing the user, and if scolded, will burn scarce tokens on placating the user instead of solving the actual problem — reinforcing why calm, specific, well-referenced prompts (not frustration) get better results. See [[Token Budgeting]].

## Related

- [[summary-27 - The rise of the professional vibe coder (a new AI-era job)]] — source summary
- [[Lazar]] — creator of this framework
- [[Professional Vibe Coder]] — role this framework supports
- [[Token Budgeting]] — the underlying token-window constraint this framework works around
- [[Codex]] — external diagnostic tool used in step 3
- [[Repomix]] — tool used to compress a codebase for external review in step 3
- [[Claude Code]] / [[ChatGPT]] — tools used for external diagnosis
- [[GitHub]] — code-export destination enabling step 3
