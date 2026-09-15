---
title: "Open Source"
type: concept
tags: [engineering, open-source, tools, sharing]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260309 - OpenAI Codex Tech Lead： How His Career Grew And How He Uses Codex ｜ Michael Bolin.md", "raw/03-transcripts/Ryan L. Peterman/Channel Only/20260323 - The Co-Creator of Kubernetes： Engineering-Led Direction and Convincing Management ｜ Brendan Burns.md"]
last_updated: 2026-09-14
---

## Definition

Open Source refers to the practice of sharing a codebase publicly, which Michael Bolin describes as a mostly bottoms-up decision at big companies, motivated by reciprocity, recruiting, and — for agents in particular — trust and transparency.

## Key Information

- Bolin open-sourced Buck and Nuclide at Facebook and now works on the open-source Codex repo at OpenAI.
- Rationale: "these companies have benefited so much from open source" — if a tool isn't the secret sauce, share it; even if nobody uses it, it serves as a reference for how a thing could be done.
- Secondary benefits include recruiting and conference talks/blog posts that "pay dividends over time" with a longer shelf life than people realize.
- Buck's open-sourcing created ecosystem pressure on Google's Blaze/Bazel effort; companies like Uber and Airbnb adopted Buck, and Bolin feels they got unofficial credit from that camp.
- Open-sourcing big-ticket items (React, PyTorch) shows clear value back to the company, while the long tail of smaller projects is more subject to manager grumbling depending on the economy.
- For Codex specifically, open source matters because "you're going to put this thing on my machine" — users care what it does, and openness surfaces bug reports and contributions.

### Brendan Burns's Kubernetes Rationale
- Open ecosystems win the way Linux did — "if you make it an exclusive… the majority of people can't use your thing, they're just going to ignore you and build their own."
- For GCP (not the market leader), building Kubernetes for everyone — but making it great on GCP — was the only path to attract developers and become a thought leader.
- Most open-source contributions come from a small core (~80–90% core/paid contributors); legal fears about liability for contributed bugs keep non-tech companies from contributing, though Burns says those worries "don't hold water legally."
- Independence (donation to the Linux Foundation's CNCF plus democratic governance) was critical to becoming an industry standard.

## Related

- [[summary-20260323 - The Co-Creator of Kubernetes： Engineering-Led Direction and Convincing Management ｜ Brendan Burns]] — source summary
- [[Kubernetes]] — the success case
- [[Linux Foundation]] — the governance body
- [[Thought Leadership]] — the motive
- [[summary-20260309 - OpenAI Codex Tech Lead： How His Career Grew And How He Uses Codex ｜ Michael Bolin]] — source summary
- [[Michael Bolin]] — who open-sourced Buck, Nuclide, and Codex
- [[Buck]] — an open-sourced build system
- [[Codex]] — the open-sourced coding agent
- [[React]] — an unambiguous success story
- [[PyTorch]] — another success story
