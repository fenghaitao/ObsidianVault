---
title: "ClaudeManagedAgents"
type: entity
tags: [product, claude, anthropic, agents, platform]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - Japan/01 - Code with Claude Tokyo 2026： Opening Keynote.md]
last_updated: 2026-06-23
---

## Definition

Claude Managed Agents is Anthropic's product offering for building and deploying production AI agents at scale. It provides an agentic harness, context management tools, and production-grade infrastructure, purpose-built for Claude models.

## Key Information

- **Harness:** separates "brain" (decision-making) from "hands" (sandbox execution); outcome-based iteration with rubrics defining what good looks like.
- **Context:** 1M token context window, memory (file system for learnings across sessions), skills (self-written knowledge gap filling), dreaming (retrospective self-improvement from past trajectories).
- **Infrastructure:** auto-scaling sandboxes, agentic fleets for parallel work, scheduled deployments (cron-based), vaults for secure secret storage.
- **Customer adoption:** Notion (agent orchestration in-product), Asana (AI teammates alongside humans in projects), Rakuten (custom internal agents across engineering, product, sales, finance).
- **Dreaming:** agents look back over all past sessions, update memory and skills for better future performance.
- **Scheduled deployments:** agents can run on any cadence (nightly, weekly, etc.) without manual triggering.

## Related

- [[summary-01 - Code with Claude Tokyo 2026： Opening Keynote]] — launch keynote
- [[ClaudeFable5]] — the model optimized for Managed Agents
- [[ClaudeCode]] — the developer-facing agent tool
- [[Anthropic]] — the company behind the platform
