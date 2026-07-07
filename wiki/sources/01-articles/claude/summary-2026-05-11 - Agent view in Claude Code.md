---
title: summary-2026-05-11 - Agent view in Claude Code
type: source
tags:
  - source
  - original-material
sources:
  - raw/01-articles/claude/2026-05-11 - Agent view in Claude Code.md
last_updated: 2026-07-04
---

## Core Summary

Anthropic introduced **agent view**, a research-preview feature in Claude Code's terminal/CLI that gives a single list-style interface for managing many concurrent Claude Code sessions at once, replacing the older workaround of juggling multiple terminal tabs or a tmux grid. Opened by pressing the left arrow from any session or running `claude agents`, agent view shows each session as a row with its status (needs input / working / done), the content of its last response, and the time of last interaction. Selecting a row lets a user "peek" at the last turn and reply inline without fully attaching, or press enter to attach to the full transcript. Any existing foreground session can be pushed into agent view via `/bg`, or a brand-new backgrounded session can be launched directly with `claude --bg [task]`. The announcement frames this as the CLI-side counterpart to the parallel-agent orchestration Claude Code's desktop app already offers, aimed at developers scaling up the number of concurrent Claude Code sessions they run.

## Key Points

- **Entry points:** press left-arrow from any session, or run `claude agents` from the terminal.
- **Row contents:** session identity, whether it needs input, last response content, time since last interaction.
- **Peek and reply:** select a session to preview its last turn and answer inline if it's waiting on a decision, without leaving agent view; press enter to attach directly for the full transcript.
- **Backgrounding:** `/bg` moves an existing/foreground session into agent view; `claude --bg [task]` launches a brand-new session directly in the background.
- **Observed usage patterns from early users:**
  - Scaling concurrent sessions — dispatching several ideas at once (optionally paired with a Skill) and returning to a list of PRs ready for review.
  - Managing long-running agents — PR babysitters, dashboard updaters, and other looping jobs show their next run time directly in the list (connects to [[ClaudeCodeRoutines]]).
  - Navigating between sessions — arrow left to start a related task or quick codebase question, then arrow right back; peek shows the answer when it lands.
  - Seeing what shipped — status indicators plus the peek title make it easy to scan which sessions produced a PR.
- **Availability:** Research Preview, available today on Pro, Max, Team, Enterprise, and Claude API plans; opt-in via `claude agents`; usual rate limits apply. Docs at `code.claude.com/docs/en/agent-view`.
- **Published:** 2026-05-11 (last modified 2026-06-21), Anthropic blog (claude.com/blog/agent-view-in-claude-code).
- **Anomaly:** none — no embedded prompt-injection-style text found in the source article. The page ends with a generic newsletter-signup CTA ("Transform how your organization operates with Claude / Get the developer newsletter"), which is standard boilerplate, not an injected instruction.

## Related

- [[ClaudeCode]] — the tool agent view is a feature of
- [[ClaudeCodeRoutines]] — looping/scheduled jobs whose next-run time surfaces in agent view
- [[MultiAgentSystem]] — the multi-session/multi-agent orchestration pattern agent view manages
- [[AgentWorkflowPatterns]] — parallel-session workflow patterns agent view supports
