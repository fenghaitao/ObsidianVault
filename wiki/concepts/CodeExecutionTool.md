---
title: "CodeExecutionTool"
type: concept
tags: [anthropic, api, code-execution, python, data-analysis, agents]
sources: [raw/01-articles/claude/2025-05-22 - New capabilities for building agents on the Anthropic API.md, raw/01-articles/claude/2025-10-16 - Introducing Agent Skills.md, raw/01-articles/claude/2026-02-17 - Increase web search accuracy and efficiency with dynamic filtering.md]
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

## Dynamic Filtering for Web Search (February 2026)

Extended to web search and web fetch tools: Claude writes and executes code to post-process search results, filtering out irrelevant content before it reaches the context window rather than reasoning over raw HTML. Improved accuracy by an average of 11% while using 24% fewer input tokens across BrowseComp and DeepSearchQA benchmarks. See [[WebSearch]].

## Harness-Design Framing (April 2026)

Anthropic frames code execution as moving *orchestration decisions* from the harness to the model — Claude decides what tool-call results to pass through, filter, or pipe onward, so only code's output reaches the context window rather than every raw tool result. Reasoning: since code is a general orchestration mechanism, a strong coding model is also a strong general agent. See [[summary-2026-04-02 - Harnessing Claude’s intelligence]].

## Programmatic Tool Calling in MCP Clients (April 2026)

Applied to MCP tool results specifically: rather than returning raw tool output to the model, an MCP client can process results inside a code-execution sandbox, letting the agent loop, filter, and aggregate across multiple tool calls with only the final output reaching context. Anthropic reports roughly 37% token-usage reduction on complex multi-step workflows, composing naturally with Tool Search across multiple MCP servers. See [[ModelContextProtocol]] and [[summary-2026-04-22 - Building agents that reach production systems with MCP]].

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
- [[WebSearch]] — dynamic filtering feature built on this tool
- [[summary-2026-02-17 - Increase web search accuracy and efficiency with dynamic filtering]] — dynamic filtering announcement
- [[summary-2026-04-02 - Harnessing Claude’s intelligence]] — harness-design framing for code execution as self-orchestration
- [[ModelContextProtocol]] — protocol whose clients use programmatic tool calling for context efficiency
- [[summary-2026-04-22 - Building agents that reach production systems with MCP]] — programmatic tool calling applied to MCP clients
