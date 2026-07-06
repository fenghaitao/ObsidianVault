---
title: "summary-2026-02-20 - Bringing automated preview, review, and merge to Claude Code on desktop"
type: source
tags: [source, claude-code, desktop, ci-cd, github]
sources: ["raw/01-articles/claude/2026-02-20 - Bringing automated preview, review, and merge to Claude Code on desktop.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic closed the development loop in Claude Code on desktop: live app preview inside the desktop interface, an automated code-review pass over local diffs, and PR monitoring with optional auto-fix/auto-merge on GitHub — plus seamless session handoff between desktop, CLI, web, and mobile.

## Key Points

- **Live preview**: Claude Code on desktop can start dev servers and preview the running app in-app — viewing the UI, reading console logs, and catching errors without the user switching to a browser to describe what they're seeing; users can select visual elements in the preview and pass feedback directly to Claude.
- **"Review code" button**: Claude examines local diffs and leaves inline comments in the desktop diff view (bugs, suggestions, potential issues) before anything leaves the machine; users can ask Claude to address the comments directly.
- **PR monitoring**: for GitHub-hosted code, Claude Code tracks PR status (CI check passes/failures) via the GitHub CLI; **auto-fix** attempts to resolve CI failures automatically, and **auto-merge** merges once all checks pass — running in the background while the user moves to a new task.
- **Session portability**: `/desktop` brings a CLI session's full context into the desktop app; "Continue with Claude Code on the web" moves a local desktop session to the cloud, pickable up from web or the mobile app.
- Available now to all users via an update/download of Claude Code on desktop.

## Related

- [[ClaudeCode]] — the product these desktop updates extend
- [[GitHub]] — platform PR monitoring and auto-merge integrate with
