---
title: "Post-Mortems for AI Workflows"
type: concept
tags: [AI, development, methodology, productivity, iteration]
sources: ["raw/03-transcripts/Lenny's Podcast/Lenny's Podcast/31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz.md"]
last_updated: 2026-07-10
---

## Definition

Post-Mortems for AI Workflows is Zevi Arnovitz's practice of retrospecting on AI mistakes to improve tooling and documentation. When an AI agent makes an error, instead of just fixing it, Zevi asks the AI to introspect on what caused the mistake and then updates prompts, documentation, or tooling to prevent recurrence.

## Key Information

- Zevi: "Updating documentation and tooling is one of the biggest hacks for productivity"
- Process: When Claude fails or creates a bad bug, Zevi asks: "What in your system prompt or tooling made you make this mistake?"
- Claude introspects and identifies the root cause of its error
- Zevi then says: "OK great, let's update your tooling and documentation so that this mistake never occurs again"
- This is done after every mistake, whether building internal tools or features
- Zevi contrasts this with his early "vibe coding" approach: "I would basically just keep running at it like running at the wall and until it worked. And once it worked, I was like, 'All right, awesome. This works. Let's keep going.'"
- The post-mortem approach is "one of the things that divides between people who are like OK with using AI and the people who actually know how to use it"
- Updates may go to slash commands, documentation files, or the AI's tooling/system prompt
- "Going back to your prompts, understanding what was not good enough, iterating on them, and then seeing how AI's responses get better — I think that's probably one of the most important things"

## Related

- [[summary-31 - How a Meta PM ships products without ever writing code ｜ Zevi Arnovitz]] — source summary
- [[Zevi Arnovitz]] — developed the practice
- [[Slash Commands Workflow]] — the workflow that benefits from post-mortems
- [[AI-Native Codebase]] — documentation that gets updated
- [[AI CTO Co-Founder]] — the system prompt that gets refined
