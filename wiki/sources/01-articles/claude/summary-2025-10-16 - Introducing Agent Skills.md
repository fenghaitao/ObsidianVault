---
title: "summary-2025-10-16 - Introducing Agent Skills"
type: source
tags: [source, original-material, agent-skills, claude-code, api, skills]
sources: ["raw/01-articles/claude/2025-10-16 - Introducing Agent Skills.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic formalized **Agent Skills** as a platform-wide capability: folders of instructions, scripts, and resources that Claude loads only when relevant to the task at hand, now usable consistently across Claude apps, Claude Code, and the Anthropic API. Skills are composable, portable (same format everywhere), efficient (load only what's needed), and can include executable code. On the API, Skills require the Code Execution Tool beta and are managed via the new `/v1/skills` endpoint. A December 18, 2025 update to the same announcement added organization-wide skill management, a directory of partner-built skills, and published Agent Skills as an open standard for cross-platform portability.

## Key Points

- **Definition**: Skills are folders (instructions + scripts + resources) Claude scans and loads only when relevant, keeping Claude fast while giving it access to specialized expertise (e.g., Excel work, brand guidelines).
- **Properties**: composable (skills stack and Claude coordinates their use), portable (same format across Claude apps, Claude Code, API), efficient (loads only what's needed), powerful (can include executable code for tasks better solved by traditional programming than token generation).
- **Claude apps**: available to Pro, Max, Team, and Enterprise users; Claude auto-invokes relevant skills (visible in its chain of thought); the "skill-creator" skill interactively builds new skills (asks about your workflow, generates folder structure, formats SKILL.md, bundles resources) with no manual file editing required. Team/Enterprise admins must enable Skills org-wide first.
- **Claude Developer Platform (API)**: Skills can be added to Messages API requests; the new `/v1/skills` endpoint gives programmatic control over custom skill versioning and management. Requires the **Code Execution Tool** beta for the secure environment Skills run in. Anthropic-created skills let Claude read/generate Excel, PowerPoint, Word, and fillable PDFs; developers can create custom skills and manage versions through the Claude Console.
- **Claude Code**: Skills extend Claude Code with a team's expertise and workflows; installable via plugins from the `anthropics/skills` marketplace, or manually by adding to `~/.claude/skills`; shareable through version control. The [[ClaudeAgentSDK]] provides the same Agent Skills support for building custom agents.
- **Security note**: Skills give Claude access to execute code — use only trusted sources.
- **December 18, 2025 update**: added organization-wide skill management, a directory featuring partner-built skills, and published Agent Skills as an open standard for cross-platform portability.

## Related

- [[ClaudeCodeSkills]] — the Claude Code-specific skills system this article generalizes to a platform-wide standard
- [[CodeExecutionTool]] — required API beta for running Skills
- [[ClaudeAgentSDK]] — provides the same Agent Skills support for custom agents
- [[ClaudeCode]] — one of three surfaces (apps, Code, API) supporting Skills
