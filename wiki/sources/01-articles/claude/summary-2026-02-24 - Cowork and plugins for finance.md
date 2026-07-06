---
title: "summary-2026-02-24 - Cowork and plugins for finance"
type: source
tags: [source, cowork, plugins, finance, mcp]
sources: ["raw/01-articles/claude/2026-02-24 - Cowork and plugins for finance.md"]
last_updated: 2026-07-04
---

## Core Summary

Anthropic expanded Cowork's finance capabilities: Claude now carries context between Excel and PowerPoint to complete multi-step finance workflows end to end (research → model update → deck) in a single session, alongside five new Anthropic-built finance plugins (financial analysis, investment banking, equity research, private equity, wealth management) and new MCP connectors for FactSet and MSCI, plus partner-built plugins from LSEG and S&P Global.

## Key Points

- **Cross-app context**: an equity analyst can ask Claude to analyze earnings, update a financial model, and build a summary slide without switching tools; when inputs change, Claude propagates updates through the rest of the workflow. Available in research preview for all paid plans on Mac and Windows.
- **Five Anthropic-built finance plugins**: available now in Anthropic's public `financial-services-plugins` GitHub repository, encoding domain expertise, expected output quality, and workflow patterns for each finance function.
- **New MCP connectors**: FactSet and MSCI give Claude direct access to institutional market-data platforms, alongside existing financial connectors.
- **Partner plugins**: LSEG and S&P Global built their own plugins (same public repository) bringing institutional data/terminology directly into Claude's context — installable as-is or customized per firm.
- Companion to the broader "[[ClaudeCowork|Cowork]] and plugins for teams across the enterprise" release covering non-finance functions.

## Related

- [[ClaudeCowork]] — the product these finance updates extend
- [[ClaudeCodePlugins]] — the plugin mechanism these finance plugins use
- [[Claude4.6Opus]] — the model powering these finance capabilities
