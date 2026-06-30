---
title: "Playwright MCP"
type: entity
tags: [tool, mcp, browser-automation, testing, playwright, microsoft, agent-integration]
sources: ["raw/03-transcripts/aiDotEngineer/Channel Only/20260516 - Beyond Code Coverage： Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft.md"]
last_updated: 2026-06-30
---

## Definition
Playwright MCP is the Model Context Protocol (MCP) server for Playwright, enabling coding agents to connect to and control Playwright's browser automation capabilities through tool calling. It is one of three ways to connect AI coding agents to Playwright, alongside the CLI tool and Playwright Agents.

## Key Information
- Provides an MCP interface for coding agents to interact with Playwright's browser automation
- Can be installed into CLI tools like GitHub Copilot CLI
- Enables agents to: open pages, type inputs, click buttons, test filters, verify search results, capture screenshots
- Used in a modified TDD workflow: agent writes failing Playwright behavioral tests (red), generates code to pass them (green), developer refactors
- Supports both headed mode (visible browser) and headless mode (background execution)
- Alternative connection methods: Playwright CLI tool, Playwright Agents (planner/generator/healer agent.md files)
- Screenshots from test runs can be added to PRs for visual verification

## Related
- [[summary-20260516 - Beyond Code Coverage： Functionality Testing with Playwright MCP — Marlene Mhangami, Microsoft]] — source
- [[Playwright]] — parent testing framework
- [[Playwright Agents]] — alternative agent integration
- [[Marlene Mhangami]] — speaker who demonstrated it
- [[Microsoft]] — creator
- [[GitHubCopilot]] — CLI tool used for integration
- [[Functionality Testing]] — testing approach enabled
- [[TDD with AI]] — methodology
- [[MCP]] — Model Context Protocol
