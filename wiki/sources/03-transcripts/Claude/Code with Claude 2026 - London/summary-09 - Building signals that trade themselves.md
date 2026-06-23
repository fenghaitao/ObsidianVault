---
title: "summary-building-signals-that-trade-themselves"
type: source
tags: [source, claude, finance, skills, governance, transcript]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London/09 - Building signals that trade themselves.md]
last_updated: 2026-06-23
---

## Core Summary

Sharan Fernando (Man Group, $200B+ AUM) presents how the firm uses Claude and skills to research, backtest, and productionize systematic trading signals. AI now proposes investment ideas, gets data, runs backtests, writes strategy proposals, and productionizes signals -- with human review. The critical lesson: skills governance is the secret sauce. Without it, skills become local optimizations (e.g., hardcoded cost centers). Their solution: a common marketplace with owned, tested, tagged, and lifecycle-managed skills, organized by business unit. This foundation enables agents to leverage decades of institutional knowledge for complex tasks like systematic trading.

## Key Points

- **AI-driven trading:** Claude proposes signals, gets data, runs backtests against 15+ years of history, writes proposals, and productionizes signals. Humans review all output.
- **Skills as connective layer:** skills connect AI to decades of institutional knowledge, data, and workflows -- the organization's "superpower."
- **Governance failure:** power users (not process owners) built skills, leading to local optimizations (hardcoded cost center in expense report skill). Skills weren't reviewed or tested.
- **Governance solution:** common marketplace with managed (owned, tested, lifecycle-managed) and community skills. Every skill is visible, tagged, and tested with evals. Organized by business unit.
- **Systematic trading demo:** used 4 skills (alternative data search, data plotting, backtesting, distributed compute) to research credit card spend as a predictive signal for retail stocks.
- **Key takeaway:** organizational context is your IP and moat. Frontier labs won't solve context for you. Focus on governance to make skills an enterprise foundation, not individual toys.

## Related

- [[ClaudeCodeSkills]] — the skills system
- [[ManGroup]] — the investment firm
- [[summary-10 - Picking the right model]] — related talk on evals
- [[ClaudeCode]] — the tool skills run in
