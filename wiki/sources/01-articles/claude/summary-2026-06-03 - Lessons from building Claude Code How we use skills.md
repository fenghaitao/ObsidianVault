---
title: "summary-2026-06-03 - Lessons from building Claude Code How we use skills"
type: source
tags: [source, claude-blog, claude-code, skills]
sources: ["raw/01-articles/claude/2026-06-03 - Lessons from building Claude Code How we use skills.md"]
last_updated: 2026-07-07
---

## Core Summary

Based on Anthropic's internal experience with hundreds of skills in active use, this article distills nine categories of effective skills and provides practical best practices for writing them. Skills are folders of instructions, scripts, and resources that agents discover and use — not just markdown files. The best skills fit cleanly into one category; those trying to do too much straddle several and confuse the agent. Key best practices include progressive disclosure via folder structure, focusing on gotchas, giving Claude code (not just instructions), using session-only hooks, and treating the skill description as a trigger signal rather than a summary. The article also covers sharing patterns (repo-checked-in vs. plugin marketplace) and usage analytics via PreToolUse hooks.

## Key Points

- Skills are folders containing instructions, scripts, assets, and data — not merely markdown files. The file system enables progressive disclosure and context engineering.
- Nine skill categories emerged from cataloging Anthropic's internal skills: Library/CLI, Verification, Data & Monitoring, Workflow Automation, Scaffolding/Boilerplate, Code Review, Deployment/CI, Debugging/Triage, and Operations/Maintenance.
- Verification skills have the most measurable impact on output quality internally — worth dedicating an engineer for a week to make them excellent.
- The highest-signal content in any skill is the Gotchas section — accumulated from common failure points Claude encounters.
- Progressive disclosure: tell Claude what files are in the skill folder and it reads them at appropriate times. Split detailed reference material into separate files (e.g., `references/api.md`, `assets/template.md`).
- Give Claude flexibility: provide necessary information but let it adapt to the situation rather than being overly prescriptive.
- The skill description is not a summary — it's a description of *when to trigger this skill*. Claude scans all available skill descriptions to decide "is there a skill for this request?"
- Skills can include memory by storing data in log files, JSON, or SQLite databases (use `${CLAUDE_PLUGIN_DATA}` for persistent storage).
- Give Claude code (scripts, libraries) so it spends turns on composition rather than reconstructing boilerplate.
- Session-only hooks: skills can include hooks activated only when the skill is called and lasting only for the session duration (e.g., `/careful` blocking destructive operations).
- Sharing patterns: for small teams, check skills into repos (`.claude/skills`); for scale, use an internal plugin marketplace with organic traction-based promotion.
- Usage analytics: a PreToolUse hook can log skill usage to identify popular skills and undertriggering.
- The best skills began as a few lines and a single gotcha, then improved iteratively as people added to them when Claude hit new edge cases.

## Related

- [[ClaudeCodeSkills]] — the comprehensive skills concept page
- [[ClaudeCode]] — the tool skills extend
- [[ThariqShihipar]] — author of this article
- [[ClaudeCodeHooks]] — hooks system, including skill-scoped session hooks
- [[ContextEngineering]] — progressive disclosure as context engineering
- [[ClaudeCodePlugins]] — plugin marketplace for skill distribution
