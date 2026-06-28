---
title: "XMLTags"
type: concept
tags: [prompt-engineering, structure, xml, formatting, best-practice]
sources: ["raw/01-articles/claude/2024-05-20 - Generate better prompts in the developer console.md"]
last_updated: 2026-06-28
---

## Definition

Using XML tags in prompts is a prompt engineering best practice that involves wrapping data sections, variables, or instructions within XML-style delimiters (e.g., `<code>`, `<instruction>`, `<input>`) to provide clear structural delineation. This technique improves information clarity, model understanding, and allows for more nuanced prompt control.

## Key Information

- **Purpose**: Clearly separate different parts of a prompt by providing explicit structural boundaries.
- **Benefit for models**: XML tagging helps models recognize and respect different data categories and their distinct roles in the task.
- **Information density**: XML-tagged sections are more information-dense and enable richer prompt composition compared to plain text delineation.
- **Application in variables**: Complex or ambiguous variables are typically wrapped in XML tags, while simple inline variables may use alternative notation like [[Handlebars]].
- **Example structure**: 
  ```
  <code>
  {{CODE_TO_TRANSLATE}}
  </code>
  ```
- **Adoption**: Widely recommended by [[Anthropic]] as part of prompt engineering best practices and automatically applied in the [[AnthropicConsole]] prompt generator.

## Related

- [[PromptEngineering]] — the discipline within which XML tagging is a key technique
- [[Handlebars]] — template variable notation often used alongside XML tags
- [[summary-2024-05-20 - Generate better prompts in the developer console]] — article demonstrating XML tag usage
- [[AnthropicConsole]] — platform applying XML tagging in generated prompts
- [[Anthropic]] — organization promoting XML tagging as a best practice
