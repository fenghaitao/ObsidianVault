---
title: "EvalDrivenDevelopment"
type: concept
tags: [methodology, evaluation, testing, claude-code, quality-assurance]
sources: ["raw/01-articles/claude/2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon.md"]
last_updated: 2026-07-07
---

## Definition

Eval-driven development is a software development methodology where evaluation criteria and benchmarks are established before feature implementation, and development decisions are guided by measured results against those benchmarks rather than intuition. It was most prominently demonstrated by Benjamin Torralbo in building MaestrIA, where a 9-dimension evaluation framework was the "first commit."

## Key Information

- **Core principle**: "Eval first, features later." Build an auditable evaluation framework against real cases with ground truth before writing features, so measured results — not intuition — tell you what is working and what isn't.
- **Contrasts with**: Intuition-driven development where features are built based on assumptions about what will work, without systematic measurement.

### MaestrIA Example

- Benjamin Torralbo built a 9-dimension eval against 12 real cases with ground truth recorded by his father (a master carpenter with 30 years of experience).
- The eval measured diagnostic accuracy against a human master's judgment.
- A single JSON file of domain knowledge (17 diagnostic rules, local materials, trade dialect, benchmark prices, common mistakes) lifted eval scores from 74% to 81% — without touching the system prompt.
- "That eval, not my intuition, told me what was working and what wasn't. If I did another hackathon, the eval would be the first commit."

### ARIA Example

- Idriss Benguezzou advised: "Let Claude audit. Ask Claude to find if there's anything wrong with what you've already built before building the next thing."
- This creates a continuous evaluation loop integrated into the development process.

### Relationship to Claude Code

Eval-driven development pairs naturally with Claude Code's capabilities:
- Claude can be prompted to audit completed work for issues before moving on.
- Claude Managed Agents can run parallel evaluation agents.
- The methodology provides concrete feedback for iterative improvement rather than relying on developer intuition.

## Related

- [[summary-2026-06-15 - Meet the winners of the Built with Opus 4.7 Claude Code hackathon]] — source summary
- [[SpecFirstDevelopment]] — complementary methodology, plan before building
- [[PromptEvaluation]] — systematic prompt evaluation framework
- [[MaestrIA]] — hackathon project exemplifying eval-driven development
- [[ARIA]] — hackathon project using audit-loop evaluation
- [[ExplorePlanCodeCommit]] — Claude Code workflow with built-in review phase
