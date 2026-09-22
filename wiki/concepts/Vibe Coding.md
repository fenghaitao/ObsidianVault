---
title: "Vibe Coding"
type: concept
tags: [AI, agents, software-engineering, coding]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh.md"]
last_updated: 2026-09-22
---
## Definition
Vibe coding is Andrej Karpathy's term (transcript garbles it as "Andre Carpathy") for writing software by prompting AI and not looking at the code at all — one extreme of the modern spectrum of how software gets built.

## Key Information
- Charlie describes a widening spectrum of software-construction styles, from true vibe coding ("don't look at the code at all") to not using LLMs, with "a lot of different stuff in between."
- He applies different standards per project: a personal/internal Rust linter was shipped fully agent-generated and unread, whereas uv (relied on by millions) gets much more care and verification.
- Warns about the "gray area" of partially AI-generated code that is acceptable but below the bar an engineer would previously have held.
- Risk-based verification maps onto the old "risk of the change" trade-off: internal, low-risk changes can be stamped unread, while critical customer-facing changes need multiple reviewers.

## Related
- [[AI and Software Engineering]] — how agents reshape the craft
- [[Charlie Marsh]] — describes the spectrum
- [[summary-20260622 - Creator of uv, ty, Ruff： How Software Engineering Is Changing ｜ Charlie Marsh]] — source summary
