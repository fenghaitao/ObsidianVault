---
title: "ClaudeInChrome"
type: entity
tags: [product, browser-extension, anthropic, chrome]
sources: ["raw/01-articles/claude/2025-08-25 - Piloting Claude in Chrome.md"]
last_updated: 2026-06-28
---

## Definition

Claude in Chrome is an [[Anthropic]]-built browser extension for [[GoogleChrome]] that lets Claude take actions within the browser on behalf of users — clicking buttons, filling forms, managing calendars, composing emails, and navigating websites.

## Key Information

- **Launch**: Research preview pilot began August 2025 with 1,000 Max plan users (waitlist at claude.ai/chrome).
- **Expansion**:
  - Nov 24, 2025 — beta available to all [[ClaudeMax]] subscribers, including scheduled tasks, multi-tab workflows, and smarter navigation.
  - Dec 18, 2025 — available to Pro, [[ClaudeTeamPlan|Team]], and [[ClaudeEnterprise|Enterprise]] plans.
- **Claude Code integration** (Dec 2025): developers can build in the terminal and have Claude verify results in the browser, with Claude reading console errors and DOM state directly. See [[ClaudeCode]].
- **Enterprise controls**: admins can enable/disable the extension org-wide, configure site allowlists and blocklists.
- **Internal use cases at Anthropic**: managing calendars, scheduling meetings, drafting email responses, handling routine expense reports, and testing new website features.
- **Safety focus**: the product was explicitly designed as a controlled real-world experiment to develop and validate [[PromptInjection]] defenses before wider rollout.
- **Permission model**: users control what Claude can access and do; blocked by default from high-risk website categories (financial services, adult content, pirated content).
- Documented in Anthropic's trustworthy agents framework: agents must operate within well-defined user-granted permissions.
- **"Teach Mode" (referenced May 2026)**: an internal workflow-recording feature — the user demonstrates a task once (screenshots, click coordinates/selectors, optional voice narration), and the demonstration becomes a reusable specification Claude replays adaptively on later requests (adapting to layout changes rather than blindly replaying recorded coordinates). Anthropic describes the underlying pattern (capture a demonstration, feed it back as context) as broadly applicable beyond Claude in Chrome. See [[summary-2026-05-13 - Best practices for computer and browser use with Claude]].

## Related

- [[summary-2025-08-25 - Piloting Claude in Chrome]] — source article
- [[Anthropic]] — creator of the extension
- [[GoogleChrome]] — the browser platform
- [[PromptInjection]] — primary security challenge addressed during pilot
- [[BrowserUseAgent]] — the capability category this product exemplifies
- [[ClaudeCode]] — integrated with Claude in Chrome for terminal-to-browser development workflows
- [[ClaudeMax]] — original pilot and beta plan tier
- [[ClaudeTeamPlan]] — expanded access tier
- [[ClaudeEnterprise]] — expanded access tier with org admin controls
- [[AIAgent]] — Claude in Chrome as a browser-using AI agent
- [[summary-2026-05-13 - Best practices for computer and browser use with Claude]] — describes the internal "Teach Mode" workflow-recording pattern
