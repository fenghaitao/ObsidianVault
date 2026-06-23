---
title: "summary-troubleshooting-skills"
type: source
tags: [source, claude-code, skills, troubleshooting, transcript]
sources: [raw/03-transcripts/Claude/Claude Code Skills/02 - Troubleshooting skills.md]
last_updated: 2026-06-23
---

## Core Summary

When Claude Code skills don't work, the problem typically falls into one of four categories: not triggering, not loading, conflicts with other skills, or runtime failures. Most fixes are straightforward. Use the agent skills verifier tool for structural validation. Trigger issues are almost always due to insufficient semantic overlap between the skill description and user phrasing. Loading issues stem from wrong file location or naming. Conflicts arise from overly similar descriptions or enterprise skills shadowing personal ones.

## Key Points

- **Not triggering:** improve the description with trigger phrases users would actually say; test with variations. Claude uses semantic matching, so the request must overlap with the description's meaning.
- **Not loading:** skills must be in the right location with the right structure (`skill.md` inside a named directory, not at skills root; filename must be exactly `skill.md`). Run `claude-debug` to see loading errors.
- **Wrong skill used:** descriptions are too similar; make them more distinct and specific.
- **Shadowed:** enterprise or higher-priority skills with the same name override personal ones; rename the personal skill to be more distinct.
- **Plugins missing:** clear cache, restart Claude Code, reinstall. Use the validator tool to check plugin structure.
- **Runtime failure:** ensure external packages are installed, scripts have execute permissions, and use forward slashes in paths everywhere (including Windows).

## Related

- [[ClaudeCodeSkills]] — the skills system being troubleshot
- [[summary-01 - What are skills]] — introduction to skills
- [[ClaudeCode]] — the tool skills run in
