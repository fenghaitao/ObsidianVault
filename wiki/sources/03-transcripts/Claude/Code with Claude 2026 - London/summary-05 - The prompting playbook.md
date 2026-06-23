---
title: "summary-the-prompting-playbook"
type: source
tags: [source, prompting, claude, best-practices, transcript]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London/05 - The prompting playbook.md]
last_updated: 2026-06-23
---

## Core Summary

Margo van Laar presents a prompting playbook through two scenarios: debugging an existing production prompt and building a new agent from scratch. For existing prompts, the workflow is: build evals, apply general hygiene (structure with XML tags, remove redundant patches, define output contracts), then target failure modes one at a time. Key lessons: instructions don't add capability (give tools instead), patches for old models can become anti-patterns, and models optimize for stated goals -- present both sides of trade-offs. For new agents, compare model/prompt/harness combinations systematically.

## Key Points

- **Eval structure:** control cases (should always pass), edge cases (previously failed), capability boundary cases (should escalate/refuse).
- **General hygiene:** use XML tags to separate role, guidelines, policy, tone; remove redundant info (website copy, old model patches); define output contracts.
- **Failure mode: information withholding.** "Never give wrong info" patches cause models to withhold correct info they have. Fix: trust the model's instruction following, provide balanced guidance.
- **Failure mode: mental math.** "Always calculate correctly" doesn't add capability. Fix: give the model a tool to do calculations reliably.
- **Failure mode: escalation avoidance.** One-sided cost framing ("escalation costs $8") prevents escalation. Fix: present both sides (cost of getting it wrong: refunds + trust).
- **New agent building:** start simple (Sonnet + basic prompt), try larger model (Opus), try adaptive thinking, then optimize prompt. Use programmatic evals for hard constraints.
- **Version control prompts:** track why defensive changes were added so they can be revisited when models improve.

## Related

- [[PromptEngineering]] — the broader discipline
- [[ClaudeCode]] — the tool prompts are written for
- [[summary-10 - Picking the right model]] — related model selection talk
