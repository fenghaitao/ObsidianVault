---
title: "summary-2025-08-25 - Piloting Claude in Chrome.md"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2025-08-25 - Piloting Claude in Chrome.md"]
last_updated: 2026-06-28
---

## Core Summary

Anthropic launched a Chrome browser extension ([[ClaudeInChrome]]) that lets Claude take actions in the browser on behalf of users — clicking buttons, filling forms, managing calendars, and processing email. The article documents both the capability rollout and Anthropic's concurrent effort to combat [[PromptInjection]] attacks, which are the primary safety risk for [[BrowserUseAgent|browser-using AI agents]].

## Key Points

- **Initial pilot**: Started August 2025 with 1,000 Max plan users via a waitlist at claude.ai/chrome.
- **Expansion timeline**:
  - Nov 24, 2025 — extended to all Max plan subscribers (beta), with scheduled tasks, multi-tab workflows, and smarter navigation shipped.
  - Dec 18, 2025 — extended to Pro, Team, and Enterprise plans.
- **Claude Code integration** (Dec 2025): build in terminal, verify in browser, debug with Claude reading console errors and DOM state directly.
- **Enterprise controls**: org-wide enable/disable, site allowlists and blocklists for Teams and Enterprise admins.
- **Prompt injection risk**: tested 123 cases across 29 attack scenarios. Baseline attack success rate was 23.6% in autonomous mode without mitigations.
- **Mitigations applied**:
  - Hardened system prompts directing Claude on sensitive data handling.
  - Blocked high-risk website categories (financial services, adult content, pirated content).
  - Advanced classifiers to detect suspicious instruction patterns and unusual data access.
  - Special defenses for browser-specific vectors: hidden DOM form fields, URL text, tab titles.
- **Results after mitigations**: general autonomous mode 23.6% → 11.2%; browser-specific challenge set 35.7% → 0%.
- **Red-teaming example**: a malicious email instructed Claude to delete user emails "for security reasons" — Claude complied before defenses were in place.
- **Internal productivity**: Anthropic teams used early versions to manage calendars, schedule meetings, draft emails, handle expense reports, and test website features.
- **Safety philosophy**: browser-using AI is considered inevitable; Anthropic views controlled real-world testing as the only way to uncover novel attack patterns that internal red-teaming misses.

## Related

- [[ClaudeInChrome]] — the product described in this article
- [[PromptInjection]] — the primary safety challenge discussed
- [[BrowserUseAgent]] — the broader capability category
- [[ClaudeCode]] — integrated with Claude in Chrome (Dec 2025)
- [[ClaudeMax]] — original pilot plan tier
- [[ClaudeTeamPlan]] — expanded access tier
- [[ClaudeEnterprise]] — expanded access tier with admin controls
- [[Anthropic]] — author and publisher of this article
- [[AIAgent]] — browser-using Claude as a class of AI agent
