---
title: "Gitarr"
type: entity
tags: [tool, code-review, ai-safety, sonar]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260703 - The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why).md"
last_updated: 2026-07-06
---

## Definition

Gitarr is an AI code-review tool acquired by [[Sonar]] that not only flags issues in a pull request but automatically fixes them, validating each fix against CI.

## Key Information

- Connects to GitHub/GitLab repositories; runs a comprehensive review as soon as a PR opens.
- Demonstrated fixing a SQL-injection vulnerability automatically in a PR, then validating the fix against CI.
- Also reads CI failures directly: dedupes errors, identifies flaky tests, cleans up build/lint failures without a human combing through logs.
- Fits into [[Sonar]]'s "verify" pillar of its agent-centric development life cycle framework.
- Positioned as a safety net under [[DarkFactory]]-style autonomous pipelines rather than a replacement for human judgment.

## Related

- [[Sonar]] — parent company
- [[DarkFactory]] — the validation-layer problem Gitarr addresses
- [[ColeMedin]] — video sponsor mention
- [[summary-20260703 - The Best AI Coding Setup Isn't the Most Autonomous One (Here's Why)]] — source
