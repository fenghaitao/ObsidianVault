---
title: "Get to production faster with the upgraded Anthropic Console"
type: source
tags: [console, anthropic, prompt-engineering, collaboration, extended-thinking]
sources: [raw/01-articles/claude/2025-03-06 - Get to production faster with the upgraded Anthropic Console.md]
last_updated: 2026-06-28
---

## Article Summary

Anthropic announced a redesigned [[AnthropicConsole]] that serves as a unified platform for building, testing, and iterating on AI deployments with Claude and teammates. The upgrades include support for [[Claude3.7Sonnet]], the latest model featuring [[ExtendedThinking]] capabilities, and new collaboration features like shareable prompts.

## Key Features

### Building Reliable AI Applications

The Console streamlines AI development through a comprehensive workflow:

**Workbench**: Interactive environment for structuring prompts, incorporating examples, and integrating external [[ToolUse|tools]], with interactive API testing capabilities.

**Prompt Generation**: Automatic prompt generation using [[ChainOfThoughtReasoning]] and other advanced [[PromptEngineering]] techniques. Users describe their desired outcomes, and Claude generates effective, precise, and reliable starting prompts.

**Prompt Optimization**: Automatic refinement of existing prompts using advanced techniques. Particularly useful for adapting prompts originally written for other AI models or optimizing hand-written prompts.

**Evaluation and Comparison**: Features for evaluating prompts against real-world scenarios with:
- [[TestCaseGeneration]]: Automatic test case generation
- Side-by-side output comparison between prompt variants
- Test suite execution and scoring
- Data-driven decisions about which prompts to deploy

### Collaboration and Standardization

**Shareable Prompts**: New feature enabling centralized prompt development and standardization across organizations. Previously, teams relied on copy-paste workflows between documents and chat applications, creating version control issues and knowledge silos.

**Team Collaboration**: Developers, domain experts, product managers, and QA specialists can now collaborate directly in the Console on a shared library of prompts, establishing and maintaining best practices.

### Extended Thinking Support

[[Claude3.7Sonnet]] represents Anthropic's latest and most intelligent model, featuring the ability to:
- Produce near-instant responses for straightforward tasks
- Generate visible, step-by-step reasoning for complex problems
- Control thinking budget via maximum token limits

The Console now includes **thinking optimization**: developers can specify that a prompt will be used with [[ExtendedThinking]] enabled, and Claude will generate responses optimized for this mode. The Console also provides controls for setting the maximum thinking token budget.

## Availability

The upgraded Anthropic Console is immediately available to all users. Production-ready API calls can be generated via "Get Code" button for immediate deployment.

## Related Concepts

- [[PromptEngineering]] — discipline enhanced by console tools
- [[PromptEvaluation]] — evaluation features for refining prompts
- [[ChainOfThoughtReasoning]] — technique used in automatic prompt generation
- [[ToolUse]] — external tool integration in Workbench
- [[TestCaseGeneration]] — automatic test generation feature
- [[ExtendedThinking]] — new reasoning capability in Claude 3.7 Sonnet
- [[AdaptiveThinking]] — complementary thinking capability

## Related Entities

- [[AnthropicConsole]] — the platform described in the article
- [[Claude3.7Sonnet]] — latest model supporting extended thinking
- [[Anthropic]] — creator and maintainer

## Related Sources

- [[summary-2024-05-20 - Generate better prompts in the developer console]] — prompt generator feature
- [[summary-2024-07-09 - Evaluate prompts in the developer console]] — evaluation features
- [[summary-2024-10-14 - Improve your prompts in the developer console]] — prompt improvement features
