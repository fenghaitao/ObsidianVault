---
title: "How Anthropic Uses Claude in Product Management"
type: source
tags: [anthropic, product-management, data-analysis, evals, claude-code]
sources: [raw/03-transcripts/Claude/How Anthropic uses Claude/04 - How Anthropic uses Claude in Product Management.md]
last_updated: 2026-06-23
---

## Core Summary

An Anthropic product manager describes using Claude Code for two key workflows: data analysis via BigQuery MCP (no SQL knowledge needed — just interpret results) and eval generation (expanding 1-2 test cases into 50). Claude Code generates polished visualizations with rolling averages and plan-type breakdowns that would take hours manually. The theme is Claude extending what PMs can accomplish independently, shifting their time from coordination and operations to strategy, customer conversations, and decision-making.

## Key Points

- **Data analysis without SQL:** BigQuery MCP connects product data tables to Claude Code. PM asks natural language questions; Claude writes queries, generates graphs with rolling averages and breakdowns.
- **Eval generation:** Claude expands 1-2 example test cases into 50, dramatically accelerating the eval creation process for AI product testing.
- **Independence and empowerment:** PMs can test product ideas before involving anyone else, operating much more independently.
- **Time shift:** From hours of manual data work to minutes of interpretation; from coordination/operations to strategy and customer conversations.
- **Beyond automation:** Claude extends what PMs are capable of doing independently, not just automating existing workflows.

## Related

- [[Anthropic]] — the company using Claude internally
- [[ClaudeCode]] — the tool used for data analysis and eval generation
- [[ModelContextProtocol]] — BigQuery MCP for data access
