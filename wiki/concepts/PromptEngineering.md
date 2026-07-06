---
title: "PromptEngineering"
type: concept
tags: [prompting, system-prompt, interview, requirements, progressive-disclosure]
sources: [raw/03-transcripts/Claude/Code with Claude 2026 - London/05 - The prompting playbook.md, raw/03-transcripts/Claude/Code with Claude 2026 - London Day 2/06 - How we Claude Code.md, raw/03-transcripts/Claude/Code with Claude 2026 - London Day 2/04 - Evals for taste： Hill-climbing a slide-generation agent.md, raw/01-articles/claude/2024-05-20 - Generate better prompts in the developer console.md, raw/01-articles/claude/2024-10-14 - Improve your prompts in the developer console.md, raw/01-articles/claude/2025-11-10 - Best practices for prompt engineering.md]
last_updated: 2026-07-04
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
- **Role setting:** Encourage Claude to adopt the characteristics of an expert at the chosen task (e.g., "You will be acting as a content moderator...").
- **Chain of Thought reasoning:** Provide space for Claude to explicitly articulate intermediate reasoning steps and collect thoughts before answering, improving thoroughness and quality.
- **XML tag structuring:** Use XML-style delimiters (e.g., `<code>`, `<instruction>`) to clearly delineate different parts of prompts, improving clarity and information density.
- **Automated prompt generation:** The [[AnthropicConsole]] includes a feature to automatically generate production-ready prompt templates by applying prompt engineering best practices, helping both novices and experienced engineers accelerate development.
- **Automated prompt improvement:** The [[AnthropicConsole]] prompt improver refines existing prompts using advanced techniques like [[ChainOfThoughtReasoning]] and example enrichment. Particularly useful for adapting prompts originally written for other AI models or optimizing hand-written prompts. Includes iterative feedback loops for continuous refinement. Testing shows 30% accuracy improvements on multilabel classification and 100% adherence to output format constraints on summarization tasks.
- **Retrieval-directing prompts:** an early (2023) example of prompting overriding model behavior — see [[LongContextRetrieval]], where appending "Here is the most relevant sentence in the context:" to a response raised [[Claude2.1]]'s long-document retrieval accuracy from 27% to 98%.

## Core Techniques (November 2025 consolidation)

- **Explicit instructions:** state exactly what's wanted rather than relying on inference — e.g., "include as many relevant features and interactions as possible" instead of "create a dashboard."
- **Motivating context:** explaining *why* something matters (e.g., a formatting preference) lets the model generalize the reasoning to related decisions, not just follow a single rule.
- **Specificity:** structure requests with explicit units, constraints, and required output sections rather than vague asks.
- **Examples (one/few-shot):** Claude 4.x pays close attention to example details, so examples must model the exact target behavior; start with one example and add more only if output still misses the mark.
- **Permission for uncertainty:** explicitly allowing "say so rather than speculating" reduces hallucination and increases trustworthiness.
- **Prefilling:** starting the assistant's response (e.g., with `{`) forces continuation in that format — useful for enforcing JSON output or skipping preambles; approximable in chat UIs with explicit instructions.
- **Formatting control:** state what TO do rather than what NOT to do; match the prompt's own formatting style to the desired output style.
- **Prompt chaining:** breaks a complex task into sequential prompts/stages, each feeding the next — trades latency for higher accuracy on complex tasks; cannot be done in a single prompt.
- **Legacy techniques still occasionally useful:** [[XMLTags]] for large data blocks (less necessary with modern models, which handle plain headings/whitespace well); role prompting, where over-constrained personas ("world-renowned expert who never makes mistakes") can reduce helpfulness — being explicit about the desired analytical perspective is often more effective than assigning a persona.

## Related

- [[ClaudeCodeSkills]] — skills as the progressive disclosure mechanism
- [[summary-06 - How we Claude Code]] — interview-based prompting and HTML specs
- [[summary-04 - Evals for taste： Hill-climbing a slide-generation agent]] — eval-driven prompt refinement
- [[ClaudeFable5]] — smarter models reducing prompt engineering burden
- [[CLAUDE-md]] — persistent project-level prompting
- [[PromptEvaluation]] — systematic testing and evaluation of prompts
- [[summary-2024-07-09 - Evaluate prompts in the developer console]] — prompt evaluation in Anthropic Console
- [[ChainOfThoughtReasoning]] — detailed exploration of CoT as a core technique
- [[XMLTags]] — structural technique for prompt clarity
- [[AnthropicConsole]] — platform with integrated prompt generator and improver
- [[summary-2024-05-20 - Generate better prompts in the developer console]] — automated prompt generation feature
- [[summary-2024-10-14 - Improve your prompts in the developer console]] — automated prompt improvement, example management, and evaluation enhancements
- [[RetrievalAugmentedGeneration]] — application architecture benefiting from effective prompting
- [[LongContextRetrieval]] — early retrieval-prompting technique for long-context reluctance
- [[Claude2.1]] — model on which the retrieval-prompting technique was demonstrated
- [[ExtendedThinking]] — model-native alternative to manual chain-of-thought prompting
- [[ContextEngineering]] — the broader discipline prompt engineering feeds into
- [[summary-2025-11-10 - Best practices for prompt engineering]] — November 2025 consolidation of core and advanced techniques
