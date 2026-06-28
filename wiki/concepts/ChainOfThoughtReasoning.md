---
title: "ChainOfThoughtReasoning"
type: concept
tags: [prompt-engineering, reasoning, technique, llm-capability]
sources: ["raw/01-articles/claude/2024-05-20 - Generate better prompts in the developer console.md"]
last_updated: 2026-06-28
---

## Definition

Chain of Thought (CoT) reasoning is a prompt engineering technique that instructs AI models to explicitly articulate their intermediate reasoning steps before arriving at a final answer. By providing space and structure for the model to "think through" a problem, CoT improves the quality, thoroughness, and reliability of responses, particularly for complex queries.

## Key Information

- **Core principle**: Give the model space to collect and articulate its thoughts before answering, rather than jumping directly to conclusions.
- **Effectiveness**: Produces more thorough and well-reasoned responses to complex queries compared to direct prompting.
- **Implementation**: Often uses explicit sections (e.g., `<scratchpad>`, `<reasoning>`) where the model brainstorms, lists options, provides rationales, or works through sub-problems.
- **Example use case**: When asked to generate product recommendations, the model is instructed to brainstorm multiple options with explanations before selecting the best recommendation.
- **Best practice**: CoT is one of the foundational techniques employed by automated prompt generators like the [[AnthropicConsole]] prompt generator.
- **Scalability**: CoT reasoning scales naturally with model capability — more capable models can handle deeper and more complex reasoning chains.

## Related

- [[PromptEngineering]] — the broader discipline within which CoT is a key technique
- [[summary-2024-05-20 - Generate better prompts in the developer console]] — article demonstrating CoT in auto-generated prompts
- [[AnthropicConsole]] — platform that applies CoT in its prompt generator
- [[Anthropic]] — creator of prompt engineering best practices including CoT
