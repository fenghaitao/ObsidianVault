---
title: "summary-2025-11-10 - Best practices for prompt engineering"
type: source
tags: [source, prompt-engineering, techniques]
sources: ["raw/01-articles/claude/2025-11-10 - Best practices for prompt engineering.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic's team consolidates core and advanced prompt engineering techniques for Claude: explicit instructions, motivating context, specificity, examples (one/few-shot), and permission to express uncertainty as foundational habits; prefilling, chain-of-thought, formatting control, and prompt chaining as advanced techniques for agentic and complex tasks; and XML tags/role prompting as legacy techniques still occasionally useful. Frames prompt engineering as the essential building block of context engineering.

## Key Points

- **Explicit instructions**: state exactly what you want; modern models like Claude respond well to direct, unambiguous asks rather than inference.
- **Motivating context**: explaining *why* something matters (e.g., a formatting preference) helps the model generalize the reasoning to related decisions, not just follow a rule.
- **Specificity**: structure instructions with explicit guidelines (units, constraints, format) rather than vague requests.
- **Examples (one/few-shot)**: Claude 4.x pays close attention to example details — ensure examples model the exact behavior wanted; start with one example, add more only if needed.
- **Permission for uncertainty**: explicitly allowing "say so rather than speculating" reduces hallucination and increases trustworthiness.
- **Prefilling**: starting the assistant's response (e.g., with `{`) forces continuation in that format, useful for enforcing JSON output or skipping preambles; approximable in chat UIs via explicit instruction.
- **Chain of thought (CoT)**: basic ("think step-by-step"), guided (specific reasoning stages), and structured (`<thinking>` tags) variants; [[ExtendedThinking]] is generally preferable when available, but manual CoT remains complementary for transparent, reviewable reasoning.
- **Formatting control**: tell the model what TO do rather than what NOT to do; match the prompt's own formatting style to the desired output; use explicit paragraph/markdown rules for fine control.
- **Prompt chaining**: breaks a complex task into sequential prompts, trading latency for accuracy — cannot be done in a single prompt.
- **Legacy techniques**: [[XMLTags]] were once essential for structuring large data blocks in prompts but are less necessary with modern models; role prompting can help but over-constrained personas ("world-renowned expert who never makes mistakes") often reduce helpfulness — being explicit about the desired analytical perspective is often more effective than assigning a persona.
- **Context awareness**: Claude 4.x has improved "lost-in-the-middle" handling, but task-splitting remains valuable for focus and scope, not just context-limit avoidance.
- Frames prompt engineering as foundational to [[ContextEngineering]]: every well-crafted prompt becomes part of the context shaping agent behavior alongside history, files, and system instructions.

## Related

- [[PromptEngineering]] — the concept this article substantially expands
- [[ExtendedThinking]] — the model-native alternative to manual chain-of-thought
- [[XMLTags]] — legacy structuring technique discussed
- [[ContextEngineering]] — the broader discipline prompt engineering feeds into
