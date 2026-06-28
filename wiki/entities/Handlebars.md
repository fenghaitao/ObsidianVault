---
title: "Handlebars"
type: entity
tags: [templating, notation, variable-syntax, web-development]
sources: ["raw/01-articles/claude/2024-05-20 - Generate better prompts in the developer console.md"]
last_updated: 2026-06-28
---

## Definition

Handlebars is a popular templating language and variable notation system that uses double-braced syntax (e.g., `{{variable_name}}`) to mark dynamic fields and expressions. In the context of prompt engineering, Handlebars notation is used to indicate template variables that can be dynamically populated with user-provided data.

## Key Information

- **Syntax**: Variables are denoted with double braces: `{{variable_name}}`
- **Usage in prompts**: Used by [[Anthropic]]'s [[AnthropicConsole]] prompt generator to mark dynamic input fields in generated prompt templates.
- **Complementary to XML tags**: Handlebars notation often works alongside [[XMLTags]] — complex variables are wrapped in XML for clarity, while simpler variables use inline Handlebars notation.
- **Simplicity**: Handlebars provides a simple, readable way to indicate where custom data should be inserted.
- **Standard adoption**: Widely recognized notation that users can easily understand and work with when editing generated prompts.

## Related

- [[XMLTags]] — structural technique used alongside Handlebars notation
- [[PromptEngineering]] — discipline employing Handlebars in prompt templates
- [[AnthropicConsole]] — platform using Handlebars notation in generated prompts
- [[summary-2024-05-20 - Generate better prompts in the developer console]] — source introducing Handlebars in prompt context
