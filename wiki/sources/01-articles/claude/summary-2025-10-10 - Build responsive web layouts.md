---
title: "summary-2025-10-10 - Build responsive web layouts"
type: source
tags: [source, original-material, responsive-design, css, claude-ai, claude-code]
sources: ["raw/01-articles/claude/2025-10-10 - Build responsive web layouts.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic describes using Claude to generate and debug responsive web layouts, replacing the traditional cycle of manual media-query authoring, multi-device testing, and iterative dev-tools debugging. [[Claude.ai]] is positioned for quick prototyping — describing a layout to get working HTML/CSS with proper viewport configuration and breakpoint explanations. [[ClaudeCode]] is positioned for codebase-wide refactoring — scanning stylesheets across a project, identifying viewport-specific problems, implementing fixes, testing at multiple viewport sizes, and generating a Playwright regression-test suite.

## Key Points

- Traditional responsive workflow: write base styles, add media queries at common breakpoints (768px, 1024px, 1440px), then manually test across browser dev tools and real devices — time-consuming, and edge cases still slip through (e.g., iOS Safari's expanding address bar breaking a fixed footer that looked fine in Chrome's emulator).
- CSS frameworks (Bootstrap, Tailwind) provide responsive utility classes but lock projects into predefined breakpoint systems that may not match specific content needs, and abstract away CSS in ways that complicate debugging.
- **Claude.ai workflow**: describe a layout (e.g., "product landing page with fixed header, hero section, three feature cards, footer, cards row on desktop / stacked on mobile") and receive semantic HTML5 with responsive CSS, including comments explaining breakpoint choices. Also useful for explaining trade-offs between layout approaches (e.g., flexbox vs. grid for navigation).
- **Claude Code workflow**: example case — a dashboard that breaks on tablet viewports. Claude Code scans `layout.css`, identifies fixed-width styles causing overflow with line numbers, replaces them with responsive alternatives (max-width, flex basis, grid-template-columns with auto-fit), adds breakpoint-specific media queries, tests at 320px and 512px to confirm no horizontal overflow, then generates a Playwright test suite validating responsive behavior across real device sizes (iPhone SE, iPhone 12, iPad, iPad Pro, Desktop) to prevent regressions.

## Related

- [[Claude.ai]] — used for quick responsive layout prototyping
- [[ClaudeCode]] — used for codebase-wide responsive refactoring
- [[ResponsiveWebDesign]] — the practice this article documents
