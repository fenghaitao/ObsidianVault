---
title: "Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz"
type: source-summary
source: "raw/03-transcripts/aiDotEngineer/Channel Only/20260408 - Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz.md"
author: "aiDotEngineer"
date: 2026-04-08
ingested: 2026-06-26
---

# Bending a Public MCP Server Without Breaking It — Nimrod Hauser, Baz

## Core Thesis
Third-party MCP server tools often fail out of the box because they are designed for generic use cases, but applying five best practices — curating, wrapping, adding deterministic guardrails, composing new tools, and using tools as deterministic functions — can transform them into highly effective, tailored components for specific agentic workflows.

## Summary
Nimrod Hauser, founding engineer at Baz, presents a practical framework for optimizing third-party agentic tools (from MCP servers, libraries, or anywhere else) for specific use cases. Using Playwright's MCP server as an example within Baz's spec reviewer product (an AI agent that compares requirements from tickets and Figma designs against actual implementations), he demonstrates five progressively sophisticated techniques:

1. **Tool Curation**: Filter out unnecessary tools to reduce context window load and prevent agent confusion. The example excludes browser resize, drag, and code execution tools that are irrelevant to the spec reviewer use case.

2. **Tool Wrapping**: Replace generic tool descriptions with use-case-specific enhanced descriptions that guide agent behavior — for example, instructing the agent to call the accessibility snapshot tool before any click or hover action, and preferring it over visual screenshots.

3. **Deterministic Guardrails**: Add deterministic validation logic around sensitive operations. The example validates that screenshot file paths are within an allowed directory, raising a friendly agent-facing error message if not, rather than letting the agent save files anywhere.

4. **Tool Composition**: Create new tools built on existing ones with specialized descriptions. The example creates an "evidence tool" that wraps the screenshot tool with instructions for naming files with ticket numbers and only using it for evidence capture.

5. **Deterministic Tool Usage**: Use MCP tools as plain callable functions outside the agentic loop for operations that are always required and potentially tricky (like login with JWT tokens), unburdening the agent and its context window.

The talk concludes with a live demonstration showing the spec reviewer succeeding after all optimizations are applied, where the baseline vanilla approach had failed with hallucinations and incorrect results.

## Entities
- [[NimrodHauser]] — founding engineer at Baz, speaker
- [[Baz]] — AI-powered code reviewer company
- [[Playwright]] — browser automation library with MCP server
- [[LangChain]] — framework used for loading MCP tools
- [[Figma]] — design tool used for visual requirements
- [[Jira]] — ticketing system for requirements
- [[Linear]] — ticketing system for requirements

## Concepts
- [[ThirdPartyToolOptimization]] — five best practices for adapting third-party agentic tools
- [[ToolCuration]] — filtering irrelevant tools to reduce context window load
- [[ToolWrapping]] — replacing generic tool descriptions with use-case-specific guidance
- [[DeterministicGuardrails]] — adding deterministic validation around sensitive agent operations
- [[ToolComposition]] — creating new specialized tools from existing ones
- [[DeterministicToolUsage]] — using agentic tools as plain functions outside the agent loop
- [[MCP]] — Model Context Protocol, updated with third-party tool challenges
- [[ToolCalling]] — updated with tool optimization practices
- [[Context Management]] — updated with context window reduction via curation

## Related
- [[summary-20251222 - The 3 Pillars of Autonomy – Michele Catasta, Replit]] — related browser automation testing
- [[summary-20251226 - How Claude Code Works - Jared Zoneraich, PromptLayer]] — related tool calling architecture
