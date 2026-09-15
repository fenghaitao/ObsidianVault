---
title: "Michael Bolin"
type: entity
tags: [person, engineer, distinguished-engineer, dev-tools]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260309 - OpenAI Codex Tech Lead： How His Career Grew And How He Uses Codex ｜ Michael Bolin.md"]
last_updated: 2026-09-14
---

## Definition

Michael Bolin is a software engineer who is tech lead for the open-source Codex repository at OpenAI. He previously was a Distinguished Engineer at Meta (formerly Facebook), where he built Buck, Nuclide, and the Eden/Miles virtual file system projects.

## Key Information

- His master's thesis project was Chickenfoot, a Firefox extension for end-user programming of the web (functions like "enter" and "click" with accessibility tags/alt text) that he sees as a early ancestor of today's coding agents.
- Early career at Google: he worked on Google Calendar and Google Tasks and wrote "the book on Closure" (the JavaScript tool suite), but concluded he was working on things that mattered to him more than to Google.
- At Facebook, he built Buck, a much faster Android build system, because he knew the inherited contractor code's build was not fundamentally that slow; he credited knowing a better system existed at Google as the "existence proof."
- Buck won adoption despite early skepticism and being beyond the norm partly by being scoped as "an Android build system" rather than a company-wide takeover, and by borrowed credibility from senior engineer John Perlow.
- Championed Nuclide, the desktop React-based IDE replacement for Xcode, over a competing web-based GWT project; leadership sided with him partly on the technology argument and partly on his Buck credibility.
- At Meta he rose to E8 (principal) and worked on web speed after promotion, where he admitted the "hero quest" of single-handedly fixing a Gordian knot of a stale problem did not play to his strengths.
- The virtual file system Eden, and the fuzzy file-search index Miles (with Hanson Wong), were his force-multiplier projects; Miles served fuzzy camelCase search over a million files in ~10–20 ms and spread widely as an internal thrift service.
- Learned influence the hard way: pushing too hard about Nuclide's foundation after Microsoft's GitHub acquisition (VS Code, atom) got his promotion delayed and led to coaching on recognizing personal triggers.
- Now leads Codex at OpenAI and is a heavy user of his own tool: roughly 80–90% of his code is model-generated, while he hand-writes safety-critical sandboxing code in Rust.
- His advice to younger engineers: be open to learning more things sooner and don't cling to your first language or tool — he went too deep on JavaScript before ever writing C.

## Related

- [[summary-20260309 - OpenAI Codex Tech Lead： How His Career Grew And How He Uses Codex ｜ Michael Bolin]] — source summary
- [[OpenAI]] — where he leads Codex
- [[Codex]] — his current product
- [[Google]] — Calendar, Tasks, Closure
- [[Facebook]] — where he built the dev tools
- [[Buck]] — the build system he built
- [[Nuclide]] — the IDE he championed
- [[Eden]] — the virtual file system
- [[Miles]] — the fuzzy file-search index
- [[Monorepo]] — the scaling problem his VFS targeted
- [[VS Code]] — the incumbent that ultimately won over Nuclide
- [[Open Source]] — his bottom-up rationale for sharing tools
