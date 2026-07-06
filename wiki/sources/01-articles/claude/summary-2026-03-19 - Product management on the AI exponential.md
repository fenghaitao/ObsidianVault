---
title: "summary-2026-03-19 - Product management on the AI exponential"
type: source
tags: [source, original-material]
sources: ["raw/01-articles/claude/2026-03-19 - Product management on the AI exponential.md"]
last_updated: 2026-07-04
---

## Core Summary

Cat Wu, Head of Product for Claude Code at Anthropic, argues that the traditional product management playbook — gather information upfront, lock a roadmap, execute against it for months — breaks down when model intelligence improves exponentially, because constraints designed around at project start can disappear mid-project. She illustrates the pace with a running test: asking Claude Code to add a table tool to Excalidraw failed through Sonnet 3.5 (new), partially succeeded with Opus 4 (June 2025), and became reliable enough to one-shot live on stage with Opus 4.6, a jump METR's benchmarks quantify as roughly 41x in agentic task time-horizon over 16 months. In response, the Claude Code team adopted four shifts: plan in short "side quest" sprints rather than long roadmaps, favor demos and evals over docs-first specs, treat every model release as a prompt to revisit shipped features, and "do the simple thing that works" so implementations aren't built around model limitations that will soon disappear. Wu also describes her own three-tool division of labor — Claude.ai as a thought-partner, Claude Code for building, and Cowork for everything else — a pattern echoed by product managers at Decagon and Datadog.

## Key Points

- Recurring test: prompting Claude Code to add a table tool to Excalidraw with each new model — failed through Sonnet 3.5 (new); partially succeeded with Opus 4 (June 2025), enough to become a pre-recorded Claude 4 launch demo; reliably one-shot by Opus 4.6, demoed live.
- METR data cited: Opus 4.6 completes software tasks taking humans ~12 hours about half the time; Sonnet 3.5 (new) could only handle ~21-minute tasks when Claude Code was first built — roughly a 41x jump in 16 months.
- Four shifts the Claude Code team embraced: (1) plan in short sprints via self-directed "side quests" instead of long-term roadmaps; (2) encourage demos and evals over docs; (3) revisit shipped features with every new model release; (4) do the simple thing that works, since workarounds for model limitations become unnecessary complexity once the next model drops.
- Side-quest-born features: Claude Code on Desktop, the AskUserQuestion tool, todo lists, plugins (grew from Noah's spec prototyped by Claude Code), and Claude Code with Chrome (emerged from users manually copy-pasting between Claude Code and Claude in Chrome).
- "Do the simple thing" example: the todo-list system-reminder hack (nudging the agent to update its list) was removed once the next model handled it natively; system prompt and tool descriptions have been cut with each model, including a 20% reduction for Opus 4.6.
- Agent teams (coordinating multiple Claude Code instances) were validated through hand-crafted evals (built by Conner) rather than a written spec.
- Wu's own three-product workflow: Claude.ai (thought partner, no action needed), Claude Code (prototypes/evals/scripts), Cowork (inbox zero, todo tracking, slide decks, Slack history search, travel booking).
- External PM quotes: Bihan Jiang (Director of Product, Decagon) describes starting in Cowork to pull context from Slack/codebase/docs, then moving to Claude Code for a demo-able prototype in hours; Kai Xin Tai (Senior PM, Datadog) describes evaluating Bits AI SRE agent via offline evals on production incidents and tight feedback loops, reframing PM craft as "accelerating discovery" rather than "defining certainty upfront."
- Anthropic-wide framing: data science, finance, marketing, legal, and design teams have also picked up Claude tools on their own, letting the whole org move at the same speed instead of waiting on handoffs.

## Related

- [[ClaudeCode]] — the tool and team this article centers on
- [[ClaudeCowork]] — the "everything else" knowledge-work tool in Wu's workflow
- [[Claude.ai]] — the "thought partner" tool in Wu's workflow
- [[Anthropic]] — publisher and employer of the author
- [[Claude4.6Opus]] — model that one-shots the Excalidraw test and shows the METR jump
- [[METR]] — benchmarking organization behind the time-horizon figures
- [[Decagon]] — PM quote source (Bihan Jiang)
- [[Datadog]] — PM quote source (Kai Xin Tai)
- [[MultiAgentSystem]] — related to the "agent teams" feature mentioned
- [[ClaudeCodePlugins]] — plugins system, whose origin story is described here
- [[AgentWorkflowPatterns]] — related Anthropic guidance on structuring agentic work
