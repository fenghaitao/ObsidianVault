---
title: "MetaPrompt"
type: concept
tags: [prompt-engineering, iteration, system-prompt, optimization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize.md", "raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md"]
last_updated: 2026-06-25
---

## Definition
A meta prompt is a prompt that takes as input the original system prompt, the current rules, the problem input, the LLM-as-judge evaluation, and the explanation of failures, and outputs an improved set of system prompt rules.

## Key Information
- In the prompt learning workflow, the meta prompt receives: the original system prompt (e.g., Claude Code's or Cline's), the current rules (initially empty), the problem input, the LLM-as-judge eval result, and the explanation from that eval.
- It performs a diff-like comparison between the "old world" (original system prompt with no rules) and the "new world" (system prompt with learned rules appended).
- The output is a set of rules about what to avoid and what to do differently, synthesized from all the mistakes the agent made across the training examples.
- The meta prompt is the mechanism that closes the prompt learning loop, transforming evaluation feedback into actionable system prompt improvements.
- In the workshop implementation, the prompt learning optimizer (part of Arize's SDK) takes the original prompt, correctness labels, explanations, and rule violations as input to produce optimized prompts.

## Related
- [[PromptLearning]] — the overall technique that uses meta prompts
- [[LLM-as-Judge]] — provides the evaluation input to the meta prompt
- [[EvalEngineering]] — the quality of eval explanations fed into the meta prompt determines its effectiveness
- [[RuleBasedPrompting]] — the output of the meta prompt process
- [[summary-20251223 - The Unreasonable Effectiveness of Prompt Learning – Aparna Dhinakaran, Arize]] — source
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — source
