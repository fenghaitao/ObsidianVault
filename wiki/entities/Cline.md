---
title: "Cline"
type: entity
tags: [tool, coding-agent, open-source]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md"]
last_updated: 2026-06-25
---

## Definition
Cline is an open-source coding agent that uses LLMs to autonomously write and edit code. It supports customizable rules that can be appended to its system prompt.

## Key Information
- In prompt learning experiments, vanilla Cline (with no rules added) resolved approximately 30% of SWE-bench GitHub issues using Claude Sonnet.
- After prompt learning with 150 training examples, Cline improved to approximately 45% — a 15 percentage point gain, the largest improvement observed.
- A case study demonstrated that Cline's original system prompt had no rules section — just a basic role description. Adding explicit rules (error handling, system design alignment, test requirements) drove the 15% improvement.
- The improvement was achieved with no fine-tuning, no tool changes, and no architecture changes — purely through system prompt iteration.
- Uses a rules mechanism similar to Claude Code's Claude.md file, allowing users to append repository-specific instructions.
- The large improvement from prompt learning suggests Cline benefits particularly strongly from well-crafted system prompt rules.

## Related
- [[ClaudeCode]] — another coding agent benchmarked alongside Cline
- [[SWE-bench]] — benchmark used to evaluate Cline
- [[PromptLearning]] — technique used to improve Cline's performance
- [[RuleBasedPrompting]] — the approach that drove Cline's improvement
- [[summary-20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize]] — source
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — source
