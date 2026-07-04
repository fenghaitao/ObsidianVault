---
title: "CLAUDE-md"
type: concept
tags: [claude-code, memory, configuration, markdown]
sources: [raw/03-transcripts/Claude/Claude Code 101/05 - The CLAUDE.md file.md, raw/01-articles/claude/2025-10-15 - How to scale agentic coding across your engineering organization.md]
last_updated: 2026-07-04
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

## Organizational Rollout Practice (October 2025)

When scaling [[AgenticCoding]] across an engineering organization, Anthropic recommends treating CLAUDE.md like living documentation:

- **Create project-level files** checked into the repository root so everyone inherits the same configuration automatically.
- **Update alongside architecture changes**: include CLAUDE.md updates in the same pull requests as the code changes that prompted them.
- **Include in onboarding**: make reviewing the project's CLAUDE.md part of new-hire onboarding.
- **Branch-specific variants**: for projects with significantly different patterns across branches, maintain branch-specific CLAUDE.md content.

## Related

- [[summary-05 - The CLAUDE.md file]] — source summary
- [[ClaudeCode]] — the tool that consumes CLAUDE.md
- [[ContextWindow]] — the memory constraint CLAUDE.md helps manage
- [[AgenticCoding]] — organizational rollout methodology recommending CLAUDE.md as shared documentation
- [[summary-2025-10-15 - How to scale agentic coding across your engineering organization]] — CLAUDE.md-as-documentation guidance
