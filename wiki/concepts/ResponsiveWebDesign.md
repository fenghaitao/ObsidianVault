---
title: "ResponsiveWebDesign"
type: concept
tags: [css, responsive-design, frontend, claude-ai, claude-code]
sources: ["raw/01-articles/claude/2025-10-10 - Build responsive web layouts.md"]
last_updated: 2026-07-04
---

## Definition

Responsive web design with Claude is the practice of generating and debugging CSS layouts that adapt correctly across viewport sizes, using Claude to replace manual media-query authoring and multi-device testing cycles.

## Key Information

- **Traditional pain points**: manually choosing breakpoints (768px, 1024px, 1440px) requires understanding specific content, not just device categories; CSS frameworks (Bootstrap, Tailwind) provide shortcuts but lock in predefined breakpoints and obscure underlying CSS, complicating debugging; browser device emulators approximate but don't perfectly replicate real devices (e.g., iOS Safari's expanding address bar can break a fixed footer that looked fine in Chrome DevTools).
- **[[Claude.ai]] workflow**: describe layout requirements in natural language (e.g., a three-column card grid that stacks on mobile) and receive complete, semantic HTML5 with responsive CSS, proper viewport meta tags, and comments explaining breakpoint choices. Also useful for explaining trade-offs between layout techniques (e.g., flexbox vs. grid).
- **[[ClaudeCode]] workflow**: systematic, project-wide refactoring — scans stylesheets to find fixed-width styles and overflow-causing patterns (with line numbers), replaces them with responsive alternatives (`max-width`, flex basis, `grid-template-columns` with `auto-fit`), adds breakpoint-specific media queries, tests at multiple viewport widths to confirm no overflow, and generates a Playwright test suite across real device sizes (iPhone SE, iPhone 12, iPad, iPad Pro, Desktop) to prevent regressions.

## Related

- [[Claude.ai]] — quick, ad-hoc layout generation and explanation
- [[ClaudeCode]] — systematic, codebase-wide responsive refactoring
- [[summary-2025-10-10 - Build responsive web layouts]] — source article
