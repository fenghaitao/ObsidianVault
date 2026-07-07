---
title: "ClaudeDesign"
type: entity
tags: [tool, design, anthropic, html, design-system]
sources: ["raw/01-articles/claude/2026-05-20 - Using Claude Code The unreasonable effectiveness of HTML.md", "raw/01-articles/claude/2026-06-17 - Claude Design now stays on brand for daily work.md", "raw/01-articles/claude/2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon.md"]
last_updated: 2026-07-07
---

## Definition

Claude Design is an Anthropic tool for prototyping and sketching designs using HTML. It leverages HTML's expressiveness for visual design, even when the final implementation surface is not HTML (e.g., React, Swift). First launched in beta, it had over one million users in its first week and was rebuilt in June 2026 to stay consistent with user design systems across projects, integrate fluidly with [[ClaudeCode]], and offer a direct canvas editor.

## Key Information

- Built on HTML, because HTML is highly expressive for visual design.
- Can prototype interactions such as animations, actions, sliders, and knobs.
- Useful for sketching designs before implementing in a target language like React or Swift.
- Claude Code can generate HTML design artifacts with more context (filesystem, MCPs, browser, git history) than Claude.ai or Claude Design alone can access.

## June 2026 Update: On-Brand Daily Work

### Design System Integration

- **Design system import**: Bring in one or several design systems from a GitHub repo, design files, or raw uploads. Claude builds with your components, checks its output against your design system, and makes corrections before showing results.
- **Admin role**: For larger teams, an admin can approve one standard design system and lock down edits, ensuring all work matches company guidelines.

### Claude Code Integration

- **`/design-sync`**: Pull your design system into Claude Design, so everything you build starts from your existing components.
- **`/design`** in Claude Code: Create, edit, and sync design projects without leaving the terminal. Import a design into your codebase, turn code into a live prototype, or let Claude carry a project all the way through.
- When a design is ready to become software, hand it off to Claude Code, which continues from existing work instead of starting from a screenshot.

### Canvas Editor

- Direct, fine-grained control over every element with drag, resize, and align controls.
- Hundreds of stability fixes for real daily use.

### Usage and Limits

- Shared usage limits with chat, [[ClaudeCowork]], and Claude Code, giving most users more headroom.
- Average turn uses fewer tokens to achieve the same results; errors are down sharply.

### Export and Connectors

- Reliable export to PDF and PowerPoint.
- Connectors to: [[Adobe]], [[Base44]], [[Canva]], [[Gamma]], [[Lovable]], [[Miro]], [[Replit]], [[Vercel]], and [[Wix]], with more destinations coming soon.

### Availability

- Beta on Claude Pro, Max, Team, and Enterprise plans, included with subscription.
- Off by default for Enterprise users; admins enable in organization settings. Work is shareable only within the organization.
- Accessible at claude.ai/design or in the sidebar on the desktop app.

### Endorsement

[[AlexLieberman]] (Cofounder, Morning Brew & [[Tenex]]): "The combination of approachable UX with strong taste & design instinct is why it's become a core part of my tech stack. And then the hand-off between Claude Design and Claude Code makes the process of prototype to production seamless."

## Related

- [[ClaudeCode]] — bidirectional design/code handoff via /design-sync and /design commands
- [[HTMLAsAgentOutputFormat]] — HTML as the medium for design prototyping
- [[DesignSystem]] — the design system integration pattern
- [[DesignToCodeHandoff]] — the design-to-code workflow pattern
- [[summary-2026-05-20 - Using Claude Code The unreasonable effectiveness of HTML]] — source summary
- [[summary-2026-06-17 - Claude Design now stays on brand for daily work]] — source summary
- [[Adobe]] — export connector
- [[Base44]] — export connector
- [[Canva]] — export connector
- [[Gamma]] — export connector
- [[Lovable]] — export connector
- [[Miro]] — export connector
- [[Replit]] — export connector
- [[Vercel]] — export connector
- [[Wix]] — export connector
- [[Tenex]] — company co-founded by Alex Lieberman, cited as a Claude Design user
- [[AlexLieberman]] — cofounder of Morning Brew and Tenex, Claude Design advocate
- [[ClaudeCowork]] — shares usage limits with Claude Design
- [[WrenchBoard]] — hackathon project prototyped in Claude Design, then handed off to Claude Code
- [[Superpowers]] — skills framework used alongside Claude Design for structured brainstorming
- [[summary-2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon]] — hackathon source summary
