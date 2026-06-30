---
title: "Back Pressure Loop"
type: concept
tags: [ai, agents, linting, esLint, guardrails, code-quality]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful.md"]
last_updated: 2026-06-29
---

## Definition

A Back Pressure Loop uses ESLint (or similar linting tools) with custom rules to constrain AI coding agents from taking shortcuts or producing unsafe patterns. When the model finds a workaround for a banned pattern, a new rule is added — creating a feedback loop that progressively tightens code quality. Michael Arnaldi describes it as "babysitting a junior developer with a knife running through the kitchen."

## Key Information

- ESLint is an essential piece of the feedback loop that keeps AI on track in agent-assisted codebases
- Custom lint rules prohibit specific AI shortcuts: `as X` type assertions, `any` type, `unknown` type, SQL type interfaces (force SQL schema usage)
- When the model finds workarounds (e.g., `as never as X` after `as X` was banned), more rules are added
- Forces branded types for identifiers instead of plain strings to prevent type confusion between different ID types
- Forces schema validation at the API edge instead of constructors inside handlers
- Michael Arnaldi's "accountability" repository has thousands of lines of custom ESLint rules
- The loop: watch what the model produces → if there's an undesirable pattern → write a lint rule to prohibit it → the model adapts → repeat
- All diagnostics should be set to error (not warning) so the model cannot accept code with any issues
- This is a form of mechanical enforcement — the model cannot proceed until lint passes

## Related

- [[summary-20260507 - Vibe Engineering Effect Apps — Michael Arnaldi, Effectful]] — source
- [[Michael Arnaldi]] — developed the pattern
- [[ESLint]] — the linting tool used
- [[Vibe Engineering]] — the parent methodology
- [[Clone the Repo Pattern]] — complementary technique
- [[MechanicalEnforcement]] — the enforcement philosophy
