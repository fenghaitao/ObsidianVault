---
title: "CodeExecutionTool"
type: concept
tags: [anthropic, api, code-execution, python, data-analysis, agents]
sources: [raw/01-articles/claude/2025-05-22 - New capabilities for building agents on the Anthropic API.md, raw/01-articles/claude/2025-10-16 - Introducing Agent Skills.md]
last_updated: 2026-07-04
---

# Code Execution Tool

The code execution tool is an [[Anthropic]] API feature that enables Claude to run Python code in a sandboxed environment, transforming Claude from a code-writing assistant into an autonomous data analyst that can execute computational tasks end-to-end.

## Definition

The code execution tool allows Claude to:
- Execute Python code in an isolated, sandboxed environment
- Perform computational analysis and data processing
- Generate visualizations and charts
- Iterate on outputs based on execution results
- Return analytical results within a single API call

## Key Capabilities

- **Python Execution:** Run Python code with common data science libraries
- **Dataset Processing:** Load, clean, and analyze datasets
- **Visualizations:** Generate exploratory charts and graphs
- **Iterative Refinement:** Process results and refine analysis based on outputs
- **End-to-End Analysis:** Complete analytical workflows without human intervention between steps

## Use Cases

- **Financial modeling:** Generate financial projections, analyze investment portfolios, calculate complex financial metrics
- **Scientific computing:** Execute simulations, process experimental data, analyze research datasets
- **Business intelligence:** Create automated reports, analyze sales data, generate performance dashboards
- **Document processing:** Extract and transform data across formats, generate formatted reports, automate document workflows
- **Statistical analysis:** Perform regression analysis, hypothesis testing, predictive modeling

## Availability

- [[Anthropic]] API (beta)
- Works with [[Claude4Opus]] and [[Claude4Sonnet]]

## Pricing

- 50 free hours of usage per day per account
- $0.05/hour per container for additional usage

## Contrast

Unlike the [[CodeExecution|analysis tool]] in [[Claude.ai]] which uses JavaScript:
- API code execution tool uses Python
- Enables scientific and data analysis workflows
- Serverless container-based execution

## Agent Skills Dependency (October 2025)

[[ClaudeCodeSkills|Agent Skills]] on the Anthropic API require the Code Execution Tool beta, which provides the secure sandboxed environment Skills need to run — for example, Anthropic-created skills that read/generate Excel, PowerPoint, Word, and fillable PDFs.

## Related

- [[Anthropic]] — API provider
- [[AIAgent]] — agents using code execution for autonomous analysis
- [[ToolUse]] — related tool-calling capability
- [[FilesAPI]] — integrates with code execution for file access
- [[PromptCaching]] — extends context for long-running analysis workflows
- [[Claude4Opus]] — flagship model with code execution support
- [[Claude4Sonnet]] — code execution capable model
- [[summary-2025-05-22 - New capabilities for building agents on the Anthropic API]] — announcement article
- [[ClaudeCodeSkills]] — Agent Skills feature that depends on this tool via the API
- [[summary-2025-10-16 - Introducing Agent Skills]] — Agent Skills announcement noting the Code Execution Tool dependency
