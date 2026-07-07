---
title: "MaestrIA"
type: entity
tags: [hackathon, home-repair, claude-code, diagnostics, non-programmer, localization]
sources: ["raw/01-articles/claude/2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon.md"]
last_updated: 2026-07-07
---

## Definition

MaestrIA is a web app that gives ordinary people master-level home repair diagnostics while giving skilled tradespeople a way to demonstrate expertise. Built by Benjamin Torralbo, who had no prior programming experience, it uses Claude to stream diagnostic reasoning in real time and connects users with nearby certified tradespeople.

## Key Information

- **Creator**: Benjamin Torralbo, a 20-year-old from Chiloé, Chile, with no prior programming experience. His father, Juan Rodrigo Torralbo, is a certified *Maestro Mayor* carpenter with 30 years of craft experience restoring UNESCO-listed churches.
- **Problem addressed**: Hundreds of thousands of skilled tradespeople in Chile are invisible to the formal system. Meanwhile, people needing home repairs don't know what is wrong, what it costs, who to call, or whether they're being charged fairly.
- **How it works**: Users photograph their problem, describe it in voice or text, and share their location. Claude streams its reasoning in real time with animated bounding boxes over the photos, then delivers structured diagnoses: what's broken, material, severity (1–5), project budget, and time estimate. The agent renders a map of nearby maestros filtered by trade while a second agent drafts a WhatsApp message to send.
- **Technical heart**: A JSON file injected into every diagnosis containing 17 diagnostic rules, 7 native Chilote woods, 16 terms of local trade dialect, 19 benchmark prices, and 9 common mistakes of the craft — all distilled from hours of interviews with Benjamin's father. Without touching the system prompt, this single file lifted eval scores from 74% to 81% against a human master's judgment.
- **Development approach**: Benjamin acted as "site foreman" overseeing Claude's technical execution. Before writing any feature, he asked Claude Code to design specs, staged action plans, and the security model (input sanitization against prompt injection, rate limiting, origin validation, Zod schemas). He reviewed each feature diff by diff.
- **Future plans**: Expand into new builds, hardware-store integration, formal budgets, contracts, reviews, and a certification system covering multiple trades (carpenters, architects, plumbers, electricians, masons).
- **URL**: [maestriachile.cl](https://maestriachile.cl/)

## Related

- [[summary-2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon]] — source summary
- [[ClaudeCode]] — development environment
- [[Claude4.7Opus]] — model used
- [[EvalDrivenDevelopment]] — eval-first methodology Benjamin applied
- [[SpecFirstDevelopment]] — spec-before-code approach used in development
