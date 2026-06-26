---
title: "UnifiedDiffing"
type: concept
tags: [coding-agents, diff, editing, efficiency]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer.md"]
last_updated: 2026-06-25
---

## Definition
Unified diffing is the technique of using diffs (unified diff format) instead of rewriting entire files when coding agents edit code. It is faster, uses less context, and is less prone to mistakes — analogous to crossing out text on paper rather than rewriting the entire document.

## Key Information
- Claude Code's Edit tool uses diffs rather than rewriting files most of the time
- Way faster than full file rewrites
- Uses significantly less context (token savings)
- Way fewer issues compared to full rewrites
- Analogy: if asked to review slides and make revisions, crossing out specific parts is much easier than rewriting all slides from scratch
- Diff is a "natural thing to prevent mistakes"
- Some coding agents built their own slight variations on unified diff (e.g., not always needing line numbers)
- Standard unified diff format works well enough
- Highly recommended for any agent being built

## Related
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — source
- [[ClaudeCode]] — primary example using unified diffs
- [[Context Management]] — diffing helps by reducing token usage
