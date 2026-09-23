---
title: "Claude"
type: entity
tags: [AI, LLM, Anthropic, tool]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story).md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260511 - Harvard Professor： CS50, What Matters More Than Programming Now, Lecturing Well ｜ David J Malan.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling.md",
  "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260907 - How Anthropic Builds And How Engineering Will Change Soon ｜ Thariq Shihipar.md"]
last_updated: 2026-09-23
---

## Definition

Claude is an AI assistant developed by Anthropic. Evan King mentioned using Claude as a development tool at Hello Interview to accelerate coding.

## Key Information

- Evan King mentioned that Hello Interview (still only 2 full-time employees) leverages AI tools like Claude to accelerate development
- Evan noted that with "two highly capable engineers and Claude at your disposal, you can move pretty quick"
- He acknowledged there are "plenty of opinions about where Claude's useful, where it slows you down" but deferred that to a different conversation
- The use of LLMs like Claude allows small startups to accomplish what would have taken "many week cycles at even a Meta with a team of some number of engineers"
- David J. Malan: CS50's final project encourages/welcomes students to use Claude (or ChatGPT or Gemini), even though such tools are disallowed for regular assignments.
- Malan prototyped with Claude: it returned a solution that was ~90% correct, and he had to push back against a hallucinated API detail.
- James Cowling warns against deferring all thinking to Claude; struggle and uncertainty are where engineers grow, and "it's not very hard to use Claude" — the hard, human part remains architecture, simplicity, and design.

### Thariq Shihipar on Using Claude
- Treat Claude as a thought partner: start from "Can Claude do it? If not, why not?" and always ask whether you can move up an abstraction level — build the system that builds the system.
- Onboarding is now mostly technical-solved by Claude; the onboarding buddy remains for social and cultural reasons (how the team works, buy-in, friendship).
- Use Claude for knowledge work, not just shipping: accounting with Python instead of Excel, video editing with FFmpeg; most knowledge work is reducible to code.
- Model choice is not a durable skill: use the frontier model ("Fable" as transcribed) for planning, brainstorming, finding unknowns, and specs, and Opus 5 for implementation via workflows and a verification harness.
- Artifacts give Claude a second interface — interactive web apps that can call MCPs (e.g., read your inbox) or show coding plans, readable on a phone.
- Models default to the average user's fast response; give explicit permission to spend compute, use subagents/workflows, or "don't do work yet — brainstorm with me."
- Computer/browser use is improving (Opus 5) but hits UX edge cases (one-passwords, latency) and is a state machine where you don't control all state; APIs and MCPs absorb many use cases.

## Related

- [[summary-20250117 - 25 Year Old Staff Eng @ Meta (Promotion Story)]] — source summary
- [[Hello Interview]] — company using Claude
- [[Evan King]] — uses Claude for development
- [[summary-20260511 - Harvard Professor： CS50, What Matters More Than Programming Now, Lecturing Well ｜ David J Malan]] — source summary (Malan)
- [[David J. Malan]] — uses Claude for prototyping
- [[CS50]] — allows Claude for final projects
- [[summary-20260525 - Dropbox’s Former Most Senior Eng： Building Great Systems and Advice for the AI Era ｜ James Cowling]] — source summary
- [[Thariq Shihipar]] — thought-partner framing and model choice
- [[summary-20260907 - How Anthropic Builds And How Engineering Will Change Soon ｜ Thariq Shihipar]] — source summary
