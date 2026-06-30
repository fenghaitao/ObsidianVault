---
title: "Observe Skill"
type: concept
tags: [coding-agents, observability, evaluations, automation, microsoft-foundry, skills]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260514 - Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft.md"]
last_updated: 2026-06-30
---

## Definition
The Observe Skill is a Microsoft Foundry coding agent skill (activated via GitHub Copilot Chat) that automates the entire agent observability loop — generating evaluation datasets, running batch evaluations, analyzing failures, optimizing prompts, comparing versions, and rolling back to the best-performing configuration — all with a human in the loop.

## Key Information

### Capabilities
- **Dataset generation**: Reads agent instructions and automatically generates evaluation datasets — solves the "no existing data" problem for new agents
- **Batch evaluation**: Runs quality, safety, and agentic evaluators against the generated dataset
- **Failure analysis**: Identifies which metrics failed and provides reasoning for each failure
- **Prompt optimization**: Analyzes failure patterns and rewrites prompts to fix issues (e.g., tightening instructions that were too open to misinterpretation)
- **Re-evaluation**: Runs the same evaluators against the optimized agent
- **Version comparison**: Tracks version history, compares eval scores across versions, identifies the best-performing version
- **Rollback**: Deploys the best version (e.g., "version 5 was the best, let's use that")

### Human in the Loop
- The skill proposes actions and shows reasoning — the human decides whether to proceed
- After each optimization cycle, it asks whether to continue or stop
- Critical when the skill starts "chasing the dragon" — iterating with diminishing returns or regressions
- Example: Skill went through 10 versions, found version 5 was best, recommended rollback

### Transparency
- Shows what it's looking for in evaluations
- Explains why failures occurred
- Provides a full history of what was tried and what worked/didn't

### Extensibility
- Can convert prompt agents to hosted agents (e.g., LangGraph)
- Can guide through red teaming
- Can explore alternative tools (e.g., replacing slow web search)
- Default skill has best practices; users can add domain knowledge

### Origin
- Released ~May 2026 (2 weeks before AI Engineer London)
- PM: Felicia Shaw
- Part of the Microsoft Foundry skill set (open source on GitHub)
- Uses the Foundry MCP server for interactions
- Trigger words: "evaluate my agent", "help me build a dataset", etc.

## Related
- [[Microsoft Foundry]] — platform hosting the skill
- [[Nitya Narasimhan]] — demonstrated the skill at AI Engineer
- [[AgentObservability]] — the loop this skill automates
- [[AgenticEvaluations]] — evaluations run by the skill
- [[ContinuousEvaluation]] — the continuous improvement pattern
- [[EvalEngineering]] — evaluation methodology
- [[Agent Skills]] — broader skill concept for coding agents
- [[summary-20260514 - Mind the Gap (In your Agent Observability) — Amy Boyd & Nitya Narasimhan, Microsoft]] — source
