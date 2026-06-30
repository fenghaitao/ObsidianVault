---
title: "Backtesting for AI Systems"
type: concept
tags: [evals, testing, accuracy, monitoring, ai-engineering]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260517 - Fighting AI with AI — Lawrence Jones, Incident.md"]
last_updated: 2026-06-30
---

## Definition

Backtesting for AI systems is the practice of running batches of AI-generated outputs (e.g., investigations, RCA reports) on a recurring basis against known accounts to produce aggregate accuracy metrics. It provides a quantitative signal of whether an AI system is improving or degrading over time, but alone it cannot explain why the number changed.

## Key Information

- **Origin**: Used at [[IncidentIo]] as part of their AI engineering workflow, alongside prompts, evals, scorecards, traces, and datasets
- **Implementation**: A batch of investigations is run daily against incident.io's own account and a selection of customer accounts, producing a rolled-up accuracy metric (e.g., "86% accurate RCA on our account")
- **Limitation**: Aggregate numbers do not explain why accuracy went up or down, which failure modes changed, or how to improve the system for specific accounts
- **Complementary pattern**: Backtests provide the "what" (system accuracy), while [[AI Analysis Pipelines]] provide the "why" (root causes and failure modes)
- **Relationship to traditional backtesting**: Analogous to financial backtesting (running strategies against historical data) but applied to AI output quality rather than trading performance
- **Scale**: incident.io runs thousands of investigations across hundreds of customer accounts daily
- **Workflow integration**: Backtest results trigger analysis pipeline runs when metrics change, leading to identified issues, code changes via [[Eval Red Green Cycle]], and PRs that deploy fixes

## Related

- [[summary-20260517 - Fighting AI with AI — Lawrence Jones, Incident]] — primary source
- [[AI Analysis Pipelines]] — downstream analysis that explains backtest results
- [[Eval Red Green Cycle]] — fix workflow triggered by backtest findings
- [[EvalFlywheel]] — broader continuous improvement loop
- [[OnlineEvals]] — complementary live-traffic evaluation
- [[IncidentIo]] — company that developed this pattern
- [[ContinuousEvaluation]] — related continuous monitoring practice
