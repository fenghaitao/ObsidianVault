---
title: "RuleBasedPrompting"
type: concept
tags: [prompt-engineering, system-prompt, coding-agents, optimization]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize.md"]
last_updated: 2026-06-25
---

## Definition
Rule-based prompting is the practice of adding explicit, structured rules to system prompts that encode best practices and domain-specific guidance, rather than relying on vague role descriptions.

## Key Information
- In the Cline case study, the original system prompt had no rules section — just a basic role description ("you are a cloud agent").
- Adding explicit rules (e.g., handle errors in specific ways, ensure changes align with system design, accompany changes with tests) improved performance by 15% on SWE-bench Lite.
- The rules encode what a good engineer would naturally do, making implicit best practices explicit in the prompt.
- Rule-based prompting is the lowest-lift way to achieve massive improvement gains in agents — no fine-tuning, tool changes, or architecture changes required.
- The approach mirrors how humans learn: writing down lessons from mistakes and referencing them in future work.

## Related
- [[PromptLearning]] — the iterative technique for generating and refining rules
- [[OverfittingAsExpertise]] — the philosophy behind domain-specific rules
- [[MetaPrompt]] — the mechanism that synthesizes rules from evaluation feedback
- [[summary-20260106 - Build a Prompt Learning Loop - SallyAnn DeLucia & Fuad Ali, Arize]] — source
