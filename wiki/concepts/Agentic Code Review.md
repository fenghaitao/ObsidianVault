---
title: "Agentic Code Review"
type: concept
tags: [concept, code-review, agents, developer-experience, process]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260515 - Agents Don't Do Standups： Building the Post-Engineer Engineering Org — Mike Spitz, PFF.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind.md"]
last_updated: 2026-06-30
---

## Definition
Agentic Code Review is the practice of delegating style and opinionated code review feedback (variable names, formatting, code style consistency) to AI agents, removing the emotional friction from human code reviews and freeing engineers to focus on system design and architectural concerns.

## Key Information
- **Origin**: Presented by [[MikeSpitz]] as part of the [[Post-Engineer Engineering Org]] model at [[PFF]]
- **What Agents Review**: Variable names, code style consistency, formatting, opinionated/preference-based feedback — the kind of feedback engineers typically dislike giving and receiving
- **What Humans Review**: System design, architecture, big-picture concerns — the work engineers find meaningful
- **Key Benefit**: Removes the emotional aspect from code review — style criticism from an agent doesn't carry the interpersonal friction of peer criticism
- **Contrast with Full Agent Review**: PFF deliberately does NOT use agents for system design review, only for the mechanical/opinionated aspects
- **Integration**: Fits into the autonomous pipeline after PR auto-generation but before the Autonomous QA Agent
- **Buy-in Strategy**: Offloading work engineers hate is the fastest way to get team adoption

## Related
- [[MikeSpitz]] — presented the concept
- [[PFF]] — company using agentic code review
- [[Post-Engineer Engineering Org]] — organizational model
- [[ClaudeCode]] — coding agent used for code review
- [[Lightweight Design Document]] — defines the design standards agents check against
- [[Composable Skills]] — code review rules encoded as a skill
- [[summary-20260515 - Agents Don't Do Standups： Building the Post-Engineer Engineering Org — Mike Spitz, PFF]] — source
- [[summary-20260524 - How Google DeepMind Runs Agents at Scale — KP Sawhney & Ian Ballantyne, Google DeepMind]] — source (Google's auto-review models, fine-tuned on style guides)
- [[GoogleDeepMind]] — organization with language-specific fine-tuned review models
- [[KP Sawhney]] — received agent-generated PR review without manual triggering
