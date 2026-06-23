---
title: "summary-creating-a-subagent"
type: source
tags: [source, claude-code, subagents, tutorial, transcript]
sources: [raw/03-transcripts/Claude/Claude Code subagents/04 - Creating a subagent.md]
last_updated: 2026-06-23
---

## Core Summary

Custom sub-agents are markdown files with YAML frontmatter containing configuration that helps Claude understand when to use them and provides directions to the sub-agent itself. The easiest creation method is the `/agents` command, which opens a management panel. Claude can auto-generate the name, description, and system prompt from a natural-language description. Key configuration fields: name (unique identifier), description (single line, controls delegation), tools (restricted access list), model (Sonnet/Opus/Haiku/inherit), and the system prompt body.

## Key Points

- **Creation:** use `/agents` command -> "create new agent" -> choose project or personal scope -> describe what you want -> Claude auto-generates config.
- **Configuration fields:**
  - `name`: unique identifier; reference via `@agentName` or by asking Claude directly.
  - `description`: single line; controls when Claude decides to use the sub-agent. Add "proactively" for more automatic use. Include example conversations.
  - `tools`: list of allowed tools; match to the sub-agent's purpose.
  - `model`: Haiku (fast), Opus (complex analysis), Sonnet (balanced), or inherit (same as main conversation).
  - **Body:** system prompt guiding how the sub-agent completes tasks and returns information.
- **Testing:** make code changes and ask Claude to review. If the sub-agent isn't used when expected, add more specific examples to the description.
- **Scope:** project sub-agents (shared via repo) or personal (across all projects).

## Related

- [[summary-03 - What are subagents]] — what sub-agents are
- [[summary-02 - Designing effective subagents]] — design patterns
- [[ClaudeCode]] — the tool sub-agents extend
