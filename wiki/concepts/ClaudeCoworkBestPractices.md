---
title: "ClaudeCoworkBestPractices"
type: concept
tags: [claude-cowork, best-practices, delegation, knowledge-work, framework]
sources: ["raw/01-articles/claude/2026-06-03 - Best practices for getting started with Claude Cowork.md"]
last_updated: 2026-07-07
---

## Definition

Claude Cowork Best Practices is a practical framework, authored by Anthropic growth marketing lead Austin Lau, for non-technical knowledge workers to decide what work to delegate to [[ClaudeCowork]] and how to do it effectively. It centers on a decision framework distinguishing Chat, Cowork, and Code workspaces, a five-ingredient checklist for identifying Cowork-shaped tasks, and prompting patterns that improve output quality.

## Key Information

### Chat vs Cowork vs Code Decision Framework

All three workspaces run the same [[Claude]] models, but they serve different work types:

- **Chat**: For answers, brainstorming, and thinking out loud. You bring your work to Claude (upload a file, paste text, ask a question). The output is a thought in your head.
- **Claude Cowork**: For deliverables — a file someone will open, a deck someone will present, a spreadsheet to be sorted. You bring Claude to your work by pointing it at folders and connecting apps. The output is something you hand to someone else.
- **Claude Code**: For developers building and shipping software. If your work lives in code, start here.

Rule of thumb: use Chat if what you want fits in a few exchanges (a question, explanation, brainstorm, or gut check). Use Claude Cowork if what you need is a deliverable, or anything multi-step that touches more than one file or app, or that you'd describe as a task rather than a question.

### Five Ingredients of a Cowork-Shaped Task

A heuristic checklist for deciding what to delegate to Claude Cowork. A good candidate hits a few of these criteria (not all five are required):

1. **More than one thing goes in**: Multiple files, a whole folder, or a file plus connectors. Single-input tasks are usually fine in Chat.
2. **A file comes out**: A deliverable you can attach, present, share, or repurpose — a doc, deck, spreadsheet, or CSV.
3. **You'll do it again**: One-offs are fine, but recurring tasks are the sweet spot. They can be scheduled to run automatically.
4. **You already know what good looks like**: Familiarity with the output shape lets you judge in 15 seconds whether it's right, wrong, or 70% there.
5. **The middle is the boring part**: The thinking lives at the start (deciding what you want) and the end (deciding if it's right). Everything in between — extract, compile, reconcile, reformat — is what you hand off.

### "Make Claude Ask Clarifying Questions First" Pattern

The single most useful prompting habit for Claude Cowork. Include this instruction in the prompt:

> Before we begin, repeat my ask back to me so we're aligned, then ask me as many clarifying questions as you have.

This surfaces unstated assumptions (time period, definition of "good," edge cases) that are obvious to the human but unknown to Claude. Answering five questions upfront costs 30 seconds; finding gaps afterwards costs time, tokens, and is harder to fix.

### Common Mistakes

- **Chat for everything**: Never feeling the difference Claude Cowork can make.
- **Cowork for one-off questions**: Waiting around for something Chat would have answered in five seconds.

### Practical Workflow Examples

- **Daily briefing**: Auto-runs at 6am, connected to Slack and Gmail, reviews unread emails and channels, sorts into buckets, produces a short report with TLDR, flagged emails, channel summaries, and overnight incidents.
- **Budget pacing**: Connected to Google Ads and Meta Ads, creates a live HTML dashboard pulling daily spend and calculating pacing, with plain-English filtering and campaign controls.
- **Weekly reporting**: Connected to Google Search Console, pulls queries/countries/pages, reconciles into a single sheet (instead of Google's one-CSV-per-dimension default), adds context (last 7 days vs prior 7, country filters, meaningful movements), auto-scheduled weekly.

### Getting Started (First 10 Minutes)

1. Open the Claude desktop app and switch to the Claude Cowork tab.
2. Give Claude something to work with: drop in files, point at a folder, or connect an app (Slack, Gmail, Notion, CRM).
3. Describe the outcome you want and provide necessary context.
4. Start with a real task you know well — you'll see immediately where it's strong and where it needs context.
5. Use the "clarifying questions first" pattern.
6. If unsure what to hand off, ask Claude itself — it has memory and can search past conversations to suggest which tasks to try.

## Related

- [[ClaudeCowork]] — the product this framework is designed for
- [[ClaudeCode]] — the developer-focused counterpart workspace
- [[AgentWorkflowPatterns]] — broader patterns for agent-driven workflows
- [[summary-2026-06-03 - Best practices for getting started with Claude Cowork]] — source summary
