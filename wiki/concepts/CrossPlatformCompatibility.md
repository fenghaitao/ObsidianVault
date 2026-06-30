---
title: "CrossPlatformCompatibility"
type: concept
tags: [agents, skills, prompt-engineering, cursor]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor.md"]
last_updated: 2026-06-29
---

## Definition

Cross-Platform Compatibility in agent skills refers to the need for markdown-based instructions to include platform-specific guidance (Windows, Linux, macOS) so that agents can correctly execute commands regardless of the user's operating system.

## Key Information

- Cursor's work tree skill includes Windows-specific instructions alongside Linux and macOS instructions
- The skill must account for different shell syntax, file path conventions, and Git behavior across platforms
- This is one of the considerations when writing markdown-based agent instructions instead of platform-abstracted code
- The agent must correctly identify the platform and apply the appropriate instructions

## Related

- [[summary-20260430 - Replacing 12K LoC with a 200 LoC Skill — David Gomes, Cursor]] — source
- [[Skills]] — the mechanism that must be cross-platform
- [[MarkdownAsCode]] — the paradigm requiring platform awareness
- [[Cursor]] — the product
