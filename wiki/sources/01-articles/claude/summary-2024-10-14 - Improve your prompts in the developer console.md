---
title: "Improve your prompts in the developer console"
type: source
tags: [prompt-engineering, console, developer-tools, automation, examples, evaluation]
sources: [raw/01-articles/claude/2024-10-14 - Improve your prompts in the developer console.md]
last_updated: 2026-06-28
---

## Summary

Anthropic announced new prompt improvement and example management capabilities in the [[AnthropicConsole]]. These features streamline the application of [[PromptEngineering]] best practices and enable faster, more reliable AI application development. The article highlights three main capabilities: automated prompt improvement, structured example management, and enhanced evaluation with ideal output specifications.

## Key Capabilities

### Prompt Improver
- **Automated refinement**: Claude automatically refines existing prompts using advanced prompt engineering techniques
- **Techniques applied**: [[ChainOfThoughtReasoning]], example enrichment, and other best practices
- **Use case compatibility**: Ideal for adapting prompts originally written for other AI models as well as optimizing hand-written prompts
- **Iterative refinement**: Users can provide feedback on what is and isn't working to further improve the prompt
- **Format flexibility**: Can modify prompts based on arbitrary requests (e.g., converting JSON-formatted outputs to XML-formatted outputs)
- **Performance improvements**: Testing shows:
  - 30% accuracy increase on multilabel classification tasks (500 Wikipedia articles matching titles to random article sentences with Claude 3 Haiku)
  - 100% word count adherence on summarization tasks (10 Wikipedia articles)

### Example Management
- **Structured format**: Manage examples directly in the Workbench with clear input/output pairs
- **Automated generation**: Claude can automatically create synthetic example inputs and draft outputs
- **Benefits**: Adding examples to prompts is one of the most effective ways to improve model response quality, especially for precise output format compliance
- **Improvements from examples**:
  - Increased accuracy and consistency
  - Better adherence to output format specifications
  - More precise model behavior

### Enhanced Evaluation
- **Ideal output column**: Optional column in the Evaluations tab for specifying ideal/expected outputs
- **5-point scale grading**: Users can effectively and consistently grade model outputs
- **Benchmarking**: Helps benchmark and compare prompt performance objectively
- **Integration**: Works with the existing [[PromptEvaluation]] framework in the Console

## Company Implementation

### Kapa.ai Case Study
- **Company background**: Technology company that turns technical knowledge bases into production-ready AI assistants
- **Challenge**: Migrating critical AI workflows to Claude
- **Solution**: Used the prompt improver to streamline migration to [[Claude3.5Sonnet]]
- **Outcome**: Enabled faster time-to-production for their AI assistant offerings
- **Quote from Finn Bauer (Co-Founder)**: "Anthropic's prompt improver streamlined our migration to Claude 3.5 Sonnet and enabled us to get to production faster"

## Product Availability & Documentation

- **Platform**: All capabilities available to all users in the [[AnthropicConsole]]
- **Documentation**: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-improver

## Related Capabilities

- **Prompt Evaluator**: Existing tool for testing prompts under various scenarios
- **Prompt Generator**: Earlier feature for creating prompts from task descriptions

## Impact & Context

The prompt improver represents an evolution of Anthropic's developer tooling in the Console, complementing earlier releases of the prompt generator (May 2024) and evaluation framework (July 2024). Together, these features create a complete workflow for prompt engineering: generate, improve, manage examples, and evaluate iteratively.


## Related

- [[AnthropicConsole]] — platform where prompt improver, example management, and evaluation features are available
- [[PromptEngineering]] — broader discipline enabled and streamlined by these tools
- [[PromptEvaluation]] — evaluation framework enhanced with ideal output specifications
- [[ChainOfThoughtReasoning]] — key technique applied by prompt improver
- [[Kapa.ai]] — company case study using prompt improver for Claude migration
- [[Claude3.5Sonnet]] — model used in Kapa.ai's migration workflow

