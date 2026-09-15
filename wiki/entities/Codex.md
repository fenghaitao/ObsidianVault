---
title: "Codex"
type: entity
tags: [tool, AI, coding-agent, open-source]
sources: ["raw/03-transcripts/Ryan L. Peterman/Channel Only/20260309 - OpenAI Codex Tech Lead： How His Career Grew And How He Uses Codex ｜ Michael Bolin.md"]
last_updated: 2026-09-14
---

## Definition

Codex is OpenAI's coding-agent product (CLI, web/cloud, and VS Code extension) whose open-source repository Michael Bolin leads.

## Key Information

- Codex CLI launched in April 2025 as a "one more thing" at the end of the O3/O4-mini live stream, was open-sourced, and gathered ~10–20K GitHub stars in a week or two.
- The initial CLI launch was rushed; a month later a team of about seven engineers (plus researchers) launched Codex web/cloud, where users can run Codex in a container or kick off work from a phone.
- Growth inflected in August 2025 with GPT-5, a refreshed terminal UI, an open-weights model supported on the harness, and the VS Code extension.
- Bolin sees local agents as the stronger product-market fit today but argues the long-run majority of agent compute will run in the cloud (automation pipelines triggered by GitHub issues or Linear tasks can't live on a laptop).
- The harness (which Bolin works on) is written in Rust, including the sandboxing that keeps the model inside the bounds it sets.
- Codex is open source in part because "you're going to put this thing on my machine" — users should be able to inspect what it does.
- Usage grew ~5x since the start of 2025 and, per Ryan, over a million people use it now.

## Related

- [[summary-20260309 - OpenAI Codex Tech Lead： How His Career Grew And How He Uses Codex ｜ Michael Bolin]] — source summary
- [[Michael Bolin]] — tech lead of the open-source Codex repo
- [[OpenAI]] — the company that ships Codex
- [[VS Code]] — the extension surface bolin emphasized
- [[Open Source]] — the rationale for the CLI/repo being open
- [[Code Review Culture]] — how agents change review
