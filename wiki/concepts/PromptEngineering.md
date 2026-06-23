---
title: "PromptEngineering"
type: concept
tags: [prompting, system-prompt, interview, requirements, progressive-disclosure]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London/05 - The prompting playbook.md, raw/03-transcripts/Claude/Code with Claude 2026 - London Day 2/06 - How we Claude Code.md, raw/03-transcripts/Claude/Code with Claude 2026 - London Day 2/04 - Evals for taste： Hill-climbing a slide-generation agent.md]
last_updated: 2026-06-23
---

## Definition

Prompt engineering is the practice of designing effective instructions for AI models to produce desired outputs. In the context of Claude Code and agent systems, it has evolved from static prompt writing to dynamic techniques including interview-based requirements extraction, progressive disclosure through skills, and iterative refinement driven by evals.

## Key Information

- **Interview-based prompting:** Instead of specifying all requirements upfront, let Claude interview you using the "ask user question" tool. Claude is often better at extracting latent requirements than humans are at articulating them.
- **Progressive disclosure:** Move detailed business logic from system prompts into skills that load on demand. System prompts should only contain information Claude needs regardless of the task.
- **System prompt bloat:** Accumulating requirements in system prompts leads to conflicts, confusion, and eval regression. A 400-line system prompt can often be reduced to 15 lines with skills.
- **Output schema in tool descriptions:** Include expected output format in tool descriptions so Claude can plan ahead without extra round trips.
- **Effort levels as prompt influence:** Low through max effort control how thoroughly Claude works on a task, affecting thinking depth and token usage.
- **QA loop prompting:** "Approach QA as a bug hunt, not a confirmation step" — adversarial self-critique produces better results than confirmatory review.
- **Smarter models reduce prompt engineering:** Opus 4.7 with a minimal prompt can outperform Sonnet 4.6 with extensive instructions, as model intelligence substitutes for detailed configuration.
- **HTML over Markdown for specs:** HTML specs are more information-dense and ergonomic for human review, enabling richer feedback loops.

## Related

- [[ClaudeCodeSkills]] — skills as the progressive disclosure mechanism
- [[summary-06 - How we Claude Code]] — interview-based prompting and HTML specs
- [[summary-04 - Evals for taste： Hill-climbing a slide-generation agent]] — eval-driven prompt refinement
- [[ClaudeFable5]] — smarter models reducing prompt engineering burden
- [[CLAUDE-md]] — persistent project-level prompting
