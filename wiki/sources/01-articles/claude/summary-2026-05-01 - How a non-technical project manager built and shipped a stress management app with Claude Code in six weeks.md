---
title: "summary-2026-05-01 - How a non-technical project manager built and shipped a stress management app with Claude Code in six weeks"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-05-01 - How a non-technical project manager built and shipped a stress management app with Claude Code in six weeks.md"]
last_updated: 2026-07-04
---

## Core Summary

This Anthropic "Day zero: founder stories" blog post profiles Kostiantyn Vlasenko, a Kyiv-based project manager at [[Mythical Games|Mythical Games]] with a decade of PM experience and zero prior coding background, who built and shipped **Respiro**, a science-backed, real-time stress-management iOS app, after entering the Built With Opus 4.6 Claude Code Hackathon (hosted by Cerebral Valley) in February 2026. Starting from a one-line prompt, he used [[ClaudeCode|Claude Code]] to research agent architectures and relevant Apple APIs, then directed a 15+ specialized-subagent build (TCA architect, Swift developer, Metal specialist, code reviewer, and more) running in parallel across modules, orchestrating them the way he'd manage a human team. When an early React Native MVP became untestable (he had no Android device), Claude Code rewrote the app in Swift from scratch in a few hours. Going from idea to a full-featured, App Store-ready product took just under six weeks; Respiro shipped on the [[AppleAppStore|Apple App Store]] with hundreds of users. Vlasenko also used Claude to navigate the Apple Developer Program, integrate Sentry and Amplitude via screenshot-guided setup (citing [[ComputerUse|vision capabilities]] as Claude's most underrated feature), build out analytics funnels/retention tracking, write marketing content, and devise a practitioner-referral growth strategy. He has since brought the same Claude-based workflow into his day job, becoming an internal advocate at Mythical Games, where a small team now delivers work entirely through Claude — not without friction, as some engineers resisted ceding line-by-line code control.

## Key Points

- **Builder**: Kostiantyn Vlasenko, ~10 years as a project manager (most recently at [[Mythical Games]], Kyiv), no prior programming experience; previously used Claude for Jira updates and Slack meeting-note automation before adopting the Claude Code CLI.
- **Trigger**: entered the **Built With Opus 4.6 Claude Code Hackathon** (guest-list event hosted via cerebralvalley.ai) in February 2026; idea crystallized while on vacation in western Ukraine, frustrated that existing stress apps schedule fixed-time reminders rather than detecting stress signals in real time.
- **Product**: [[Respiro]] — an iOS app that detects stress from personal-device signals and intervenes with guided breathing (e.g., box breathing) at the moment of stress, not on a fixed schedule. Live on the [[AppleAppStore|Apple App Store]] with hundreds of users as of publication.
- **Timeline**: idea-to-App-Store-ready took "just under six weeks"; the article's headline/summary frames the hackathon build itself as "72 hours."
- **Architecture**: 15+ specialized subagents built and orchestrated by Vlasenko himself, including a TCA (The Composable Architecture) architect agent, a Swift developer agent, a Metal specialist agent, and a code-reviewer agent, running in parallel across different modules — Vlasenko frames this as directly analogous to his experience managing human teams ("I have a lot of experience managing real people... this was the same thing, only managing agents inside my IDE").
- **Rewrite pivot**: initial MVP was React Native; became untestable because Vlasenko had no Android phone. Claude Code rewrote the app in Swift from scratch in a few hours.
- **Third-party integrations set up with Claude's help**: the Apple Developer Program (step-by-step, screenshot-guided), [[Sentry]] (logging), and Amplitude (analytics) — Claude went beyond basic SDK wiring to build full user funnels and DAU/MAU retention tracking.
- **Vision capabilities**: Vlasenko calls Claude's vision capability its most underappreciated feature — screenshotting a confusing interface (e.g., creating a Meta API token) and having Claude explain what to click and guide him through the flow.
- **Growth strategy**: Claude suggested reaching out to psychologists and mindfulness practitioners to recommend Respiro to their clients; Vlasenko tried it and practitioners began recommending the app. Claude also helped write blog posts and TikTok content.
- **Spillover to day job**: Vlasenko now commits code and ships features directly at Mythical Games, shares his "Claude folder and workflows" with the engineering team, and reports colleagues found it better than their existing process. Mythical Games now has a small internal team delivering work entirely through Claude. Adoption wasn't frictionless — some engineers found it hard to give up controlling every line of code.
- **Next steps**: voice-guided practices and motion exercises planned for Respiro's next release, from a roadmap Claude helped write; Vlasenko logs 7-8 hours of coding after his regular workday.
- **Quote**: "I would say that Claude Code is my new addiction."
- **Anomaly**: no prompt-injection-style scraped text or widget boilerplate was found in the raw article; it reads as a clean, direct blog post/interview.

## Related

- [[ClaudeCode]] — the tool used for the entire build, from architecture research through App Store shipping
- [[Respiro]] — the stress-management app profiled in this article
- [[MultiAgentSystem]] — Respiro's 15+ specialized-subagent architecture is a production instance of the orchestrator-subagent pattern
- [[ClaudeCodeSubagents]] — subagent orchestration Vlasenko built and directed personally
- [[AgenticCoding]] — case study of a non-technical builder using Claude Code as a thought partner rather than a code generator
- [[AppleAppStore]] — distribution platform Respiro shipped on
- [[Sentry]] — logging integration set up via Claude-guided onboarding
- [[MythicalGames]] — Vlasenko's employer, now running an internal team delivering work entirely through Claude
- [[ComputerUse]] — Claude's screenshot/vision-guided navigation of unfamiliar developer consoles (Apple Developer Program, Meta API)
