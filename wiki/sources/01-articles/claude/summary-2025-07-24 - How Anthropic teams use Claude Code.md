---
title: "How Anthropic teams use Claude Code"
type: source
tags: [claude-code, workflow-automation, agentic-coding, anthropic-usage]
sources: [raw/01-articles/claude/2025-07-24 - How Anthropic teams use Claude Code.md]
last_updated: 2026-06-28
---

# How Anthropic teams use Claude Code

Anthropic employees across different teams use [[ClaudeCode]] to accelerate development workflows, debug production issues, navigate unfamiliar codebases, and build custom automation tools. The pattern reveals that agentic coding is dissolving the boundary between technical and non-technical work, enabling anyone to build solutions from problem descriptions.

## Onboarding & Codebase Navigation

Infrastructure team data scientists feed their entire codebase to [[ClaudeCode]], which reads `CLAUDE.md` files to identify relevant ones, explains data pipeline dependencies, and shows upstream data sources feeding into dashboards—replacing traditional data catalog tools.

Product Engineering team refers to [[ClaudeCode]] as their "first stop" for programming tasks, using it to identify files for bug fixes, features, and analysis, eliminating manual context gathering.

## Testing & Code Review

Product Design team automated [[UnitTesting]] through GitHub Actions, using [[ClaudeCode]] to write comprehensive tests and handle formatting issues and test case refactoring.

Security Engineering team transformed their workflow to test-driven development, asking [[ClaudeCode]] for pseudocode and checking in periodically, resulting in more reliable and testable code.

Inference team translates tests across programming languages. When testing in unfamiliar languages like [[Rust]], they explain the test requirements and [[ClaudeCode]] writes the native logic.

## Production Issue Resolution

Security Engineering feeds [[ClaudeCode]] stack traces and documentation to trace control flow. Problems that took 10-15 minutes now resolve 3x faster.

Product Engineering gained confidence tackling bugs in unfamiliar codebases, asking [[ClaudeCode]] to analyze observed behavior and proposing solutions without relying on other teams.

Data Infrastructure team used [[ClaudeCode]] during a Kubernetes outage: feeding dashboard screenshots, receiving step-by-step [[GoogleCloud]] UI guidance, and obtaining exact commands to fix pod IP address exhaustion, saving 20 minutes during system downtime.

## Rapid Prototyping & Feature Development

Product Design feeds [[Figma]] design files to [[ClaudeCode]], setting up autonomous loops where the tool writes code, runs tests, and iterates. In one case, it built Vim key bindings with minimal human review.

Product Design discovered [[ClaudeCode]] helps map error states, logic flows, and system statuses to identify edge cases during design—improving initial design quality and reducing debugging hours.

Data scientists build [[React]] applications for visualizing [[ReinforcementLearning]] model performance using [[TypeScript]], without being fluent in the language. One-shot prompting generates entire visualizations.

## Knowledge Consolidation & Documentation

[[ClaudeCode]] consolidates scattered technical documentation via [[MCP]] and `CLAUDE.md` files into accessible formats. Inference team members without ML backgrounds use it to explain model-specific functions, reducing research time from one hour to 10-20 minutes (80% reduction).

Security Engineering ingests multiple documentation sources to create markdown runbooks and troubleshooting guides for production debugging.

## Custom Automation

Growth Marketing built an agentic workflow processing CSV files with hundreds of ads: identifying underperformers and generating variations within strict character limits using two sub-agents, generating hundreds of ads in minutes.

Growth Marketing developed a [[Figma]] plugin that generates up to 100 ad variations by programmatically swapping headlines and descriptions, reducing copy-pasting hours to 0.5 seconds per batch.

Legal team created prototype "phone tree" systems to help team members connect with the right lawyer at Anthropic—demonstrating custom tool development without traditional development resources.

## Key Pattern

The most successful teams treat [[ClaudeCode]] as a thought partner rather than a code generator, exploring possibilities, prototyping rapidly, and sharing discoveries across technical and non-technical users.

## Related

- [[ClaudeCode]] — Anthropic's terminal-based coding agent
- [[AgenticCoding]] — AI-driven workflow automation and development paradigm
- [[Anthropic]] — Company where these use cases originate
- [[TestDrivenDevelopment]] — Development methodology accelerated by agentic coding
- [[UnitTesting]] — Testing methodology automated through Claude Code
- [[Figma]] — Design tool integrated with Claude Code
- [[GoogleCloud]] — Cloud platform used by Anthropic teams
- [[React]] — UI framework for building visualizations
- [[TypeScript]] — Language used for visualization development
- [[Rust]] — Language supported through test translation
- [[MCP]] — Protocol for documentation consolidation
- [[ReinforcementLearning]] — ML methodology with visualizations built via Claude Code
