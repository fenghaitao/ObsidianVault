---
title: "Nebius"
type: entity
tags: [company, ai, evaluation, benchmark]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260604 - SWE-rebench： Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius.md"]
last_updated: 2026-06-30
---

## Definition
Nebius is an AI company that develops and maintains the SWE-rebench coding agent evaluation leaderboard, along with open-source training datasets SWE-Rehab and SWE-Rehab V2.

## Key Information
- Maintains [[SWE-rebench]], a monthly-refreshed leaderboard evaluating ~30 coding models on real-world software engineering tasks
- Released SWE-Rehab, an open-source dataset of ~30,000 RL environments (Docker images with real-world software engineering tasks), used by frontier labs for training
- Released SWE-Rehab V2, expanding to software engineering tasks across 20 programming languages
- Uses GitHub Archive as primary data source for benchmark task collection
- Evaluates both closed-source and open-weight models with a consistent harness
- Reports metrics beyond mean resolved rate: tokens per problem, tries per problem, pass@5, pass all 5
- Provides reference numbers for Claude Code, Codex, and Genie harnesses alongside their own scaffold

## Related
- [[Ibragim Badertdinov]] — researcher at Nebius
- [[SWE-rebench]] — their flagship leaderboard
- [[Harbor]] — terminal bench format used for evaluations
- [[summary-20260604 - SWE-rebench： Lessons from Evaluating Coding Agents — Ibragim Badertdinov, Nebius]] — source transcript
