---
title: "CLAUDE-md"
type: concept
tags: [claude-code, memory, configuration, markdown]
sources: [raw/03-transcripts/Claude/Claude Code 101/05 - The CLAUDE.md file.md]
last_updated: 2026-06-23
---

## Definition

CLAUDE.md is a markdown configuration file that provides Claude Code with persistent project memory. Placed at the project root, its contents are automatically appended to every prompt, giving Claude ongoing context about the tech stack, conventions, commands, and preferences.

## Key Information

- Generated via the `/init` command, which analyzes the codebase and creates an initial version.
- Typical contents: tech stack, dev/build/test commands, code style (indentation, exports), architectural conventions (where routes go, preferred patterns).
- **Hierarchy:** project-level CLAUDE.md (root, shared via version control), user-level CLAUDE.md (personal config directory, applies across all projects), and session memory (saved on request when correcting Claude).
- **Best practice:** start without one, observe where Claude needs correction, then add only those items. Keep it compact.
- **Sharing:** project-level CLAUDE.md is intended for version control so the whole team benefits.
- References to project docs can be included using the `@` symbol with file paths.

## Related

- [[summary-05 - The CLAUDE.md file]] — source summary
- [[ClaudeCode]] — the tool that consumes CLAUDE.md
- [[ContextWindow]] — the memory constraint CLAUDE.md helps manage
