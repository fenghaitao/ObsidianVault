---
title: "Retool"
type: entity
tags: [tool, low-code, deployment, dashboards, internal-tools]
sources:
  - "raw/03-transcripts/Cole Medin/Channel Only/20260618 - The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore!.md"
last_updated: 2026-06-21
---

## Definition

Retool is a low-code platform for building and deploying internal tools / dashboards with a **governed path to production** (permission groups, audit trails, human-in-the-loop approvals). [[ColeMedin]] uses it to take locally-built control dashboards (e.g. his [[LoopEngineering]] orchestrator dashboard) to the cloud so they can be accessed remotely or shared with a team.

## Key Information

- **Import or build**: build apps directly in Retool, or **import existing React code** (Cole zips the dashboard front end Claude Code built and imports it).
- **Data connections**: connects to backends/databases — e.g. a [[Neon]] Postgres connection for the durable run-state of a loop system.
- **Governance**: permission groups gate sensitive actions (e.g. pause/resume a workflow) behind approvals with identity-aware audit trails — useful as the [[HumanInTheLoop]] surface for autonomous systems.
- **Use case in this corpus**: deploying observability/control dashboards for [[LoopEngineering]] and [[SecondBrain]] automation so they're usable beyond localhost.

## Related

- [[LoopEngineering]] — Retool deploys the loop-control dashboard
- [[Neon]] — the Postgres backend it connects to
- [[HumanInTheLoop]] — Retool's approval/permission gating
- [[ColeMedin]] — user
- [[summary-20260618 - The Creators of Claude Code and OpenClaw don't Prompt Their Agents Anymore!]] — primary source
